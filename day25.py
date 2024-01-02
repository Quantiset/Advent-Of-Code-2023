import constants
import networkx

data = constants.day25
data_lines = data.split("\n")

def main():
    graph = networkx.Graph()

    for line in data_lines:
        o_node = line.split(": ")[0]
        connected_nodes = line.split(": ")[1].split(" ")
        for connected_node in connected_nodes:
            graph.add_edge(o_node, connected_node)

    for edge in (networkx.minimum_edge_cut(graph)):
        graph.remove_edge(edge[0], edge[1])
    
    ans = 1
    for connection in networkx.connected_components(graph):
        ans *= len(connection)
    print(ans)

main()