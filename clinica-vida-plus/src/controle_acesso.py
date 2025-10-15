"""
Sistema de Controle de Acesso - Clínica Vida+
Módulo para controle lógico de acesso de pacientes

Variáveis Lógicas:
- A: Paciente tem agendamento marcado
- B: Paciente está com documentos em dia
- C: Há médico disponível
- D: Paciente está em dia com pagamentos

Regras de Acesso:
- Consulta Normal: (A ∧ B ∧ C) ∨ (B ∧ C ∧ D)
- Emergência: C ∧ (B ∨ D)

Author: Sistema Clínica Vida+
Date: 2025-10-15
"""

from typing import Dict, List, Tuple
try:
    from colorama import Fore, Style
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False
    class Fore:
        GREEN = CYAN = YELLOW = RED = MAGENTA = BLUE = WHITE = ""
    class Style:
        BRIGHT = RESET_ALL = ""


class ControleAcesso:
    """Classe para gerenciar o controle lógico de acesso de pacientes"""

    @staticmethod
    def consulta_normal(A: bool, B: bool, C: bool, D: bool) -> bool:
        """
        Verifica se paciente pode ter consulta normal
        Regra: (A ∧ B ∧ C) ∨ (B ∧ C ∧ D)

        Args:
            A: Paciente tem agendamento marcado
            B: Paciente está com documentos em dia
            C: Há médico disponível
            D: Paciente está em dia com pagamentos

        Returns:
            bool: True se pode ter consulta, False caso contrário
        """
        return (A and B and C) or (B and C and D)

    @staticmethod
    def emergencia(A: bool, B: bool, C: bool, D: bool) -> bool:
        """
        Verifica se paciente pode ter atendimento de emergência
        Regra: C ∧ (B ∨ D)

        Args:
            A: Paciente tem agendamento marcado (não usado na emergência)
            B: Paciente está com documentos em dia
            C: Há médico disponível
            D: Paciente está em dia com pagamentos

        Returns:
            bool: True se pode ter atendimento, False caso contrário
        """
        return C and (B or D)

    @staticmethod
    def gerar_tabela_verdade_consulta_normal() -> List[Tuple]:
        """
        Gera tabela verdade completa para consulta normal

        Returns:
            Lista de tuplas com (A, B, C, D, Resultado)
        """
        tabela = []
        for A in [False, True]:
            for B in [False, True]:
                for C in [False, True]:
                    for D in [False, True]:
                        resultado = ControleAcesso.consulta_normal(A, B, C, D)
                        tabela.append((A, B, C, D, resultado))
        return tabela

    @staticmethod
    def gerar_tabela_verdade_emergencia() -> List[Tuple]:
        """
        Gera tabela verdade completa para emergência

        Returns:
            Lista de tuplas com (A, B, C, D, Resultado)
        """
        tabela = []
        for A in [False, True]:
            for B in [False, True]:
                for C in [False, True]:
                    for D in [False, True]:
                        resultado = ControleAcesso.emergencia(A, B, C, D)
                        tabela.append((A, B, C, D, resultado))
        return tabela

    @staticmethod
    def contar_situacoes_permitidas() -> Dict[str, int]:
        """
        Conta quantas situações permitem atendimento

        Returns:
            Dicionário com contagens para consulta normal e emergência
        """
        tabela_normal = ControleAcesso.gerar_tabela_verdade_consulta_normal()
        tabela_emergencia = ControleAcesso.gerar_tabela_verdade_emergencia()

        permitidas_normal = sum(1 for linha in tabela_normal if linha[4])
        permitidas_emergencia = sum(1 for linha in tabela_emergencia if linha[4])

        return {
            "consulta_normal": permitidas_normal,
            "emergencia": permitidas_emergencia,
            "total_combinacoes": 16
        }

    @staticmethod
    def exibir_tabela_verdade(tipo: str = "consulta_normal"):
        """
        Exibe a tabela verdade formatada no console

        Args:
            tipo: "consulta_normal" ou "emergencia"
        """
        if tipo == "consulta_normal":
            print(f"\n{Fore.CYAN}{Style.BRIGHT}=== TABELA VERDADE: CONSULTA NORMAL ===")
            print(f"{Fore.YELLOW}Regra: (A ∧ B ∧ C) ∨ (B ∧ C ∧ D)")
            tabela = ControleAcesso.gerar_tabela_verdade_consulta_normal()
        else:
            print(f"\n{Fore.CYAN}{Style.BRIGHT}=== TABELA VERDADE: EMERGÊNCIA ===")
            print(f"{Fore.YELLOW}Regra: C ∧ (B ∨ D)")
            tabela = ControleAcesso.gerar_tabela_verdade_emergencia()

        print(f"\n{Fore.WHITE}{'A':^5} | {'B':^5} | {'C':^5} | {'D':^5} | {'Resultado':^10}")
        print(f"{'-'*50}")

        for linha in tabela:
            A, B, C, D, resultado = linha
            a_str = 'V' if A else 'F'
            b_str = 'V' if B else 'F'
            c_str = 'V' if C else 'F'
            d_str = 'V' if D else 'F'
            resultado_str = f"{Fore.GREEN}PERMITIDO" if resultado else f"{Fore.RED}NEGADO"

            print(f"{Fore.WHITE}{a_str:^5} | {b_str:^5} | {c_str:^5} | {d_str:^5} | {resultado_str:^20}")

    @staticmethod
    def verificar_acesso(A: bool, B: bool, C: bool, D: bool, tipo: str = "consulta_normal") -> Dict:
        """
        Verifica acesso e retorna resultado detalhado

        Args:
            A: Paciente tem agendamento marcado
            B: Paciente está com documentos em dia
            C: Há médico disponível
            D: Paciente está em dia com pagamentos
            tipo: "consulta_normal" ou "emergencia"

        Returns:
            Dicionário com resultado e detalhes
        """
        if tipo == "consulta_normal":
            permitido = ControleAcesso.consulta_normal(A, B, C, D)
            regra = "(A ∧ B ∧ C) ∨ (B ∧ C ∧ D)"
        else:
            permitido = ControleAcesso.emergencia(A, B, C, D)
            regra = "C ∧ (B ∨ D)"

        return {
            "permitido": permitido,
            "tipo": tipo,
            "regra": regra,
            "valores": {
                "A - Agendamento": A,
                "B - Documentos": B,
                "C - Médico disponível": C,
                "D - Pagamentos": D
            }
        }


