from django.shortcuts import render, reverse
from django.views import generic
from django.core.mail import send_mail
from leads.models import Agent
from .mixins import OrganisorRequiredMixin
from .forms import AgentModelForm
from secrets import randbelow


class AgentListView(OrganisorRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    context_object_name = "agents"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentCreateView(OrganisorRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self) -> str:
        return reverse("agents:agent-list")
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.set_password(''.join([str(randbelow(10000)) for i in range(20)]))
        user.save()

        Agent.objects.create(
            user = user,
            organisation=self.request.user.userprofile,
        )

        send_mail(
            from_email="admin@test.com",
            recipient_list=[user.email],
            subject="You are invited to be an Agent",
            message="You were added as an agent on Ingot CRM."
        )

        # agent.organisation = self.request.user.userprofile
        # agent.save()
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(OrganisorRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentUpdateView(OrganisorRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm
    context_object_name = "agent"
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        queryset = Agent.objects.filter(organisation=organisation)
        return queryset

    def get_success_url(self) -> str:
        return reverse("agents:agent-detail")
    

class AgentDeleteView(OrganisorRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name = "agent"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    def get_success_url(self) -> str:
        return reverse("agents:agent-list")