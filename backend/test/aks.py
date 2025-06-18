import akshare as ak
import time
import pandas as pd


# futures_contract_detail_df = ak.futures_contract_detail(symbol='MA2509')
# print(futures_contract_detail_df)

# futures_main_sina_hist = ak.futures_main_sina(symbol="V0", start_date="20200101", end_date="20220101")
# print(futures_main_sina_hist)


# futures_display_main_sina_df = ak.futures_display_main_sina()
# print(futures_display_main_sina_df)

# a = ak.match_main_contract(symbol='all')
# print(a)


# 接口示例-订阅所有商品期货(大商所, 上期所, 郑商所主力合约)

# dce_text = ak.match_main_contract(symbol="dce")
# czce_text = ak.match_main_contract(symbol="czce")
# shfe_text = ak.match_main_contract(symbol="shfe")
# gfex_text = ak.match_main_contract(symbol="gfex")
#
# while True:
#     time.sleep(3)
#     futures_zh_spot_df = ak.futures_zh_spot(
#         symbol=",".join([dce_text, czce_text, shfe_text, gfex_text]),
#         market="CF",
#         adjust='0')
#     print(futures_zh_spot_df)

# 接口示例-白糖期货的所有合约

# futures_zh_realtime_df = ak.futures_zh_realtime(symbol="白糖")
# print(futures_zh_realtime_df)

# 接口示例-所有期货品种的所有合约（请注意数据获取频率）

futures_symbol_mark_df = ak.futures_symbol_mark()

big_df = pd.DataFrame()
for item in futures_symbol_mark_df['symbol']:
    print(item)
    futures_zh_realtime_df = ak.futures_zh_realtime(symbol=item)
    big_df = pd.concat([big_df, futures_zh_realtime_df], ignore_index=True)

print(big_df)