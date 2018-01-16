from django.contrib import admin
from django.conf.urls import url
from issuetracker.views import StatView
from issuetracker.views import IssueListView,FormView,IssueUpdateView


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', StatView.as_view(), name='stat_view'),
    url(r'^(?P<slug>\w+)/$', IssueListView.as_view()),
    url(r'^/create/$', FormView.as_view(), name='create_issue'),
    url(regex=r'^issues/edit/(?P<issue_id>\d+)/$',
        view=IssueUpdateView.as_view(),
        name='issue-update')
]