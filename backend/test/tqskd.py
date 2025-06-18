# 天勤skd测试
from tqsdk import TqApi, TqAuth



USERNAME = '18800008769'
PASSWORD = 'RsZmDYwmkw9odrk'


api = TqApi(auth=TqAuth(USERNAME, PASSWORD))

# 快速上手
# quote = api.get_quote("SHFE.ni2206")
#
# print (quote.last_price, quote.volume)
#
# while True:
#     api.wait_update()
#     print (quote.datetime, quote.last_price)

# 获取全部主力合约

# try:
#     # 查询所有主力合约（格式为 "KQ.m@交易所代码.品种"）
#     main_contracts = api.query_quotes(ins_class="CONT", expired=False)
#
#     # 打印主力合约列表
#     print("主力合约列表：", main_contracts)
#
# finally:
#     api.close()  # 关闭 API 连接

# 获取主力合约对应的标的合约
# try:
#     ls = api.query_cont_quotes()
#     print(ls)  # 全部主连合约对应的标的合约
# finally:
#     api.close()  # 关闭 API 连接
# ['CZCE.CF509', 'CZCE.CJ509', 'SHFE.ru2509', 'CFFEX.IC2506', 'CZCE.PF508', 'CFFEX.IF2506', 'CZCE.OI509', 'CZCE.SA509', 'INE.lu2508', 'SHFE.rb2510', 'DCE.jm2509', 'CZCE.ZC509', 'INE.nr2507', 'DCE.b2509', 'DCE.l2509', 'CZCE.SF509', 'DCE.fb2510', 'CZCE.LR509', 'CFFEX.TS2509', 'CZCE.WH509', 'SHFE.al2507', 'DCE.cs2507', 'DCE.m2509', 'DCE.lh2509', 'DCE.j2509', 'CFFEX.IM2506', 'SHFE.wr2510', 'CZCE.PK510', 'CZCE.RI509', 'DCE.bb2511', 'SHFE.bu2509', 'DCE.i2509', 'SHFE.sn2507', 'SHFE.br2507', 'CFFEX.TF2509', 'DCE.v2509', 'SHFE.zn2507', 'SHFE.ss2508', 'DCE.a2509', 'DCE.y2509', 'SHFE.hc2510', 'CZCE.UR509', 'CZCE.SH509', 'DCE.c2507', 'CZCE.MA509', 'CZCE.PM509', 'DCE.eg2509', 'CFFEX.TL2509', 'CZCE.RM509', 'SHFE.ad2511', 'INE.sc2508', 'CZCE.JR509', 'DCE.eb2507', 'CZCE.SM509', 'DCE.jd2508', 'SHFE.fu2509', 'DCE.lg2507', 'GFEX.lc2509', 'SHFE.cu2507', 'CZCE.SR509', 'INE.ec2508', 'CZCE.PX509', 'DCE.p2509', 'SHFE.pb2507', 'GFEX.si2509', 'GFEX.ps2507', 'SHFE.ao2509', 'SHFE.au2508', 'CZCE.AP510', 'SHFE.ni2507', 'DCE.rr2508', 'DCE.pp2509', 'SHFE.sp2507', 'DCE.pg2507', 'CZCE.FG509', 'CFFEX.T2509', 'CZCE.TA509', 'INE.bc2507', 'CZCE.CY509', 'SHFE.ag2508', 'CFFEX.IH2506', 'CZCE.RS507', 'CZCE.PR509']

# 获取行情数据
try:
    symbol = ['CZCE.CF509', 'CZCE.CJ509', 'SHFE.ru2509', 'CFFEX.IC2506', 'CZCE.PF508', 'CFFEX.IF2506', 'CZCE.OI509', 'CZCE.SA509', 'INE.lu2508', 'SHFE.rb2510', 'DCE.jm2509', 'CZCE.ZC509', 'INE.nr2507', 'DCE.b2509', 'DCE.l2509', 'CZCE.SF509', 'DCE.fb2510', 'CZCE.LR509', 'CFFEX.TS2509', 'CZCE.WH509', 'SHFE.al2507', 'DCE.cs2507', 'DCE.m2509', 'DCE.lh2509', 'DCE.j2509', 'CFFEX.IM2506', 'SHFE.wr2510', 'CZCE.PK510', 'CZCE.RI509', 'DCE.bb2511', 'SHFE.bu2509', 'DCE.i2509', 'SHFE.sn2507', 'SHFE.br2507', 'CFFEX.TF2509', 'DCE.v2509', 'SHFE.zn2507', 'SHFE.ss2508', 'DCE.a2509', 'DCE.y2509', 'SHFE.hc2510', 'CZCE.UR509', 'CZCE.SH509', 'DCE.c2507', 'CZCE.MA509', 'CZCE.PM509', 'DCE.eg2509', 'CFFEX.TL2509', 'CZCE.RM509', 'SHFE.ad2511', 'INE.sc2508', 'CZCE.JR509', 'DCE.eb2507', 'CZCE.SM509', 'DCE.jd2508', 'SHFE.fu2509', 'DCE.lg2507', 'GFEX.lc2509', 'SHFE.cu2507', 'CZCE.SR509', 'INE.ec2508', 'CZCE.PX509', 'DCE.p2509', 'SHFE.pb2507', 'GFEX.si2509', 'GFEX.ps2507', 'SHFE.ao2509', 'SHFE.au2508', 'CZCE.AP510', 'SHFE.ni2507', 'DCE.rr2508', 'DCE.pp2509', 'SHFE.sp2507', 'DCE.pg2507', 'CZCE.FG509', 'CFFEX.T2509', 'CZCE.TA509', 'INE.bc2507', 'CZCE.CY509', 'SHFE.ag2508', 'CFFEX.IH2506', 'CZCE.RS507', 'CZCE.PR509']
    klines = api.get_kline_serial(symbol, 86400, data_length=5)
    print("多合约K线：", klines)
    while True:
        api.wait_update()
        if api.is_changing(klines.iloc[-1], ["close1", "close"]):  # 判断任何一个收盘价是否有更新
            dif = klines.close1 - klines.close  # 使用对齐的K线直接计算价差等数据
            print("价差序列：", dif)
finally:
    api.close()  # 关闭API连接