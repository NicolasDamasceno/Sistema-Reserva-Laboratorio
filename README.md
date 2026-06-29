# Sistema de Reserva de Laboratórios

API REST para gerenciamento de laboratórios e reservas, desenvolvida na disciplina **Engenharia de Software II** — IFPI TADS.

## Equipe

| Nome | Matrícula | Responsabilidade principal |
|---|---|---|
| Guilherme Alves Barbosa | 2025111TADS0010 | Services (regras de negócio) |
| Marcos Gabriel Mendes Silva | 2024211TADS0007 | Routers, Schemas e Evidências |
| Nicolas Antônio Damasceno | 2025111TADS0023 | Repositories e Integração |

## Tecnologias

- Python 3.13+
- FastAPI
- Pydantic v2
- Uvicorn
- Pytest + HTTPX
- Persistência em JSON

## Estrutura do Projeto

```
app/
├── exceptions/         # Exceções customizadas
├── models/             # Entidades do domínio (Laboratorio, Reserva)
├── repositories/       # Persistência em arquivos JSON
├── routers/            # Endpoints da API (Controllers)
├── schemas/            # Schemas Pydantic (DTOs de entrada/saída)
├── services/           # Regras de negócio
└── main.py             # Inicialização da aplicação

data/
├── laboratorios.json   # Dados persistidos de laboratórios
└── reservas.json       # Dados persistidos de reservas

docs/
├── sprint1/            # Artefatos da Sprint 1
├── sprint2/            # Artefatos da Sprint 2
└── sprint3/            # Artefatos da Sprint 3

tests/
├── test_laboratorios.py
└── test_reservas.py
```

## Pré-requisitos

- Python 3.13 ou superior
- pip

## Instalação

**1. Clonar o repositório**

```bash
git clone https://github.com/NicolasDamasceno/Sistema-Reserva-Laboratorio.git
cd Sistema-Reserva-Laboratorio
```

**2. Criar e ativar o ambiente virtual**

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

**3. Instalar as dependências**

```bash
pip install -r requirements.txt
```

## Executando a Aplicação

```bash
uvicorn app.main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

## Documentação Interativa (Swagger)

Com a aplicação rodando, acesse:

```
http://127.0.0.1:8000/docs
```

O Swagger UI permite testar todos os endpoints diretamente pelo navegador.

## Endpoints Disponíveis

### Laboratórios

| Método | Endpoint | Descrição |
|---|---|---|
| POST | `/laboratorios/` | Cadastrar laboratório |
| GET | `/laboratorios/` | Listar laboratórios |
| GET | `/laboratorios/{id}` | Buscar laboratório por ID |
| PUT | `/laboratorios/{id}` | Atualizar laboratório |

### Reservas

| Método | Endpoint | Descrição |
|---|---|---|
| POST | `/reservas/` | Solicitar reserva |
| GET | `/reservas/` | Listar reservas |
| GET | `/reservas/{id}` | Buscar reserva por ID |
| PATCH | `/reservas/{id}/avaliar` | Aprovar ou rejeitar reserva |
| PATCH | `/reservas/{id}/cancelar` | Cancelar reserva |

## Exemplo de Uso

**Cadastrar laboratório:**
```json
POST /laboratorios/
{
  "nome": "Laboratório de Redes",
  "capacidade": 30
}
```

**Solicitar reserva:**
```json
POST /reservas/
{
  "laboratorio_id": "<id-do-laboratorio>",
  "solicitante": "Guilherme",
  "data": "2027-08-10",
  "hora_inicio": "08:00",
  "hora_fim": "10:00"
}
```

**Aprovar reserva:**
```json
PATCH /reservas/{id}/avaliar
{
  "acao": "aprovar"
}
```

**Rejeitar reserva (justificativa obrigatória):**
```json
PATCH /reservas/{id}/avaliar
{
  "acao": "rejeitar",
  "justificativa": "Laboratório em manutenção"
}
```

**Cancelar reserva:**
```
PATCH /reservas/{id}/cancelar?solicitante=Guilherme
```

## Executando os Testes

```bash
pytest tests/ -v
```

Resultado esperado: **14 testes passando** cobrindo US01 a US05.

```
tests/test_laboratorios.py::test_cadastrar_laboratorio_sucesso PASSED
tests/test_laboratorios.py::test_cadastrar_nome_duplicado PASSED
tests/test_laboratorios.py::test_listar_laboratorios PASSED
tests/test_laboratorios.py::test_buscar_laboratorio_por_id PASSED
tests/test_laboratorios.py::test_buscar_laboratorio_inexistente PASSED
tests/test_laboratorios.py::test_atualizar_laboratorio PASSED
tests/test_reservas.py::test_solicitar_reserva_sucesso PASSED
tests/test_reservas.py::test_solicitar_reserva_laboratorio_inexistente PASSED
tests/test_reservas.py::test_aprovar_reserva PASSED
tests/test_reservas.py::test_rejeitar_reserva_sem_justificativa PASSED
tests/test_reservas.py::test_rejeitar_reserva_com_justificativa PASSED
tests/test_reservas.py::test_conflito_de_horario PASSED
tests/test_reservas.py::test_cancelar_reserva_sucesso PASSED
tests/test_reservas.py::test_cancelar_reserva_solicitante_errado PASSED
```

## Regras de Negócio Implementadas

- Laboratório não pode ter nome duplicado
- Reserva não pode ser feita para data passada
- Hora de fim deve ser posterior à hora de início
- Laboratório inativo não aceita novas reservas
- Reservas não podem conflitar com reservas já aprovadas no mesmo horário
- Apenas reservas com status **PENDENTE** podem ser avaliadas
- Rejeição exige justificativa obrigatória
- Cancelamento só é permitido pelo próprio solicitante
- Reserva cancelada não bloqueia novos agendamentos

## Histórias de Usuário

| ID | História |
|---|---|
| US01 | Como administrador, desejo gerenciar os laboratórios para manter as informações atualizadas |
| US02 | Como usuário, desejo consultar os laboratórios disponíveis para verificar sua disponibilidade |
| US03 | Como usuário, desejo solicitar uma reserva de laboratório para realizar minhas atividades |
| US04 | Como administrador, desejo aprovar ou rejeitar solicitações de reserva para controlar a utilização |
| US05 | Como solicitante, desejo cancelar uma reserva para liberar o laboratório quando necessário |

## Repositório

[https://github.com/NicolasDamasceno/Sistema-Reserva-Laboratorio](https://github.com/NicolasDamasceno/Sistema-Reserva-Laboratorio)
