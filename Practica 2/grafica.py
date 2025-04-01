from graphviz import Digraph

input_size = 10 # Número de características de entrada que va a usar el modelo.
hidden_size = 32 # Número de neuronas de la capa oculta
output_size = 1 # Número de nueronas de salida. Ponemos 1 porque va a ser una clasificación binaria (vivo/muerto)

def dibujar_red():
    dot = Digraph(format="png")
    dot.attr(rankdir='LR', nodesep='1', ranksep='10')  # QUÍNTUPLE SEPARACIÓN ENTRE CAPAS

    # Crear nodos de entrada
    input_nodes = [f"X{i+1}" for i in range(input_size)]  # 10 entradas
    for node in input_nodes:
        dot.node(node, shape="circle", style="filled", fillcolor="lightblue", width="0.8", height="0.8")

    # Crear nodos de la primera capa oculta
    hidden1_nodes = [f"H1_{i+1}" for i in range(hidden_size)]  # 1ª capa oculta
    for node in hidden1_nodes:
        dot.node(node, shape="circle", style="filled", fillcolor="lightgreen", width="0.8", height="0.8")

    # Crear nodos de la segunda capa oculta
    hidden2_nodes = [f"H2_{i+1}" for i in range(hidden_size*2)]  # 2ª capa oculta
    for node in hidden2_nodes:
        dot.node(node, shape="circle", style="filled", fillcolor="yellow", width="0.8", height="0.8")

    # Crear nodos de la tercera capa oculta
    hidden3_nodes = [f"H3_{i+1}" for i in range(hidden_size)]  # 3ª capa oculta
    for node in hidden3_nodes:
        dot.node(node, shape="circle", style="filled", fillcolor="lightcoral", width="0.8", height="0.8")

    # Crear nodo de salida
    output_node = "Salida"
    dot.node(output_node, shape="circle", style="filled", fillcolor="red", width="1", height="1")

    # Conectar capa de entrada a la primera capa oculta
    for i in input_nodes:
        for h in hidden1_nodes:
            dot.edge(i, h)

    # Conectar primera capa oculta a la segunda capa oculta
    for h1 in hidden1_nodes:
        for h2 in hidden2_nodes:
            dot.edge(h1, h2)

    # Conectar segunda capa oculta a la tercera capa oculta
    for h2 in hidden2_nodes:
        for h3 in hidden3_nodes:
            dot.edge(h2, h3)

    # Conectar tercera capa oculta a la capa de salida
    for h3 in hidden3_nodes:
        dot.edge(h3, output_node)

    return dot

# Generar y mostrar el gráfico
red = dibujar_red()
red.render('red_neuronal', view=True)  # Guarda y abre el archivo generado
