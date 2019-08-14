from random import randint


def quicksort(n):
    if n == 0:
        return jogadores[n]
    for i, j in range(int(n/2)):

    return


jogadores = []
Q = int(input("Quantidade de jogadores: "))

for i in range(0, Q):
    jogadores.append(randint(1, 6))

for j in jogadores:
    print(f"O Jogador{j+1} tirou {j}")

print(quicksort(Q-1))
