# Sistema de Reserva de Laboratórios

Projeto desenvolvido para a disciplina Engenharia de Software II do IFPI.

## Tecnologias

- Python 3.13+
- FastAPI
- Pydantic
- Uvicorn
- JSON

## Estrutura do Projeto

```text
app/
├── routers/
├── services/
├── repositories/
├── models/
├── schemas/
└── exceptions/

data/
docs/
tests/
```

## Clonando o Projeto

```bash
git clone https://github.com/NicolasDamasceno/Sistema-Reserva-Laboratorio.git
cd Sistema-Reserva-Laboratorio
```

## Criando Ambiente Virtual

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:

```bash
python -m venv venv
source venv/bin/activate
```

## Instalando Dependências

```bash
pip install -r requirements.txt
```

## Executando a Aplicação

```bash
uvicorn app.main:app --reload
```

## Documentação Swagger

Após iniciar a aplicação:

```text
http://127.0.0.1:8000/docs
```

## Integrantes

- Guilherme Alves Barbosa
- Nicolas Antônio Damasceno
- Marcos Gabriel
- Nicole Oliveira