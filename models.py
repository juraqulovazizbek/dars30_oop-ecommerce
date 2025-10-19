from typing import List

class Car:

    def __init__(self , name: str , price: float , stock: int):
        self.name = name
        self.price = price
        self.stock = stock
    
    def reduce_stock(self , quantity: int)-> None:
        if quantity <= self.stock:
            self.stock -= quantity
        else:
            print(f"{self.name} MY CAR SHOP da bu rusum yetarlicha yo'q. MY CAR SHOP: {self.stock} ta bor!")


class Customer:

    def __init__(self , name:str , balance: float) -> None:
        self.name = name
        self.balance = balance

    def deduct_balance(self , amount: float)-> None:
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f"Balance da yetarlicha pul mavjud emas. Mablag': {self.balance}")


class Item:

    def __init__(self, car: Car, quantity: int) -> None:
        self.car = car               # oldingi xato: self.product
        self.quantity = quantity

        car.reduce_stock(quantity)


class Order:
    
    def __init__(self, customer: Customer) -> None:
        self.customer = customer
        self.items: List[Item] = []

    def add_item(self, car: Car, quantity: int) -> None:
        item = Item(car, quantity)
        self.items.append(item)

    def calculate_total(self) -> float:
        total = 0
        for item in self.items:
            total += item.car.price * item.quantity
        return total
    
    def complete_order(self) -> None:
        self.customer.deduct_balance(self.calculate_total())


class Shop:
    
    def __init__(self , name: str):
        self.name = name
        self.cars: list[Car] = []
        self.customers: list[Customer] = []

    def add_car(self, car: Car) -> None:
        self.cars.append(car)
    
    def add_customer(self, customer: Customer) -> None:
        self.customers.append(customer)
