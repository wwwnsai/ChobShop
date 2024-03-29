import persistent
import datetime
import BTrees.OOBTree

class Product(persistent.Persistent):
    def __init__(self, name, price, description, category, stock) -> None:
        self.name = name
        self.price = price
        self.description = description
        self.category = category
        self.stock = stock
        self.sold = 0
        self.reviews = BTrees.OOBTree.BTree()

    def add_review(self, review):
        self.reviews[datetime.datetime.now()] = review

    def toJSON(self):
        return {
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "category": self.category,
            "stock": self.stock,
            "sold": self.sold,
            "reviews": self.reviews
        }
    
    def __str__(self) -> str:
        return f"name: {self.name}, price: {self.price}, description: {self.description}, category: {self.category}, stock: {self.stock}, sold: {self.sold}, reviews: {self.reviews}"
    
class Cart(persistent.Persistent):
    def __init__(self, products) -> None:
        self.products = products
        self.total = len(products)

    def add_product(self, product):
        self.products.append(product)
        self.total += 1

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            self.total -= 1

    def toJSON(self):
        return {
            "products": self.products,
            "total": self.total
        }
    
    def __str__(self) -> str:
        return f"products: {self.products}, total: {self.total}"


class GeneralUser(persistent.Persistent):
    def __init__(self, username, email, password) -> None:
        self.username = username
        self.email = email
        self.password = password
        self.gender = None
        self.name = None
        self.lastname = None
        self.address = None
        self.birthday = None
        self.phone = None
        self.admin = False

    def toJSON(self):
        return {
            "username": self.username,
            "email": self.email,
            "name": self.name,
            "lastname": self.lastname,
            "address": self.address,
            "birthday": self.birthday,
            "phone": self.phone,
            "admin": self.admin
        }
    
    def __str__(self) -> str:
        return f"username: {self.username}, email: {self.email}, name: {self.name}, lastname: {self.lastname}, address: {self.address}, birthday: {self.birthday}, phone: {self.phone}, admin: {self.admin}"

class Admin(GeneralUser):
    def __init__(self, username, shopname, name, lastname, description, address, email, phone, password) -> None:
        super().__init__(username, email, password)
        self.shopname = shopname
        self.name = name
        self.lastname = lastname
        self.description = description
        self.address = address
        self.phone = phone
        self.admin = True

    def toJSON(self):
        return {
            "username": self.username,
            "shopname": self.shopname,
            "name": self.name,
            "lastname": self.lastname,
            "description": self.description,
            "address": self.address,
            "phone": self.phone,
            "admin": self.admin
        }
    
    def __str__(self) -> str:
        return super().__str__()
    
class Customer(GeneralUser):
    def __init__(self, username, email, password) -> None:
        super().__init__(username, email, password)
        self.cart = BTrees.OOBTree.BTree()
        self.orders = BTrees.OOBTree.BTree()
        self.reviews = BTrees.OOBTree.BTree()
        self.admin = False

    def add_to_cart(self, product, quantity):
        if product in self.cart:
            self.cart[product] += quantity
        else:
            self.cart[product] = quantity

    def remove_from_cart(self, product, quantity):
        if product in self.cart:
            if self.cart[product] > quantity:
                self.cart[product] -= quantity
            else:
                del self.cart[product]

    def add_to_wishlist(self, product):
        self.wishlist[product] = datetime.datetime.now()

    def remove_from_wishlist(self, product):
        if product in self.wishlist:
            del self.wishlist[product]

    def add_review(self, product, review):
        self.reviews[product] = review

    def add_order(self, order):
        self.orders[order] = datetime.datetime.now()

    def toJSON(self):
        return {
            "username": self.username,
            "email": self.email,
            "name": self.name,
            "lastname": self.lastname,
            "address": self.address,
            "phone": self.phone,
            "admin": self.admin,
            "cart": self.cart,
            "orders": self.orders,
        }
    
    def __str__(self) -> str:
        return f"username: {self.username}, email: {self.email}, name: {self.name}, lastname: {self.lastname}, address: {self.address}, phone: {self.phone}, admin: {self.admin},cart: {self.cart}, orders: {self.orders}"

class LoggedInUser(persistent.Persistent):
    def __init__(self, user=None) -> None:
        self.user = user
        self.logged_in = False

    def toJSON(self):
        return {
            "user": self.user,
            "logged_in": self.logged_in
        }
    
    def __str__(self) -> str:
        return f"user: {self.user}, logged_in: {self.logged_in}"

class Order(persistent.Persistent):
    def __init__(self, products, total) -> None:
        self.products = products
        self.total = total
        self.status = "Processing"
        self.date = datetime.datetime.now()

    def cancel_order(self):
        self.status = "Cancelled"

    def ship_order(self):
        self.status = "Shipped"

    def complete_order(self):
        self.status = "Completed"

    def toJSON(self):
        return {
            "products": self.products,
            "total": self.total,
            "status": self.status,
            "date": self.date
        }
    
    def __str__(self) -> str:
        return f"products: {self.products}, total: {self.total}, status: {self.status}, date: {self.date}"
    
class Category(persistent.Persistent):
    def __init__(self, product, category) -> None:
        self.category = category
        self.product = product

    def toJSON(self):
        return {
            "product": self.product,
            "category": self.category
        }
    
    def __str__(self) -> str:
        return f"product: {self.product}, category: {self.category}"
    