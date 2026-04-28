import marimo

__generated_with = "0.23.3"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import pandas as pd

    file_path = "Stok_Marcet/Data/Нужные данные из сводных таблиц.xlsx"

    # # Загрузка данных из файла
    # df = pd.read_excel(file_path)


    # # Вывод первых 5 строк DataFrame
    # # print(df.head()

    # Загрузка данных из файла с несколькими листами
    # df_sheet1 = pd.read_excel(file_path, sheet_name="Упорядоченные данные")
    df_sheet2 = pd.read_excel(file_path, sheet_name="Все данные")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Столбци для отчета *xlsx*

    Упорядоченные данные
    [
      "Date",
      "ETH Price",
      "Event",
      "DynamicInRange",
      "DynamicPa",
      "DynamicPn",
      "DynamicPb",
      "RangeWidth",
      "DynamicL",
      "ShortActive",
      "Short ETH",
      "ShortEntryPrice",
      "BEP",
      "LastBEP",
      "CloseShortTrigger",
      "CloseShortReason",
      "LastCloseReason",
      "CloseShortPrice",
      "Pool Value",
      "Pool ETH",
      "Pool USDC",
      "CurrentPoolValue",
      "Pool Exit Value",
      "Pool Exit Price",
      "Pool Exit Realized PnL",
      "Pool Exited",
      "Pending Cash",
      "Compounded Cash",
      "Compound Event",
      "Compound Cost",
      "Accrued Fees",
      "Funding PnL",
      "Short Realized PnL",
      "Costs",
      "Daily PnL",
      "Realized PnL",
      "Total PnL",
      "Cumulative PnL",
      "ROI",
      "Total ROI",
      "Total Portfolio Value",
      "Drawdown_15min",
      "Daily_Max_Drawdown",
      "Daily_Max_Runup",
      "Daily_Return",
      "Daily_Drawdown_From_Prev"
    ]

    Все данные
    [
      "open_time",
      "open",
      "high",
      "low",
      "close",
      "volume",
      "close_time",
      "quote_asset_volume",
      "number_of_trades",
      "taker_buy_base_asset_volume",
      "taker_buy_quote_asset_volume",
      "ignore",
      "ETH Price",
      "Date",
      "High",
      "Low",
      "Open",
      "OutOfRangeCount",
      "BelowPaCount",
      "OutOfRangeHours",
      "BelowPaHours",
      "CloseShortPrice",
      "LastBEP",
      "LastCloseReason",
      "DaysSinceClose",
      "HoursSinceClose",
      "HoursSinceTrigger",
      "DynamicPn",
      "DynamicPa",
      "DynamicPb",
      "DynamicL",
      "RangeWidth",
      "ShortEntryPrice",
      "CloseShortTrigger",
      "CloseShortReason",
      "Short ETH",
      "ShortActive",
      "ShortLiquidity",
      "MaxPriceSinceClose",
      "ShouldReopenShort",
      "BEP",
      "Short Unrealized PnL",
      "Short Realized PnL",
      "Pool Realized PnL",
      "Realized IL on Shift",
      "CurrentPoolValue",
      "Pending Cash",
      "Compounded Cash",
      "Compound Event",
      "Compound Cost",
      "Pool Exit Value",
      "Pool Exit Price",
      "Pool Exit Realized PnL",
      "Pool Exited",
      "ExitTime",
      "LastReinvestDate",
      "DynamicInRange",
      "Cash To Reinvest",
      "ReinvestTrigger",
      "sqrt_price",
      "sqrt_dynamic_pa",
      "sqrt_dynamic_pb",
      "Pool ETH",
      "Pool USDC",
      "Pool Value",
      "Accrued Fees",
      "Funding PnL",
      "Expected_Pending",
      "PriceBetweenPaAndPn",
      "Pool PnL Daily",
      "Delta Pool",
      "Cumulative Fees",
      "Cumulative Funding",
      "Costs",
      "Daily PnL",
      "Realized PnL",
      "Total PnL",
      "Total Portfolio Value",
      "Cumulative PnL",
      "ROI",
      "Total ROI",
      "Drawdown_1min",
      "Date_Day",
      "Daily_First_Value",
      "Daily_Last_Value",
      "Daily_Min_Value",
      "Daily_Max_Value",
      "Daily_Max_Drawdown",
      "Daily_Max_Runup",
      "Prev_Day_Close",
      "Daily_Return",
      "Daily_Drawdown_From_Prev",
      "Event",
      "Correct Drawdown",
      "Drawdown"
    ]
    """)
    return


if __name__ == "__main__":
    app.run()
