# Guia de Início Rápido - Clínica Vida+

Este guia rápido ajudará você a começar a usar o Sistema de Gestão da Clínica Vida+ em poucos minutos.

---

## Instalação Rápida

### 1. Instalar Python
Certifique-se de ter Python 3.8 ou superior instalado:
```bash
python --version
```

### 2. Instalar Dependências
```bash
cd clinica-vida-plus
pip install -r requirements.txt
```

---

## Uso Básico

### Sistema Principal (Cadastro de Pacientes)

```bash
python src/main.py
```

**Ações principais:**
1. Digite `1` para cadastrar um novo paciente
2. Digite `2` para ver estatísticas
3. Digite `3` para buscar um paciente
4. Digite `4` para listar todos
5. Digite `5` para fazer backup

**Exemplo de cadastro:**
```
Nome completo: João da Silva
Idade: 45
Telefone: (11) 98765-4321
CPF: 123.456.789-09
```

---

### Sistema de Controle de Acesso

```bash
python src/controle_acesso.py
```

**Ações principais:**
1. Digite `1` para verificar acesso (Consulta Normal)
2. Digite `2` para verificar acesso (Emergência)
3. Digite `3` para ver tabela verdade (Consulta Normal)
4. Digite `6` para executar teste prático

**Variáveis do sistema:**
- A: Agendamento marcado (V/F)
- B: Documentos em dia (V/F)
- C: Médico disponível (V/F)
- D: Pagamentos em dia (V/F)

---

### Gerenciamento de Fila

```bash
python src/fila_atendimento.py
```

**Ações principais:**
1. Digite `1` para inserir paciente na fila
2. Digite `2` para chamar próximo paciente
3. Digite `3` para mostrar fila completa
4. Digite `5` para ver demonstração do algoritmo

**Prioridades disponíveis:**
- 1: Emergência (atendido primeiro)
- 2: Preferencial (atendido em seguida)
- 3: Normal (atendido por último)

---

## Estrutura de Arquivos

Após a primeira execução, você verá:

```
clinica-vida-plus/
├── src/                    # Código fonte
├── data/                   # Dados dos pacientes (JSON)
├── backups/                # Backups automáticos
├── docs/                   # Documentação
└── README.md              # Documentação completa
```

---

## Exemplos Práticos

### Exemplo 1: Cadastrar 3 Pacientes

1. Execute: `python src/main.py`
2. Escolha opção `1` (Cadastrar paciente)
3. Insira os dados:
   - Nome: Maria Santos
   - Idade: 32
   - Telefone: (11) 91234-5678
   - CPF: 987.654.321-00
4. Repita para mais 2 pacientes
5. Escolha opção `4` para ver todos cadastrados

### Exemplo 2: Testar Controle de Acesso

1. Execute: `python src/controle_acesso.py`
2. Escolha opção `6` (Teste prático)
3. Veja o resultado para:
   - A=F, B=V, C=V, D=F
   - Consulta Normal: NEGADO
   - Emergência: PERMITIDO

### Exemplo 3: Gerenciar Fila de Atendimento

1. Execute: `python src/fila_atendimento.py`
2. Escolha opção `5` (Demonstração)
3. Veja como funciona:
   - 3 pacientes são inseridos
   - O primeiro (preferencial) é chamado
   - Restam 2 na fila normal

---

## Validações Importantes

### CPF válidos para teste:
```
123.456.789-09  ✓
987.654.321-00  ✓
111.222.333-44  ✓
```

### Telefone válido:
```
(11) 98765-4321  ✓
(21) 3456-7890   ✓
```

### Idade válida:
```
1 a 149 anos  ✓
```

---

## Dicas Rápidas

1. **Backup automático**: Use opção 5 no menu principal para criar backups
2. **Cores no terminal**: Instale colorama para melhor visualização
3. **Dados persistentes**: Tudo é salvo automaticamente em JSON
4. **Busca inteligente**: A busca não diferencia maiúsculas/minúsculas
5. **Validação automática**: CPF e telefone são validados automaticamente

---

## Atalhos de Teclado

- `Ctrl+C`: Cancela a operação atual
- `Enter`: Confirma a entrada
- `6` ou `7`: Geralmente a opção "Sair" ou "Voltar"

---

## Resolução Rápida de Problemas

### Problema: "colorama não instalado"
**Solução:** `pip install colorama`

### Problema: "Arquivo JSON corrompido"
**Solução:** Delete `data/pacientes.json` ou restaure um backup

### Problema: "CPF inválido"
**Solução:** Use um CPF com dígitos verificadores válidos

---

## Próximos Passos

Depois de se familiarizar com o sistema:

1. Leia o `README.md` completo para recursos avançados
2. Consulte `docs/tabelas_verdade.md` para entender a lógica
3. Visualize `docs/diagrama_casos_uso.puml` para ver o fluxo completo
4. Explore o código fonte em `src/` para customizações

---

## Suporte

Dúvidas? Consulte:
- README.md (documentação completa)
- Código fonte (bem comentado)
- Arquivos em docs/ (documentação técnica)

---

**Pronto para começar! Execute `python src/main.py` agora! 🚀**
