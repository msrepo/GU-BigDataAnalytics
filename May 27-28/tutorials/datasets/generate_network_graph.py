import networkx as nx
import matplotlib.pyplot as plt

# Function to load the adjacency list from the file
def load_adjacency_list(file_path):
    adjacency_list = {}
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split("\t")
            if len(parts) == 2:
                user = int(parts[0])
                friends = list(map(int, parts[1].split(",")))
                adjacency_list[user] = friends
            elif len(parts) == 1:  # Handle users with no friends
                user = int(parts[0])
                adjacency_list[user] = []
    return adjacency_list

# Function to create a graph from the adjacency list
def create_graph(adjacency_list):
    graph = nx.Graph()
    for user, friends in adjacency_list.items():
        for friend in friends:
            graph.add_edge(user, friend)  # Add an edge between the user and their friend
    return graph

# Function to visualize the graph
def visualize_graph(graph, sample_size=50):
    # Take a subgraph of the first `sample_size` nodes for visualization
    subgraph = graph.subgraph(list(graph.nodes)[:sample_size])
    
    # Draw the graph
    plt.figure(figsize=(12, 12))
    nx.draw(subgraph, with_labels=True, node_color="skyblue", node_size=500, edge_color="gray", font_size=10)
    plt.title("Friend Network (Sample)")
    plt.show()

# Main function
def main():
    file_path = "soc-LiveJournal1Adj.txt"  # Path to the adjacency list file

    # Load the adjacency list
    adjacency_list = load_adjacency_list(file_path)

    # Create the graph
    graph = create_graph(adjacency_list)

    # Visualize the graph
    visualize_graph(graph, sample_size=300)  # Visualize a sample of 50 nodes

if __name__ == "__main__":
    main()