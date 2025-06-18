# backend/routers/futures.py
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


router = APIRouter()

# 数据缓存
contract_cache = {}
boll_data_cache = {}
last_update_time = None
update_lock = threading.Lock()


# 初始化函数，启动定时更新任务
def init_future_data_updater():
    threading.Thread(target=update_data_periodically, daemon=True).start()


# 定时更新数据
def update_data_periodically():
    global last_update_time
    while True:
        try:
            update_all_futures_data()
            last_update_time = datetime.now()
            print(f"数据更新完成，下次更新将在3秒后进行")
        except Exception as e:
            print(f"数据更新失败: {str(e)}")
        time.sleep(3)  # 每3秒更新一次


# 更新所有期货数据
def update_all_futures_data1():
    try:
        # 获取主力合约
        with update_lock:
            dce_text = ak.match_main_contract(symbol="dce")
            czce_text = ak.match_main_contract(symbol="czce")
            shfe_text = ak.match_main_contract(symbol="shfe")
            gfex_text = ak.match_main_contract(symbol="gfex")
            
            contract_cache['main_contracts'] = {
                'dce': dce_text,
                'czce': czce_text,
                'shfe': shfe_text,
                'gfex': gfex_text
            }
            
            # 直接处理主力合约，移除futures_zh_spot中间步骤
            main_contracts = [dce_text, czce_text, shfe_text, gfex_text]
            print('================')
            print('main_contracts')
            print(main_contracts)
            # 为每个合约获取日线数据并计算布林带
            for exchange_contracts in main_contracts:
                # 将每个交易所的合约字符串按逗号分割为单独的合约代码
                symbols = exchange_contracts.split(',')
                for symbol in symbols:
                    symbol = symbol.strip()  # 去除可能的空格
                    if not symbol:
                        continue
                    
                    try:
                        # 获取日线数据
                        daily_data = ak.futures_zh_daily_sina(symbol=symbol)
                        print('daily_data')
                        print(daily_data)
                        if daily_data.empty:
                            print(f"合约 {symbol} 日线数据为空")
                            continue
                        
                        # 计算布林带
                        df = daily_data.copy()
                        df['MA20'] = df['close'].rolling(window=20).mean()
                        df['STD20'] = df['close'].rolling(window=20).std()
                        df['Upper'] = df['MA20'] + 2 * df['STD20']
                        df['Lower'] = df['MA20'] - 2 * df['STD20']
                        
                        # 处理所有非标准浮点值 (NaN, inf, -inf)
                        import numpy as np
                        df = df.replace([np.nan, np.inf, -np.inf], None)
                        
                        # 缓存布林带数据
                        # boll_data_cache[symbol] = df[['date', 'close', 'MA20', 'Upper', 'Lower']].to_dict('records')
                        
                        # 缓存布林带数据（保留所有字段）
                        boll_data_cache[symbol] = df.to_dict('records')
                        print(f"成功更新合约 {symbol} 的布林带数据")
                    except Exception as e:
                        print(f"处理合约 {symbol} 失败: {str(e)}")
        # print(boll_data_cache)
    
    except Exception as e:
        print(f"更新全部数据失败: {str(e)}")
        raise


def update_all_futures_data2():
    try:
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
            
            print('================')
            print('main_contracts')
            print(main_contracts)
            contract_cache['main_contracts'] = main_contracts
            
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
                        
                        if 'close' not in daily_data.columns:
                            print(f"合约 {symbol} 数据格式异常，缺少close列")
                            print(daily_data.columns)  # 打印列名用于调试
                            continue
                        
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
    
    except Exception as e:
        print(f"更新全部数据失败: {str(e)}")
        raise


def update_all_futures_data3():
    try:
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
            # 将所有合约拼接成字符串, 获取最新数据
            # 使用的方法为ak.futures_zh_spot(symbol='这里是拼接的字符串', market="CF", adjust='0')
            # 补全这里
            
            
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


