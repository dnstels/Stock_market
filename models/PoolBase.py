from random import uniform

class PoolBase:
    __pb: float = None
    __pn: float = None
    __pa: float = None
    __is_close = True
    
    # def __init__(self, range: float, k_async: float=0.0):
    def __init__(self,  *args, **kwargs):
        k_async = kwargs.get("k_async", 0.0)
        range_size = kwargs.get("range_size",uniform(0,1000))
        self.__set_async_factor(k_async)
        self.__range = range_size
        self.__is_close = True
        
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
            raise ValueError(init_obj)
        self.__is_close = False

    def close(self) -> None:
        self.__reset_range()
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