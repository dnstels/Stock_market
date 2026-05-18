try:
    from models.PoolBase import PoolBase
except:
    from PoolBase import PoolBase
# from models.Short import Short

class Pool(PoolBase):
    # short: Short
    __pt: float = None
    __date_time: str = None
    
    @property
    def Size(self):
        return super().Size()
    
    def step(self, date_time, price):
        self.__pt = price
        self.__date_time = date_time
        self.on_action = None
        # Триггеры
        if self.IsClose:
            self.open(price)
            # return
        if not self.IsClose:    
            if self.Pa > price:
                self.close("price < Pa")
                return
            if self.Pb < price:
                self.close("price > Pb")
                return

    def get_Info(self):
        info_base = super().get_Info()
        info_pool = {
            # 'Size': self.Size,
            'price': self.__pt,
            'date_time': self.__date_time
        }
        info = {**info_pool, **info_base}
        return info
    
    def get_PnL(self):
        self.Pt - self.Pn # Просадка
