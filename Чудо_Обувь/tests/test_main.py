import unittest

class TestChudoObuv(unittest.TestCase):
    def test_total_sum(self):
        items = [{'price': 100, 'quantity': 2}]
        total = sum(i['price'] * i['quantity'] for i in items)
        self.assertEqual(total, 200)

    def test_filter_by_price(self):
        products = [{'price': 5000}, {'price': 7000}, {'price': 9000}]
        result = [p for p in products if 5000 <= p['price'] <= 8000]
        self.assertEqual(len(result), 2)

if __name__ == '__main__':
    unittest.main()
