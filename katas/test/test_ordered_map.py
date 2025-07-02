import unittest
from katas.ordered_map import OrderedMap
class TestOrderedMap(unittest.TestCase):

    def test_put_and_get(self):
        omap = OrderedMap()
        omap.put("a", 1)
        omap.put("b", 2)
        self.assertEqual(omap.get("a"), 1)
        self.assertEqual(omap.get("b"), 2)

    def test_update_value(self):
        omap = OrderedMap()
        omap.put("x", 10)
        omap.put("x", 20)
        self.assertEqual(omap.get("x"), 20)
        self.assertEqual(omap.keys(), ["x"])  # order should be preserved

    def test_remove(self):
        omap = OrderedMap()
        omap.put("one", 1)
        omap.put("two", 2)
        omap.remove("one")
        self.assertEqual(omap.get("one"), None)
        self.assertEqual(omap.keys(), ["two"])

    def test_keys_order(self):
        omap = OrderedMap()
        omap.put("first", 100)
        omap.put("second", 200)
        omap.put("third", 300)
        self.assertEqual(omap.keys(), ["first", "second", "third"])

    def test_size(self):
        omap = OrderedMap()
        self.assertEqual(omap.size(), 0)
        omap.put("a", 1)
        omap.put("b", 2)
        self.assertEqual(omap.size(), 2)
        omap.put("a", 100)  # update should not change size
        self.assertEqual(omap.size(), 2)
        omap.remove("b")
        self.assertEqual(omap.size(), 1)

    def test_clear(self):
        omap = OrderedMap()
        omap.put("a", 1)
        omap.put("b", 2)
        omap.clear()
        self.assertEqual(omap.size(), 0)
        self.assertEqual(omap.keys(), [])
        self.assertEqual(omap.get("a"), None)

if __name__ == '__main__':
    unittest.main()
