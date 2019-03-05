from django import forms
from .models import GameModel
from .models import CollectorModel
from django.shortcuts import redirect


class GameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        exclude = ['collector']

    # def clean_dateMade(self):
    #     dateMadeData = self.cleaned_data['dateMade']
    #     if '0000-00-00' in dateMadeData:
    #         raise forms.ValidationError('enter valid date')
    #
    #     return dateMadeData

    def clean_ageLimit(self):
        ageLimitData = self.cleaned_data['ageLimit']
        if ageLimitData < 13:
            raise forms.ValidationError("must be 13 or older")
        return ageLimitData


class CollectorForm(forms.ModelForm):
    class Meta:
        model = CollectorModel
        fields = ['username', 'password1', 'password2']

    # function that validates that passwords match


def clean_password(self):
    cleanPasswordData = self.cleaned_data['password2']
    if 'password1' != 'password2' in cleanPasswordData:
        raise forms.ValidationError('Passwords do not match! Re-enter!')
    else:
        return redirect('gameapp/mygames.html')
