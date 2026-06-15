from django.shortcuts import render
from .f1_service import obtener_resultados_corrida, obter_calendario_2025

def dashboard_f1(request):
    """
    View principal que renderiza a tabela com o grid de largada e chegada.
    Permite filtrar por pista através de parâmetros na URL (?pista=Monaco Grand Prix).
    """
    # Define 'Bahrain Grand Prix' como o padrão caso nenhuma pista seja selecionada
    pista_selecionada = request.GET.get('pista', 'Bahrain Grand Prix')
    
    # Busca todas as pistas da temporada de 2025 dinamicamente
    lista_pistas = obter_calendario_2025()
    
    # Busca os dados da corrida selecionada
    dados_corrida = obtener_resultados_corrida(ano=2025, pista=pista_selecionada)
    
    context = {
        'resultados': dados_corrida,
        'pista_atual': pista_selecionada,
        'pistas': lista_pistas
    }
    
    return render(request, 'analisador/dashboard.html', context)
