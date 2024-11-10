from django.shortcuts import render
from .models import TipoSolo
from .forms import AnaliseSoloForm
from django.http import HttpResponse

def gerar_recomendacao_view(request):
    form = AnaliseSoloForm(request.POST or None)
    recomendacoes = []

    if form.is_valid():
        tipo_solo = form.cleaned_data['tipo_solo']
        niveis_nutrientes = {
            'pH': float(form.cleaned_data['ph']),
            'Matéria Orgânica': float(form.cleaned_data.get('materia_organica', 0)),
            'Fósforo': float(form.cleaned_data.get('fosforo', 0)),
            'Cálcio': float(form.cleaned_data['calcio']),
            'Magnésio': float(form.cleaned_data['magnesio']),
            'Potássio': float(form.cleaned_data['potassio']),
            'Saturação por Bases': float(form.cleaned_data['saturacao_bases'])
        }

        # Função genérica de recomendação com base nos limites do tipo de solo
        def calcular_recomendacao(nutriente, valor_atual, min_ideal, max_ideal, recomendacao_base):
            valor_atual, min_ideal, max_ideal = map(float, (valor_atual, min_ideal, max_ideal))
            deficit = max(min_ideal - valor_atual, 0)  # Apenas valores abaixo do ideal são considerados
            if deficit > 0:
                return recomendacao_base(deficit)
            return None

        # Definir cada recomendação com base nos níveis de nutrientes e limites do tipo de solo selecionado
        recomendacoes.append(
            calcular_recomendacao('pH', niveis_nutrientes['pH'], tipo_solo.ph_min, tipo_solo.ph_max,
                                  lambda deficit: f"Adicione aproximadamente {round(deficit * 2, 1)} toneladas de calcário por hectare para ajuste de pH.")
        )

        recomendacoes.append(
            calcular_recomendacao('Matéria Orgânica', niveis_nutrientes['Matéria Orgânica'], tipo_solo.mo_min, tipo_solo.mo_max,
                                  lambda deficit: f"Adicionar {round(deficit * 10, 1)} toneladas de composto orgânico por hectare.")
        )

        recomendacoes.append(
            calcular_recomendacao('Fósforo', niveis_nutrientes['Fósforo'], tipo_solo.fosforo_min, tipo_solo.fosforo_max,
                                  lambda deficit: f"Aplique aproximadamente {round(deficit * 50, 1)} kg de superfosfato por hectare.")
        )

        recomendacoes.append(
            calcular_recomendacao('Cálcio', niveis_nutrientes['Cálcio'], tipo_solo.calcio_min, tipo_solo.calcio_max,
                                  lambda deficit: f"Aplicação de {round(deficit * 1.5, 1)} toneladas de calcário dolomítico por hectare para aumentar o cálcio.")
        )

        recomendacoes.append(
            calcular_recomendacao('Magnésio', niveis_nutrientes['Magnésio'], tipo_solo.magnesio_min, tipo_solo.magnesio_max,
                                  lambda deficit: f"Para correção de magnésio, adicionar {round(deficit * 100, 1)} kg de sulfato de magnésio por hectare.")
        )

        recomendacoes.append(
            calcular_recomendacao('Potássio', niveis_nutrientes['Potássio'], tipo_solo.potassio_min, tipo_solo.potassio_max,
                                  lambda deficit: f"Adicione aproximadamente {round(deficit * 400, 1)} kg de cloreto de potássio por hectare para ajuste de potássio.")
        )

        # Após as correções acima, recomenda-se observar a saturação por bases
        if niveis_nutrientes['Saturação por Bases'] < tipo_solo.saturacao_bases:
            recomendacoes.append(f"A saturação por bases deve atingir pelo menos {tipo_solo.saturacao_bases}%. Realize as correções para alcançar esse valor.")

        # Remover None (sem recomendação) e exibir apenas recomendações relevantes
        recomendacoes = [rec for rec in recomendacoes if rec]

    return render(request, 'recomendacoes/gerar_recomendacao.html', {'form': form, 'recomendacoes': recomendacoes})






def home(request):
    return render(request, 'recomendacoes/home.html')
