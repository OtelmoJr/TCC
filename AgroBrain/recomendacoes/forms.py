# recomendacoes/forms.py
from django import forms
from .models import TipoSolo

class AnaliseSoloForm(forms.Form):
    tipo_solo = forms.ModelChoiceField(queryset=TipoSolo.objects.all(), label="Tipo de Solo")
    ph = forms.FloatField(label="pH")
    mo = forms.FloatField(label="Matéria Orgânica (%)")
    fosforo = forms.FloatField(label="Fósforo (mg/dm³)")
    potassio = forms.FloatField(label="Potássio (cmolc/dm³)")
    calcio = forms.FloatField(label="Cálcio (cmolc/dm³)")
    magnesio = forms.FloatField(label="Magnésio (cmolc/dm³)")
    saturacao_bases = forms.IntegerField(label="Saturação por Bases (%)")
