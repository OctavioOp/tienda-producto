from tienda import Shop
from producto import Product

tiendasPoop = Shop('tienda poop')
tiendasPoop.add_product('Beerfalo 1lt', 1000, 'Delicias',1).add_product('coffeina',5000,'bebestibles magicos',2).add_product('Pastel Sorpresa', 10000,'sorpesa',3).show_products()
##vendemos un productos
print('-----------------------------------------------------------')
#tiendasPoop.sell_product(2).show_products() funciona..
#inflacion en un producto
tiendasPoop.inflation(50).show_products()
print('-----------------------------------------------------------')
tiendasPoop.set_clearence(80).show_products()






