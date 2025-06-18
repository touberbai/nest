from fastapi import APIRouter, HTTPException
import requests
import re
import json
import akshare as ak
import time
import pandas as pd
import threading
from datetime import datetime
import asyncio

# 数据缓存
contract_cache = {}
boll_data_cache = {}
last_update_time = None
update_lock = threading.Lock()

def update_all_futures_data():
    try:
        # 获取主力合约
        with update_lock:
            # 获取主力合约 - 添加验证
            exchanges = ['dce', 'czce', 'shfe', 'gfex']
            main_contracts = {}
            
            for exchange in exchanges:
                contract_text = ak.match_main_contract(symbol=exchange)
                if not contract_text:
                    print(f"获取{exchange}主力合约失败，返回空值")
                    continue
                main_contracts[exchange] = contract_text
            
            contract_cache['main_contracts'] = main_contracts
            
            # 此处的合约需要是近期的合约, 否则会报错
            futures_zh_spot_df = ak.futures_zh_spot(symbol='V2205, P2205, B2201, M2205', market="CF", adjust='0')
            
            # 处理每个交易所的主力合约
            for exchange, exchange_contracts in main_contracts.items():
                symbols = exchange_contracts.split(',')
                for symbol in symbols:
                    symbol = symbol.strip()
                    if not symbol:
                        continue
                    
                    try:
                        # 获取日线数据 - 添加验证
                        daily_data = ak.futures_zh_daily_sina(symbol=symbol)
                        
                        # 验证数据有效性
                        if daily_data is None or daily_data.empty:
                            print(f"合约 {symbol} 日线数据为空")
                            continue
                        
                        # 检查必要列是否存在
                        required_columns = ['close']
                        for col in required_columns:
                            if col not in daily_data.columns:
                                print(f"合约 {symbol} 数据格式异常，缺少{col}列")
                                print(daily_data.columns)
                                continue
                        
                        # 确保有足够的数据点计算布林带
                        if len(daily_data) < 20:
                            print(f"合约 {symbol} 数据行数不足(需要至少20行)，实际行数: {len(daily_data)}")
                            continue
                        
                        
                        # 通过
                        
                        # 计算布林带
                        df = daily_data.copy()
                        df['MA20'] = df['close'].rolling(window=20).mean()
                        df['STD20'] = df['close'].rolling(window=20).std()
                        df['Upper'] = df['MA20'] + 2 * df['STD20']
                        df['Lower'] = df['MA20'] - 2 * df['STD20']
                        
                        # 处理非标准浮点值
                        import numpy as np
                        df = df.replace([np.nan, np.inf, -np.inf], None)
                        
                        # 缓存布林带数据
                        boll_data_cache[symbol] = df.to_dict('records')
                        print(f"成功更新合约 {symbol} 的布林带数据")
                    
                    except Exception as e:
                        print(f"处理合约 {symbol} 失败: {str(e)}")
                        # 打印更详细的错误信息用于调试
                        import traceback
                        print(traceback.format_exc())
    
    except Exception as e:
        print(f"更新全部数据失败: {str(e)}")
        raise
