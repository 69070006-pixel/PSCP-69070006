"""billtax"""
price = int(input())
case1 = (price + 50) * 1.07
case2 = ((price * 0.1) + price) * 1.07
case3 = (price + 1000) * 1.07
if price <= 500:
    print(f'{case1:.2f}')
elif  500 < price <= 10000:
    print(f'{case2:.2f}')
elif price > 10000:
    print(f'{case3:.2f}')
