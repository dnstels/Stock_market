import marimo

__generated_with = "0.23.3"
app = marimo.App(width="full")

with app.setup:
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Stock Marcket
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Постанивка задачи
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Исходные данные
    """)
    return


@app.cell
def _():
    mo.md(r"""
    - Ширина _пула_ - $P_w$
    - Процент комиссионных ($\pi$)
    - Начальный капитал ($C$)
    - Величена шага - $t$
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Применяем обозначения для переменных
    """)
    return


@app.cell
def _():
    mo.md(r"""
    $P$ - пул
    $S$ - шорт
    $\beta$ -> $BEP$ - точка без убыточности
    $P_a$ - нижняя граница пула
    $P_b$ - верхняя граница пула
    $P_n$ - середина и начальное значений пула
    $L$ - ликвидность
    $P_t$ - Текущая цена (цена на шаге)
    $P_{loss}$ - Величина потерь
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Величины которые расчитываются на каждом шаге
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    $var$
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Работа триггетов
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Величины которые расчитываются при **открытии** *пула*
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Величины которые расчитываются при **открытии** *шорта*
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Величины которые расчитываются при **зактытии** *пула*
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Величины которые расчитываются при **зактытии** *шорта*
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Примеры расчетов
    """)
    return


@app.cell
def _():
    p_n = 2000
    Range = 1000
    Asyn_pct = 50
    Kasyn = 0.3

    p_b_1 = p_n + Range * Asyn_pct / 100
    p_b_2 = p_n + Range * Kasyn

    p_a_1 = p_n - Range * (100 - Asyn_pct) / 100
    p_a_2 = p_n - Range * (1 - Kasyn)

    out_b = p_b_1 == p_b_2
    out_a = p_a_1 == p_a_2
    return p_a_2, p_b_2, p_n


@app.cell
def _(p_a_2, p_b_2, p_n):
    pb = p_b_2
    pn = p_n
    pa = p_a_2
    bep = 1365
    prices = np.array([2000, 2120, 1950, 1400, 1450])

    step_count = 5  # len(prices)
    steps = np.arange(step_count, dtype=np.int16)

    plt.axhline(y=pb, linestyle="--", label="$P_b$")
    plt.axhline(y=pn, linestyle="--", color="gray", label="$P_n$")
    plt.axhline(y=pa, linestyle="--", color="red", label="$P_a$")
    plt.axhline(y=bep, linestyle="--", color="tab:orange", label="$BEP$")

    plt.scatter(steps, prices)
    plt.plot(steps, prices, color="blue", label="Цена")

    plt.axvline(x=0, color="g", linestyle=":", label="Открыть пул")
    plt.axvline(x=3, color="r", linestyle=":", label="Закрыть пул")
    plt.annotate("$P_{loss}$", (1, prices[1] + 50))
    plt.annotate("$\\beta$", (3 + 0.05, prices[3] + 50))

    plt.xticks(steps + 1)

    plt.title("Pool / Short")
    plt.xlabel("Ось шаг")
    plt.ylabel("Ось Цена")
    plt.grid(False)
    plt.legend(loc="best")
    # plt.show()
    return


@app.cell
def _():
    x1 = [1, 2, 3, 4]
    y1 = [10, 15, 20, 25]
    labels1 = ["A", "B", "C", "D"]

    plt.scatter(x1, y1)  # Создаём точечный график

    for x_coord1, y_coord1, label1 in zip(x1, y1, labels1):
        plt.text(
            x_coord1, y_coord1, label1
        )  # Добавляем текстовую метку к каждой точке

    plt.show()  # Отображаем график
    return


@app.cell
def _():
    # # import matplotlib.pyplot as plt
    # x = [1, 2, 3, 4]
    # y = [10, 15, 20, 25]
    # labels = ["A", "B", "C", "D"]  # Метки точек

    # plt.scatter(x, y)  # Создаём точечный график

    # for x_coord, y_coord, label in zip(x, y, labels):
    #     plt.annotate(
    #         label, (x_coord + 0.01, y_coord + 1)
    #     )  # Добавляем текстовую метку к каждой точке
    # plt.show()
    return


if __name__ == "__main__":
    app.run()
