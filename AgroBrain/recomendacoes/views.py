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

        def calcular_recomendacao(nutriente, valor_atual, min_ideal, max_ideal, recomendacao_base, justificativa):
            valor_atual, min_ideal, max_ideal = map(float, (valor_atual, min_ideal, max_ideal))
            deficit = max(min_ideal - valor_atual, 0)
            if deficit > 0:
                return {
                    "texto": f"{recomendacao_base(deficit)} {justificativa}",
                    "classe": "deficiencia"
                }
            return {
                "texto": f"{nutriente} está dentro do nível ideal.",
                "classe": "ideal"
            }

        recomendacoes.append(
            calcular_recomendacao(
                'pH',
                niveis_nutrientes['pH'],
                tipo_solo.ph_min,
                tipo_solo.ph_max,
                lambda deficit: f"PH: Adicione aproximadamente {round(deficit * 2, 1)} toneladas de calcário por hectare para ajuste de pH.",
                "O solo com pH adequado melhora a disponibilidade de nutrientes para as plantas e aumenta a eficiência da adubação."
            )
        )

        recomendacoes.append(
            calcular_recomendacao(
                'Matéria Orgânica',
                niveis_nutrientes['Matéria Orgânica'],
                tipo_solo.mo_min,
                tipo_solo.mo_max,
                lambda deficit: f"Matéria Orgânica: Adicionar {round(deficit * 10, 1)} toneladas de composto orgânico por hectare.",
                "A matéria orgânica melhora a retenção de água, estrutura do solo e fornece nutrientes gradualmente."
            )
        )

        recomendacoes.append(
            calcular_recomendacao(
                'Fósforo',
                niveis_nutrientes['Fósforo'],
                tipo_solo.fosforo_min,
                tipo_solo.fosforo_max,
                lambda deficit: f"Fósforo: Aplique aproximadamente {round(deficit * 50, 1)} kg de superfosfato por hectare.",
                "Sendo essencial para o crescimento das raízes e desenvolvimento inicial das plantas."
            )
        )

        recomendacoes.append(
            calcular_recomendacao(
                'Cálcio',
                niveis_nutrientes['Cálcio'],
                tipo_solo.calcio_min,
                tipo_solo.calcio_max,
                lambda deficit: f"Cálcio: Aplicação de {round(deficit * 1.5, 1)} toneladas de calcário dolomítico por hectare para aumentar o cálcio.",
                "O cálcio melhora a estrutura do solo e fortalece a parede celular das plantas."
            )
        )

        recomendacoes.append(
            calcular_recomendacao(
                'Magnésio',
                niveis_nutrientes['Magnésio'],
                tipo_solo.magnesio_min,
                tipo_solo.magnesio_max,
                lambda deficit: f"Magnésio: Para correção desse nutriente, adicionar {round(deficit * 100, 1)} kg de sulfato de magnésio por hectare.",
                "O magnésio é importante para a fotossíntese, pois faz parte da clorofila."
            )
        )

        recomendacoes.append(
            calcular_recomendacao(
                'Potássio',
                niveis_nutrientes['Potássio'],
                tipo_solo.potassio_min,
                tipo_solo.potassio_max,
                lambda deficit: f"Potássio: Adicione aproximadamente {round(deficit * 400, 1)} kg de cloreto de potássio por hectare para ajuste de potássio.",
                "O potássio ajuda na resistência a doenças e regula o equilíbrio hídrico das plantas."
            )
        )

        if niveis_nutrientes['Saturação por Bases'] < tipo_solo.saturacao_bases:
            recomendacoes.append(
                {
                    "texto": f"Saturação por Bases: deve atingir pelo menos {tipo_solo.saturacao_bases}%, a aplicação de calcário ajudará a alcançar esse valor. "
                             "A saturação por bases em um nível mais alto indica maior fertilidade do solo, favorecendo o crescimento saudável das plantas.",
                    "classe": "deficiencia"
                }
            )
        else:
            recomendacoes.append(
                {
                    "texto": "A saturação por bases está dentro do nível ideal.",
                    "classe": "ideal"
                }
            )

    return render(request, 'recomendacoes/gerar_recomendacao.html', {'form': form, 'recomendacoes': recomendacoes})







def home(request):
    return render(request, 'recomendacoes/home.html')
