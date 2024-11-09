from recomendacoes.models import TipoSolo

def populate_all_solos():
    tipos_de_solo = [
        {
            'nome': 'Latossolos',
            'ph_min': 5.5, 'ph_max': 6.5,
            'mo_min': 2, 'mo_max': 3,
            'fosforo_min': 10, 'fosforo_max': 15,
            'potassio_min': 0.15, 'potassio_max': 0.3,
            'calcio_min': 2, 'calcio_max': 4,
            'magnesio_min': 0.5, 'magnesio_max': 1.5,
            'saturacao_bases': 50,
        },
        {
            'nome': 'Argissolos',
            'ph_min': 5.0, 'ph_max': 6.0,
            'mo_min': 2, 'mo_max': 3,
            'fosforo_min': 8, 'fosforo_max': 12,
            'potassio_min': 0.1, 'potassio_max': 0.25,
            'calcio_min': 1.5, 'calcio_max': 3.5,
            'magnesio_min': 0.3, 'magnesio_max': 1.0,
            'saturacao_bases': 45,
        },
        {
            'nome': 'Neossolos',
            'ph_min': 5.5, 'ph_max': 6.5,
            'mo_min': 1, 'mo_max': 2,
            'fosforo_min': 5, 'fosforo_max': 10,
            'potassio_min': 0.05, 'potassio_max': 0.2,
            'calcio_min': 1.0, 'calcio_max': 2.5,
            'magnesio_min': 0.2, 'magnesio_max': 0.8,
            'saturacao_bases': 40,
        },
        {
            'nome': 'Cambissolos',
            'ph_min': 5.5, 'ph_max': 6.0,
            'mo_min': 2, 'mo_max': 4,
            'fosforo_min': 8, 'fosforo_max': 15,
            'potassio_min': 0.15, 'potassio_max': 0.3,
            'calcio_min': 1.5, 'calcio_max': 4.0,
            'magnesio_min': 0.3, 'magnesio_max': 1.2,
            'saturacao_bases': 50,
        },
        {
            'nome': 'Nitossolos',
            'ph_min': 5.5, 'ph_max': 6.5,
            'mo_min': 2, 'mo_max': 3,
            'fosforo_min': 10, 'fosforo_max': 20,
            'potassio_min': 0.2, 'potassio_max': 0.35,
            'calcio_min': 3.0, 'calcio_max': 5.0,
            'magnesio_min': 0.5, 'magnesio_max': 1.5,
            'saturacao_bases': 60,
        },
        {
            'nome': 'Planossolos',
            'ph_min': 5.0, 'ph_max': 6.0,
            'mo_min': 2, 'mo_max': 3,
            'fosforo_min': 8, 'fosforo_max': 12,
            'potassio_min': 0.1, 'potassio_max': 0.25,
            'calcio_min': 1.5, 'calcio_max': 3.5,
            'magnesio_min': 0.3, 'magnesio_max': 1.0,
            'saturacao_bases': 45,
        },
        {
            'nome': 'Gleissolos',
            'ph_min': 5.0, 'ph_max': 5.5,
            'mo_min': 3, 'mo_max': 5,
            'fosforo_min': 5, 'fosforo_max': 10,
            'potassio_min': 0.05, 'potassio_max': 0.2,
            'calcio_min': 1.0, 'calcio_max': 2.0,
            'magnesio_min': 0.2, 'magnesio_max': 0.8,
            'saturacao_bases': 40,
        },
        {
            'nome': 'Chernossolos',
            'ph_min': 6.0, 'ph_max': 6.5,
            'mo_min': 3, 'mo_max': 6,
            'fosforo_min': 15, 'fosforo_max': 25,
            'potassio_min': 0.3, 'potassio_max': 0.5,
            'calcio_min': 3.5, 'calcio_max': 5.5,
            'magnesio_min': 0.8, 'magnesio_max': 1.5,
            'saturacao_bases': 65,
        },
    ]

    # Insere cada tipo de solo no banco de dados
    for solo in tipos_de_solo:
        TipoSolo.objects.update_or_create(nome=solo['nome'], defaults=solo)

    print("Todos os tipos de solo foram inseridos com sucesso.")

# Chama a função para inserir os dados
populate_all_solos()
