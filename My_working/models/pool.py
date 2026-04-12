import numpy as np
from random import uniform


class Setting():
    APR = 0.6
    # HOURS_IN_YEAR = 24 * 365
    # TIME_STEP_HOURS = 1/60
    MINUTE_IN_YEAR = 525600

class Pool():
    __pb: float = None
    __pn: float = None
    __pa: float = None
    __apr = Setting.APR
    def __init__(self, range: float, k_async: float=0.5):
        self.__k_async = Pool.set_async_factor(k_async)
        self.__range = uniform(0,1000) if range is Ellipsis else range
        self.__is_close = True

    @classmethod
    def set_async_factor(cls, k) -> float:
        k_async = k if abs(k) <= 1 else float(k / 100)
        return round(k_async if k_async > 0 else 1 - abs(k_async), 2)
    
    @property
    def range(self) ->float:
        return self.__range
    
    @property
    def async_factor(self):
        return self.__k_async

    @property
    def pb(self):
        """Величина верхней границы
        Returns:
            float: Величина верхней границы
        """
        return self.__pb
    
    @property
    def pn(self):
        return self.__pn
    
    @property
    def pa(self):
        """Величина нижней границы
        Returns:
            float: Величина нижней границы
        """
        return self.__pa
    
    @property
    def capital(self):
        return self.__capital
    
    @property
    def is_close(self):
        return self.__is_close
    
    def __calc_range(self):
        self.__pb = self.__pn + self.__range * self.__k_async
        self.__pa = self.__pn - self.__range * (1 - self.__k_async)

    def step(self, time, price):
        if self.is_close:
            self.open(time, self.capital, price)
        if self.__validate_bep_proximity(price): 
            pass

        self.__countStep += 1

    def close(self):
        self.__is_close = True
    
    def __validate_bep_proximity(self, price)->bool:
        return False
    
    def open(self, time, capital: float, price: float):
        self.__pn = price
        self.__capital = capital
        self.__time_open = time
        self.__calc_range()
        self.__countStep = 0
        self.__is_close = False

    def liquid(self, capital_amount: float) -> float:
        """Правильная формула ликвидности для Uniswap V3"""
        # if pn_price <= self.pa or pn_price >= self.pb:
        #     pn_price = (self.pa + self.pb) / 2

        sqrt_pn = np.sqrt(self.pn)
        sqrt_pa = np.sqrt(self.pa)
        sqrt_pb = np.sqrt(self.pb)
        
        term1 = sqrt_pn - sqrt_pa
        term2 = self.pn * (1/sqrt_pn - 1/sqrt_pb)
        if (term1 + term2) == 0:
            return 0.0
        
        k_liquid = capital_amount / (term1 + term2)
        
        # if verbose_logging and abs(calculate_pool_value(self.pn, self.pa, self.pb, k_liquid) - capital_amount) > capital_amount * 0.01:
        #     print(f"  Внимание: разница в расчетах. Capital=${capital_amount:.2f}, Pool Value at Pn=${calculate_pool_value(self.pn, self.pa, self.pb, k_liquid):.2f}")
        return k_liquid
    
    @property
    def size(self):
        return self.capital + self.getCommissionCost()
    
    def getCommissionCost(self) -> float:
        """Расчет комиссии 

        Returns:
            float: Величина комиссии 
        """
        commission_in_year = self.capital * self.__apr
        return  commission_in_year * self.__countStep / Setting.MINUTE_IN_YEAR
    
    def reinvest(self):
        """Реинвестирование"""
        self.__capital = self.size