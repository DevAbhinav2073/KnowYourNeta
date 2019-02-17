from django import forms

from apps.system.models import Constituency, Party, Vote


class NetaChoiceForm(forms.Form):
    party = forms.ModelChoiceField(queryset=Party.objects.all(), required=True)
    postal_code = forms.CharField(max_length=30, required=False)
    constituency = forms.ModelChoiceField(queryset=Constituency.objects.all(), required=True)
    name = forms.CharField(max_length=60, required=False)


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = [
            'party', 'constituency',
        ]
