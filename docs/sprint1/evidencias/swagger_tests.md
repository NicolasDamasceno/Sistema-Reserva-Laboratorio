# Evidências de Testes - Swagger

## Ambiente

* Framework: FastAPI
* Documentação: Swagger UI
* Data dos testes: Sprint 01

---

## Teste 01 - Criar Laboratório

### Endpoint

POST /laboratorios

### Resultado

* Requisição executada com sucesso.
* Laboratório registrado corretamente.

### Status

Aprovado.

---

## Teste 02 - Listar Laboratórios

### Endpoint

GET /laboratorios

### Resultado

* Lista de laboratórios retornada corretamente.

### Status

Aprovado.

---

## Teste 03 - Criar Reserva

### Endpoint

POST /reservas

### Resultado

* Reserva registrada corretamente.

### Status

Aprovado.

---

## Teste 04 - Listar Reservas

### Endpoint

GET /reservas

### Resultado

* Reservas retornadas corretamente.

### Status

Aprovado.

---

## Observações

As validações dos Schemas Pydantic foram executadas durante os testes e os endpoints responderam conforme esperado.
