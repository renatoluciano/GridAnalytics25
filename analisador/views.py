from django.shortcuts import render
from .f1_service import obtener_resultados_corrida

def dashboard_f1(request):
    """
    View principal que renderiza a tabela com o grid de largada e chegada.
    Permite filtrar por pista através de parâmetros na URL (?pista=Bahrain).
    """
    # Define 'Bahrain' como a pista padrão caso nenhuma seja selecionada
    pista_selecionada = request.GET.get('pista', 'Bahrain')
    
    # Busca os dados da temporada de 2025 usando o nosso serviço
    dados_corrida = obtener_resultados_corrida(ano=2025, pista=pista_selecionada)
    
    context = {
        'resultados': dados_corrida,
        'pista': pista_selecionada
    }
    
    return render(request, 'analisador/dashboard.html', context)
