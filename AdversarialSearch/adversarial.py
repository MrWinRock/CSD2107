import math


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def minimax(node, depth, maximizing_player):
    if depth == 0 or len(node.children) == 0:
        return node.value

    if maximizing_player:
        max_eval = -math.inf
        for child in node.children:
            eval = minimax(child, depth - 1, False)
            if eval > max_eval:
                max_eval = eval
        return max_eval
    else:
        min_eval = math.inf
        for child in node.children:
            eval = minimax(child, depth - 1, True)
            if eval < min_eval:
                min_eval = eval
        return min_eval


def alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or len(node.children) == 0:
        return node.value

    if maximizing_player:
        max_eval = -math.inf
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
            alpha = max(alpha, eval)
            if alpha >= beta:
                break
        return max_eval
    else:
        min_eval = math.inf
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            if eval < min_eval:
                min_eval = eval
            beta = min(beta, eval)
            if alpha >= beta:
                break
        return min_eval


# Create a tree
root = Node(-math.inf)
""
root.children = [Node(math.inf), Node(math.inf)]
""
root.children[0].children = [Node(math.inf), Node(math.inf)]
root.children[1].children = [Node(math.inf), Node(math.inf)]
""
root.children[0].children[0].children = [Node(-1), Node(3)]
root.children[0].children[1].children = [Node(5), Node(1)]
root.children[1].children[0].children = [Node(-6), Node(-4)]
root.children[1].children[1].children = [Node(0), Node(9)]


# Call minimax
# score = minimax(root, 3, True)
# print("Minimax Score:", score)

# Call alpha-beta pruning
score = alpha_beta(root, 3, -math.inf, math.inf, True)
print("Alpha-Beta Score:", score)
