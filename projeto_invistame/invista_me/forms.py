from django.forms import ModelForm
from .models import Investimento

# creating model forms
class InvestimentoForm(ModelForm):
    class Meta:
        model = Investimento
        fields = '__all__'