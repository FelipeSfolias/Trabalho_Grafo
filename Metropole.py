import networkx as nx
import matplotlib.pyplot as plt

# Definição d as cidades e conexões com distâncias reais aproximdas em km
cidadesMetropolitaneas = [
    "Curitiba", "São José dos Pinhais", "Araucária", "Colombo", "Pinhais",
    "Piraquara", "Almirante Tamandaré", "Campo Largo", "Fazenda Rio Grande", "Quatro Barras",
    "Campo Magro", "Balsa Nova", "Rio Branco do Sul", "Mandirituba", "Itaperuçu"
]
#Define percurso aproximado entre as cidadesMetropolitanas
caminhos = [
    ("Curitiba", "São José dos Pinhais", 15),
    ("Curitiba", "Araucária", 28),
    ("Curitiba", "Colombo", 15),
    ("Curitiba", "Pinhais", 10),
    ("Curitiba", "Piraquara", 22),
    ("Curitiba", "Almirante Tamandaré", 15),
    ("Curitiba", "Campo Largo", 29),
    ("Curitiba", "Fazenda Rio Grande", 27),
    ("Curitiba", "Quatro Barras", 25),
    ("Curitiba", "Campo Magro", 21),
    ("Curitiba", "Balsa Nova", 52),
    ("Curitiba", "Rio Branco do Sul", 32),
    ("Curitiba", "Mandirituba", 41),
    ("Curitiba", "Itaperuçu", 50),
    ("São José dos Pinhais", "Piraquara", 20),
    ("Araucária", "Campo Largo", 30),
    ("Colombo", "Quatro Barras", 20),
    ("Pinhais", "Piraquara", 10),
    ("Almirante Tamandaré", "Campo Magro", 17),
    ("Fazenda Rio Grande", "Mandirituba", 19),
    ("Rio Branco do Sul", "Itaperuçu", 15)
]

# Criando o grafo
G = nx.Graph()
for cidade in cidadesMetropolitaneas: # for para realizar a distribuição de cada item dentro da lista cidadesMetropolitanas
    G.add_node(cidade)
for cidade1, cidade2, distancia in caminhos:
    G.add_edge(cidade1, cidade2, weight=distancia)

# Representação do grafo
print("Lista de Adjacência:")
for node in G.adjacency():
    print(node)

print("\nMatriz de Adjacência:")
print(nx.to_numpy_array(G))

# Visualização do grafo
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=35)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12)
edge_labels = {(u, v): f"{d['weight']} km" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Rede de Transporte na Região Metropolitana de Curitiba")
plt.show()


# Algoritmos de Busca
def bfs(grafo, inicio):
    visitados = set()
    fila = [inicio]

    while fila:
        vertice = fila.pop(0)
        if vertice not in visitados:
            print(vertice, end=" -> ")
            visitados.add(vertice)
            fila.extend(set(grafo[vertice]) - visitados)


def dfs(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)
    print(inicio, end=" -> ")
    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados)

def dijkstra(grafo, inicio):
    return nx.single_source_dijkstra_path_length(grafo, inicio)

def floyd_warshall(grafo):
    return dict(nx.floyd_warshall(grafo))

print("\nBFS a partir de Curitiba:")
bfs(G, "Curitiba")
print("Fim")

print("\nDFS a partir de Curitiba:")
dfs(G, "Curitiba")
print("Fim")

print("\nMenores distâncias a partir de Curitiba usando Dijkstra:")
print(dijkstra(G, "Curitiba"))

print("\nTodas as menores distâncias entre pares de cidades usando Floyd-Warshall:")
fw_result = floyd_warshall(G)
for origem, destinos in fw_result.items():
    print(f"{origem}: {destinos}")
