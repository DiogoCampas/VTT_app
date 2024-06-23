from django import forms
from .models import MedicalImage, TestResult

class MedicalImageForm(forms.ModelForm):
    class Meta:
        model = MedicalImage
        fields = ('title', 'image')

class TestResultForm(forms.ModelForm):
    class Meta:
        model = TestResult
        fields = ('clinician_name', 'diagnosis', 'confidence')