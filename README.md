# API de Câmbio - Flask

Esta é uma API desenvolvida com Flask e SQLAlchemy para fornecer taxas de câmbio de três bancos de Angola: **BAI, BIC e Standard Bank**. A API utiliza **Playwright** para raspagem de dados, garantindo informações atualizadas. Além de consultar as taxas, também permite calcular valores convertidos entre moedas com base nas taxas de câmbio mais recentes.

## Funcionalidades
- Consulta de taxas de câmbio dos bancos suportados.
- Conversão de valores entre moedas.
- Atualização automática das taxas de câmbio via web scraping com Playwright.

## Tecnologias Utilizadas
- **Flask**: Framework web para desenvolvimento da API.
- **Flask-SQLAlchemy**: ORM para gerenciamento do banco de dados.
- **Playwright**: Ferramenta para raspagem de dados das taxas de câmbio.

