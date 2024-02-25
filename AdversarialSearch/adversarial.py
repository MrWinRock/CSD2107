import math

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def minimax(node, depth, maximizing_player):
    if depth == 0 or len(node.children) == 0:
        return node.value, None

    if maximizing_player:
        max_eval = -math.inf
        best_move = None
        for child in node.children:
            eval, _ = minimax(child, depth - 1, False)
            if eval > max_eval:
                max_eval = eval
                best_move = child
        return max_eval, best_move
    else:
        min_eval = math.inf
        best_move = None
        for child in node.children:
            eval, _ = minimax(child, depth - 1, True)
            if eval < min_eval:
                min_eval = eval
                best_move = child
        return min_eval, best_move

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or len(node.children) == 0:
        return node.value, None

    if maximizing_player:
        max_eval = -math.inf
        best_move = None
        for child in node.children:
            eval, _ = alpha_beta(child, depth - 1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best_move = child
            alpha = max(alpha, eval)
            if alpha >= beta:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        best_move = None
        for child in node.children:
            eval, _ = alpha_beta(child, depth - 1, alpha, beta, True)
            if eval < min_eval:
                min_eval = eval
                best_move = child
            beta = min(beta, eval)
            if alpha >= beta:
                break
        return min_eval, best_move

# Example usage:
# Create a tree
root = Node(float('inf'))
root.children = [Node(float('-inf')), Node(float('-inf'))]
root.children[0].children = [Node(7), Node(8)]
root.children[1].children = [Node(-4), Node(5)]

# Call minimax
score, best_move = minimax(root, 3, True)
print("Minimax Score:", score)

# Call alpha-beta pruning
score, best_move = alpha_beta(root, 3, -math.inf, math.inf, True)
print("Alpha-Beta Score:", score)
