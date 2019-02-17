from django import forms

from apps.system.models import Constituency, Party, Vote


class NetaChoiceForm(forms.Form):
    party = forms.ModelChoiceField(queryset=Party.objects.all(), label='Select Party', required=True)
    constituency = forms.ModelChoiceField(queryset=Constituency.objects.all(), label='Select Lok Sabha', required=True)


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = [
            'party', 'constituency',
        ]
