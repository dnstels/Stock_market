from unittest import TestCase, mock
from unittest.mock import patch
from autofaker import autodata
from models.Pool import Pool

class TestPool(TestCase):
    def setUp(self):
        # self.my_list = [1, 2, 3, 4]
        self.pool_range = 10.0
        self.pool = Pool(self.pool_range, 0.3)
        pass
    def tearDown(self):
        # self.my_list.clear()  # Очистка после теста
        pass

    @autodata(float)
    def test_range_devZero(self,init_price):
        sut = Pool(self.pool_range, k_async=0)
        sut.open(init_price)
        
        self.assertEqual(sut.Pn, init_price)
        self.assertEqual(sut.Pa, init_price - sut.Range*0.5)
        self.assertEqual(sut.Pb, init_price + sut.Range*0.5)
        
    @autodata(float)
    def test_range_devDown(self,init_price):
        sut = Pool(self.pool_range, k_async=0.3)
        sut.open(init_price)
        
        self.assertEqual(sut.Pn, init_price)
        self.assertEqual(sut.Pa, init_price - sut.Range*0.7)
        self.assertEqual(sut.Pb, init_price + sut.Range*0.3)

    @autodata(float)
    def test_range_devUp(self,init_price):
        sut = Pool(self.pool_range, k_async=-0.3)
        sut.open(init_price)
        
        self.assertEqual(sut.Pn, init_price)
        self.assertEqual(sut.Pa, init_price - sut.Range*0.3)
        self.assertEqual(sut.Pb, init_price + sut.Range*0.7)

    def test_init_IsClose_True(self):
        sut = Pool(self.pool_range)

        self.assertTrue(sut.IsClose)

    @autodata(float)
    def test_open_InitPrice_IsClose_False(self,init_price):
        sut = Pool(self.pool_range)

        sut.open(init_price)
        
        self.assertFalse(sut.IsClose)

    # @mock.patch.object(Pool, '_Pool__is_close', new_callable=mock.PropertyMock)
    # def test_close_IsClose_True(self, is_close: mock.PropertyMock):
        # is_close.return_value = False
        # sut = Pool(...)
        # self.assertFalse(sut.IsClose)

    def test_open_InitPool_IsClose_False(self):
        # raise NotImplementedError("Метод ещё не реализован")
        init_pool = Pool(self.pool_range)
        sut = Pool(init_pool)

        sut.open(init_pool)

        self.assertFalse(sut.IsClose)

    def test_close_IsClose_True(self):
        sut = Pool(self.pool_range)
        sut._Pool__is_close = False

        sut.close()
        
        self.assertTrue(sut.IsClose)

    def test_Size_isZero(self):
        sut = Pool(self.pool_range)

        size = sut.Size

        self.assertIs(size,0)
        
    def test_GetInfo(self):
        sut = Pool(self.pool_range)
        print('*'*80)
        print(sut.get_Info())
        print(sut.Size)

    def test_step_1(self):
        sut = self.pool

        print(sut.get_Info())
        sut.step(None,10.1)
        print(sut.get_Info())
        sut.step(None,3.0)
        print(sut.get_Info())
        sut.step(None,7.0)
        print(sut.get_Info())




