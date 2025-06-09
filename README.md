# 📚 Cadastro de Livros
![Python](https://img.shields.io/badge/Python-blue?style=flat&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-blue?style=flat&logo=mysql&logoColor=white)

Sistema de cadastro de livros usando Python com banco de dados MySQL. Permite cadastrar, consultar e remover livros do banco.

📋 Funcionalidades do programa em Python:
°Consultar todos os livros cadastrados
°Cadastrar novo livro
°Consultar por ID
°Consultar por autor
°Remover livro

💾 Estrutura do Banco de Dados:
°Tabela livros com os campos: id (auto_increment, primary key), nome, autor, editora.

🗂️ Estrutura dos Arquivos:
° main.py:
- Arquivo principal, com todas as funções e a integração com o banco de dados MySQL.

° main_antigo.py:
- Versão anterior do programa, sem integração com o MySQL. O armazenamento de dados era feito em uma lista de dicionários.

° banco_de_dados.sql:
- Arquivo .sql com a criação do banco de dados.
