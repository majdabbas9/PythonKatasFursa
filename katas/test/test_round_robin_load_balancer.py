import unittest
from katas.round_robin_load_balancer import RoundRobinLoadBalancer
from katas.round_robin_load_balancer import IP
class TestRoundRobinLoadBalancer(unittest.TestCase):

    def setUp(self):
        self.lb = RoundRobinLoadBalancer()
        self.server1 = IP("10.0.0.1")
        self.server2 = IP("10.0.0.2")
        self.server3 = IP("10.0.0.3")

    def test_1_add_and_route_single_server(self):
        self.lb.add_server(self.server1)
        for _ in range(3):
            self.assertEqual(self.lb.route_request(), self.server1)

    def test_2_round_robin_routing(self):
        self.lb.add_server(self.server1)
        self.lb.add_server(self.server2)
        self.lb.add_server(self.server3)

        expected = [self.server1, self.server2, self.server3,
                    self.server1, self.server2, self.server3]
        actual = [self.lb.route_request() for _ in range(6)]
        self.assertEqual(actual, expected)

    def test_3_remove_server(self):
        self.lb.add_server(self.server1)
        self.lb.add_server(self.server2)
        self.lb.remove_server(self.server1)

        self.assertEqual(self.lb.route_request(), self.server2)
        self.assertEqual(self.lb.route_request(), self.server2)

    def test_4_remove_server_not_found(self):
        self.lb.add_server(self.server1)
        with self.assertRaises(ValueError):
            self.lb.remove_server(self.server2)

    def test_5_empty_load_balancer(self):
        self.assertIsNone(self.lb.route_request())

    def test_6_add_server_type_check(self):
        with self.assertRaises(TypeError):
            self.lb.add_server("192.168.0.1")  # Not an IP object

    def test_7_remove_server_type_check(self):
        with self.assertRaises(TypeError):
            self.lb.remove_server("10.0.0.1")  # Not an IP object

    def test_8_duplicate_servers(self):
        self.lb.add_server(self.server1)
        self.lb.add_server(self.server1)
        result = [self.lb.route_request(), self.lb.route_request(), self.lb.route_request()]
        self.assertEqual(result, [self.server1, self.server1, self.server1])

    def test_9_index_wraps_after_removal(self):
        self.lb.add_server(self.server1)
        self.lb.add_server(self.server2)
        self.lb.add_server(self.server3)

        self.lb.route_request()  # server1
        self.lb.route_request()  # server2
        self.lb.remove_server(self.server3)  # next index was server3

        # Should now wrap back to server1
        self.assertEqual(self.lb.route_request(), self.server1)
        self.assertEqual(self.lb.route_request(), self.server2)

    def test_10_add_and_remove_multiple(self):
        self.lb.add_server(self.server1)
        self.lb.add_server(self.server2)
        self.lb.add_server(self.server3)

        self.lb.remove_server(self.server2)
        self.lb.remove_server(self.server1)

        self.assertEqual(self.lb.route_request(), self.server3)
        self.lb.remove_server(self.server3)
        self.assertIsNone(self.lb.route_request())

if __name__ == '__main__':
    unittest.main()