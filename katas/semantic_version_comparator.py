def compare_versions(version1, version2):
    """
    Compares two semantic version strings to determine their relative order.

    Semantic versioning follows the format "MAJOR.MINOR.PATCH" where:
    - MAJOR version increments for incompatible API changes
    - MINOR version increments for backward-compatible functionality
    - PATCH version increments for backward-compatible bug fixes

    Each component must be compared numerically, not lexicographically.

    Args:
        version1: the first version string (e.g., "MAJOR.MINOR.PATCH")
        version2: the second version string (e.g., "MAJOR.MINOR.PATCH")

    Returns:
        -1 if version1 < version2
         0 if version1 = version2
         1 if version1 > version2
    """
    numbers_v1 = version1.split('.')
    numbers_v2 = version2.split('.')
    min_len = min(len(numbers_v1),len(numbers_v2))
    for i in range(min_len):
        if int(numbers_v1[i]) > int(numbers_v2[i]):
            return 1
        if int(numbers_v1[i]) < int(numbers_v2[i]):
            return -1
    if i + 1 == len(numbers_v1) == len(numbers_v2):
        return 0
    if len(numbers_v1) > len(numbers_v2):
        for j in range(i+1,len(numbers_v1)):
            if int(numbers_v1[j])!=0:
                return 1
    else :
        for j in range(i+1,len(numbers_v2)):
            if int(numbers_v2[j])!=0:
                return -1
    return 0


if __name__ == '__main__':
    print(f"'1.0.0' compared to '1.0.0': {compare_versions('1.0', '1')}")  # Expected: -1
    # print(f"'2.1.0' compared to '1.9.9': {compare_versions('2.1.0', '1.9.9')}")  # Expected: 1
    # print(f"'1.2.3' compared to '1.2.3': {compare_versions('1.2.3', '1.2.3')}")  # Expected: 0
    #
    # # Additional test cases
    # print(f"'1.2' compared to '1.2.0': {compare_versions('1.2', '1.2.0')}")  # Expected: 0
    # print(f"'1.10.0' compared to '1.2.0': {compare_versions('1.10.0', '1.2.0')}")  # Expected: 1
    # print(f"'2.0.0' compared to '10.0.0': {compare_versions('2.0.0', '10.0.0')}")  # Expected: -1