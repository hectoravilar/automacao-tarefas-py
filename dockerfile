
# usa uma imagem base do python 3.9 mais leve (slim)
FROM python:3.9-slim

# definindo o diretorio de trabalho dentro do container
WORKDIR /app

# instalando as dependencias do sistema necessarias para o chrome e selenium
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    unzip \
    # adicionando  a chave de assinatura do google chrome
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg \
    # adicionando o repositório do chrome à lista de fontes
    && echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    # instalando o google chrome estável
    && apt-get install -y google-chrome-stable --no-install-recommends \
    # limpando o cache do apt para reduzir o tamanho da imagem
    && rm -rf /var/lib/apt/lists/*

# baixando e instalando o chromedriver compativel com a versão do chrome
RUN wget -q https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.127/linux64/chromedriver-linux64.zip \
    && unzip chromedriver-linux64.zip \
    # movendo o chromedriver para um local acessível globalmente
    && mv chromedriver-linux64/chromedriver /usr/bin/chromedriver \
    # tornando o chromedriver executável
    && chmod +x /usr/bin/chromedriver \
    # removendo os arquivos temporários
    && rm -rf chromedriver-linux64.zip chromedriver-linux64

# copia o arquivo de dependências python primeiro (para aproveitar o cache do docker)
COPY requirements.txt .
# instalando as dependências python sem cache para reduzir o tamanho
RUN pip install --no-cache-dir -r requirements.txt

# copiando todo o código da aplicação para o container
COPY . .

# definindo o comando padrão que será executado quando o container iniciar
CMD ["python", "auto.py"]
