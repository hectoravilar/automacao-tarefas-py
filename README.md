# AutoTarefasPy

> RPA em Python para automação de cadastro de produtos

## Sobre o Projeto

Este projeto é uma solução de RPA (Robotic Process Automation) desenvolvida para automatizar o cadastro em massa de produtos em sistemas web. Utiliza Selenium para interagir com elementos da página de forma robusta, sem depender de coordenadas de tela, garantindo maior confiabilidade na automação.

O sistema foi projetado para ser executado em modo headless (sem interface gráfica), tornando-o ideal para execução em servidores ou containers Docker.

## Como Funciona

### Fluxo Principal
1. **Inicialização** - Configura o navegador Chrome em modo headless
2. **Autenticação** - Realiza login automático usando credenciais seguras
3. **Processamento** - Lê dados do CSV e processa produto por produto
4. **Cadastro** - Preenche formulários web automaticamente
5. **Monitoramento** - Gera logs e screenshots para acompanhamento

### Tratamento de Erros
- Screenshots automáticos quando ocorrem falhas
- Logs detalhados para debugging
- Parada graceful em caso de erros críticos
- Retry automático para elementos não encontrados

## Tecnologias e Arquitetura

### Stack Principal
- **Python 3.9+** - Linguagem principal
- **Selenium WebDriver** - Automação web 
- **Pandas** - Manipulação eficiente de dados CSV
- **Chrome Headless** - Navegação
- **Docker** - Containerização 

### Dependências
- `selenium` - Automação web
- `pandas` - Processamento de dados
- `python-dotenv` - Gerenciamento de variáveis de ambiente


## Configuração

### Variáveis de Ambiente
O projeto utiliza arquivo `.env` para gerenciar credenciais de forma segura:
```env
LOGIN_EMAIL=seu_email@exemplo.com
LOGIN_SENHA=sua_senha_segura
```

## Funcionalidades

### Automação Web
- ✅ Login automatizado com validação
- ✅ Preenchimento inteligente de formulários
- ✅ Navegação entre páginas
- ✅ Tratamento de elementos dinâmicos

### Processamento de Dados
- ✅ Leitura de arquivos CSV
- ✅ Validação de dados
- ✅ Processamento em lote
- ✅ Contador de progresso

### Monitoramento e Debug
- ✅ Screenshots automáticos em erros
- ✅ Logs estruturados
- ✅ Script de debug dedicado
- ✅ Verificação de conectividade

### DevOps e Infraestrutura
- ✅ Containerização completa
- ✅ Execução headless
- ✅ Variáveis de ambiente seguras
- ✅ Volumes persistentes para screenshots

## Casos de Uso

- **E-commerce** - Cadastro em massa de produtos
- **Sistemas ERP** - Migração de dados
- **Plataformas Web** - Automação de formulários
- **Testes Automatizados** - Validação de fluxos
