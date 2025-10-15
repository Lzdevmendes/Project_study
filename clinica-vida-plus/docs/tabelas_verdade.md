# Tabelas Verdade - Sistema de Controle de Acesso

## Clínica Vida+

---

## Variáveis Lógicas

- **A**: Paciente tem agendamento marcado
- **B**: Paciente está com documentos em dia
- **C**: Há médico disponível
- **D**: Paciente está em dia com pagamentos

---

## Regras de Acesso

### 1. Consulta Normal
**Expressão Lógica**: `(A ∧ B ∧ C) ∨ (B ∧ C ∧ D)`

**Interpretação**: O paciente pode ter consulta normal se:
- Tem agendamento marcado **E** está com documentos em dia **E** há médico disponível, **OU**
- Está com documentos em dia **E** há médico disponível **E** está em dia com pagamentos

### 2. Emergência
**Expressão Lógica**: `C ∧ (B ∨ D)`

**Interpretação**: O paciente pode ter atendimento de emergência se:
- Há médico disponível **E** (está com documentos em dia **OU** está em dia com pagamentos)

---

## Tabela Verdade: Consulta Normal

| A | B | C | D | A∧B∧C | B∧C∧D | (A∧B∧C)∨(B∧C∧D) | Resultado |
|:-:|:-:|:-:|:-:|:-----:|:-----:|:---------------:|:---------:|
| F | F | F | F |   F   |   F   |        F        |  NEGADO   |
| F | F | F | V |   F   |   F   |        F        |  NEGADO   |
| F | F | V | F |   F   |   F   |        F        |  NEGADO   |
| F | F | V | V |   F   |   F   |        F        |  NEGADO   |
| F | V | F | F |   F   |   F   |        F        |  NEGADO   |
| F | V | F | V |   F   |   F   |        F        |  NEGADO   |
| F | V | V | F |   F   |   F   |        F        |  NEGADO   |
| F | V | V | V |   F   |   V   |        V        | **PERMITIDO** |
| V | F | F | F |   F   |   F   |        F        |  NEGADO   |
| V | F | F | V |   F   |   F   |        F        |  NEGADO   |
| V | F | V | F |   F   |   F   |        F        |  NEGADO   |
| V | F | V | V |   F   |   F   |        F        |  NEGADO   |
| V | V | F | F |   F   |   F   |        F        |  NEGADO   |
| V | V | F | V |   F   |   F   |        F        |  NEGADO   |
| V | V | V | F |   V   |   F   |        V        | **PERMITIDO** |
| V | V | V | V |   V   |   V   |        V        | **PERMITIDO** |

### Análise da Consulta Normal
- **Total de combinações**: 16
- **Situações que permitem atendimento**: 3 (linhas 8, 15, 16)
- **Situações que negam atendimento**: 13
- **Percentual de acesso**: 18.75%

---

## Tabela Verdade: Emergência

| A | B | C | D | B∨D | C∧(B∨D) | Resultado |
|:-:|:-:|:-:|:-:|:---:|:-------:|:---------:|
| F | F | F | F |  F  |    F    |  NEGADO   |
| F | F | F | V |  V  |    F    |  NEGADO   |
| F | F | V | F |  F  |    F    |  NEGADO   |
| F | F | V | V |  V  |    V    | **PERMITIDO** |
| F | V | F | F |  V  |    F    |  NEGADO   |
| F | V | F | V |  V  |    F    |  NEGADO   |
| F | V | V | F |  V  |    V    | **PERMITIDO** |
| F | V | V | V |  V  |    V    | **PERMITIDO** |
| V | F | F | F |  F  |    F    |  NEGADO   |
| V | F | F | V |  V  |    F    |  NEGADO   |
| V | F | V | F |  F  |    F    |  NEGADO   |
| V | F | V | V |  V  |    V    | **PERMITIDO** |
| V | V | F | F |  V  |    F    |  NEGADO   |
| V | V | F | V |  V  |    F    |  NEGADO   |
| V | V | V | F |  V  |    V    | **PERMITIDO** |
| V | V | V | V |  V  |    V    | **PERMITIDO** |

### Análise da Emergência
- **Total de combinações**: 16
- **Situações que permitem atendimento**: 6 (linhas 4, 7, 8, 12, 15, 16)
- **Situações que negam atendimento**: 10
- **Percentual de acesso**: 37.5%

---

## Teste Prático

### Cenário: A=F, B=V, C=V, D=F

#### Consulta Normal
```
Expressão: (A ∧ B ∧ C) ∨ (B ∧ C ∧ D)
Substituição: (F ∧ V ∧ V) ∨ (V ∧ V ∧ F)
Cálculo:
  - (F ∧ V ∧ V) = F
  - (V ∧ V ∧ F) = F
  - F ∨ F = F

Resultado: NEGADO ❌
```

**Justificativa**: O paciente não tem agendamento marcado (A=F) e também não está em dia com os pagamentos (D=F), então nenhuma das condições da regra é satisfeita.

#### Emergência
```
Expressão: C ∧ (B ∨ D)
Substituição: V ∧ (V ∨ F)
Cálculo:
  - (V ∨ F) = V
  - V ∧ V = V

Resultado: PERMITIDO ✓
```

**Justificativa**: Há médico disponível (C=V) e o paciente está com documentos em dia (B=V), satisfazendo a regra de emergência.

### Conclusão do Teste
Neste cenário:
- **Consulta Normal**: NEGADO
- **Emergência**: PERMITIDO

O paciente seria atendido apenas em caso de emergência, não para consulta normal agendada.

---

## Comparação entre Regras

### Flexibilidade de Acesso
- **Emergência** é mais flexível (37.5% de aprovação)
- **Consulta Normal** é mais restritiva (18.75% de aprovação)

### Dependências Críticas
- **Consulta Normal**: Exige documentos em dia (B) E médico disponível (C) como requisitos mínimos
- **Emergência**: Exige apenas médico disponível (C) como requisito absoluto

### Importância das Variáveis

| Variável | Consulta Normal | Emergência |
|:--------:|:---------------:|:----------:|
| A (Agendamento) | Alta | Nenhuma |
| B (Documentos) | Crítica | Alta |
| C (Médico) | Crítica | Crítica |
| D (Pagamentos) | Média | Alta |

---

## Situações Especiais

### Atendimento Garantido
Para garantir atendimento em **ambos** os tipos:
- Deve ter: B=V, C=V, D=V (documentos em dia, médico disponível, pagamentos em dia)
- Variável A (agendamento) é opcional

### Bloqueio Total
Situações que **negam** atendimento em ambos os tipos:
- C=F (sem médico disponível) sempre bloqueia
- C=V mas B=F e D=F (sem documentos e sem pagamentos) também bloqueia

---

## Implementação Computacional

O sistema implementa essas regras no arquivo `src/controle_acesso.py`:

```python
def consulta_normal(A: bool, B: bool, C: bool, D: bool) -> bool:
    return (A and B and C) or (B and C and D)

def emergencia(A: bool, B: bool, C: bool, D: bool) -> bool:
    return C and (B or D)
```

Para testar estas regras, execute:
```bash
python src/controle_acesso.py
```

---

**Documento gerado pelo Sistema de Gestão Clínica Vida+**
*Data: 2025-10-15*
