# AutoTarefasPy

> RPA em Python para cadastro automatizado de produtos

## Sobre o Projeto

Script de automação web que realiza cadastro em massa de produtos usando Selenium WebDriver. Lê dados de um arquivo CSV e preenche formulários web automaticamente em modo headless.

## Arquivos do Projeto

- `auto.py` - Script principal de automação
- `debug_auto.py` - Script para debug e testes de conectividade
- `produtos.csv` - Arquivo com dados dos produtos para cadastro
- `requirements.txt` - Dependências Python
- `Dockerfile` - Configuração para containerização
- `docker-compose.yml` - Orquestração do container
- `.env.example` - Exemplo de variáveis de ambiente

## Dependências

```
pandas
selenium
python-dotenv
```

## Configuração

Crie um arquivo `.env` baseado no `.env.example`:
```env
LOGIN_EMAIL=seu_email@exemplo.com
LOGIN_SENHA=sua_senha_segura
```

## Como Funciona

### Script Principal (auto.py)
1. Configura Chrome em modo headless
2. Acessa página de login
3. Realiza login com credenciais do `.env`
4. Lê dados do `produtos.csv`
5. Para cada produto:
   - Preenche campos: codigo, marca, tipo, categoria, preco_unitario, custo, obs
   - Submete o formulário
   - Mostra progresso a cada 10 produtos
6. Salva screenshots em caso de erro

### Script de Debug (debug_auto.py)
- Testa conectividade com o site
- Verifica se elementos essenciais estão presentes
- Salva screenshot para análise se necessário

## Estrutura do CSV

O arquivo `produtos.csv` deve conter as colunas:
- `codigo` - Código do produto
- `marca` - Marca do produto
- `tipo` - Tipo do produto
- `categoria` - Categoria (numérica)
- `preco_unitario` - Preço unitário
- `custo` - Custo do produto
- `obs` - Observações (opcional)

## Execução

### Local
```bash
python auto.py
```

### Docker
```bash
docker-compose up --build
```

## Tratamento de Erros

- Screenshots automáticos salvos em `screenshots/`
- Logs de erro no console
- Parada do script em caso de falha crítica
- Timeout de 10 segundos para elementos da página