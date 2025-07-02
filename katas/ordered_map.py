class OrderedMap:
    def __init__(self):
        self._keys = []
        self._values = []

    def put(self, key, value):
        if key in self._keys:
            index = self._keys.index(key)
            self._values[index] = value
        else:
            self._keys.append(key)
            self._values.append(value)

    def get(self, key):
        if key in self._keys:
            index = self._keys.index(key)
            return self._values[index]
        return None

    def remove(self, key):
        if key in self._keys:
            index = self._keys.index(key)
            del self._keys[index]
            del self._values[index]

    def keys(self):
        return self._keys[:]

    def size(self):
        return len(self._keys)

    def clear(self):
        self._keys = []
        self._values = []


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
