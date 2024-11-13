from django import forms
from .models import Study

class StudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = ['study_name', 'study_description', 'study_phase', 'sponsor_name','attachments']
        widgets = {
            'study_phase': forms.Select(choices=Study.STUDY_PHASE_CHOICES),
        }
