"""
Sistema de Fila de Atendimento - Clínica Vida+
Módulo para gerenciamento de fila de atendimento de pacientes

Implementa uma estrutura de dados FIFO (First In, First Out)
para controle da ordem de atendimento.

Author: Sistema Clínica Vida+
Date: 2025-10-15
"""

from collections import deque
from typing import Optional, Dict
import re
try:
    from colorama import Fore, Style
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False
    class Fore:
        GREEN = CYAN = YELLOW = RED = MAGENTA = BLUE = WHITE = ""
    class Style:
        BRIGHT = RESET_ALL = ""


class PacienteFila:
    """Classe que representa um paciente na fila"""

    def __init__(self, nome: str, cpf: str, prioridade: str = "normal"):
        self.nome = nome
        self.cpf = cpf
        self.prioridade = prioridade  # "normal", "preferencial", "emergencia"

    def __str__(self) -> str:
        return f"{self.nome} (CPF: {self.cpf}) [{self.prioridade.upper()}]"

    def to_dict(self) -> Dict:
        """Converte para dicionário"""
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "prioridade": self.prioridade
        }


class FilaAtendimento:
    """
    Classe para gerenciar a fila de atendimento da clínica

    Implementa três filas com prioridades diferentes:
    - Emergência (maior prioridade)
    - Preferencial (prioridade média)
    - Normal (prioridade padrão)
    """

    def __init__(self):
        self.fila_emergencia = deque()
        self.fila_preferencial = deque()
        self.fila_normal = deque()

    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        """Valida formato e dígitos verificadores do CPF"""
        cpf = re.sub(r'\D', '', cpf)

        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False

        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma * 10 % 11) % 10

        if digito1 != int(cpf[9]):
            return False

        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma * 10 % 11) % 10

        return digito2 == int(cpf[10])

    def inserir_paciente(self, nome: str, cpf: str, prioridade: str = "normal") -> bool:
        """
        Insere um paciente na fila apropriada

        Args:
            nome: Nome do paciente
            cpf: CPF do paciente
            prioridade: "normal", "preferencial" ou "emergencia"

        Returns:
            bool: True se inserido com sucesso, False caso contrário
        """
        if not self.validar_cpf(cpf):
            print(f"{Fore.RED}CPF inválido!")
            return False

        # Formata o CPF
        cpf_numeros = re.sub(r'\D', '', cpf)
        cpf_formatado = f"{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]}"

        paciente = PacienteFila(nome, cpf_formatado, prioridade)

        if prioridade == "emergencia":
            self.fila_emergencia.append(paciente)
        elif prioridade == "preferencial":
            self.fila_preferencial.append(paciente)
        else:
            self.fila_normal.append(paciente)

        print(f"{Fore.GREEN}Paciente {nome} adicionado à fila {prioridade.upper()}")
        return True

    def remover_proximo(self) -> Optional[PacienteFila]:
        """
        Remove e retorna o próximo paciente da fila
        Segue ordem de prioridade: emergência > preferencial > normal

        Returns:
            PacienteFila ou None se não houver pacientes
        """
        if self.fila_emergencia:
            return self.fila_emergencia.popleft()
        elif self.fila_preferencial:
            return self.fila_preferencial.popleft()
        elif self.fila_normal:
            return self.fila_normal.popleft()
        return None

    def mostrar_fila(self):
        """Exibe todos os pacientes nas filas"""
        total = len(self.fila_emergencia) + len(self.fila_preferencial) + len(self.fila_normal)

        print(f"\n{Fore.CYAN}{Style.BRIGHT}=== FILA DE ATENDIMENTO ===")
        print(f"{Fore.WHITE}Total de pacientes: {Fore.YELLOW}{total}\n")

        if self.fila_emergencia:
            print(f"{Fore.RED}{Style.BRIGHT}EMERGÊNCIA ({len(self.fila_emergencia)} paciente(s)):")
            for i, paciente in enumerate(self.fila_emergencia, 1):
                print(f"{Fore.WHITE}  {i}. {paciente}")

        if self.fila_preferencial:
            print(f"\n{Fore.YELLOW}{Style.BRIGHT}PREFERENCIAL ({len(self.fila_preferencial)} paciente(s)):")
            for i, paciente in enumerate(self.fila_preferencial, 1):
                print(f"{Fore.WHITE}  {i}. {paciente}")

        if self.fila_normal:
            print(f"\n{Fore.GREEN}{Style.BRIGHT}NORMAL ({len(self.fila_normal)} paciente(s)):")
            for i, paciente in enumerate(self.fila_normal, 1):
                print(f"{Fore.WHITE}  {i}. {paciente}")

        if total == 0:
            print(f"{Fore.YELLOW}Nenhum paciente na fila")

    def obter_proximo_sem_remover(self) -> Optional[PacienteFila]:
        """
        Retorna o próximo paciente sem removê-lo da fila

        Returns:
            PacienteFila ou None se não houver pacientes
        """
        if self.fila_emergencia:
            return self.fila_emergencia[0]
        elif self.fila_preferencial:
            return self.fila_preferencial[0]
        elif self.fila_normal:
            return self.fila_normal[0]
        return None

    def esta_vazia(self) -> bool:
        """Verifica se todas as filas estão vazias"""
        return (len(self.fila_emergencia) == 0 and
                len(self.fila_preferencial) == 0 and
                len(self.fila_normal) == 0)

    def tamanho_total(self) -> int:
        """Retorna o número total de pacientes em todas as filas"""
        return len(self.fila_emergencia) + len(self.fila_preferencial) + len(self.fila_normal)


