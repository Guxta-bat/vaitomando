# :`  Pipeline CI/CD com GitHub Actions e CodeQL

Projeto desenvolvido para a disciplina de Desenvolvimento de Sistemas da FATEC.

---

# Objetivo

Implementar uma pipeline CI/CD utilizando GitHub Actions com:

- Integração Contínua (CI)
- Pull Request automatizado
- Testes automatizados
- Deploy automatizado
- Análise de segurança com CodeQL

---

# Tecnologias Utilizadas

- Python
- Git
- GitHub
- GitHub Actions
- CodeQL
- Pytest

---

# Estrutura do Projeto

```bash
.github/
│
├── workflows/
│   └── codeql.yml
│
tests/
│   └── test_main.py
│
code.py
requirements.txt
README.md
```

---

# Funcionamento da Pipeline

A pipeline é executada automaticamente quando ocorre:

- Push para a branch `main`
- Abertura de Pull Request

---

# Fluxo da Pipeline

## 1. Análise de Segurança

O GitHub Actions executa o CodeQL para verificar vulnerabilidades e possíveis falhas de segurança no código Python.

## 2. Testes Automatizados

Os testes automatizados são executados utilizando Pytest.

## 3. Deploy para Stage

Após a validação da segurança e testes, a pipeline realiza um deploy de demonstração para ambiente Stage.

---

# Pull Request

Foi criada uma branch para validação da pipeline CI/CD.

```bash
git checkout -b feature/teste-pipeline
```

Após o push da branch, foi aberto um Pull Request no GitHub, disparando automaticamente a pipeline.

---

# Evidências

## Pipeline executando com sucesso/ Executado

<img width="1510" height="430" alt="Captura de tela 2026-05-28 163228" src="https://github.com/user-attachments/assets/aa3cdb2e-9e02-4b37-aef6-85ac268652a7" />


```markdown
```

---

## Pull Request criado


<img width="1518" height="344" alt="Captura de tela 2026-05-28 161411" src="https://github.com/user-attachments/assets/7e79eb25-87c3-4695-abed-a3561f46c0d8" />

## EVIDÊNCIAS

<img width="1518" height="344" alt="Captura de tela 2026-05-28 161411" src="https://github.com/user-attachments/assets/d5a909f2-045d-4a2b-89b1-c7108d0d5eff" />

<img width="1518" height="344" alt="Captura de tela 2026-05-28 161411" src="https://github.com/user-attachments/assets/1b8e9be2-7957-43d8-967a-9a9c1e8d0bce" />


Falhas por injeção SQL e "fast fail" por uma mudança no código .py

```

---

# Resultado Final


<img width="1521" height="340" alt="Captura de tela 2026-05-28 160509" src="https://github.com/user-attachments/assets/58bc5af7-198b-4738-bd20-46a491dc5715" />


A pipeline executou corretamente:

- Análise de Segurança
- Testes Automatizados
- Deploy para Stage

Todos os processos foram concluídos com sucesso.

---

# Autor

Nome: Gustavo Paulo de Sousa

SegInfo — FATEC

Disciplina: Desenvolvimento de Sistema seguro (SO)

Professor: Idirley Soares
