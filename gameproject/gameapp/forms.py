from django import forms
from .models import GameModel
from .models import CollectorModel


class GameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        exclude = ['collector']

    def clean_dateMade(self):
        dateMadeData = self.cleaned_data['dateMade']
        if '0000-00-00' in dateMadeData:
            raise forms.ValidationError('enter valid date')

        return dateMadeData

    def clean_ageLimit(self):
        ageLimitData = self.cleaned_data['ageLimit']
        if ageLimitData < 13:
            raise forms.ValidationError("must be 13 or older")
        return ageLimitData


class CollectorForm(forms.ModelForm):
    class Meta:
        model = CollectorModel
        exclude = ['userTableForeignKey']
