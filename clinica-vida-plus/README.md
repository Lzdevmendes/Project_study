# Sistema de Gestão - Clínica Vida+

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

Sistema completo de gestão para clínicas médicas, desenvolvido para resolver problemas de agendamentos manuais, acompanhamento de históricos de pacientes e erros em cobranças/relatórios.

---

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Módulos do Sistema](#módulos-do-sistema)
- [Documentação Técnica](#documentação-técnica)
- [Exemplos de Uso](#exemplos-de-uso)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

---

## Sobre o Projeto

A Clínica Vida+ enfrentava desafios significativos com processos manuais:
- Agendamentos realizados em papel
- Dificuldade no acompanhamento de históricos médicos
- Erros frequentes em cobranças e relatórios
- Falta de controle de fila de atendimento

Este sistema foi desenvolvido para automatizar e otimizar todos esses processos, oferecendo uma solução completa e profissional.

---

## Funcionalidades

### Sistema de Cadastro de Pacientes
- Cadastro completo com validação de CPF
- Validação de formato de telefone
- Busca inteligente por nome (case-insensitive)
- Estatísticas automáticas (idade média, mais novo, mais velho)
- Persistência de dados em JSON
- Sistema de backup automático
- Timestamps em todos os cadastros

### Sistema de Controle de Acesso
- Lógica booleana para autorização de consultas
- Regras diferenciadas para consulta normal e emergência
- Validação de documentos e pagamentos
- Verificação de disponibilidade de médicos
- Tabelas verdade completas
- Análise estatística de acesso

### Gerenciamento de Fila de Atendimento
- Três níveis de prioridade:
  - Emergência (prioridade máxima)
  - Preferencial (prioridade média)
  - Normal (prioridade padrão)
- Estrutura FIFO (First In, First Out)
- Validação de CPF automática
- Visualização em tempo real da fila

### Recursos Adicionais
- Interface colorida no terminal (colorama)
- Tratamento robusto de erros
- Validações completas de entrada
- Sistema de backup automático
- Exportação de dados

---

## Estrutura do Projeto

```
clinica-vida-plus/
├── src/
│   ├── main.py                  # Sistema principal de cadastro
│   ├── controle_acesso.py       # Lógica de controle de acesso
│   └── fila_atendimento.py      # Gerenciamento de filas
├── docs/
│   ├── tabelas_verdade.md       # Documentação de lógica booleana
│   └── diagrama_casos_uso.puml  # Diagrama UML
├── data/
│   └── pacientes.json           # Banco de dados (criado automaticamente)
├── backups/                     # Backups automáticos
├── README.md                    # Este arquivo
└── requirements.txt             # Dependências do projeto
```

---

## Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. Clone ou baixe o projeto:
```bash
cd clinica-vida-plus
```

2. (Opcional) Crie um ambiente virtual:
```bash
python -m venv venv

# No Windows:
venv\Scripts\activate

# No Linux/Mac:
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

---

## Como Usar

### Sistema Principal de Cadastro

Execute o sistema principal:
```bash
python src/main.py
```

Você verá o menu interativo:
```
=== SISTEMA CLÍNICA VIDA+ ===
1. Cadastrar paciente
2. Ver estatísticas
3. Buscar paciente
4. Listar todos os pacientes
5. Fazer backup dos dados
6. Sair
```

### Sistema de Controle de Acesso

Execute o módulo de controle de acesso:
```bash
python src/controle_acesso.py
```

Funcionalidades disponíveis:
- Verificar acesso para consulta normal
- Verificar acesso para emergência
- Visualizar tabelas verdade completas
- Ver estatísticas de acesso
- Executar teste prático

### Gerenciamento de Fila

Execute o módulo de fila:
```bash
python src/fila_atendimento.py
```

Opções disponíveis:
- Inserir paciente na fila (com seleção de prioridade)
- Chamar próximo paciente
- Mostrar fila completa
- Ver próximo paciente sem remover
- Executar demonstração do algoritmo

---

## Módulos do Sistema

### 1. main.py - Sistema de Cadastro

**Classes principais:**
- `Paciente`: Representa um paciente
- `SistemaClinica`: Gerencia todo o sistema de cadastro

**Métodos principais:**
```python
cadastrar_paciente()    # Cadastra novo paciente
ver_estatisticas()      # Exibe estatísticas
buscar_paciente()       # Busca por nome
listar_pacientes()      # Lista todos
fazer_backup()          # Cria backup com timestamp
```

### 2. controle_acesso.py - Lógica de Acesso

**Classe principal:**
- `ControleAcesso`: Implementa lógica booleana

**Regras implementadas:**
- Consulta Normal: `(A ∧ B ∧ C) ∨ (B ∧ C ∧ D)`
- Emergência: `C ∧ (B ∨ D)`

Onde:
- A: Paciente tem agendamento marcado
- B: Paciente está com documentos em dia
- C: Há médico disponível
- D: Paciente está em dia com pagamentos

### 3. fila_atendimento.py - Filas

**Classes principais:**
- `PacienteFila`: Representa paciente na fila
- `FilaAtendimento`: Gerencia as filas

**Características:**
- Três filas independentes (emergência, preferencial, normal)
- Atendimento por ordem de prioridade
- Validação automática de CPF

---

## Documentação Técnica

### Tabelas Verdade

Consulte o arquivo `docs/tabelas_verdade.md` para:
- Tabelas verdade completas (16 linhas cada)
- Análise estatística de situações de acesso
- Teste prático com valores específicos
- Comparação entre regras de consulta normal e emergência

### Diagrama de Casos de Uso

O arquivo `docs/diagrama_casos_uso.puml` contém:
- Diagrama completo de casos de uso
- Relacionamentos entre atores (Secretária, Médico, Paciente)
- Casos de uso com relacionamentos include/extend
- Pré-condições e pós-condições

Para visualizar o diagrama:
1. Use um editor PlantUML online: http://www.plantuml.com/plantuml/uml/
2. Ou instale uma extensão PlantUML no seu editor (VS Code, IntelliJ, etc.)

---

## Exemplos de Uso

### Cadastrar um Paciente

```python
from src.main import SistemaClinica

sistema = SistemaClinica()
# O sistema carrega automaticamente dados existentes

# Use o menu interativo ou chame métodos diretamente
sistema.cadastrar_paciente()
```

### Verificar Acesso

```python
from src.controle_acesso import ControleAcesso

# Teste: sem agendamento, documentos ok, médico disponível, sem pagamento
A, B, C, D = False, True, True, False

# Consulta Normal
permitido = ControleAcesso.consulta_normal(A, B, C, D)
print(f"Consulta Normal: {'PERMITIDO' if permitido else 'NEGADO'}")

# Emergência
permitido = ControleAcesso.emergencia(A, B, C, D)
print(f"Emergência: {'PERMITIDO' if permitido else 'NEGADO'}")
```

### Gerenciar Fila

```python
from src.fila_atendimento import FilaAtendimento

fila = FilaAtendimento()

# Inserir pacientes
fila.inserir_paciente("João Silva", "123.456.789-09", "emergencia")
fila.inserir_paciente("Maria Santos", "987.654.321-00", "normal")

# Chamar próximo (emergência tem prioridade)
proximo = fila.remover_proximo()
print(f"Chamar: {proximo}")

# Mostrar fila restante
fila.mostrar_fila()
```

---

## Tecnologias Utilizadas

### Linguagem
- **Python 3.8+**: Linguagem principal do projeto

### Bibliotecas Python
- **json**: Persistência de dados
- **datetime**: Timestamps e datas
- **re**: Validação com expressões regulares
- **collections.deque**: Estrutura de dados para fila
- **typing**: Type hints para melhor documentação
- **colorama**: Interface colorida no terminal (opcional)

### Ferramentas de Documentação
- **Markdown**: Documentação
- **PlantUML**: Diagramas UML

### Padrões e Boas Práticas
- **PEP 8**: Estilo de código Python
- **Type Hints**: Tipagem estática
- **Docstrings**: Documentação inline
- **OOP**: Programação Orientada a Objetos
- **SOLID**: Princípios de design

---

## Validações Implementadas

### CPF
- Formato: XXX.XXX.XXX-XX
- Validação de dígitos verificadores
- Rejeita sequências repetidas (111.111.111-11)

### Telefone
- Formato: (XX) XXXXX-XXXX ou (XX) XXXX-XXXX
- Aceita com ou sem espaços

### Idade
- Valor entre 1 e 149 anos
- Validação de tipo numérico

### Nome
- Mínimo de 3 caracteres
- Trimming automático de espaços

---

## Persistência de Dados

### Formato JSON
Os dados são salvos em `data/pacientes.json`:
```json
[
  {
    "nome": "João da Silva",
    "idade": 45,
    "telefone": "(11) 98765-4321",
    "cpf": "123.456.789-09",
    "data_cadastro": "2025-10-15 14:30:45"
  }
]
```

### Backups
- Criados manualmente ou automaticamente
- Salvos em `backups/` com timestamp
- Formato: `pacientes_backup_YYYYMMDD_HHMMSS.json`

---

## Resolução de Problemas

### Erro: colorama não instalado
```bash
pip install colorama
```
O sistema funciona sem colorama, mas sem cores no terminal.

### Erro: Arquivo JSON corrompido
1. Restaure um backup de `backups/`
2. Ou delete `data/pacientes.json` para começar do zero

### Erro: Permissão negada
Verifique as permissões das pastas `data/` e `backups/`

---

## Roadmap

Funcionalidades planejadas para futuras versões:

- [ ] Interface gráfica (GUI) com Tkinter/PyQt
- [ ] Banco de dados SQL (PostgreSQL/MySQL)
- [ ] Sistema de autenticação e autorização
- [ ] API REST para integração
- [ ] Relatórios em PDF
- [ ] Sistema de notificações (SMS/Email)
- [ ] Integração com agenda do Google
- [ ] Dashboard web com Flask/Django
- [ ] Aplicativo mobile
- [ ] Sistema de prontuário eletrônico

---

## Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

---

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## Autores

**Sistema Clínica Vida+**
- Desenvolvido com Claude Code
- Data: 2025-10-15

---

## Suporte

Para reportar bugs ou solicitar funcionalidades:
- Abra uma issue no repositório
- Entre em contato com a equipe de desenvolvimento

---

## Agradecimentos

- À equipe da Clínica Vida+ por confiar no projeto
- À comunidade Python pelas excelentes bibliotecas
- A todos que contribuíram com feedback e sugestões

---

**Sistema de Gestão Clínica Vida+ - Simplificando o cuidado com a saúde**
