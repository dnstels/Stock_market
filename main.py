import pandas as pd
from tqdm import tqdm
# import time
import sys
sys.path.append('./models')
from models_old.Pool import Pool
# from models.Short import Short


pool = Pool(1000)
# short = Short()

# data_in = pd.read_csv("in_datas/eth_2025_full.csv", nrows=10)
data_in = pd.read_csv("in_datas/eth_2025_full.csv")
data_in = data_in.head(100)

# columns_out = [
#     'time', 'price'
# ]
# data_out = pd.DataFrame(columns=columns_out)
data_out = pd.DataFrame()
for index, row in tqdm(data_in.iterrows(), total=len(data_in), desc="Обработка строк"):
    time = row['open_time']
    price = row['close']
    pool.step(date_time=time, price=price)
    processed_row = {
        'time': time,
        'price': price,
        'Pool_close': pool.IsClose,
        # 'Short_close': short.IsClose,
        'Pool_Pb': pool.Pb,
        'Pool_Pn': pool.Pn,
        'Pool_Pa': pool.Pa,
    }
    
    data_out = pd.concat([data_out, pd.DataFrame(processed_row, index=[0])], ignore_index=True)

print('*'*80)
# print(data_in)
print(data_out)
