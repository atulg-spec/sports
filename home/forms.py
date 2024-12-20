from django import forms
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'team_leader', 'player_two', 'player_three', 'player_four']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'Enter your team name'}),
            'team_leader': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'In game Unique Id.'}),
            'player_two': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'In game Unique Id.'}),
            'player_three': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'In game Unique Id.'}),
            'player_four': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500', 'placeholder': 'In game Unique Id.'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'w-full px-4 py-2 border rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
