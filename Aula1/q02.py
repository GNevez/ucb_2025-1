import psutil

    
usoCPU = 0
processo = -1

for X in psutil.process_iter(['pid', 'name']):
    try:
        if X.cpu_percent() >= usoCPU:
            usoCPU = X.cpu_percent()
            processo = X.info['pid']
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess): 
        pass
    
print(f"O processo {processo} está gastando {usoCPU}")


