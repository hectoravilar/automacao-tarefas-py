# AutoTarefasPy

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> RPA (Robotic Process Automation) containerizado para automação de cadastro de produtos em sistemas web

## 📋 Sobre o Projeto

Solução de automação web desenvolvida com foco em DevOps e boas práticas de desenvolvimento. O sistema automatiza o processo completo de login e cadastro em massa de produtos, utilizando containerização Docker para garantir portabilidade e consistência entre ambientes.

### Funcionalidades

- ✅ Login automatizado com credenciais seguras
- ✅ Cadastro em massa via arquivo CSV
- ✅ Execução headless (sem interface gráfica)
- ✅ Screenshots para debug e monitoramento
- ✅ Tratamento robusto de erros
- ✅ Containerização completa com Docker

## 🛠️ Stack Tecnológica

| Tecnologia | Versão | Propósito |
|------------|--------|----------|
| **Python** | 3.9+ | Runtime principal |
| **Selenium** | Latest | Automação web |
| **Pandas** | Latest | Manipulação de dados CSV |
| **Docker** | Latest | Containerização |
| **Chrome Headless** | Latest | Browser engine |

## 🚀 Quick Start

### Pré-requisitos

- Docker e Docker Compose instalados
- Arquivo `.env` configurado (veja [Configuração](#configuração))
- Arquivo `produtos.csv` com os dados

### Instalação

```bash
# Clone o repositório
git clone <repository-url>
cd autotarefaspy

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env com suas credenciais

# Execute com Docker Compose
docker-compose up --build
```

## ⚙️ Configuração

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
LOGIN_EMAIL=seu_email@exemplo.com
LOGIN_SENHA=sua_senha_segura
```

### Formato do CSV

O arquivo `produtos.csv` deve seguir o formato:

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
PROD001,Marca A,Tipo 1,1,29.90,15.00,Observação opcional
PROD002,Marca B,Tipo 2,2,45.50,25.00,
```

## 🐳 Docker

### Execução Local

```bash
# Build da imagem
docker build -t autotarefaspy .

# Execução do container
docker run -v $(pwd)/screenshots:/app/screenshots autotarefaspy
```

### Docker Compose

```bash
# Execução completa
docker-compose up

# Execução em background
docker-compose up -d

# Logs em tempo real
docker-compose logs -f
```

## 🔧 Debug e Monitoramento

### Script de Debug

```bash
# Teste de conectividade
python debug_auto.py
```

### Screenshots

Todos os screenshots são salvos em `./screenshots/`:
- `debug_page_load.png` - Página carregada
- `erro_login.png` - Erros de login
- `erro_produto_X.png` - Erros específicos por produto

## 📁 Estrutura do Projeto

```
autotarefaspy/
├── auto.py              # Script principal
├── debug_auto.py        # Script de debug
├── produtos.csv         # Dados dos produtos
├── requirements.txt     # Dependências Python
├── Dockerfile          # Configuração do container
├── docker-compose.yml  # Orquestração Docker
├── .env               # Variáveis de ambiente (criar)
├── .gitignore         # Arquivos ignorados pelo Git
└── screenshots/       # Screenshots de debug
```

## 🔒 Segurança

- ✅ Credenciais gerenciadas via variáveis de ambiente
- ✅ Arquivo `.env` não versionado
- ✅ Execução em container isolado
- ✅ Sem hardcoding de senhas no código

## 📊 Monitoramento

- Logs estruturados com informações de progresso
- Screenshots automáticos em caso de erro
- Contador de produtos processados
- Tratamento graceful de falhas

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📝 License

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**Desenvolvido com foco em DevOps e automação eficiente** 🚀