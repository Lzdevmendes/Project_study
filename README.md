# Sistema de Gestão - Clínica Vida+
## Sistema de Cadastro e Gerenciamento de Pacientes

### 📋 Descrição do Projeto
Sistema de gestão desenvolvido para clínicas de saúde, permitindo cadastro de pacientes, cálculo de estatísticas e gerenciamento de informações de forma eficiente e organizada.

---

## 🚀 Funcionalidades

### Sistema de Cadastro de Pacientes
**Arquivo:** [sistema_clinica.py](sistema_clinica.py)

✨ **Recursos principais:**
- ✅ Cadastro completo de pacientes (nome, idade, telefone)
- ✅ Cálculo automático de estatísticas:
  - Número total de pacientes
  - Idade média dos pacientes
  - Identificação do paciente mais novo e mais velho
- ✅ Sistema de busca por nome (busca parcial)
- ✅ Listagem organizada de todos os pacientes
- ✅ Menu interativo e intuitivo
- ✅ Validação de dados de entrada
- ✅ Tratamento completo de erros

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.x instalado
- Terminal/Console

### Executando o Sistema
```bash
python sistema_clinica.py
```

### Exemplo de Uso
```
=== SISTEMA CLÍNICA VIDA+ ===
1. Cadastrar paciente
2. Ver estatísticas
3. Buscar paciente
4. Listar todos os pacientes
5. Sair

Escolha uma opção: 1

--- CADASTRAR NOVO PACIENTE ---
Nome do paciente: João Silva
Idade: 45
Telefone: (11) 99999-9999

✅ Paciente cadastrado com sucesso!
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
  - Estruturas de dados nativas (listas e dicionários)
  - Tratamento de exceções
  - Validação de entrada de dados
  - Programação funcional

---

## 📝 Estrutura do Código

### Principais Funções

- `exibir_menu()` - Exibe o menu principal do sistema
- `cadastrar_paciente()` - Cadastra novo paciente com validações
- `calcular_estatisticas()` - Calcula e exibe estatísticas dos pacientes
- `buscar_paciente()` - Busca pacientes por nome (parcial)
- `listar_pacientes()` - Lista todos os pacientes cadastrados
- `validar_idade()` - Valida entrada de idade (0-120 anos)

---

## 🎯 Funcionalidades Detalhadas

### 1. Cadastro de Pacientes
- Validação de campos obrigatórios
- Validação de idade (0-120 anos)
- Armazenamento em estrutura de dicionário
- Feedback visual de sucesso/erro

### 2. Estatísticas
- Contador total de pacientes
- Cálculo de idade média
- Identificação de extremos (mais novo/mais velho)
- Exibição formatada dos dados

### 3. Busca de Pacientes
- Busca por nome (case-insensitive)
- Busca parcial (match em qualquer parte do nome)
- Exibição detalhada dos resultados
- Suporte a múltiplos resultados

### 4. Listagem
- Exibição numerada de todos os pacientes
- Formatação organizada
- Informações completas de cada paciente

---

## 🔒 Validações Implementadas

- ✅ Nome não pode ser vazio
- ✅ Idade deve ser numérica e entre 0-120 anos
- ✅ Telefone não pode ser vazio
- ✅ Tratamento de entradas inválidas
- ✅ Proteção contra interrupção (Ctrl+C)

---

## 🚧 Melhorias Futuras

- [ ] Persistência de dados em arquivo/banco de dados
- [ ] Validação avançada de CPF
- [ ] Formatação automática de telefone
- [ ] Sistema de agendamento de consultas
- [ ] Interface gráfica (GUI)
- [ ] Geração de relatórios em PDF
- [ ] Sistema de autenticação

---

## 👤 Autor

**Luiz Mendes**
Desenvolvedor | Estudante de ADS
📧 [Seu Email]
🔗 [LinkedIn] | [GitHub]

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

---

## 📞 Suporte

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para:
- Abrir uma [Issue](../../issues)
- Enviar um email
- Conectar-se no LinkedIn

---

**⭐ Se este projeto foi útil para você, considere dar uma estrela!**