def update_all_futures_data4():
    try:
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
            
            # 将所有合约拼接成字符串，获取最新数据
            all_symbols = []
            for exchange, contracts in main_contracts.items():
                symbols = [s.strip() for s in contracts.split(',') if s.strip()]
                all_symbols.extend(symbols)
            
            # 拼接为逗号分隔的字符串
            symbols_str = ','.join(all_symbols)
            
            try:
                # 获取实时行情数据
                spot_data = ak.futures_zh_spot(symbol=symbols_str, market="CF", adjust='0')
                
                if spot_data is None or spot_data.empty:
                    print("获取期货实时行情数据失败，返回空值")
                else:
                    # 缓存实时行情数据，用于后续处理
                    contract_cache['spot_data'] = spot_data.to_dict('records')
                    print(f"成功获取{len(all_symbols)}个合约的实时行情数据")
                    
                    # 可以在这里添加更多实时数据处理逻辑
                    # 例如，提取settls字段用于后续的排序计算
            
            except Exception as e:
                print(f"获取期货实时行情数据失败: {str(e)}")
            
            # 处理每个交易所的主力合约
            for exchange, exchange_contracts in main_contracts.items():
                symbols = exchange_contracts.split(',')
                for symbol in symbols:
                    symbol = symbol.strip()
                    if not symbol:
                        continue
                    
                    try:
                        # 获取日线数据 - 添加验证
                        print(f"正在获取合约 {symbol} 的日线数据...")
                        daily_data = ak.futures_zh_daily_sina(symbol=symbol)
                        
                        # 验证数据有效性
                        if daily_data is None or daily_data.empty:
                            print(f"合约 {symbol} 日线数据为空")
                            continue
                        
                        # 打印数据基本信息用于调试
                        print(
                            f"合约 {symbol} 日线数据获取成功，行数: {len(daily_data)}, 列数: {len(daily_data.columns)}")
                        
                        # 检查必要列是否存在
                        required_columns = ['close']
                        for col in required_columns:
                            if col not in daily_data.columns:
                                print(f"合约 {symbol} 数据格式异常，缺少{col}列")
                                print(f"实际列名: {list(daily_data.columns)}")
                                print(f"数据内容示例: {daily_data.head().to_dict()}")
                                continue
                        
                        # 确保有足够的数据点计算布林带
                        if len(daily_data) < 20:
                            print(f"合约 {symbol} 数据行数不足(需要至少20行)，实际行数: {len(daily_data)}")
                            continue
                        
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


def update_all_futures_data5():
    try:
        with update_lock:
            # 获取主力合约 - 添加验证
            exchanges = ['dce', 'czce', 'shfe', 'gfex']
            main_contracts = {}
            
            for exchange in exchanges:
                try:
                    # 添加超时设置，防止请求挂起
                    contract_text = ak.match_main_contract(symbol=exchange)
                    
                    # 验证返回内容是否有效
                    if not contract_text or not isinstance(contract_text, str):
                        print(f"获取{exchange}主力合约失败，返回无效值: {contract_text}")
                        continue
                    
                    # 检查返回内容是否包含有效合约
                    if not any(char.isalnum() for char in contract_text):
                        print(f"获取{exchange}主力合约失败，返回内容不包含有效合约: {contract_text}")
                        continue
                    
                    main_contracts[exchange] = contract_text
                
                except Exception as e:
                    print(f"获取{exchange}主力合约异常: {str(e)}")
                    continue
            
            # 检查是否获取到任何主力合约
            if not main_contracts:
                raise ValueError("未能获取到任何交易所的主力合约")
            
            contract_cache['main_contracts'] = main_contracts
            
            # 处理每个交易所的主力合约
            for exchange, exchange_contracts in main_contracts.items():
                symbols = exchange_contracts.split(',')
                for symbol in symbols:
                    symbol = symbol.strip()
                    if not symbol:
                        continue
                    
                    try:
                        # 获取日线数据 - 添加验证
                        print(f"正在获取合约 {symbol} 的日线数据...")
                        daily_data = ak.futures_zh_daily_sina(symbol=symbol)
                        
                        # 验证数据有效性
                        if daily_data is None or daily_data.empty:
                            print(f"合约 {symbol} 日线数据为空")
                            continue
                        
                        # 打印数据基本信息用于调试
                        print(
                            f"合约 {symbol} 日线数据获取成功，行数: {len(daily_data)}, 列数: {len(daily_data.columns)}")
                        
                        # 检查必要列是否存在
                        required_columns = ['close']
                        for col in required_columns:
                            if col not in daily_data.columns:
                                print(f"合约 {symbol} 数据格式异常，缺少{col}列")
                                print(f"实际列名: {list(daily_data.columns)}")
                                print(f"数据内容示例: {daily_data.head().to_dict()}")
                                continue
                        
                        # 确保有足够的数据点计算布林带
                        if len(daily_data) < 20:
                            print(f"合约 {symbol} 数据行数不足(需要至少20行)，实际行数: {len(daily_data)}")
                            continue
                        
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
        # 打印完整的堆栈信息
        import traceback
        print(traceback.format_exc())
        raise
    
