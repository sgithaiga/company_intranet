from django import forms
from .models import Applications

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Applications
        fields = ('name', 'Pf_no', 'job_applied_for', 'cover_letter', 
        	       'cv', 'certs')

