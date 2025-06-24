class OrderedMap:
    """
    Implement an OrderedMap data structure that behaves like a regular dictionary
    but maintains the order of keys based on their insertion order.

    IMPORTANT:
    You MUST NOT use built-in types or libraries that maintain order automatically,
    such as:
      - dict (in Python 3.7+)
      - collections.OrderedDict
      - any other similar built-in or library.

    Instead, build your own logic to track and maintain insertion order.
    """

    def __init__(self):
        """
        Initialize the internal data structures needed to track keys and values
        while preserving insertion order.
        """
        pass

    def put(self, key, value):
        """
        Add a key-value pair to the map.
        If the key already exists, update its value while preserving the order.

        Args:
            key: The key to insert.
            value: The value to associate with the key.
        """
        raise NotImplementedError("Not implemented yet.")

    def get(self, key):
        """
        Retrieve the value associated with a given key.

        Args:
            key: The key to look up.

        Returns:
            The value associated with the key, or None if the key does not exist.
        """
        raise NotImplementedError("Not implemented yet.")

    def remove(self, key):
        """
        Remove a key-value pair from the map.

        Args:
            key: The key to remove.
        """
        raise NotImplementedError("Not implemented yet.")

    def keys(self):
        """
        Return all keys in the order they were added.

        Returns:
            A list of keys in insertion order.
        """
        raise NotImplementedError("Not implemented yet.")

    def size(self):
        """
        Return the number of key-value pairs in the map.

        Returns:
            int: The number of elements in the map.
        """
        raise NotImplementedError("Not implemented yet.")

    def clear(self):
        """
        Remove all key-value pairs from the map.
        """
        raise NotImplementedError("Not implemented yet.")


if __name__ == '__main__':
    ordered_map = OrderedMap()

    ordered_map.put("One", 1)
    ordered_map.put("Two", 2)
    ordered_map.put("Three", 3)

    print("Keys in order:", ordered_map.keys())  # ["One", "Two", "Three"]
    print("Value of 'Two':", ordered_map.get("Two"))  # 2

    ordered_map.remove("Two")
    print("Keys after removal:", ordered_map.keys())  # ["One", "Three"]

    ordered_map.put("Two", 22)
    print("Keys after re-adding 'Two':", ordered_map.keys())  # ["One", "Three", "Two"]

    print("Map size:", ordered_map.size())  # 3

    ordered_map.clear()
    print("Map size after clearing:", ordered_map.size())  # 0
