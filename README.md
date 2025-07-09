# 📚 Cadastro de Livros
![Python](https://img.shields.io/badge/Python-blue?style=flat&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-blue?style=flat&logo=mysql&logoColor=white)

Sistema de cadastro de livros desenvolvido em **Python**, com integração ao banco de dados **MySQL**.

---

### 📌 Funcionalidades:

- Consultar todos os livros cadastrados  
- Cadastrar novo livro  
- Consultar por ID  
- Consultar por autor  
- Remover livro  

---

### 📌 Estrutura do Banco de Dados:

- Tabela livros com os campos:
  - id (PRIMARY KEY, AUTO_INCREMENT)  
  - nome  
  - autor  
  - editora  

---

### 📌 Estrutura dos Arquivos:

- **main.py**  
  Arquivo principal, com todas as funções e integração com o banco de dados MySQL.

- **main_antigo.py**  
  Versão anterior do programa, sem integração com o MySQL. Os dados eram armazenados em uma lista de dicionários.

- **banco_de_dados.sql**  
  Script para criação da estrutura do banco de dados MySQL.
