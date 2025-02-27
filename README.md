
# 📊 API de Câmbio - Flask

Esta API foi desenvolvida em **Flask** para consultar e converter taxas de câmbio de três bancos angolanos: **BAI**, **BIC** e **Standard Bank**.  
A API utiliza **Playwright** para buscar as taxas diretamente dos sites oficiais dos bancos, garantindo dados atualizados.

---

## 📌 Funcionalidades

✅ Obter taxas de câmbio atualizadas dos bancos: BAI, BIC e Standard Bank.  
✅ Consultar a taxa de câmbio específica de uma moeda.  
✅ Realizar conversões de valores entre moedas diretamente pela API.

---

## 📦 Estrutura da Pasta

```
cambio_controller/
├── app/
│   ├── controller/
│   │   ├── standard_controller.py
│   │   ├── bai_controller.py
│   │   └── bic_controller.py
│   ├── models/
│   │   ├── standard_model.py
│   │   ├── bai_model.py
│   │   └── bic_model.py
│   ├── scrapping/
│   │   ├── standard_scraper.py
│   │   ├── bai_scraper.py
│   │   └── bic_scraper.py
│   ├── routes/
│   │   ├── standard_route.py
│   │   ├── bai_route.py
│   │   └── bic_route.py
│   ├── tasks/
│   │   ├── standard_schedule.py
│   │   ├── bai_schedule.py
│   │   └── bic_schedule.py
├── instance/
├── .gitignore
├── requirements.txt
├── README.md
└── run.py
```

---

## ⚙️ Tecnologias Usadas

| Tecnologia        | Descrição |
|------------------|-----------|
| Flask            | Framework principal da API |
| Flask-SQLAlchemy  | ORM para persistência |
| Playwright        | Scraper para buscar taxas |
| SQLite            | Banco de dados local |

---

## 📖 Endpoints da API

### 1️⃣ Obter Todas as Taxas de Câmbio

#### Standard Bank
```
GET /get_standard_rates/
```

#### BAI
```
GET /get_bai_rates/
```

#### BIC
```
GET /get_bic_rates/
```

📊 **Exemplo de Resposta**:
```json
{
    "compra": "641.0540",
    "moeda": "CAD",
    "venda": "658.7280"
  },
  {
    "compra": "912.0000",
    "moeda": "USD",
    "venda": "939.3600"
  }
```

---

### 2️⃣ Obter Taxa de Câmbio de Uma Moeda Específica

#### Standard Bank
```
GET /get_standard_rates/<coin_name>
```

#### BAI
```
GET /get_bai_rates/<coin_name>
```

#### BIC
```
GET /get_bic_rates/<coin_name>
```

📊 **Exemplo de Resposta**:
```json
{
    "compra": "641.0540",
    "moeda": "CAD",
    "venda": "658.7280"
  }
```

---

### 3️⃣ Converter Valores Entre Moedas

> A conversão é baseada nas taxas atualizadas diretamente dos bancos.

#### Standard Bank
```
GET /standard/convert?source_currency=USD&target_currency=AOA&amount=100
```

#### BAI
```
GET /bai/convert?source_currency=USD&target_currency=AOA&amount=100
```

#### BIC
```
GET /bic/convert?source_currency=USD&target_currency=AOA&amount=100
```

📊 **Exemplo de Resposta**:
```json
{
    "source_currency": "USD",
    "target_currency": "AOA",
    "amount": 100,
    "converted_amount": "83570,00"
}
```

---

## 📅 Atualização Automática das Taxas

A API atualiza as taxas de câmbio automaticamente usando **Playwright**. Cada banco tem seu próprio script de agendamento:

| Banco          | Arquivo de Schedule |
|----------------|---------------------|
| Standard Bank  | `standard_schedule.py` |
| BAI            | `bai_schedule.py` |
| BIC            | `bic_schedule.py` |

---

## 🏗️ Como Executar

1. Criar e ativar ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```
2. Instalar as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3. Executar a API:
    ```bash
    python run.py
    ```

---


