import networkx as nx
import matplotlib.pyplot as plt

# Arc-consistency algorithm


def arc_consistency(variables, domain, constraints):
    queue = list(constraints)

    while queue:
        (teacher, class_) = queue.pop(0)
        revised = False

        for value in domain[class_][:]:
            if all((teacher, value) not in constraint for constraint in constraints if constraint != (teacher, class_)):
                domain[class_].remove(value)
                revised = True

        if revised:
            for related_class in variables:
                if (related_class, class_) in constraints:
                    queue.append((related_class, class_))

    return domain


# Create a directed graph
G = nx.DiGraph()

# Define nodes
nodes = ['Class1', 'Class2', 'Class3', 'Class4',
         'Class5', 'Teacher A', 'Teacher B', 'Teacher C']

# Define edges
edges = [('Teacher A', 'Class3'), ('Teacher A', 'Class4'),
         ('Teacher B', 'Class2'), ('Teacher B',
                                   'Class3'), ('Teacher B', 'Class4'), ('Teacher B', 'Class5'),
         ('Teacher C', 'Class1'), ('Teacher C', 'Class2'), ('Teacher C', 'Class3'),
         ('Teacher C', 'Class4'), ('Teacher C', 'Class5')]

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Arc consistency computation
domain = {node: ['A', 'B', 'C'] for node in nodes}
domain = arc_consistency(nodes, domain, edges)
print(domain)

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes

nx.draw(G, pos, with_labels=True, node_size=5000,
        node_color='skyblue', font_size=10, font_weight='bold')

plt.show()
