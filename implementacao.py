import time, csv, tracemalloc

def escada_recursiva(n: int) -> int:
    if(n == 0 or n == 1):
        return 1

    return escada_recursiva(n - 1) + escada_recursiva(n - 2)

def escada_dinamica(n: int) -> int:
    if(n == 0 or n == 1):
        return 1
    
    vetor = [0 for _ in range(n+1)]
    vetor[0] = vetor[1] = 1

    for i in range(2, n+1):
        vetor[i] = vetor[i-1] + vetor[i-2]

    return vetor[n]


def linha(char: str = "=", tam: int = 70):
    print(char * tam)

with open("tempos_escada2.csv", mode="w", newline="") as arquivoCSV:
    writer = csv.writer(arquivoCSV)
    writer.writerow(["degrau", "algoritmo", "iteracao", "tempo", "memoria_pico_b"])

    iteracoes = 30
    lista_degraus = [10, 40]

    for degrau in lista_degraus:
        linha()
        for funcao in [escada_dinamica, escada_recursiva]:
            print(f"POSSIBILIDADES PARA SUBIR {degrau} DEGRAUS POR [{(funcao.__name__).upper()}]")
            for it in range(iteracoes):
                tracemalloc.start()
                inicio = time.perf_counter()

                funcao(degrau)

                fim = time.perf_counter()
                memoria_atual_b, memoria_pico_b = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                tempo = fim - inicio

                print(f"[{it+1}ª Iteração] {tempo:.6f} segundos, com pico de {memoria_pico_b:.2f} bytes")
                writer.writerow([degrau, funcao.__name__, it+1, f"{tempo:.6f}", f"{memoria_pico_b:.2f}"])
            linha(char="-", tam=60)
            