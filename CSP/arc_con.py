def revise(Xi, Xj, constraint, initial_domain):
    """
    Filters Xi's domain based on the constraint with Xj.

    Args:
        Xi: The first variable in the constraint.
        Xj: The second variable in the constraint.
        constraint: A function that takes two values (one from Xi and one from Xj)
                    and returns True if they satisfy the constraint, False otherwise.
        initial_domain: A dictionary containing the initial domain for each variable.

    Returns:
        A revised domain for Xi if it differs from the initial domain, None otherwise.
    """
    revised_domain = []
    for val in initial_domain[Xi]:
        if any(constraint(val, xj) for xj in initial_domain[Xj]):
            revised_domain.append(val)
    return revised_domain if revised_domain != initial_domain[Xi] else None


def AC3(constraints, initial_domain):
    """
    Applies the AC3 algorithm for arc consistency in constraint satisfaction problems.

    Args:
        constraints: A list of tuples representing constraints between variables.
        initial_domain: A dictionary containing the initial domain for each variable.

    Returns:
        A dictionary representing the revised domain for each variable after applying arc consistency.
    """
    queue = constraints.copy()
    while queue:
        (Xi, Xj) = queue.pop(0)
        revised_domain = revise(Xi, Xj, lambda x, y: True, initial_domain)
        if revised_domain:
            initial_domain[Xi] = revised_domain
            for (Xk, Xl) in constraints:
                if Xk == Xi and Xl != Xj:
                    queue.append((Xl, Xi))
    return initial_domain


# Define constraints
constraints = [('Teacher A', 'Class3'), ('Teacher A', 'Class4'),
               ('Teacher B', 'Class2'), ('Teacher B',
                                         'Class3'), ('Teacher B', 'Class4'), ('Teacher B', 'Class5'),
               ('Teacher C', 'Class1'), ('Teacher C',
                                         'Class2'), ('Teacher C', 'Class3'),
               ('Teacher C', 'Class4'), ('Teacher C', 'Class5')]

# Define the initial domain
initial_domain = {
    'Class1': ['C'],
    'Class2': ['B', 'C'],
    'Class3': ['A', 'B', 'C'],
    'Class4': ['A', 'B', 'C'],
    'Class5': ['B', 'C'],
    'Teacher A': ['A'],
    'Teacher B': ['B'],
    'Teacher C': ['C']
}

# Apply arc-consistency to the initial domain
revised_domains = AC3(constraints, initial_domain.copy())
print(revised_domains)
