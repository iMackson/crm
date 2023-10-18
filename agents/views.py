import random
from django.urls import reverse
from django.views import generic
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin

from leads.models import Agent
from .forms import AgentModelForm
from .mixins import LoginRequiredAndOrganizerMixin


class AgentListView(LoginRequiredAndOrganizerMixin, generic.ListView):
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        return Agent.objects.filter(organization=self.request.user.userprofile)


class AgentCreateView(LoginRequiredAndOrganizerMixin, generic.CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self) -> str:
        return reverse('agents:agent-list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_organizer = False
        user.is_agent = True
        user.set_password(f"{random.randint(0, 1000000)}")
        user.save()
        Agent.objects.create(
            user=user,
            organization=self.request.user.userprofile
        )
        send_mail(
            subject="You were invited to be an agent",
            message="You were added as an agent on DJCRM. Please come login to start working.",
            from_email="noreply@crm.com",
            recipient_list=[user.email]
        )
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(LoginRequiredAndOrganizerMixin, generic.DetailView):
    template_name = 'agents/agent_detail.html'
    queryset = Agent.objects.all()
    context_object_name = 'agent'


class AgentUpdateView(LoginRequiredAndOrganizerMixin, generic.UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentModelForm
    context_object_name = 'agent'

    def get_queryset(self):
        return Agent.objects.all()

    def get_success_url(self):
        return reverse('agents:agent-list')


class AgentDeleteView(LoginRequiredAndOrganizerMixin, generic.DeleteView):
    template_name = 'agents/agent-delete.html'
    context_object_name = 'agent'

    def get_queryset(self):
        return Agent.objects.filter(organization=self.request.user.userprofile)

    def get_success_url(self):
        return reverse('agents:agent-list')
