from django import forms
from .models import ChildGeneralist, ChildPresenter

class ChildGeneralistForm(forms.ModelForm):
    class Meta:
        model = ChildGeneralist
        fields = ['name', 'father_name', 'mother_name', 'student_class', 'district', 'phone_no']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['district'].required = True  # Make sure district is required

class ChildPresenterForm(forms.ModelForm):
    class Meta:
        model = ChildPresenter
        fields = ['name', 'father_name', 'mother_name', 'student_class', 'district', 'phone_no']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['district'].required = True  # Make sure district is required
