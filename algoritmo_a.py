import heapq

def ler_matriz(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    tamanho = tuple(map(int, linhas[0].split()))
    inicio = tuple(map(int, linhas[1].split()))
    matriz = [list(map(int, linha.split())) for linha in linhas[2:]]

    return tamanho, inicio, matriz

def movimento_valido(x, y):
    return 0 <= x < tamanho[0] and 0 <= y < tamanho[1] and matriz[x][y] != -1 if matriz and 0 <= y < len(matriz[0]) else False

def a_estrela(tamanho, inicio, matriz):
    direcoes = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def heuristica(atual, objetivo):
        return abs(atual[0] - objetivo[0]) + abs(atual[1] - objetivo[1])

    fila_prioridade = [(heuristica(inicio, inicio), 0, inicio)]
    visitados = set()

    while fila_prioridade:
        _, custo, atual = heapq.heappop(fila_prioridade)

        if atual in visitados:
            continue

        visitados.add(atual)

        if atual == tamanho:
            return custo

        for dx, dy in direcoes:
            nx, ny = atual[0] + dx, atual[1] + dy

            if movimento_valido(nx, ny):
                novo_custo = custo + 1
                prioridade = novo_custo + heuristica((nx, ny), tamanho)
                heapq.heappush(fila_prioridade, (prioridade, novo_custo, (nx, ny)))

    return float('inf')

if __name__ == "__main__":
    caminho_arquivo = "C:/Users/david/OneDrive/Área de Trabalho/arquivo_mapa.txt"
    tamanho, inicio, matriz = ler_matriz(caminho_arquivo)

    print(f"Tamanho da matriz: {tamanho}")
    print(f"Ponto de início: {inicio}")

    for linha in matriz:
        print(linha)

    objetivo = tuple(map(int, input("Digite o ponto de destino (x y): ").split()))

    if 0 <= objetivo[0] < tamanho[0] and 0 <= objetivo[1] < tamanho[1]:
        if matriz[objetivo[0]][objetivo[1]] == -1:
            print("O ponto de destino é um obstáculo.")
        else:
            resultado = a_estrela(tamanho, inicio, matriz)
            if resultado == float('inf'):
                print("Caminho não encontrado.")
            else:
                print(f"Custo mínimo para alcançar o destino: {resultado}")
    else:
        print("O ponto de destino está fora dos limites.")