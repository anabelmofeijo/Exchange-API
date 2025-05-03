# Usa a imagem oficial do Playwright com Python 3.12
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia todo o código para dentro do container
COPY . .

# Instala todas as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Adiciona no Dockerfile, antes do CMD
RUN playwright install --with-deps

# Expõe a porta 5000 (opcional)
EXPOSE 5000

# Comando para rodar a app com Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
