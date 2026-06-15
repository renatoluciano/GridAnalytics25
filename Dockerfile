FROM python:3.11-slim

# Evita que o Python escreva arquivos .pyc no disco
ENV PYTHONDONTWRITEBYTECODE=1
# Garante que os logs do console sejam exibidos imediatamente
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala dependências do sistema necessárias para o Pandas/FastF1
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Instala as dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . /app/

# Cria a pasta de cache para a biblioteca FastF1
RUN mkdir -p /app/data_cache

EXPOSE 8000
