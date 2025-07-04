class CircularBuffer:
    """
    Design a circular buffer (ring buffer).

    The buffer should operate in constant time.
    When the buffer is full, adding a new element should overwrite the oldest element.
    """

    def __init__(self, capacity):
        self.arr = [0] * capacity
        self.capacity = capacity
        self.current_added_elements = 0
        pass

    def add(self, val):
        """
        Adds an element to the buffer.

        Args:
            val: the value to add
        """
        self.arr[self.current_added_elements%self.capacity] = val
        self.current_added_elements += 1


    def get(self):
        """
        Retrieves the oldest element from the buffer.

        Returns:
            the oldest element, or -1 if the buffer is empty
        """
        if not self.is_empty():
            return self.arr[self.current_added_elements%self.capacity]
        return -1

    def is_full(self):
        """
        Checks if the buffer is full.

        Returns:
            True if the buffer is full, False otherwise
        """
        return self.current_added_elements >= self.capacity

    def is_empty(self):
        """
        Checks if the buffer is empty.

        Returns:
            True if the buffer is empty, False otherwise
        """
        return self.current_added_elements==0


if __name__ == '__main__':
    buffer = CircularBuffer(3)
    buffer.add(1)
    buffer.add(2)
    buffer.add(3)
    print(buffer.get())  # 1
    buffer.add(4)
    print(buffer.get())  # 2
    buffer.add(5)
    print(buffer.is_full())  # True
