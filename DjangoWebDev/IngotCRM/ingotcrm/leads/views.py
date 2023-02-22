from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, JsonResponse
from django.views.generic import (
    TemplateView, ListView, DetailView, 
    CreateView, DeleteView, UpdateView, FormView)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Lead, Agent, Category, Document
from .forms import (
    LeadForm, LeadModelForm,
    CustomUserCreationForm, AssignAgentForm,
    LeadCategoryUpdateForm, UploadDocumentModelForm)
from agents.mixins import OrganisorRequiredMixin


DOCUMENTS_PER_PAGE = 2


class LandingPageView(TemplateView):
    template_name = "landing.html"


class LeadListView(LoginRequiredMixin, ListView):
    template_name = "lead_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile, agent__isnull=False)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation, agent__isnull=False)
            queryset = Lead.objects.filter(agent__user=user)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile, agent__isnull=True)
            context.update({
                "unassigned_leads": queryset
            })
        return context


class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "lead_details.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = "lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.organisation = self.request.user.userprofile
        lead.save()
        
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "lead_update.html"
    form_class = LeadModelForm

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            queryset = Lead.objects.filter(agent__user=user)
        
        return queryset

    def get_success_url(self):
        return reverse("leads:lead-list")


class LeadDeleteView(OrganisorRequiredMixin, DeleteView):
    template_name = "lead_delete.html"

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        return reverse("leads:lead-list")


class AssignAgentView(OrganisorRequiredMixin, FormView):
    template_name = "assign_agent.html"
    form_class = AssignAgentForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs

    def get_success_url(self):
        return reverse("leads:lead-list")
    
    def form_valid(self, form):
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()

        return super(AssignAgentView, self).form_valid(form)


class CategoryListView(LoginRequiredMixin, ListView):
    template_name = "category_list.html"
    context_object_name = "category_list"

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        user = self.request.user

        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)

        context.update({
            "unassigned_lead_count": queryset.filter(category__isnull=True).count()
        })
        return context
    
    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Category.objects.filter(organisation=user.userprofile)
        else:
            queryset = Category.objects.filter(organisation=user.agent.organisation)
        
        return queryset


class CategoryDetailView(LoginRequiredMixin, DetailView):
    template_name = "category_detail.html"
    context_object_name = "category"

    # def get_context_data(self, **kwargs):
    #     context = super(CategoryDetailView, self).get_context_data(**kwargs)

    #     #queryset = Lead.objects.filter(category=self.get_object())
    #     queryset = self.get_object().lead_cat.all()   # Called by the related name in ForeignKey Model obj.

    #     context.update({
    #         "leads": queryset
    #     })
    #     return context
    
    def get_queryset(self):
        user = self.request.user

        if user.is_organisor:
            queryset = Category.objects.filter(organisation=user.userprofile)
        else:
            queryset = Category.objects.filter(organisation=user.agent.organisation)
        
        return queryset


class LeadCategoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "lead_category_update.html"
    form_class = LeadCategoryUpdateForm

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            queryset = Lead.objects.filter(agent__user=user)
        
        return queryset

    def get_success_url(self):
        return reverse("leads:lead-detail", kwargs={"pk": self.get_object().id})


class SignupView(CreateView):
    template_name = "registration/register.html"
    form_class = CustomUserCreationForm

    def get_success_url(self) -> str:
        return reverse("login")


class DocumentListView(LoginRequiredMixin, ListView):
    template_name = "document_list.html"
    context_object_name = "documents"

    paginate_by = DOCUMENTS_PER_PAGE
    
    def get_queryset(self):
        user = self.request.user

        if user.is_organisor:
            documents = Document.objects.filter(organisation=user.userprofile)
        else:
            documents = Document.objects.filter(organisation=user.agent.organisation, is_secret=False)
        
        documents = documents.order_by('-date_added')

        ordering = self.request.GET.get('ordering', "")
        if ordering:
            documents = documents.order_by(ordering)

        # Return a JSON response
        return documents


class DocumentDetailView(LoginRequiredMixin, DetailView):
    template_name = "document_detail.html"
    queryset = Document.objects.all()
    context_object_name = "document"


class DocumentUploadView(LoginRequiredMixin, CreateView):
    template_name = "upload_document.html"
    form_class = UploadDocumentModelForm

    def get_success_url(self) -> str:
        return reverse("leads:document-list")
    
    def form_valid(self, form):
        return super(DocumentUploadView, self).form_valid(form)


class DocumentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "document_update.html"
    form_class = UploadDocumentModelForm

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Document.objects.filter(organisation=user.userprofile)
        else:
            queryset = Document.objects.filter(organisation=user.agent.organisation)
            queryset = Document.objects.filter(agent__user=user)
        
        return queryset

    def get_success_url(self):
        return reverse("leads:document-detail", kwargs={"pk": self.get_object().id})


class DocumentDeleteView(OrganisorRequiredMixin, DeleteView):
    template_name = "document_delete.html"

    def get_queryset(self):
        user = self.request.user
        return Document.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        return reverse("leads:document-list")



#def listDocuments(request):
#    document = Document.objects.all()
#
#    ordering = request.GET.get('ordering', "")
#
#    if ordering:
#        document = document.order_by(ordering)
#
#    page = request.GET.get('page', 1)
#    documents_paginator = Paginator(document, DOCUMENTS_PER_PAGE)
#
#    try:
#        document = documents_paginator.page(page)
#    except EmptyPage:
#        document = documents_paginator.page(documents_paginator.num_pages)
#    except:
#        document = documents_paginator.page(DOCUMENTS_PER_PAGE)
#
#    return render(request, "document_list.html", {"documents": document, "page_obj": document, "is_paginated":True, "paginator":documents_paginator})


# def  landing_page(request):
#     return render(request, 'landing.html')


# def lead_list(request):
#     leads = Lead.objects.all()

#     context = {
#         "leads": leads
#     }

#     return render(request, "lead_list.html", context)


# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)

#     context = {
#         'lead': lead
#     }

#     return render(request, "lead_details.html", context)


# def lead_create(request):
#     form = LeadModelForm()

#     if request.method == "POST":
#         form = LeadModelForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect("/leads")

#     context = {
#         'form': form
#     }

#     return render(request, "lead_create.html", context)


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)

#     if request.method == "POST":
#         form = LeadModelForm(request.POST, instance=lead)

#         if form.is_valid():
#             form.save()
#             return redirect('/leads')
    
#     context = {
#         'form': form,
#         'lead': lead
#     }

#     return render(request, "lead_update.html", context)


# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()

#     return redirect("/leads")

# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()

#     if request.method == 'POST':
#         form = LeadForm(request.POST)

#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']

#             lead.first_name=first_name
#             lead.last_name=last_name
#             lead.age=age
#             lead.save()
            
#             return redirect('/leads')

#     context = {
#         'form': form,
#         'lead': lead
#     }

#     return render(request, "lead_update.html", context)


# def lead_create(request):
#     form = LeadModelForm()

#     if request.method == "POST":
#         form = LeadModelForm(request.POST)

#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
            
#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent=agent
#             )

#             return redirect("/leads")

#     context = {
#         'form': form
#     }

#     return render(request, "lead_create.html", context)