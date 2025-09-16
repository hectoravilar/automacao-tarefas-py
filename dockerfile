# pegando uma imagem oficial do Linux (Debian) que já venha com o Python 3.9 instalado.
FROM python:3.9-slim

# configurando o ambiente dentro do container
WORKDIR /app

# copinando arquivos para dentro do container
COPY . .

# instalando o Chrome
RUN apt-get uptade && apt get install -y \
    wget \
    gnupg \
    && wget -q -O -https:dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] https:google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google-chrome.list \
    && apt-get uptade && apt-get install -y google-chrome-stable \


# instalando as bibliotecas Python    
RUN pip install -r requirements.txt

# rodando script 
CMD ["python", "auto.py"]