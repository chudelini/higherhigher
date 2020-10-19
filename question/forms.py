from django import forms
from .models import Grade


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['candidate', 'recruiter', 'task', 'value']

    def clean(self):
        value = self.cleaned_data.get('value')

        # conditions to be met to pass the form
        if value < 0 or value > 5:
            self._errors['value'] = self.error_class([
                'Grade should be between 0 and 5'])

        # return any errors if found
        return self.cleaned_data