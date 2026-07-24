# 📱 Controle de Dispositivos IoT (simulação)

Projeto desenvolvido com o objetivo de consolidar meus conhecimentos em **Programação Orientada a Objetos (POO)** utilizando Python e servir como parte do meu portfólio de estudos para desenvolvimento Backend.

Ao longo do desenvolvimento, busquei aplicar conceitos fundamentais da linguagem e boas práticas de organização de código, simulando um sistema simples de gerenciamento de dispositivos IoT.

---

## 🎯 Objetivo

Este projeto foi criado principalmente para fortalecer conceitos como:

* Programação Orientada a Objetos (POO)
* Encapsulamento
* Herança
* Polimorfismo
* Composição
* Organização em módulos
* Tipagem estática (Type Hints)
* Tratamento de exceções
* Responsabilidade entre classes

Em vez de apenas estudar teoria, optei por construir uma aplicação que me obrigasse a aplicar esses conceitos na prática.

---

## ⚙️ Funcionalidades

Atualmente o sistema permite:

* Cadastro de usuários
* Cadastro de dispositivos
* Associação de dispositivos a usuários
* Desassociação de dispositivos
* Busca de usuários por ID
* Busca de dispositivos por ID
* Gerenciamento de bateria e status dos dispositivos
* Dispositivos especializados através de herança:

  * Detector de Quedas
  * Sensor de Temperatura
  * Sensor BPM

---

## 📂 Estrutura do Projeto

```text
Models/
├── device_model.py
├── usuario_model.py
├── gerenciadordispositivos_model.py
├── detectorqueda_model.py
├── sensortemperatura_model.py
└── sensorbpm_model.py
```

A organização foi pensada para separar responsabilidades e facilitar futuras expansões do sistema.

---

## 🚀 Próximos Passos

Este projeto continuará evoluindo conforme avanço nos meus estudos em desenvolvimento Backend.

As próximas melhorias planejadas incluem:

* Implementação de um banco de dados (SQLite inicialmente)
* Persistência real dos dados
* Desenvolvimento de uma API utilizando FastAPI
* Validação de dados com Pydantic
* Autenticação com JWT
* Testes automatizados
* Hospedagem da API para acesso público

---

## 💻 Tecnologias Utilizadas

* Python 3
* Programação Orientada a Objetos
* UUID
* Type Hints

---

## 📚 Sobre este projeto

Este projeto representa uma etapa importante da minha evolução como desenvolvedor Python.

O foco não foi apenas criar um sistema funcional, mas também praticar arquitetura, organização do código e boas práticas de desenvolvimento, preparando a base para projetos mais completos utilizando banco de dados, APIs REST e deploy.

Novas funcionalidades serão adicionadas conforme eu evoluir nos estudos de Backend.
