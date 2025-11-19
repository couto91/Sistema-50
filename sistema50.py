# -*- coding: utf-8 -*-
import pandas as pd
from datetime import datetime

# ===========================================================
# BLOCO 1 – ESTRUTURA DE DADOS / DATAFRAMES
# Aqui ficam as "tabelas" onde todo o sistema guarda informações.
# O uso de DataFrame atende ao requisito de manipulação de dados.
# ===========================================================

usuarios = pd.DataFrame(columns=['nome', 'idade', 'email', 'nivel', 'pontuacao'])
atividades = pd.DataFrame(columns=['nome', 'data', 'horas', 'pausas', 'humor'])

vagas = pd.DataFrame({
    'titulo': ['Assistente Administrativo', 'Atendente Digital', 'Analista Júnior'],
    'nivel': ['Iniciante', 'Iniciante', 'Intermediário'],
    'modalidade': ['Remoto', 'Híbrido', 'Remoto']
})


# ===========================================================
# BLOCO 2 – FUNÇÕES DE SAÍDA (APRESENTAÇÃO)
# São funções que apenas exibem informações.
# Atendem ao requisito "estrutura de saída".
# ===========================================================

def mostrar_menu():
    print("\n========== MENU PRINCIPAL ==========")
    print("1 - Cadastrar Usuário")
    print("2 - Fazer Avaliação")
    print("3 - Ver Plano de Estudos")
    print("4 - Buscar Vagas")
    print("5 - Registrar Meu Dia")
    print("6 - Ver Relatório")
    print("0 - Sair")
    print("====================================")


def titulo(texto):
    print("\n----", texto, "----\n")


# ===========================================================
# BLOCO 3 – FUNÇÕES DE ENTRADA
# Aqui o sistema coleta dados do usuário.
# Envolve input() e validação com estrutura de repetição.
# ===========================================================

def pedir_numero(texto, minimo, maximo):
    # Estrutura de repetição: repete até o usuário digitar corretamente.
    while True:
        try:
            valor = int(input(texto))
            # Estrutura de condição: valida o intervalo
            if minimo <= valor <= maximo:
                return valor
            print("Valor fora do intervalo.")
        except:
            print("Digite um número válido.")


# ===========================================================
# BLOCO 4 – CADASTRO DE USUÁRIO
# Entradas + uso de DataFrame + retorno do nome.
# ===========================================================

def cadastrar_usuario():
    global usuarios

    titulo("Cadastro de Usuário")

    # Estrutura de entrada
    nome = input("Nome: ")
    idade = pedir_numero("Idade (mínimo 50 anos): ", 50, 120)
    email = input("Email: ")

    # Cria linha no DataFrame
    novo = pd.DataFrame([{
        'nome': nome,
        'idade': idade,
        'email': email,
        'nivel': 'Não avaliado',
        'pontuacao': 0
    }])

    usuarios = pd.concat([usuarios, novo], ignore_index=True)

    print("Usuário cadastrado.")
    return nome


# ===========================================================
# BLOCO 5 – AVALIAÇÃO DIGITAL
# Usa repetição, condição, DataFrame, funções dentro de funções.
# AQUI ESTÁ O ENCAPSULAMENTO AVANÇADO: função dentro de função
# ===========================================================

def fazer_avaliacao(nome):
    global usuarios

    # FUNÇÃO DENTRO DE FUNÇÃO - Encapsulamento Avançado
    def calcular_nivel(pontos):
        """Função interna que calcula o nível baseado na pontuação"""
        # Estrutura de condição: define o nível conforme faixa de pontos
        if pontos <= 6:
            return "Iniciante"
        elif pontos <= 12:
            return "Intermediário"
        return "Avançado"

    titulo("Avaliação Digital")

    # Lista simples de perguntas
    perguntas = [
        "Usa email? (0-2): ",
        "Faz videochamadas? (0-2): ",
        "Usa redes sociais? (0-2): ",
        "Cria documentos? (0-2): ",
        "Usa nuvem? (0-2): ",
        "Compra online? (0-2): "
    ]

    pontos = 0

    # Estrutura de repetição: percorre todas as perguntas
    for p in perguntas:
        pontos += pedir_numero(p, 0, 2)

    # Chamando a função interna (encapsulada)
    nivel = calcular_nivel(pontos)

    # Atualiza DataFrame
    usuarios.loc[usuarios['nome'] == nome, ['pontuacao', 'nivel']] = [pontos, nivel]

    print("Avaliação concluída.")
    print("Pontuação:", pontos)
    print("Nível:", nivel)


# ===========================================================
# BLOCO 6 – PLANO DE ESTUDOS
# Estruturas de condição + repetição simples para exibir conteúdo.
# ===========================================================

