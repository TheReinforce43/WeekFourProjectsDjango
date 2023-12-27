from . models import Musician
from django import forms 


class MusicianForm(forms.ModelForm):

    class Meta:

        fields='__all__'
        model=Musician

        widgets={
            'Email':forms.EmailInput(attrs={'maxlength':50}),
        }
        labels={
            'FirstName':'First Name',
            'LastName':'Last Name',

        }

        help_text={
            'InstrumentType':'select type of instrument',
            
        }
