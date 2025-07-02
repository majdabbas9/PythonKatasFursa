class IP:
    """
    Represents an IPv4 address.

    You MUST implement your own IP validation logic.
    Do NOT use built-in libraries like `ipaddress` or regex modules.
    """

    def __init__(self, address: str):
        """
        Initializes an IP address.

        Args:
            address: The IP address as a string.

        Raises:
            ValueError: If the address is invalid.
        """
        if not self._is_valid_ip(address):
            raise ValueError(f"Invalid IP address: {address}")
        self.address = address

    def _is_valid_ip(self, address: str) -> bool:
        """
        Validates an IPv4 address.

        Args:
            address: The address string to validate.

        Returns:
            True if valid, False otherwise.
        """
        address_parts = address.split('.')
        if len(address_parts) != 4:
            return False
        for part in address_parts:
            if not part.isdigit() or not (0 <= int(part) <= 255):
                return False
        return True

    def __str__(self):
        return self.address

    def __eq__(self, other):
        return isinstance(other, IP) and self.address == other.address

    def __hash__(self):
        raise NotImplementedError("hashCode logic not implemented.")


class RoundRobinLoadBalancer:
    """
    Implements a round-robin load balancer.

    A load balancer distributes requests to a pool of server instances.
    This implementation routes requests in a circular (round-robin) manner.
    """

    def __init__(self):
        """
        Initializes the load balancer with an empty pool of servers.
        """
        self.servers = []
        self.current_index = 0

    def add_server(self, server: IP):
        """
        Adds a server instance to the load balancer.

        Args:
            server: An IP instance representing the server to add.
        """
        if not isinstance(server, IP):
            raise TypeError("server must be an instance of IP")
        self.servers.append(server)

    def remove_server(self, server: IP):
        """
        Removes a server instance from the load balancer.

        Args:
            server: An IP instance representing the server to remove.
        """
        if not isinstance(server, IP):
            raise TypeError("server must be an instance of IP")
        try:
            if self.current_index == len(self.servers) - 1:
                self.current_index = 0
            self.servers.remove(server)
        except ValueError:
            raise ValueError(f"Server {server} not found in the load balancer.")

    def route_request(self) -> IP | None:
        """
        Routes a request to the next server in round-robin order.

        Returns:
            The IP instance of the server handling the request, or None if no servers are available.
        """
        if len(self.servers) == 0:
            return None
        IP = self.servers[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.servers)
        return IP


if __name__ == '__main__':
    lb = RoundRobinLoadBalancer()

    lb.add_server(IP("192.168.0.1"))
    lb.add_server(IP("192.168.0.2"))
    lb.add_server(IP("192.168.0.3"))

    print("Routing to:", lb.route_request())
    print("Routing to:", lb.route_request())
    print("Routing to:", lb.route_request())
    print("Routing to:", lb.route_request())

    lb.remove_server(IP("192.168.0.2"))

    print("Routing to:", lb.route_request())
    print("Routing to:", lb.route_request())
