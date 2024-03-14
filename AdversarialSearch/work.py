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
            print(f'At Depth: {depth}\nAlpha at {eval}: {alpha}\nBeta at {eval}: {beta}\n')
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
            print(f'At Depth: {depth}\nAlpha at {eval}: {alpha}\nBeta at {eval}: {beta}\n')
            if alpha >= beta:
                break
        return min_eval


# Create a tree
root = Node(-math.inf)
""
root.children = [Node(math.inf), Node(math.inf)]
""
root.children[0].children = [Node(math.inf), Node(math.inf), Node(math.inf)]
root.children[1].children = [Node(math.inf), Node(math.inf), Node(math.inf)]
""
root.children[0].children[0].children = [Node(-math.inf), Node(-math.inf)]
root.children[0].children[1].children = [Node(-math.inf)]
root.children[0].children[2].children = [Node(-math.inf), Node(-math.inf), Node(-math.inf)]
root.children[1].children[0].children = [Node(-math.inf)]
root.children[1].children[1].children = [Node(-math.inf), Node(-math.inf)]
root.children[1].children[2].children = [Node(-math.inf), Node(-math.inf), Node(-math.inf)]
""
# Left side of tree
root.children[0].children[0].children[0].children = [Node(4), Node(3), Node(8)]
root.children[0].children[0].children[1].children = [Node(2), Node(1)]
root.children[0].children[1].children[0].children = [Node(4), Node(2), Node(3)]
root.children[0].children[2].children[0].children = [Node(6), Node(4)]
root.children[0].children[2].children[1].children = [Node(7)]
root.children[0].children[2].children[2].children = [Node(5), Node(2)]

# Right side of tree
root.children[1].children[0].children[0].children = [Node(1), Node(9), Node(0)]
root.children[1].children[1].children[0].children = [Node(4), Node(3)]
root.children[1].children[1].children[1].children = [Node(0)]
root.children[1].children[2].children[0].children = [Node(2), Node(8), Node(4)]
root.children[1].children[2].children[1].children = [Node(3), Node(7)]
root.children[1].children[2].children[2].children = [Node(5), Node(4), Node(1)]

# Call minimax
score = minimax(root, 4, True)
print("Minimax Score:", score)

# Call alpha-beta pruning
score = alpha_beta(root, 4, -math.inf, math.inf, True)
print("Alpha-Beta Score:", score)
