from typing import List,Set

def select_minimal_test_cases(test_cases: List[List[int]]) -> List[int]:
    """
    In software testing, it's often required to select a minimal set of test cases that cover all the requirements.
    You are given a set of test cases and their associated covered requirements.
    Your task is to select the minimal subset of test cases such that all requirements are covered.

    For example, you have the following test cases and requirements they cover:

    test_cases = [
        [1, 2, 3],   # Test case 0 covers requirements 1, 2, 3
        [1, 4],      # Test case 1 covers requirements 1, 4
        [2, 3, 4],   # Test case 2 covers requirements 2, 3, 4
        [1, 5],      # Test case 3 covers requirements 1, 5
        [3, 5]       # Test case 4 covers requirements 3, 5
    ]

    Args:
        test_cases: a list of test cases, where each test case is a list of requirements it covers.
                    Assume each requirement is covered by at least one test case.

    Returns:
        A list of indices of the minimal subset of test cases that covers all requirements
    """
    all_requirements = set(req for case in test_cases for req in case)
    num_requirements = max(all_requirements)
    requirements_covered = [0] * num_requirements
    min_covered = float('inf')
    current_covered_indices: Set[int] = set()
    best_indices: List[int] = []

    def backtrack(start: int, requirements_covered_in: List[int], num_selected: int):
        nonlocal min_covered, best_indices, current_covered_indices

        if all(x > 0 for x in requirements_covered_in):
            if num_selected < min_covered:
                min_covered = num_selected
                best_indices = list(current_covered_indices)
            return

        for i in range(start, len(test_cases)):
            added = []
            for req in test_cases[i]:
                if requirements_covered_in[req - 1] == 0:
                    added.append(req)
                requirements_covered_in[req - 1] += 1

            current_covered_indices.add(i)
            backtrack(i + 1, requirements_covered_in, num_selected + 1)
            current_covered_indices.remove(i)

            for req in test_cases[i]:
                requirements_covered_in[req - 1] -= 1

    backtrack(0, requirements_covered, 0)
    return sorted(best_indices)


def main():
    test_cases = [
        [1, 2, 3],
        [1, 4],
        [2, 3, 4],
        [1, 5],
        [3, 5]
    ]
    arr = [1,2,3,4,5]

    result = select_minimal_test_cases(test_cases)
    print(result)  # Expected output: [2, 3]
if __name__ == "__main__":
    main()
