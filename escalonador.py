class Processo:    
    def __init__(self,pid,tempo,burst,prioridade):
        self.tempo = tempo
        self.pid = pid
        self.burst = burst
        self.espera = 0
        self.prioridade = prioridade
        self.andamento = 0

listaProcessos = []
processosCorrendo = []
processosConcluidos = []

arq = open("listaprocessos.txt","r")
for linha in arq.readlines():
    infos = linha.split()
    listaProcessos.append(Processo(int(infos[0]),int(infos[1]),int(infos[2]),int(infos[3])))
arq.close()

tempo = 0

executando = False

while len(listaProcessos)!=0 or len(processosCorrendo)!=0:
    if len(listaProcessos)>0:
        for processo in listaProcessos:
            if processo.tempo == tempo:
                processosCorrendo.append(processo)
                listaProcessos.remove(processo)
                print(f"Processo PID {processo.pid} adicionado na fila de execucao no tempo {tempo}")

    if len(processosCorrendo)>0:
        if executando == False: 
            for i in range(0,len(processosCorrendo)):
                if i==0:
                    processoatual = processosCorrendo[0]
                    executando = True
                if processosCorrendo[i].prioridade<processoatual.prioridade:
                    processoatual = processosCorrendo[i]
            print(f"Nenhum processo anterior em andamento, processo PID {processoatual.pid} foi definido como prioridade")
        for processo in processosCorrendo:
            if processo.prioridade<processoatual.prioridade:
                print(f"Processo de PID {processoatual.pid} foi substituido, burst = {processoatual.burst}, tempo restante = {processoatual.burst-processoatual.andamento}")
                processoatual = processo
                print(f"Processo de PID {processoatual.pid} iniciado pois possui maior prioridade, burst = {processoatual.burst}, prioridade = {processoatual.prioridade}")
                
        for processo in processosCorrendo:
            if processo.pid==processoatual.pid:
                processo.andamento+=1
                print(f"Processo com PID {processo.pid} executado no tempo {tempo}, tempo restante = {processo.burst-processo.andamento}")
                if processo.burst==processo.andamento:
                    print(f"Processo de PID {processo.pid} foi concluido no tempo {tempo}")
                    processosConcluidos.append(processo)
                    processosCorrendo.remove(processo)
                    executando=False
        for processo in processosCorrendo:
            if processo.pid!=processoatual.pid: processo.espera+=1
    else: print(f"Nenhum processo na fila de execucao no tempo {tempo}")
    tempo+=1

print(f"Execucao de todos os processos concluida no tempo {tempo}")

tempomedio = 0
for processo in processosConcluidos:
    tempomedio+=processo.espera
    print(f"PID: {processo.pid}   Tempo de espera = {processo.espera}")
print(f"Tempo medio de espera: {tempomedio/len(processosConcluidos)}")