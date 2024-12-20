from django import forms
from .models import Team
from django.core.exceptions import ValidationError

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'team_leader', 'player_two', 'player_three', 'player_four']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 text-gray-800', 'placeholder': 'Enter your team name'}),
            'team_leader': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 text-gray-800', 'placeholder': 'In game Unique Id.'}),
            'player_two': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 text-gray-800', 'placeholder': 'In game Unique Id.'}),
            'player_three': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 text-gray-800', 'placeholder': 'In game Unique Id.'}),
            'player_four': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 text-gray-800', 'placeholder': 'In game Unique Id.'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'w-full px-4 py-2 border rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 text-gray-800'


class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(max_length=10, min_length=10)

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise ValidationError("The phone number must only contain digits.")
        if len(phone_number) != 10:
            raise ValidationError("Please enter a valid 10-digit phone number.")
        return phone_number
