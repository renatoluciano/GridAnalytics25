import fastf1
import os

# Configura o diretório de cache persistente mapeado via Docker
CACHE_DIR = '/app/data_cache'
if os.path.exists(CACHE_DIR):
    fastf1.Cache.enable_cache(CACHE_DIR)

def obtener_resultados_corrida(ano=2025, pista='Bahrain', sessao='R'):
    """
    Busca os dados de uma corrida específica de F1.
    'R' indica a sessão de Corrida (Race).
    """
    try:
        # Carrega a sessão sem dados pesados de telemetria/clima para ser mais rápido
        session = fastf1.get_session(ano, pista, sessao)
        session.load(laps=False, telemetry=False, weather=False)
        
        resultados = []
        nome_pista = session.event['EventName']
        
        # Iterar sobre a tabela oficial de resultados
        for _, row in session.results.iterrows():
            pos_largada = int(row['GridPosition'])
            pos_chegada = int(row['Position'])
            
            resultados.append({
                'piloto': row['FullName'],
                'equipe': row['TeamName'],
                'pista': nome_pista,
                'largada': pos_largada,
                'chegada': pos_chegada,
                'variacao': pos_largada - pos_chegada  # Positivo = ganhou posições, Negativo = perdeu
            })
            
        return resultados
    except Exception as e:
        print(f"Erro ao coletar dados da FastF1: {e}")
        return []
