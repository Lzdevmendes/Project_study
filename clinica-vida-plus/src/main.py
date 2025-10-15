"""
Sistema de Gestão de Pacientes - Clínica Vida+
Módulo principal para cadastro e gerenciamento de pacientes

Author: Sistema Clínica Vida+
Date: 2025-10-15
"""

import json
import os
import re
from datetime import datetime
from typing import List, Dict, Optional
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False
    # Fallback para quando colorama não estiver disponível
    class Fore:
        GREEN = CYAN = YELLOW = RED = MAGENTA = BLUE = WHITE = ""
    class Style:
        BRIGHT = RESET_ALL = ""


class Paciente:
    """Classe que representa um paciente da clínica"""

    def __init__(self, nome: str, idade: int, telefone: str, cpf: str = ""):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cpf = cpf
        self.data_cadastro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self) -> Dict:
        """Converte o objeto paciente para dicionário"""
        return {
            "nome": self.nome,
            "idade": self.idade,
            "telefone": self.telefone,
            "cpf": self.cpf,
            "data_cadastro": self.data_cadastro
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Paciente':
        """Cria um objeto Paciente a partir de um dicionário"""
        paciente = Paciente(
            nome=data["nome"],
            idade=data["idade"],
            telefone=data["telefone"],
            cpf=data.get("cpf", "")
        )
        paciente.data_cadastro = data.get("data_cadastro", paciente.data_cadastro)
        return paciente


class SistemaClinica:
    """Classe principal do sistema de gestão da clínica"""

    def __init__(self):
        self.pacientes: List[Paciente] = []
        self.arquivo_dados = os.path.join("clinica-vida-plus", "data", "pacientes.json")
        self.dir_backup = os.path.join("clinica-vida-plus", "backups")
        self._garantir_diretorios()
        self.carregar_dados()

    def _garantir_diretorios(self):
        """Garante que os diretórios necessários existam"""
        os.makedirs(os.path.dirname(self.arquivo_dados), exist_ok=True)
        os.makedirs(self.dir_backup, exist_ok=True)

    def carregar_dados(self):
        """Carrega os dados dos pacientes do arquivo JSON"""
        if os.path.exists(self.arquivo_dados):
            try:
                with open(self.arquivo_dados, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                    self.pacientes = [Paciente.from_dict(p) for p in dados]
                print(f"{Fore.GREEN}Dados carregados: {len(self.pacientes)} pacientes")
            except Exception as e:
                print(f"{Fore.RED}Erro ao carregar dados: {e}")

    def salvar_dados(self):
        """Salva os dados dos pacientes no arquivo JSON"""
        try:
            dados = [p.to_dict() for p in self.pacientes]
            with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
                json.dump(dados, f, ensure_ascii=False, indent=2)
            print(f"{Fore.GREEN}Dados salvos com sucesso!")
        except Exception as e:
            print(f"{Fore.RED}Erro ao salvar dados: {e}")

    def fazer_backup(self):
        """Cria um backup dos dados com timestamp"""
        if not os.path.exists(self.arquivo_dados):
            print(f"{Fore.YELLOW}Nenhum dado para fazer backup")
            return

        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            arquivo_backup = os.path.join(self.dir_backup, f"pacientes_backup_{timestamp}.json")

            with open(self.arquivo_dados, 'r', encoding='utf-8') as f_origem:
                with open(arquivo_backup, 'w', encoding='utf-8') as f_destino:
                    f_destino.write(f_origem.read())

            print(f"{Fore.GREEN}Backup criado: {arquivo_backup}")
        except Exception as e:
            print(f"{Fore.RED}Erro ao criar backup: {e}")

    @staticmethod
    def validar_telefone(telefone: str) -> bool:
        """Valida formato de telefone (XX) XXXXX-XXXX ou (XX) XXXX-XXXX"""
        pattern = r'^\(\d{2}\)\s?\d{4,5}-?\d{4}$'
        return bool(re.match(pattern, telefone.replace(" ", "")))

    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        """Valida formato e dígitos verificadores do CPF"""
        # Remove caracteres não numéricos
        cpf = re.sub(r'\D', '', cpf)

        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False

        # Valida primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma * 10 % 11) % 10

        if digito1 != int(cpf[9]):
            return False

        # Valida segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma * 10 % 11) % 10

        return digito2 == int(cpf[10])

    def cadastrar_paciente(self):
        """Cadastra um novo paciente no sistema"""
        print(f"\n{Fore.CYAN}{Style.BRIGHT}=== CADASTRAR NOVO PACIENTE ===")

        try:
            # Nome
            nome = input(f"{Fore.WHITE}Nome completo: ").strip()
            if len(nome) < 3:
                print(f"{Fore.RED}Nome deve ter pelo menos 3 caracteres")
                return

            # Idade
            while True:
                try:
                    idade = int(input(f"{Fore.WHITE}Idade: "))
                    if 0 < idade < 150:
                        break
                    print(f"{Fore.RED}Idade deve estar entre 1 e 149")
                except ValueError:
                    print(f"{Fore.RED}Por favor, digite um número válido")

            # Telefone
            while True:
                telefone = input(f"{Fore.WHITE}Telefone (XX) XXXXX-XXXX: ").strip()
                if self.validar_telefone(telefone):
                    break
                print(f"{Fore.RED}Formato inválido. Use: (XX) XXXXX-XXXX")

            # CPF
            while True:
                cpf = input(f"{Fore.WHITE}CPF (XXX.XXX.XXX-XX): ").strip()
                if self.validar_cpf(cpf):
                    # Formata o CPF
                    cpf_numeros = re.sub(r'\D', '', cpf)
                    cpf = f"{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]}"
                    break
                print(f"{Fore.RED}CPF inválido. Verifique os dígitos")

            # Cria e adiciona o paciente
            paciente = Paciente(nome=nome, idade=idade, telefone=telefone, cpf=cpf)
            self.pacientes.append(paciente)
            self.salvar_dados()

            print(f"\n{Fore.GREEN}{Style.BRIGHT}✓ Paciente cadastrado com sucesso!")
            print(f"{Fore.CYAN}Data/Hora: {paciente.data_cadastro}")

        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Cadastro cancelado")
        except Exception as e:
            print(f"{Fore.RED}Erro ao cadastrar: {e}")

    def ver_estatisticas(self):
        """Exibe estatísticas dos pacientes cadastrados"""
        print(f"\n{Fore.CYAN}{Style.BRIGHT}=== ESTATÍSTICAS ===")

        if not self.pacientes:
            print(f"{Fore.YELLOW}Nenhum paciente cadastrado")
            return

        total = len(self.pacientes)
        idades = [p.idade for p in self.pacientes]
        idade_media = sum(idades) / total
        paciente_mais_novo = min(self.pacientes, key=lambda p: p.idade)
        paciente_mais_velho = max(self.pacientes, key=lambda p: p.idade)

        print(f"{Fore.WHITE}Total de pacientes: {Fore.GREEN}{total}")
        print(f"{Fore.WHITE}Idade média: {Fore.GREEN}{idade_media:.1f} anos")
        print(f"{Fore.WHITE}Paciente mais novo: {Fore.GREEN}{paciente_mais_novo.nome} ({paciente_mais_novo.idade} anos)")
        print(f"{Fore.WHITE}Paciente mais velho: {Fore.GREEN}{paciente_mais_velho.nome} ({paciente_mais_velho.idade} anos)")

    def buscar_paciente(self):
        """Busca um paciente por nome"""
        print(f"\n{Fore.CYAN}{Style.BRIGHT}=== BUSCAR PACIENTE ===")

        if not self.pacientes:
            print(f"{Fore.YELLOW}Nenhum paciente cadastrado")
            return

        busca = input(f"{Fore.WHITE}Digite o nome para buscar: ").strip().lower()

        encontrados = [p for p in self.pacientes if busca in p.nome.lower()]

        if encontrados:
            print(f"\n{Fore.GREEN}Encontrados {len(encontrados)} paciente(s):\n")
            for p in encontrados:
                self._exibir_paciente(p)
        else:
            print(f"{Fore.YELLOW}Nenhum paciente encontrado com esse nome")

    def listar_pacientes(self):
        """Lista todos os pacientes cadastrados"""
        print(f"\n{Fore.CYAN}{Style.BRIGHT}=== LISTA DE PACIENTES ===")

        if not self.pacientes:
            print(f"{Fore.YELLOW}Nenhum paciente cadastrado")
            return

        print(f"\n{Fore.WHITE}Total: {len(self.pacientes)} paciente(s)\n")

        for i, p in enumerate(self.pacientes, 1):
            print(f"{Fore.MAGENTA}[{i}]")
            self._exibir_paciente(p)

    @staticmethod
    def _exibir_paciente(paciente: Paciente):
        """Exibe as informações de um paciente formatadas"""
        print(f"{Fore.WHITE}Nome: {Fore.GREEN}{paciente.nome}")
        print(f"{Fore.WHITE}Idade: {Fore.GREEN}{paciente.idade} anos")
        print(f"{Fore.WHITE}Telefone: {Fore.GREEN}{paciente.telefone}")
        print(f"{Fore.WHITE}CPF: {Fore.GREEN}{paciente.cpf}")
        print(f"{Fore.WHITE}Cadastrado em: {Fore.CYAN}{paciente.data_cadastro}")
        print()

    def menu_principal(self):
        """Exibe o menu principal e processa as opções"""
        while True:
            print(f"\n{Fore.BLUE}{Style.BRIGHT}{'='*40}")
            print(f"{Fore.BLUE}{Style.BRIGHT}   SISTEMA CLÍNICA VIDA+")
            print(f"{Fore.BLUE}{Style.BRIGHT}{'='*40}")
            print(f"{Fore.WHITE}1. {Fore.CYAN}Cadastrar paciente")
            print(f"{Fore.WHITE}2. {Fore.CYAN}Ver estatísticas")
            print(f"{Fore.WHITE}3. {Fore.CYAN}Buscar paciente")
            print(f"{Fore.WHITE}4. {Fore.CYAN}Listar todos os pacientes")
            print(f"{Fore.WHITE}5. {Fore.CYAN}Fazer backup dos dados")
            print(f"{Fore.WHITE}6. {Fore.RED}Sair")
            print(f"{Fore.BLUE}{Style.BRIGHT}{'='*40}")

            try:
                opcao = input(f"\n{Fore.YELLOW}Escolha uma opção: ").strip()

                if opcao == "1":
                    self.cadastrar_paciente()
                elif opcao == "2":
                    self.ver_estatisticas()
                elif opcao == "3":
                    self.buscar_paciente()
                elif opcao == "4":
                    self.listar_pacientes()
                elif opcao == "5":
                    self.fazer_backup()
                elif opcao == "6":
                    print(f"\n{Fore.GREEN}Obrigado por usar o Sistema Clínica Vida+!")
                    break
                else:
                    print(f"{Fore.RED}Opção inválida! Escolha entre 1 e 6")

            except KeyboardInterrupt:
                print(f"\n\n{Fore.YELLOW}Programa interrompido pelo usuário")
                break
            except Exception as e:
                print(f"{Fore.RED}Erro: {e}")


def main():
    """Função principal do programa"""
    if not COLORS_AVAILABLE:
        print("Aviso: colorama não instalado. Execute: pip install colorama")
        print("O sistema funcionará sem cores.\n")

    sistema = SistemaClinica()
    sistema.menu_principal()


if __name__ == "__main__":
    main()
