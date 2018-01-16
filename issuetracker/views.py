
from django.shortcuts import render
from django.views import View
from .models import Issue
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from .forms import CreateIssueForm
import datetime
from datetime import timedelta
from django.views.generic.edit import UpdateView
from django.views.generic.edit import FormView
from issuetracker.forms import CreateIssueForm

# Create your views here.


class IssueListView(ListView):
    template_name = 'issuetracker/issue_list.html'

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug == 'open':
            queryset = Issue.objects.filter(status__iexact="assigned")
        else:
            queryset = Issue.objects.all()
        return queryset


class StatView(View):

    def get(self,request):
        if Issue.objects.filter(status__iexact="closed").exists():
            closed_lst = []
            seconds = []
            idx = 0
            count = 0
            queryset = Issue.objects.filter(status__iexact="closed")
            for tkt in queryset:
                count = count + 1
                times1 = queryset.order_by().values_list('updated').distinct()
                times = queryset.order_by().values_list('opened').distinct()
                final = times1[idx][0] - times[idx][0]
                sec = final / timedelta(seconds=1)
                idx = idx + 1
                seconds.append(sec)
            mx = max(seconds)
            mn = min(seconds)
            av = sum(seconds) / len(seconds)
            maximum = (str(mx * timedelta(seconds=1)).split('.')[0])
            minimum = (str(mn * timedelta(seconds=1)).split('.')[0])
            average = (str(av * timedelta(seconds=1)).split('.')[0])
            all_docs = len(Issue.objects.all()) - count

            return render(request,"issuetracker/main.html",{
                'maximum':maximum,
                'minimum':minimum,
                'average':average,
                'count':count,
                'all_docs':all_docs
            })
        elif Issue.objects.filter(status__iexact="assigned").exists():
            all_docs = len(Issue.objects.all())

            return render(request, "issuetracker/main.html", {
                'count': 0,
                'all_docs': all_docs
            })



class FormView(FormView):
    template_name = 'issuetracker/form.html'
    form_class = CreateIssueForm
    success_url = '/issue/'

    def form_valid(self, form):
        obj = Issue.objects.create(
            submitter=form.cleaned_data.get('submitter'),
            description=form.cleaned_data.get('description'),
            status=form.cleaned_data['status'],
            category=form.cleaned_data.get('category'),
        )
        return super().form_valid(form)



class IssueUpdateView(UpdateView):
    context_object_name = 'issue-update'
    form_class = CreateIssueForm
    template_name = 'issuetracker/update.html'
    success_url = '/issues/'

    # get object
    def get_object(self,queryset=None):
        return Issue.objects.get(id=self.kwargs["issue_id"])


    # override form_valid method
    def form_valid(self, form):
        # save cleaned post data
        clean = form.cleaned_data
        context = {}
        return super(IssueUpdateView, self).form_valid(form)
