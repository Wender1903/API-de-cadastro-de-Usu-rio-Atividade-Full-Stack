# API de Cadastro de Usuários - Flask

## Grupo 9
### - Larissa Pires dos Santos
### - Vinicios
### - Wender da Silva Santos

Essa é uma API simples desenvolvida em **Python** com **Flask**, que realiza operações de **CRUD** (Create, Read, Update, Delete) em uma lista de usuários armazenada em memória.

---

## Funcionalidades

- **Listar todos os usuários**  
  `GET /users` → Retorna uma lista JSON de todos os usuários.

- **Buscar usuário por ID**  
  `GET /users/<id>` → Retorna um usuário específico pelo ID.

- **Criar novo usuário**  
  `POST /users` → Cria um novo usuário.  
  Corpo JSON esperado:
  ```json
  {
    "nome": "Nome do Usuário",
    "email": "email@exemplo.com"
  }
  ```

- **Atualizar usuário existente**  
  `PUT /users/<id>` → Atualiza os dados de um usuário existente.  
  Corpo JSON esperado (um ou mais campos):
  ```json
  {
    "nome": "Novo Nome",
    "email": "novo@email.com"
  }
  ```

- **Deletar usuário**  
  `DELETE /users/<id>` → Remove um usuário da lista.

---

## Como rodar

1. Criar e ativar o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac
```

2. Instalar as dependências:

```bash
pip install flask
```

3. Rodar o servidor:

```bash
python app.py
```

O servidor irá rodar em: `http://localhost:5000`

---

## Observações

- Os dados são armazenados **apenas em memória**. Se o servidor for reiniciado, os usuários cadastrados serão perdidos.  
- O ID do usuário é gerado automaticamente ao criar um novo usuário.