def update_all_futures_data():
    try:
        with update_lock:
            # 获取主力合约 - 添加验证
            exchanges = ['dce', 'czce','shfe', 'gfex']
            main_contracts = {}
            
            for exchange in exchanges:
                
                try:
                    # 添加超时设置，防止请求挂起
                    contract_text = ak.match_main_contract(symbol=exchange)
                    
                    # 验证返回内容是否有效
                    if not contract_text or not isinstance(contract_text, str):
                        print(f"获取{exchange}主力合约失败，返回无效值: {contract_text}")
                        continue
                    
                    # 检查返回内容是否包含有效合约
                    if not any(char.isalnum() for char in contract_text):
                        print(f"获取{exchange}主力合约失败，返回内容不包含有效合约: {contract_text}")
                        continue
                    
                    main_contracts[exchange] = contract_text
                
                except Exception as e:
                    print(f"获取{exchange}主力合约异常: {str(e)}")
                    continue
            # 检查是否获取到任何主力合约
            if not main_contracts:
                raise ValueError("未能获取到任何交易所的主力合约")
            
            contract_cache['main_contracts'] = main_contracts
            
            print(main_contracts)
            
            # 将main_contracts里面的值拼成新的字符串
            
            # 拼接所有合约代码
            all_symbols = []
            
            for exchange, exchange_contracts in main_contracts.items():
                print('exchange_contracts:' , exchange_contracts)
                all_symbols.append(exchange_contracts)
                
                

            # 打印所有合约代码
            print('all_symbols:', all_symbols)
            print(','.join(all_symbols))
            # 一次性获取所有主力合约的最新数据
            try:
                spot_data = ak.futures_zh_spot(symbol=','.join(all_symbols), market="CF", adjust='0')
                
                if spot_data is None or spot_data.empty:
                    print("获取期货实时行情数据失败，返回空值")
                else:
                    # 缓存实时行情数据，用于后续处理
                    contract_cache['spot_data'] = spot_data.to_dict('records')
                    print('spot_data:', spot_data)
                    print('contract_cache:', contract_cache)
                    # 打印spot_data的所有表头
                    print('spot_data的所有表头:', spot_data.columns)
                    print(f"成功获取{len(all_symbols)}个合约的实时行情数据")

                    # 可以在这里添加更多实时数据处理逻辑
                    # 例如，提取settls字段用于后续的排序计算
            except Exception as e:
                print(f"获取期货实时行情数据失败: {str(e)}")
                
            # 处理每个交易所的主力合约
            for exchange, exchange_contracts in main_contracts.items():
                symbols = exchange_contracts.split(',')
                for symbol in symbols:
                    symbol = symbol.strip()
                    if not symbol:
                        continue
                    
                    try:
                        # 获取日线数据 - 添加验证
                        print(f"正在获取合约 {symbol} 的日线数据...")
                        daily_data = ak.futures_zh_daily_sina(symbol=symbol)
                        
                        # 验证数据有效性
                        if daily_data is None or daily_data.empty:
                            print(f"合约 {symbol} 日线数据为空")
                            continue
                            
                        # 将 contract_cache['spot_data']中对应的数据和daily_data合并
                        if 'spot_data' in contract_cache:
                            spot_data = pd.DataFrame(contract_cache['spot_data'])
                            # 假设 'symbol' 是用于匹配的字段
                            if 'symbol' in spot_data.columns:
                                # 合并数据
                                merged_data = pd.merge(daily_data, spot_data, on='symbol', how='left')
                                # 缓存合并后的数据
                        
                        # 打印数据基本信息用于调试
                        print(
                            f"合约 {symbol} 日线数据获取成功，行数: {len(daily_data)}, 列数: {len(daily_data.columns)}")
                        
                        # 检查必要列是否存在
                        required_columns = ['close']
                        for col in required_columns:
                            if col not in merged_data.columns:
                                print(f"合约 {symbol} 数据格式异常，缺少{col}列")
                                print(f"实际列名: {list(merged_data.columns)}")
                                print(f"数据内容示例: {merged_data.head().to_dict()}")
                                continue
                        
                        # 确保有足够的数据点计算布林带
                        if len(merged_data) < 20:
                            print(f"合约 {symbol} 数据行数不足(需要至少20行)，实际行数: {len(daily_data)}")
                            continue
                        
                        # 计算布林带
                        df = merged_data.copy()
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
        # 打印完整的堆栈信息
        import traceback
        print(traceback.format_exc())
        raise

