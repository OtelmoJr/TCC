from django.shortcuts import render
from .models import TipoSolo
from .forms import AnaliseSoloForm
from django.shortcuts import render
from django.http import HttpResponse

def gerar_recomendacao_view(request):
    form = AnaliseSoloForm(request.POST or None)
    recomendacoes = []

    if form.is_valid():
        tipo_solo = form.cleaned_data['tipo_solo']
        niveis_nutrientes = {
            'pH': form.cleaned_data['ph'],
            'Matéria Orgânica': form.cleaned_data['mo'],
            'Fósforo': form.cleaned_data['fosforo'],
            'Potássio': form.cleaned_data['potassio'],
            'Cálcio': form.cleaned_data['calcio'],
            'Magnésio': form.cleaned_data['magnesio'],
            'Saturação por Bases': form.cleaned_data['saturacao_bases']
        }

        # Verificação de pH
        if not (tipo_solo.ph_min <= niveis_nutrientes['pH'] <= tipo_solo.ph_max):
            recomendacoes.append(f"Ajuste o pH para estar entre {tipo_solo.ph_min} e {tipo_solo.ph_max}.")

        # Verificação de Matéria Orgânica
        if not (tipo_solo.mo_min <= niveis_nutrientes['Matéria Orgânica'] <= tipo_solo.mo_max):
            recomendacoes.append(f"Matéria Orgânica ideal: {tipo_solo.mo_min}% - {tipo_solo.mo_max}%.")

        # Verificação de Fósforo
        if not (tipo_solo.fosforo_min <= niveis_nutrientes['Fósforo'] <= tipo_solo.fosforo_max):
            recomendacoes.append(f"Fósforo ideal: {tipo_solo.fosforo_min} - {tipo_solo.fosforo_max} mg/dm³.")

        # Verificação de Potássio
        if not (tipo_solo.potassio_min <= niveis_nutrientes['Potássio'] <= tipo_solo.potassio_max):
            recomendacoes.append(f"Potássio ideal: {tipo_solo.potassio_min} - {tipo_solo.potassio_max} cmolc/dm³.")

        # Verificação de Cálcio
        if not (tipo_solo.calcio_min <= niveis_nutrientes['Cálcio'] <= tipo_solo.calcio_max):
            recomendacoes.append(f"Cálcio ideal: {tipo_solo.calcio_min} - {tipo_solo.calcio_max} cmolc/dm³.")

        # Verificação de Magnésio
        if not (tipo_solo.magnesio_min <= niveis_nutrientes['Magnésio'] <= tipo_solo.magnesio_max):
            recomendacoes.append(f"Magnésio ideal: {tipo_solo.magnesio_min} - {tipo_solo.magnesio_max} cmolc/dm³.")

        # Verificação de Saturação por Bases
        if niveis_nutrientes['Saturação por Bases'] < tipo_solo.saturacao_bases:
            recomendacoes.append(f"Saturação por Bases ideal: ≥ {tipo_solo.saturacao_bases}%.")

    return render(request, 'recomendacoes/gerar_recomendacao.html', {'form': form, 'recomendacoes': recomendacoes})


def home(request):
    return HttpResponse("Bem-vindo à página inicial do AgroBrain!")