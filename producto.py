class Product:
    def __init__(self, name, price, category, idProduct) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.idP = idProduct

    def update_product(self, percent_change, is_increased):
        if(is_increased == True):
            self.price = self.price + (self.price * (percent_change/100))
        else:
            self.price = self.price - (self.price * (percent_change/100))
        return self

    def print_info(self):
        return print(f'producto: {self.name}, precio: {self.price}, categoria: {self.category}')

