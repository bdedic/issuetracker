from django import forms
from .models import Issue

class CreateIssueForm(forms.ModelForm):
    STATUS = (
        ('Assigned', 'Assigned'),
        ('Closed', 'Closed'),
    )
    CATEGORY = (
        ('Bug', 'Bug'),
        ('Enhancements', 'Enhancements'),
        ('Documentation', 'Documentation')
    )

    #submitter = forms.CharField(required=False)
    submitter = forms.CharField(required=False,label='',widget=forms.TextInput(attrs={'placeholder': 'Submitter'}))
    solver = forms.CharField(required=False,label='',widget=forms.TextInput(attrs={'placeholder': 'Solver'}))
    description = forms.CharField(required=False,label='',widget=forms.Textarea(attrs={'placeholder': 'Description'}),)
    status = forms.ChoiceField(required=False,choices=STATUS,label='')
    category = forms.ChoiceField(required=False,choices=CATEGORY,label='')


    class Meta:
        model = Issue
        fields = ('submitter', 'solver', 'description','status','category')