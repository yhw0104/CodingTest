shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus.sort()
    
    for i in range(len(orders)):
        if binary_Check(menus, orders[i]) == False:
            print("주문 불가") 
            return False
        
    print("주문 가능")
    return True

def binary_Check(menus, order):
    min_index = 0
    max_index = len(menus) - 1
    half_index = (min_index + max_index) // 2
    while min_index <= max_index:
        if menus[half_index] == order:
            return True
        elif menus[half_index] > order:
            max_index = half_index -1
        else:
            min_index = half_index + 1
        half_index = (min_index + max_index) // 2

    return False

result = is_available_to_order(shop_menus, shop_orders)
print(result)