@router.get("/future/")
def get_future_list():
    url = "https://vip.stock.finance.sina.com.cn/quotes_service/view/js/qihuohangqing.js?20241116"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.text
        
        # 1. 提取 ARRFUTURESNODES 对象数据
        pattern = r'ARRFUTURESNODES\s*=\s*({.*?});'
        match = re.search(pattern, data, re.DOTALL)
        if not match:
            return {"error": "无法解析期货数据"}
        
        js_data = match.group(1)
        
        # 2. 清理 JavaScript 语法，转换为 JSON 格式
        # 移除注释
        js_data = re.sub(r'//.*?\n', '', js_data, flags=re.DOTALL)
        # 处理键名（添加引号）
        js_data = re.sub(r'(\w+)\s*:', r'"\1":', js_data)
        # 处理数组中的单引号为双引号
        js_data = re.sub(r"'([^']+)'", r'"\1"', js_data)
        
        # 新增：移除对象和数组中的尾随逗号
        js_data = re.sub(r',(\s*[}\]])', r'\1', js_data)
        
        # 3. 解析为 Python 对象
        futures_data = json.loads(js_data)
        
        # 4. 整理数据结构（可选）
        formatted_data = []
        for exchange_code, exchange_info in futures_data.items():
            exchange_name = exchange_info[0]
            for product in exchange_info[1:]:
                product_name = product[0]
                product_code = product[1]
                formatted_data.append({
                    "exchange_code": exchange_code,
                    "exchange_name": exchange_name,
                    "product_name": product_name,
                    "product_code": product_code
                })
        
        return {"data": formatted_data, "raw_data": futures_data}
    
    except requests.RequestException as e:
        return {"error": f"请求出错: {str(e)}"}
    except json.JSONDecodeError as e:
        # 打印详细错误信息（调试用）
        print(f"JSON 解析失败: {e}")
        print(f"错误位置: 第 {e.lineno} 行, 第 {e.colno} 列")
        print(f"错误片段: {js_data[e.pos - 50:e.pos + 50]}")
        return {"error": f"数据解析失败: {str(e)}"}
    
@router.post('/future/all_boll')
async def get_future_all_boll():
    # 检查数据是否已初始化
    if not boll_data_cache:
        # 如果数据还没有初始化，手动触发一次更新
        try:
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(None, update_all_futures_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"数据初始化失败: {str(e)}")
        
    # 提取每组数据的最后一项（最新数据点）
    latest_data = {}
    for symbol, data in boll_data_cache.items():
        if data:  # 确保数据不为空
            latest_data[symbol] = data[-1]  # 获取最后一项
    
    return {
        'data': latest_data,
        'last_update_time': last_update_time.strftime("%Y-%m-%d %H:%M:%S") if last_update_time else None
    }
    
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
    #     # return { 'data': futures_zh_spot_df }
    # # 根据futures_zh_spot_df里面的symbol通过ak.futures_zh_daily_sina获取行情数据,
    
        
    


future_router = router

# get_future_all_boll()