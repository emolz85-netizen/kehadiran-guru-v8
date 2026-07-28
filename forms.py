from django import forms
from .models import LeaveRequest, OfficialDuty

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ["leave_type", "start_date", "end_date", "reason", "attachment"]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
            "reason": forms.Textarea(attrs={"rows": 4}),
        }

class OfficialDutyForm(forms.ModelForm):
    class Meta:
        model = OfficialDuty
        fields = ["title", "location", "start_date", "end_date", "description", "attachment"]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 4}),
        }


class TeacherImportForm(forms.Form):
    file = forms.FileField(
        label="Fail Excel guru",
        help_text="Gunakan templat SENARAI_GURU_TEMPLATE.xlsx."
    )
    default_password = forms.CharField(
        label="Kata laluan awal",
        widget=forms.PasswordInput,
        min_length=8,
        help_text="Kata laluan awal untuk akaun baharu."
    )
