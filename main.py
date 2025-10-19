from models import Car, Customer, Order, Shop

# mashina do'kon yaratamiz
shop = Shop("My Car Shop")

# mashinalar
bmw_m3_g80 = Car("bmw_m3_g80", 120_000_000, 5)
bmw_m5_f90 = Car("bmw_m5_f90", 150_000_000, 3)
bmw_x7 = Car("bmw_x7", 200_000_000, 2)

# mijoz
user = Customer("inomarka_haydam", 300_000_000)

# buyurtma
order = Order(user)

order.add_item(bmw_m3_g80, 7)  
order.add_item(bmw_m5_f90, 1)
order.add_item(bmw_x7, 1)

# umumiy narxni chiqaramiz
print("Umumiy narx: ", order.calculate_total())

order.complete_order()
