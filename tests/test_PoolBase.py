from unittest import TestCase
from models.PoolBase import PoolBase

class PoolSample(PoolBase):
    @property
    def Size(self):
        return super().Size()

class TestPoolBase(TestCase):
    def setUp(self):
        # self.my_list = [1, 2, 3, 4]
        self.pool = PoolSample(2000)
    
    def tearDown(self):
        # self.my_list.clear()  # Очистка после теста
        pass
    
    def test_init_IsClose_True(self):
        sut = self.pool
        self.assertTrue(sut.IsClose)
    
    def test_GetInfo(self):
        sut = self.pool

        print('test_GetInfo')
        print(sut.get_Info())
        
        sut.open(2000.0)
        print(sut.get_Info())
        
        sut.close("Test_close")
        print(sut.get_Info())
