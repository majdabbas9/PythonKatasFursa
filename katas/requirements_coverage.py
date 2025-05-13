from typing import List


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
    all_requirements = set()
    for test_case in test_cases:
        all_requirements.update(test_case)

    num_test_cases = len(test_cases)
    best_solution = list(range(num_test_cases))

    for size in range(1, num_test_cases + 1):
        if len(best_solution) < size:
            break
        current_combination = [0] * size

        def generate_combinations(pos, start_idx):
            nonlocal best_solution
            if pos == size:
                covered = set()
                for idx in current_combination:
                    covered.update(test_cases[idx])
                if covered == all_requirements and len(current_combination) < len(best_solution):
                    best_solution = current_combination.copy()
                return
            for i in range(start_idx, num_test_cases):
                current_combination[pos] = i
                generate_combinations(pos + 1, i + 1)
        generate_combinations(0, 0)
        
    return best_solution


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],
        [1, 4],
        [2, 3, 4],
        [1, 5],
        [3, 5]
    ]

    result = select_minimal_test_cases(test_cases)
    print(result)  # Expected output: [2, 3]
