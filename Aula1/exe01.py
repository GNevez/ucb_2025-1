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

pid = 0
Real, Virtual = obter_memoria_processo(0)

if Real is not None:

    print(f"PID: {pid}") 
    print(f"memoria real: {Real}")
    print(f"memoria virtual: {Virtual}")

else:
    print(f"o processo com PID {pid} nao existe")    