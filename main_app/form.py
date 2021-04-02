from django.forms import ModelForm
from .models import Pouring


class PouringForm(ModelForm):
    class Meta:
        model = Pouring
        fields = ['date', 'pour']
