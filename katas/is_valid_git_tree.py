
def is_valid_git_tree(tree_map):
    """
    Determines if a given tree structure represents a valid Git tree.

    A valid Git tree should:
    1. Have exactly one root (no parent).
    2. Contain no cycles.

    Args:
        tree_map: a dictionary representing the Git tree (commit ID to list of child commit IDs)

    Returns:
        True if the tree is a valid Git tree, False otherwise
    """
    seen_nodes = set()
    number_of_roots = 0
    for node in tree_map.keys():
        for node_in in tree_map[node]:
            seen_nodes.add(node_in)
    for node in tree_map.keys():
        if node not in seen_nodes:
            number_of_roots += 1
    return number_of_roots == 1


def canFinish(numCourses, prerequisites):
    seen_courses = set()
    num_of_roots = 0
    for d in prerequisites:
        seen_courses.add(d[0])
    for d in prerequisites:
        if d[0] in seen_courses:
            num_of_roots+=1
    return num_of_roots == 1

if __name__ == '__main__':
    valid_tree = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": [],
        "D": []
    }
    invalid_tree = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"]  # cycle
    }
    tree_map = {
        "A": ["B"],
        "B": ["C"],
        "C": []
        # But you forgot to define C in keys => so it's not root
    }
    print(canFinish(2,[[1,0],[0,1]]))
    print(f"Is valid tree: {is_valid_git_tree(valid_tree)}")  # Should be True
    print(f"Is valid tree: {is_valid_git_tree(tree_map)}")  # Should be False