from unittest import TestCase, mock
from unittest.mock import patch
from autofaker import autodata
from models.PoolBase import PoolBase

class TestPoolBase(TestCase):
    def setUp(self):
        self.my_list = [1, 2, 3, 4]
    def tearDown(self):
        self.my_list.clear()  # Очистка после теста

    @autodata(float)
    def test_range_devZero(self,init_price):
        sut = PoolBase(k_async=0)
        sut.open(init_price)
        
        self.assertEqual(sut.Pn, init_price)
        self.assertEqual(sut.Pa, init_price - sut.Range*0.5)
        self.assertEqual(sut.Pb, init_price + sut.Range*0.5)
        
    @autodata(float)
    def test_range_devDown(self,init_price):
        sut = PoolBase(k_async=0.3)
        sut.open(init_price)
        
        self.assertEqual(sut.Pn, init_price)
        self.assertEqual(sut.Pa, init_price - sut.Range*0.7)
        self.assertEqual(sut.Pb, init_price + sut.Range*0.3)

    @autodata(float)
    def test_range_devUp(self,init_price):
        sut = PoolBase(k_async=-0.3)
        sut.open(init_price)
        
        self.assertEqual(sut.Pn, init_price)
        self.assertEqual(sut.Pa, init_price - sut.Range*0.3)
        self.assertEqual(sut.Pb, init_price + sut.Range*0.7)

    def test_init_IsClose_True(self):
        sut = PoolBase()

        self.assertTrue(sut.IsClose)

    @autodata(float)
    def test_open_IsClose_False(self,init_price):
        sut = PoolBase()

        sut.open(init_price)
        
        self.assertFalse(sut.IsClose)

    # @mock.patch.object(PoolBase, '_PoolBase__is_close', new_callable=mock.PropertyMock)
    # def test_close_IsClose_True(self, is_close: mock.PropertyMock):
        # is_close.return_value = False
        # sut = PoolBase(...)
        # self.assertFalse(sut.IsClose)

    def test_close_IsClose_True(self):
        sut = PoolBase()
        sut._PoolBase__is_close = False

        sut.close()
        
        self.assertTrue(sut.IsClose)
        