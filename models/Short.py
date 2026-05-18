from PoolBase import PoolBase
from Pool import Pool

class Short(PoolBase):

    def __init__(self, pool: Pool):
        super().__init__(pool.Range, pool.__k_a, pool.__k_b)

    def open(self, init_obj):
        return super().open(init_obj)
    
    def close(self, description):
        return super().close(description)

    @property
    def Size(self):
        return self.Pn - self.Pt