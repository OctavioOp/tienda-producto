from producto import Product


class Shop:

    def __init__(self, name) -> None:
        self.name = name
        self.product_list = []

    def add_product(self, new_product, price, category, idP):
        newProduct = Product(new_product, price, category, idP)
        self.product_list.append(newProduct)
        return self

    def sell_product(self, idPr):
        for i in range(0, len(self.product_list)-1):
            if self.product_list[i].idP == idPr:
                self.product_list.pop(i)
        return self

    def inflation(self, percent_increase):  
        for product in self.product_list:
            product.update_product(percent_increase, True)
        return self

    def set_clearence(self, percent_discount): 
       for product in self.product_list:
           product.update_product(percent_discount, False)
       return self

    def show_products(self):
        for i in range(0, len(self.product_list)):
            print(
                f'los productos de la tienda: {self.product_list[i].name}, {self.product_list[i].price}, {self.product_list[i].category} ')
