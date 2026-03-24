import threading

def tarefa():
    print("Executando tarefa...")

t = threading.Thread(target=tarefa) #starta a thread
t.start()
t.join()#espera ela terminar

print("Finalizado")