def criar_plano(nivel):
    # Condições determinam qual plano será usado
    if nivel == "Iniciante":
        return ["Email Básico", "Navegação na Internet", "Videochamadas"]
    if nivel == "Intermediário":
        return ["Google Drive", "Planilhas", "Redes Sociais Profissionais"]
    return ["Gestão de Projetos", "Análise de Dados", "Marketing Digital"]


def mostrar_plano(nome):
    global usuarios

    titulo("Plano de Estudos")

    usuario = usuarios[usuarios['nome'] == nome]

    if usuario.empty:
        print("Usuário não encontrado.")
        return

    nivel = usuario['nivel'].values[0]

    if nivel == "Não avaliado":
        print("É necessário fazer a avaliação.")
        return

    print("Nível atual:", nivel)
    print("Conteúdos recomendados:")

    # Estrutura de repetição
    for item in criar_plano(nivel):
        print("-", item)


# ===========================================================
# BLOCO 7 – BUSCA DE VAGAS
# Usa DataFrame + filtro + repetição.
# ===========================================================

def buscar_vagas(nome):
    global usuarios, vagas

    titulo("Vagas Disponíveis")

    usuario = usuarios[usuarios['nome'] == nome]

    if usuario.empty:
        print("Usuário não encontrado.")
        return

    nivel = usuario['nivel'].values[0]

    if nivel == "Não avaliado":
        print("Faça a avaliação primeiro.")
        return

    print("Nível:", nivel)
    print("Vagas compatíveis:\n")

    # DataFrame filtrado
    filtradas = vagas[vagas['nivel'] == nivel]

    for _, row in filtradas.iterrows():
        print("Título:", row['titulo'])
        print("Modalidade:", row['modalidade'])
        print()


# ===========================================================
# BLOCO 8 – REGISTRO DIÁRIO + RELATÓRIO
# Entrada, condição, repetição e DataFrame.
# ===========================================================

def analisar_dia(horas, pausas, humor):
    # Análise simples baseada em condições
    print("\nResumo do seu dia:")

    if horas > 8:
        print("- Excesso de horas trabalhadas.")
    else:
        print("- Horas dentro do padrão.")

    if pausas < 3:
        print("- Poucas pausas.")
    else:
        print("- Boas pausas.")

    if humor < 3:
        print("- Humor baixo.")
    else:
        print("- Humor estável.")


def registrar_dia(nome):
    global atividades

    titulo("Registro do Dia")

    horas = pedir_numero("Horas trabalhadas (0-24): ", 0, 24)
    pausas = pedir_numero("Pausas (0-10): ", 0, 10)
    humor = pedir_numero("Humor (1-4): ", 1, 4)

    novo = pd.DataFrame([{
        'nome': nome,
        'data': datetime.now().strftime("%d/%m/%Y"),
        'horas': horas,
        'pausas': pausas,
        'humor': humor
    }])

    atividades = pd.concat([atividades, novo], ignore_index=True)

    print("Dia registrado.")
    analisar_dia(horas, pausas, humor)


def mostrar_relatorio(nome):
    global usuarios, atividades

    titulo("Relatório do Usuário")

    usuario = usuarios[usuarios['nome'] == nome]

    if usuario.empty:
        print("Usuário não encontrado.")
        return

    print("Nome:", usuario['nome'].values[0])
    print("Idade:", usuario['idade'].values[0])
    print("Nível:", usuario['nivel'].values[0])

    dias = atividades[atividades['nome'] == nome]

    if dias.empty:
        print("\nNenhum registro diário.")
        return

    print("\nDias registrados:", len(dias))
    print("Média de horas:", dias['horas'].mean())
    print("Média de pausas:", dias['pausas'].mean())
    print("Humor médio:", dias['humor'].mean())


# ===========================================================
# BLOCO 9 – MENU PRINCIPAL
# Estrutura de repetição (loop) + condições para navegar.
# É o controlador geral do programa.
# ===========================================================

def menu():
    usuario = None

    print("\nBem-vindo ao sistema 50+\n")

    # Estrutura de repetição: loop principal
    while True:
        mostrar_menu()
        op = input("Escolha: ")

        # Estruturas de condição para cada fluxo
        if op == "1":
            usuario = cadastrar_usuario()

        elif op == "2":
            if usuario:
                fazer_avaliacao(usuario)
            else:
                print("Cadastre um usuário primeiro.")

        elif op == "3":
            if usuario:
                mostrar_plano(usuario)
            else:
                print("Cadastre um usuário primeiro.")

        elif op == "4":
            if usuario:
                buscar_vagas(usuario)
            else:
                print("Cadastre um usuário primeiro.")

        elif op == "5":
            if usuario:
                registrar_dia(usuario)
            else:
                print("Cadastre um usuário primeiro.")

        elif op == "6":
            if usuario:
                mostrar_relatorio(usuario)
            else:
                print("Cadastre um usuário primeiro.")

        elif op == "0":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida.")


# Execução principal
if __name__ == "__main__":
    menu()