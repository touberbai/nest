def find_best_quantities(price_a, price_b):
    best_diff = float('inf')
    best_a = 0
    best_b = 0
    
    for a in range(1, 11):
        for b in range(1, 11):
            total_a = a * price_a
            total_b = b * price_b
            diff = abs(total_a - total_b)
            
            if diff < best_diff or (diff == best_diff and (a + b) > (best_a + best_b)):
                best_diff = diff
                best_a = a
                best_b = b
    
    return best_a, best_b


# 获取用户输入
try:
    price_a = float(input("请输入A的价格: "))
    price_b = float(input("请输入B的价格: "))
    
    if price_a <= 0 or price_b <= 0:
        print("价格必须为正数!")
    else:
        quantity_a, quantity_b = find_best_quantities(price_a, price_b)
        print(f"购买A的数量: {quantity_a}, 购买B的数量: {quantity_b}")
        print(f"A的总价: {quantity_a * price_a:.2f}, B的总价: {quantity_b * price_b:.2f}")
        print(f"总价差值: {abs(quantity_a * price_a - quantity_b * price_b):.2f}")
except ValueError:
    print("输入无效，请输入有效的数字!")
    


find_best_quantities(1,1)