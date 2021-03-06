import unittest

from constantcontact import Promocode

class Test_Promocode(unittest.TestCase):
    def test_promo_init_from_dict(self):
        promocode = Promocode({'id': '123456', 'code_name': 'Name Goes Here!'})

        self.assertEqual(promocode.get_code_name(), 'Name Goes Here!')

    def test_promo_fee_ids(self):
        promocode = Promocode()

        self.assertEqual(promocode.get_fee_ids(), None)

        fee_ids = ['123', '456', '789', 'abc']

        promocode.set_fee_ids(fee_ids)

        self.assertEqual(len(promocode.get_fee_ids()), 4)

        promocode.delete_fee_by_id('789')

        self.assertFalse('789' in promocode.get_fee_ids())

        promocode.delete_fee(2)

        self.assertFalse('abc' in promocode.get_fee_ids())

        promocode.clear_fee_ids()

        self.assertFalse(promocode.get_fee_ids(), None)

if __name__ == '__main__':
    unittest.main()