def demonstracao_algoritmo():
    """
    Demonstração do algoritmo conforme solicitado:
    1. Inserir 3 pacientes
    2. Remover o primeiro
    3. Mostrar restantes
    """
    print(f"{Fore.BLUE}{Style.BRIGHT}{'='*60}")
    print(f"{Fore.BLUE}{Style.BRIGHT}   DEMONSTRAÇÃO DO ALGORITMO DE FILA")
    print(f"{Fore.BLUE}{Style.BRIGHT}{'='*60}\n")

    fila = FilaAtendimento()

    print(f"{Fore.CYAN}{Style.BRIGHT}PASSO 1: Inserindo 3 pacientes na fila\n")

    pacientes_demo = [
        ("João da Silva", "123.456.789-09", "normal"),
        ("Maria Santos", "987.654.321-00", "preferencial"),
        ("Pedro Oliveira", "111.222.333-44", "normal")
    ]

    for nome, cpf, prioridade in pacientes_demo:
        fila.inserir_paciente(nome, cpf, prioridade)

    print(f"\n{Fore.CYAN}{Style.BRIGHT}PASSO 2: Mostrando fila completa")
    fila.mostrar_fila()

    print(f"\n{Fore.CYAN}{Style.BRIGHT}PASSO 3: Removendo primeiro paciente para atendimento")
    proximo = fila.remover_proximo()
    if proximo:
        print(f"{Fore.GREEN}Chamando para atendimento: {proximo}")

    print(f"\n{Fore.CYAN}{Style.BRIGHT}PASSO 4: Mostrando pacientes restantes na fila")
    fila.mostrar_fila()


def menu_interativo():
    """Menu interativo para gerenciar a fila de atendimento"""
    fila = FilaAtendimento()

    while True:
        print(f"\n{Fore.BLUE}{Style.BRIGHT}{'='*60}")
        print(f"{Fore.BLUE}{Style.BRIGHT}   GERENCIAMENTO DE FILA DE ATENDIMENTO - CLÍNICA VIDA+")
        print(f"{Fore.BLUE}{Style.BRIGHT}{'='*60}")
        print(f"{Fore.WHITE}1. {Fore.CYAN}Inserir paciente na fila")
        print(f"{Fore.WHITE}2. {Fore.CYAN}Chamar próximo paciente")
        print(f"{Fore.WHITE}3. {Fore.CYAN}Mostrar fila completa")
        print(f"{Fore.WHITE}4. {Fore.CYAN}Ver próximo paciente (sem remover)")
        print(f"{Fore.WHITE}5. {Fore.CYAN}Executar demonstração do algoritmo")
        print(f"{Fore.WHITE}6. {Fore.RED}Voltar")
        print(f"{Fore.BLUE}{Style.BRIGHT}{'='*60}")

        try:
            opcao = input(f"\n{Fore.YELLOW}Escolha uma opção: ").strip()

            if opcao == "1":
                print(f"\n{Fore.CYAN}{Style.BRIGHT}=== INSERIR PACIENTE NA FILA ===")
                nome = input(f"{Fore.WHITE}Nome do paciente: ").strip()

                if len(nome) < 3:
                    print(f"{Fore.RED}Nome deve ter pelo menos 3 caracteres")
                    continue

                cpf = input(f"{Fore.WHITE}CPF (XXX.XXX.XXX-XX): ").strip()

                print(f"\n{Fore.WHITE}Tipo de atendimento:")
                print(f"{Fore.RED}1. Emergência")
                print(f"{Fore.YELLOW}2. Preferencial")
                print(f"{Fore.GREEN}3. Normal")

                tipo = input(f"{Fore.WHITE}Escolha (1-3): ").strip()

                if tipo == "1":
                    prioridade = "emergencia"
                elif tipo == "2":
                    prioridade = "preferencial"
                else:
                    prioridade = "normal"

                fila.inserir_paciente(nome, cpf, prioridade)

            elif opcao == "2":
                if fila.esta_vazia():
                    print(f"{Fore.YELLOW}Nenhum paciente na fila")
                else:
                    paciente = fila.remover_proximo()
                    print(f"\n{Fore.GREEN}{Style.BRIGHT}Chamando para atendimento:")
                    print(f"{Fore.WHITE}{paciente}")
                    print(f"\n{Fore.CYAN}Pacientes restantes: {fila.tamanho_total()}")

            elif opcao == "3":
                fila.mostrar_fila()

            elif opcao == "4":
                proximo = fila.obter_proximo_sem_remover()
                if proximo:
                    print(f"\n{Fore.CYAN}Próximo paciente a ser atendido:")
                    print(f"{Fore.WHITE}{proximo}")
                else:
                    print(f"{Fore.YELLOW}Nenhum paciente na fila")

            elif opcao == "5":
                print(f"\n{Fore.YELLOW}Isso criará uma nova fila de demonstração. Continuar? (S/N)")
                if input().strip().upper() == 'S':
                    demonstracao_algoritmo()

            elif opcao == "6":
                break

            else:
                print(f"{Fore.RED}Opção inválida! Escolha entre 1 e 6")

        except KeyboardInterrupt:
            print(f"\n\n{Fore.YELLOW}Programa interrompido pelo usuário")
            break
        except Exception as e:
            print(f"{Fore.RED}Erro: {e}")


def main():
    """Função principal do módulo"""
    if not COLORS_AVAILABLE:
        print("Aviso: colorama não instalado. Execute: pip install colorama\n")

    menu_interativo()


if __name__ == "__main__":
    main()
