"""
Sistema de Gestão da Clínica Vida+
Programa console para cadastro e gerenciamento de pacientes
Autor: Luiz Mendes
Data: Dezembro 2024
"""

def limpar_tela():
    """Simula limpeza de tela (multiplica quebras de linha)"""
    print("\n" * 50)

def exibir_menu():
    """Exibe o menu principal do sistema"""
    print("=" * 50)
    print("      SISTEMA CLÍNICA VIDA+")
    print("=" * 50)
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes")
    print("5. Sair")
    print("=" * 50)

def validar_idade():
    """Valida e retorna uma idade válida"""
    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 0:
                print("❌ Erro: Idade não pode ser negativa!")
            elif idade > 120:
                print("❌ Erro: Idade muito alta! Digite uma idade válida.")
            else:
                return idade
        except ValueError:
            print("❌ Erro: Digite apenas números!")

def cadastrar_paciente(pacientes):
    """Cadastra um novo paciente no sistema"""
    print("\n--- CADASTRAR NOVO PACIENTE ---")
    
    try:
        nome = input("Nome do paciente: ").strip()
        if not nome:
            print("❌ Erro: Nome não pode ser vazio!")
            return
        
        idade = validar_idade()
        
        telefone = input("Telefone: ").strip()
        if not telefone:
            print("❌ Erro: Telefone não pode ser vazio!")
            return
        
        # Cria dicionário com dados do paciente
        paciente = {
            'nome': nome,
            'idade': idade,
            'telefone': telefone
        }
        
        # Adiciona à lista de pacientes
        pacientes.append(paciente)
        
        print("\n✅ Paciente cadastrado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro ao cadastrar paciente: {e}")

def calcular_estatisticas(pacientes):
    """Calcula e exibe estatísticas dos pacientes"""
    print("\n--- ESTATÍSTICAS DA CLÍNICA ---")
    
    if not pacientes:
        print("❌ Nenhum paciente cadastrado ainda!")
        return
    
    # Total de pacientes
    total = len(pacientes)
    print(f"📊 Total de pacientes cadastrados: {total}")
    
    # Calcular idade média
    idades = [p['idade'] for p in pacientes]
    idade_media = sum(idades) / len(idades)
    print(f"📊 Idade média dos pacientes: {idade_media:.1f} anos")
    
    # Paciente mais novo
    mais_novo = min(pacientes, key=lambda p: p['idade'])
    print(f"📊 Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    
    # Paciente mais velho
    mais_velho = max(pacientes, key=lambda p: p['idade'])
    print(f"📊 Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")

def buscar_paciente(pacientes):
    """Busca um paciente pelo nome"""
    print("\n--- BUSCAR PACIENTE ---")
    
    if not pacientes:
        print("❌ Nenhum paciente cadastrado ainda!")
        return
    
    nome_busca = input("Digite o nome do paciente: ").strip().lower()
    
    encontrados = []
    for paciente in pacientes:
        if nome_busca in paciente['nome'].lower():
            encontrados.append(paciente)
    
    if encontrados:
        print(f"\n✅ {len(encontrados)} paciente(s) encontrado(s):\n")
        for p in encontrados:
            print(f"  Nome: {p['nome']}")
            print(f"  Idade: {p['idade']} anos")
            print(f"  Telefone: {p['telefone']}")
            print("-" * 40)
    else:
        print(f"❌ Nenhum paciente encontrado com o nome '{nome_busca}'")

def listar_pacientes(pacientes):
    """Lista todos os pacientes cadastrados"""
    print("\n--- TODOS OS PACIENTES ---")
    
    if not pacientes:
        print("❌ Nenhum paciente cadastrado ainda!")
        return
    
    print(f"\nTotal de {len(pacientes)} paciente(s) cadastrado(s):\n")
    
    for i, paciente in enumerate(pacientes, 1):
        print(f"{i}. {paciente['nome']}")
        print(f"   Idade: {paciente['idade']} anos")
        print(f"   Telefone: {paciente['telefone']}")
        print("-" * 40)

def main():
    """Função principal do programa"""
    pacientes = []  # Lista para armazenar os pacientes
    
    print("\n🏥 Bem-vindo ao Sistema da Clínica Vida+!")
    
    while True:
        exibir_menu()
        
        try:
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == '1':
                cadastrar_paciente(pacientes)
            
            elif opcao == '2':
                calcular_estatisticas(pacientes)
            
            elif opcao == '3':
                buscar_paciente(pacientes)
            
            elif opcao == '4':
                listar_pacientes(pacientes)
            
            elif opcao == '5':
                print("\n👋 Encerrando o sistema...")
                print("Obrigado por usar o Sistema Clínica Vida+!")
                break
            
            else:
                print("\n❌ Opção inválida! Digite um número de 1 a 5.")
            
            input("\nPressione ENTER para continuar...")
            limpar_tela()
            
        except KeyboardInterrupt:
            print("\n\n👋 Sistema encerrado pelo usuário.")
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            input("\nPressione ENTER para continuar...")

# Executa o programa
if __name__ == "__main__":
    main()