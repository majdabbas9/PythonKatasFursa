def is_valid_parentheses(s):
    """
    Checks if a given string has valid parentheses (try in O(n)).

    A string has valid parentheses if:
    1. Every opening parenthesis has a matching closing parenthesis.
    2. The parentheses are correctly nested.

    Args:
        s: the input string containing parentheses

    Returns:
        True if the string has valid parentheses, False otherwise
    """
    # Hint for efficient implementation: stack
    stack = []
    map_to_number = {"(":1,")":1,"[":2,"]":2,"{":3,"}":3}
    for i in range(len(s)):
        if s[i] in ["(","[","{"]:
            stack.append(s[i])
        elif s[i] in [")","]","}"] :
            n1 = map_to_number[s[i]]
            n2 = map_to_number[stack[-1]]
            if n1 != n2 :
                return False
            stack.pop()
    return len(stack)==0


if __name__ == '__main__':
    valid_input = "()[]{}"
    invalid_input1 = "(]"
    invalid_input2 = "([)]"
    valid_input_nested = "{[]()}"

    print(f"'{valid_input}' has valid parentheses: {is_valid_parentheses(valid_input)}")  # Should be True
    print(f"'{invalid_input1}' has valid parentheses: {is_valid_parentheses(invalid_input1)}")  # Should be False
    print(f"'{invalid_input2}' has valid parentheses: {is_valid_parentheses(invalid_input2)}")  # Should be False
    print(f"'{valid_input_nested}' has valid parentheses: {is_valid_parentheses(valid_input_nested)}")  # Should be True