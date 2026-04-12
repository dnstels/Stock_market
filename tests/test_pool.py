from My_working.models.pool import Pool


def test_set_k_async():
    # pool = Pool()
    # assert pool._Pool__set_k_async(0.3) == 0.3
    assert Pool.set_async_factor(0.3) == 0.3
    assert Pool.set_async_factor(30) == 0.3
    assert Pool.set_async_factor(-0.7) == 0.3
    assert Pool.set_async_factor(-70) == 0.3
    assert Pool.set_async_factor(-0.5) == 0.5
    assert Pool.set_async_factor(-50) == 0.5
    assert Pool.set_async_factor(0.5) == 0.5
    assert Pool.set_async_factor(50) == 0.5

def test_init_empty():
    """Проверка создания pool
    """
    pool = Pool(...)

    assert pool.range is not Ellipsis
    assert pool.async_factor
    assert pool.pb is None
    assert pool.pn is None
    assert pool.pa is None

def test_open():
    """Проверка открытия pool
    """
    pool = Pool(range=1000, k_async=0.3)

    assert pool.is_close == True
    pool.open(time=None, capital=10000, price=1000)
    
    assert pool.is_close == False
    assert pool.pn == 1000.0
    assert pool.pb == 1300.0
    assert pool.pa == 300.0
    assert pool.capital == 10000.0

def test_close_isClosed():
    """Проверка закрытия pool
    """
    pool = Pool(...)
    pool.open(None, 0.0, 0.0)
    assert pool.is_close == False

    pool.close()

    assert pool.is_close == True

def test_getCommissionCost():
    """Проверка расчета комиссии"""
    capital = 100000
    price = 2000
    pool = Pool(...)
    pool.open(..., capital, price)

    commission = pool.getCommissionCost()
    assert round(commission, 4) == 0

    pool.step(..., price)

    commission = pool.getCommissionCost()
    assert round(commission, 4) == 0.1142