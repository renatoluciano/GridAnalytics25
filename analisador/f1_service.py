import fastf1
import os

# Configura o diretório de cache persistente que mapeamos via Docker
CACHE_DIR = '/app/data_cache'
if os.path.exists(CACHE_DIR):
    fastf1.Cache.enable_cache(CACHE_DIR)

def obter_calendario_2025():
    """
    Retorna uma lista com o nome de todas as pistas válidas da temporada de 2025.
    """
    try:
        # Carrega o calendário oficial completo do ano solicitado
        calendario = fastf1.get_event_schedule(2025)
        # Filtra para remover sessões de testes (mantém apenas GPs oficiais)
        GPs = calendario[calendario['EventFormat'] != 'testing']
        return GPs['EventName'].tolist()
    except Exception as e:
        print(f"Erro ao buscar calendário: {e}")
        # Fallback seguro caso a API falhe ou esteja fora do ar
        return ['Bahrain Grand Prix', 'Saudi Arabian Grand Prix', 'Australian Grand Prix', 'Monaco Grand Prix']

def obtener_resultados_corrida(ano=2025, pista='Bahrain Grand Prix', sessao='R'):
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
        print(f"Erro ao coletar dados da FastF1 para a pista {pista}: {e}")
        return []
