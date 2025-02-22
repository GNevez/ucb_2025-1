import psutil

def obter_memoria_processo(N):
    try:
            processo = psutil.Process(N)
            Memoria_Info = processo.memory_info()
            MF = Memoria_Info.rss / (1024 * 1024)
            MV = Memoria_Info.vms / (1024 * 1024)
            return MF, MV
    except psutil.NoSuchProcess:
            return None, None
     
# "main()"
    
def estado_processo(N):
    try: 
         processo = psutil.Process(N)
         estado = processo.status
         return estado  
    except psutil.NoSuchProcess: 
        return "Processo não encontrado"



pid = int(input("Digite o PID do processo: "))
estado = estado_processo(pid)
print(f"O estado do processo é: {estado}")