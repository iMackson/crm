from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm


class LandingPageView(TemplateView):
    template_name = "landing.html"


def landing_page(request):
    return render(request, "landing.html")


class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"  # object_list is default context_object_name


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)


class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


def lead_detail(request, pk):
    lead = Lead.objects.get(pk=pk)
    context = {
        'lead': lead
    }
    return render(request, "leads/lead_detail.html", context)


class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self) -> str:
        return reverse("leads:lead-detail", args=(self.object.pk,))


def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)


def lead_update(request, pk):
    lead = Lead.objects.get(pk=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('leads:lead-detail', args=(lead.pk,)))
    context = {
        'lead': lead,
        'form': form
    }
    return render(request, 'leads/lead_update.html', context)


def lead_delete(request, pk):
    lead = Lead.objects.get(pk=pk)
    lead.delete()
    return redirect("/leads")


# def lead_update(request, pk):
#     lead = Lead.objects.get(pk=pk)
#     form = LeadForm()
#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             # return redirect('leads:detail', args=(lead.pk,))
#             return HttpResponseRedirect(reverse('leads:detail', args=(lead.pk,)))
#     context = {
#         'lead': lead,
#         'form': form
#     }
#     return render(request, "leads/lead_update.html", context)


# def lead_create(request):
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
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
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)
