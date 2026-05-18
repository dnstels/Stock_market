from random import uniform
from abc import ABC, abstractmethod

class PoolBase(ABC):
    __pb: float = None
    __pn: float = None
    __pa: float = None
    __is_close = True
    on_action: str = None
    
    def __init__(self, range_size: float, k_async: float=0.0):
    # def __init__(self,  *args, **kwargs):
        # k_async = kwargs.get("k_async", 0.0)
        # range_size = kwargs.get("range_size",uniform(0,1000))
        # range_size = kwargs.get("range_size",0.0)
        self.__set_async_factor(k_async)
        self.__range = range_size
        self.close("onInit")

    # def __init__(self, pa: float, pb: float, pn: float):
    #     self.__pa = pa
    #     self.__pb = pb
    #     self.__pn = pn
        
    def __set_async_factor(self, k) -> None:
        if k == 0:
            self.__k_b = self.__k_a = 0.5
        dirCoef = round(abs(k), 2)
        resideCoef = round(1 - dirCoef, 2)
        if k < 0:
            self.__k_b = resideCoef
            self.__k_a = dirCoef
        if k > 0:
            self.__k_b = dirCoef
            self.__k_a = resideCoef

    def __calc_range(self):
        self.__pb = self.__pn + self.__range * self.__k_b
        self.__pa = self.__pn - self.__range * self.__k_a

    def __reset_range(self):
        self.__pn = self.__pa = self.__pb = None

    def open(self, init_obj) -> None:
        if isinstance(init_obj, PoolBase) and not init_obj.IsClose:
            self.__pn = init_obj.Pn
            self.__pa = init_obj.Pa
            self.__pb = init_obj.Pb
        elif isinstance(init_obj, float):
            self.__pn = init_obj
            self.__calc_range()
        else:
            raise ValueError(f'Значение {init_obj} ошибочно.')
        self.__description_close = ''
        self.on_action = 'open'
        self.__is_close = False

    def close(self, description: str) -> None:
        self.__description_close = description
        # self.__reset_range()
        self.on_action = 'close'
        self.__is_close = True

    def step(self,time,price):
        pass

    @property
    def Pa(self):
        return self.__pa
    
    @property
    def Pb(self):
        return self.__pb
    
    @property
    def Pn(self):
        return self.__pn
    
    @property
    def Range(self):
        return self.__range
    
    @property
    def IsClose(self): 
        return self.__is_close
    
    @property
    def DescriptionClose(self):
        return self.__description_close
    
    @abstractmethod
    def Size(self):
        ...

    def get_Info(self):
        return {
            'Pb': self.Pb,
            'Pn': self.Pn,
            'Pa': self.Pa,
            'Action': self.on_action,
            # 'Size': self.__size,
            'IsClose': self.IsClose,
            'DescriptionClose': self.DescriptionClose,
        }