def menu_interativo():
    """Menu interativo para testar o sistema de controle de acesso"""
    while True:
        print(f"\n{Fore.BLUE}{Style.BRIGHT}{'='*50}")
        print(f"{Fore.BLUE}{Style.BRIGHT}   SISTEMA DE CONTROLE DE ACESSO - CLÍNICA VIDA+")
        print(f"{Fore.BLUE}{Style.BRIGHT}{'='*50}")
        print(f"{Fore.WHITE}1. {Fore.CYAN}Verificar acesso (Consulta Normal)")
        print(f"{Fore.WHITE}2. {Fore.CYAN}Verificar acesso (Emergência)")
        print(f"{Fore.WHITE}3. {Fore.CYAN}Ver tabela verdade (Consulta Normal)")
        print(f"{Fore.WHITE}4. {Fore.CYAN}Ver tabela verdade (Emergência)")
        print(f"{Fore.WHITE}5. {Fore.CYAN}Ver estatísticas de acesso")
        print(f"{Fore.WHITE}6. {Fore.CYAN}Teste prático (A=F, B=V, C=V, D=F)")
        print(f"{Fore.WHITE}7. {Fore.RED}Voltar")
        print(f"{Fore.BLUE}{Style.BRIGHT}{'='*50}")

        try:
            opcao = input(f"\n{Fore.YELLOW}Escolha uma opção: ").strip()

            if opcao == "1" or opcao == "2":
                tipo = "consulta_normal" if opcao == "1" else "emergencia"
                print(f"\n{Fore.CYAN}Digite os valores (V para Verdadeiro, F para Falso):")

                A = input(f"{Fore.WHITE}A - Paciente tem agendamento marcado (V/F): ").strip().upper() == 'V'
                B = input(f"{Fore.WHITE}B - Paciente está com documentos em dia (V/F): ").strip().upper() == 'V'
                C = input(f"{Fore.WHITE}C - Há médico disponível (V/F): ").strip().upper() == 'V'
                D = input(f"{Fore.WHITE}D - Paciente está em dia com pagamentos (V/F): ").strip().upper() == 'V'

                resultado = ControleAcesso.verificar_acesso(A, B, C, D, tipo)

                print(f"\n{Fore.CYAN}{Style.BRIGHT}=== RESULTADO DA VERIFICAÇÃO ===")
                print(f"{Fore.WHITE}Tipo: {Fore.YELLOW}{resultado['tipo'].upper()}")
                print(f"{Fore.WHITE}Regra: {Fore.YELLOW}{resultado['regra']}")
                print(f"\n{Fore.WHITE}Valores:")
                for chave, valor in resultado['valores'].items():
                    status = f"{Fore.GREEN}SIM" if valor else f"{Fore.RED}NÃO"
                    print(f"  {chave}: {status}")

                if resultado['permitido']:
                    print(f"\n{Fore.GREEN}{Style.BRIGHT}✓ ACESSO PERMITIDO")
                else:
                    print(f"\n{Fore.RED}{Style.BRIGHT}✗ ACESSO NEGADO")

            elif opcao == "3":
                ControleAcesso.exibir_tabela_verdade("consulta_normal")

            elif opcao == "4":
                ControleAcesso.exibir_tabela_verdade("emergencia")

            elif opcao == "5":
                stats = ControleAcesso.contar_situacoes_permitidas()
                print(f"\n{Fore.CYAN}{Style.BRIGHT}=== ESTATÍSTICAS DE ACESSO ===")
                print(f"{Fore.WHITE}Total de combinações possíveis: {Fore.YELLOW}{stats['total_combinacoes']}")
                print(f"\n{Fore.WHITE}Consulta Normal:")
                print(f"  Situações permitidas: {Fore.GREEN}{stats['consulta_normal']}")
                print(f"  Situações negadas: {Fore.RED}{stats['total_combinacoes'] - stats['consulta_normal']}")
                print(f"  Percentual de acesso: {Fore.YELLOW}{(stats['consulta_normal']/stats['total_combinacoes']*100):.1f}%")

                print(f"\n{Fore.WHITE}Emergência:")
                print(f"  Situações permitidas: {Fore.GREEN}{stats['emergencia']}")
                print(f"  Situações negadas: {Fore.RED}{stats['total_combinacoes'] - stats['emergencia']}")
                print(f"  Percentual de acesso: {Fore.YELLOW}{(stats['emergencia']/stats['total_combinacoes']*100):.1f}%")

            elif opcao == "6":
                print(f"\n{Fore.CYAN}{Style.BRIGHT}=== TESTE PRÁTICO ===")
                print(f"{Fore.WHITE}Valores: A=F, B=V, C=V, D=F")

                A, B, C, D = False, True, True, False

                print(f"\n{Fore.YELLOW}Teste para Consulta Normal:")
                resultado_normal = ControleAcesso.verificar_acesso(A, B, C, D, "consulta_normal")
                if resultado_normal['permitido']:
                    print(f"{Fore.GREEN}{Style.BRIGHT}✓ ACESSO PERMITIDO")
                else:
                    print(f"{Fore.RED}{Style.BRIGHT}✗ ACESSO NEGADO")

                print(f"\n{Fore.YELLOW}Teste para Emergência:")
                resultado_emergencia = ControleAcesso.verificar_acesso(A, B, C, D, "emergencia")
                if resultado_emergencia['permitido']:
                    print(f"{Fore.GREEN}{Style.BRIGHT}✓ ACESSO PERMITIDO")
                else:
                    print(f"{Fore.RED}{Style.BRIGHT}✗ ACESSO NEGADO")

                print(f"\n{Fore.CYAN}Análise:")
                print(f"{Fore.WHITE}Consulta Normal: (F ∧ V ∧ V) ∨ (V ∧ V ∧ F) = F ∨ F = {Fore.RED}F")
                print(f"{Fore.WHITE}Emergência: V ∧ (V ∨ F) = V ∧ V = {Fore.GREEN}V")

            elif opcao == "7":
                break

            else:
                print(f"{Fore.RED}Opção inválida! Escolha entre 1 e 7")

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
