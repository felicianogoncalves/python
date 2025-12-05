# Sistema de Gestão de Tarefas 
# projPython_feliciano
import json
from datetime import datetime   # importamos o datetime para guardar horas e datas

tarefas = [] # lista para adicionar tarefas


# Função para carregar tarefas do ficheiro
def carregar():
    global tarefas
    try:
        with open("memoria_tarefas.json", "r", encoding="utf-8") as file:
            tarefas = json.load(file)
    except FileNotFoundError:
        tarefas = []  # se não existir, começa com lista vazia

# Função para salvar tarefas no ficheiro que só acontecerá caso a pessoa coloque encerra programa!
def salvar():
    with open("memoria_tarefas.json", "w", encoding="utf-8") as file:
        json.dump(tarefas, file, ensure_ascii=False, indent=2)

def mostrar_menu(): #esta função permite que quando a chamar por ela mostre as opções:
    print("\n--- Sistema de Gestão de Tarefas ---")
    print("1. Adicionar nova tarefa")
    print("2. Listar/Ver tarefas")
    print("3. Concluir uma tarefa")
    print("4. Remover uma tarefa")
    print("5. Sair")

def adicionar_tarefa(): #com isto quanto a chamar irá perguntar o nome da tarefa e listar logo na na lista
    tarefa = input("Digite a nova tarefa: ")
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # aqui guardamos a hora/data atual formatada
    tarefas.append({
        "descricao": tarefa, 
        "concluida": False, 
        "criada_em": agora,   #  quando a tarefa foi criada
        "concluida_em": None # ficará None até ser concluída
    })
    print(" Tarefa adicionada com sucesso!")

def listar_tarefas(): 
    if not tarefas: #chamar este IF not primeiro irá verificar se tem algo na lista e se não vai parar.
        print("Nenhuma tarefa registrada.")
        return
    print("\n--- Lista de Tarefas ---")
    for i, t in enumerate(tarefas, start=1): # coloquei o enumerate para nao ter de fazer i=i+1 
        status = " Concluída" if t["concluida"] else " Pendente" #variavel status guarda o status 
        print(f"{i}. {t['descricao']} - {status}")
        print(f"   Criada em: {t['criada_em']}") # mostra quando foi criada
        if t["concluida_em"]: # se a tarefa já tiver sido concluída mostra também
            print(f"   Concluída em: {t['concluida_em']}")

def concluir_tarefa():# Ao ser chamado esta função vai executar logo a lista de tarefas
    listar_tarefas()
    if not tarefas: # para o caso da lista estar vazia
        return
    try: #aqui tenta EXECUTAR a conclusão e o try para evistar erro de digitação
        num = int(input("Número da tarefa a concluir: ")) # pede numero para variavel num
        tarefa_selecionada=tarefas[num - 1] # aqui guardamos a tarefa que prentende em um mariavel
        tarefa_selecionada["concluida"] = True # aqui vai à lista e coloca concluida com o true
        tarefa_selecionada["concluida_em"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S") #  quando foi concluída
        print("Tarefa concluída com sucesso!")
        # Pergunta se quer remover a tarefa concluída
        resposta = input(f"Quer remover esta tarefa da lista? (s/n):").strip().lower()
        if resposta == "s":
            tarefas.remove(tarefa_selecionada)
            print("Tarefa removida da lista.")

    except (ValueError, IndexError):
        print("O número é inválido.")

def remover_tarefa():# mesma logica que função concluir_tarefa só para remover com adição do pop que remove o num-1 ou seja
                     # se for o num=3 será na verdade o 2 da lista tarefas
    listar_tarefas()
    if not tarefas:
        return
    try:
        num = int(input("Digite o número da tarefa para remover: "))
        remover = tarefas.pop(num - 1)
        print(f" Tarefa '{remover['descricao']}' removida.")
    except (ValueError, IndexError):
        print(" Número inválido.")

carregar()
# Programa principal
while True: # aqui temos a logica de procedimentos com a seleção da opção em relação às funções criadas acima
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        concluir_tarefa()
    elif opcao == "4":
        remover_tarefa()
    elif opcao == "5":
        salvar() #salva no ficheiro antes de encerrar
        print(" Encerrar do programa...")
        break
    else:
        print(" Opção inválida. Tente novamente.")
