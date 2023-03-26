from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.views.generic import (
    TemplateView, ListView, DetailView, 
    CreateView, DeleteView, UpdateView, FormView)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Lead, Agent, Category, Document
from .forms import (
    LeadForm, LeadModelForm,
    CustomUserCreationForm, AssignAgentForm,
    LeadCategoryUpdateForm, UploadDocumentModelForm, )
from .filters import DocumentFilter
from agents.mixins import OrganisorRequiredMixin


DOCUMENTS_PER_PAGE = 2
LEADS_PER_PAGE = 2


class LandingPageView(TemplateView):
    template_name = "landing.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class PricingPageView(TemplateView):
    template_name = "pricing.html"


class LeadListView(LoginRequiredMixin, ListView):
    template_name = "lead_list.html"
    context_object_name = "leads"
    paginate_by = LEADS_PER_PAGE

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile, agent__isnull=False)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation, agent__isnull=False)
            queryset = Lead.objects.filter(agent__user=user)
        
        queryset.order_by("-date_added")

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

    def get_form(self, form_class=LeadModelForm):
        form = super().get_form(form_class)
        user = self.request.user

        if user.is_organisor:
            form.fields['agent'].queryset = Agent.objects.filter(organisation=user.userprofile)
            form.fields['category'].queryset = Category.objects.filter(organisation=user.userprofile)
        else:
            form.fields['category'].queryset = Category.objects.filter(organisation=user.agent.organisation)
            form.fields['agent'].queryset = Agent.objects.filter(user=user)

        return form

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        lead = form.save(commit=False)
        user = self.request.user

        if user.is_organisor:
            lead.organisation = user.userprofile
        else:
            lead.organisation = user.agent.organisation
        
        lead.save()
        
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )

        form.instance.organisation = lead.organisation
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
    
    def get_form(self, form_class=LeadModelForm):
        form = super().get_form(form_class)
        user = self.request.user

        if user.is_organisor:
            form.fields['agent'].queryset = Agent.objects.filter(organisation=user.userprofile)
            form.fields['category'].queryset = Category.objects.filter(organisation=user.userprofile)
        else:
            form.fields['category'].queryset = Category.objects.filter(organisation=user.agent.organisation)
            form.fields['agent'].queryset = Agent.objects.filter(user=user)

        return form
    
    def form_valid(self, form):
        lead = form.save(commit=False)
        user = self.request.user

        if user.is_organisor:
            lead.organisation = user.userprofile
        else:
            lead.organisation = user.agent.organisation
        
        lead.save()

        form.instance.organisation = lead.organisation
        return super(LeadUpdateView, self).form_valid(form)

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
            leads = Lead.objects.filter(organisation=user.userprofile)
        else:
            leads = Lead.objects.filter(organisation=user.agent.organisation)

        context.update({
            "leads": leads,
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
    
    def get_form(self, form_class=LeadCategoryUpdateForm):
        form = super().get_form(form_class)
        user = self.request.user

        if user.is_organisor:
            form.fields['category'].queryset = Category.objects.filter(organisation=user.userprofile)
        else:
            form.fields['category'].queryset = Category.objects.filter(organisation=user.agent.organisation)

        return form
    
    def form_valid(self, form):
        category = form.save(commit=False)
        user = self.request.user

        if user.is_organisor:
            category.organisation = user.userprofile
        else:
            category.organisation = user.agent.organisation
        
        category.save()

        form.instance.organisation = category.organisation
        return super(LeadCategoryUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("leads:lead-detail", kwargs={"pk": self.get_object().id})


class SignupView(CreateView):
    template_name = "registration/register.html"
    form_class = CustomUserCreationForm

    def get_success_url(self) -> str:
        return reverse("login")


class DocumentListView(LoginRequiredMixin, ListView):
    #queryset = Document.objects.all()
    template_name = "document_list.html"
    context_object_name = "documents"

    paginate_by = DOCUMENTS_PER_PAGE


    def get_queryset(self):
        #queryset = super().get_queryset()
        user = self.request.user

        if user.is_organisor:
            queryset = Document.objects.filter(organisation=user.userprofile)
        else:
            queryset = Document.objects.filter(organisation=user.agent.organisation, is_secret=False)
        
        self.filterset = DocumentFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        return context 


class DocumentDetailView(LoginRequiredMixin, DetailView):
    template_name = "document_detail.html"
    context_object_name = "document"

    def get_queryset(self):
        user = self.request.user

        if user.is_organisor:
            queryset = Document.objects.filter(organisation=user.userprofile)
        else:
            queryset = Document.objects.filter(organisation=user.agent.organisation)
        
        return queryset


class DocumentUploadView(LoginRequiredMixin, CreateView):
    template_name = "upload_document.html"
    form_class = UploadDocumentModelForm

    def get_success_url(self) -> str:
        return reverse("leads:document-list")

    def get_form(self, form_class=UploadDocumentModelForm):
        form = super().get_form(form_class)
        user = self.request.user

        if user.is_organisor:
            form.fields['lead'].queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            form.fields['lead'].queryset = Lead.objects.filter(organisation=user.agent.organisation)

        return form
    
    def form_valid(self, form):
        document = form.save(commit=False)
        user = self.request.user

        if user.is_organisor:
            document.organisation = user.userprofile
        else:
            document.organisation = user.agent.organisation
        
        document.save()
        form.instance.organisation = document.organisation
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
        
        return queryset
    
    def get_form(self, form_class=UploadDocumentModelForm):
        form = super().get_form(form_class)
        user = self.request.user

        if user.is_organisor:
            form.fields['lead'].queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            form.fields['lead'].queryset = Lead.objects.filter(organisation=user.agent.organisation)

        return form
    
    def form_valid(self, form):
        document = form.save(commit=False)
        user = self.request.user

        if user.is_organisor:
            document.organisation = user.userprofile
        else:
            document.organisation = user.agent.organisation
        
        document.save()
        form.instance.organisation = document.organisation
        return super(DocumentUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("leads:document-detail", kwargs={"pk": self.get_object().id})


class DocumentDeleteView(OrganisorRequiredMixin, DeleteView):
    model = Document
    template_name = "document_delete.html"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        file_field = self.object.file
        if file_field:
            file_field.delete()
        return super(DocumentDeleteView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("leads:document-list")
