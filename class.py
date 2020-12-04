# Класс описание продукта 
class Title:
    def __init__(self, title):
        if Title.check_title(title):
            self.__title = title
        else:
            raise ValueError

    @staticmethod 
    def check_title(title):
        if title:
            return True
        else:
            return False

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if Title.check_title(title):
            self.__title = title
        else:
            raise ValueError

# Класс описание ингредиента. 
class Product(Title):
    def __init__(self, title, calories, cost):
        if Product.check_calories(calories) and Product.check_cost(cost):
            super().__init__(title)
            self.__calories = calories
            self.__cost = cost
        else:
            raise ValueError

    @staticmethod
    def check_calories(calories):
        if calories > 0:
            return True
        else:
            return False

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, ccalories):
        if Product.check_calories(calories):
            self.__calories = calories
        else:
            raise ValueError
    
    @staticmethod
    def check_cost(cost):
        if cost > 0:
            return True
        else:
            return False
    @property
    def cost(self):
        return self.__cost
    @cost.setter
    def cost(self, cost):
        if Product.check_cost(cost):
            self.__cost = cost
        else:
            raise ValueError


class Ingredient:
    def __init__(self, product, weight):
        if Ingredient.check_weight(weight):
            self.product = product
            self.weight = weight
        else:
            raise ValueError

    def get_calories(self):
        return self.weight / 100 * self.product.calories
    def get_selfcost(self):
        return self.weight / 100 * self.product.cost
    
    @staticmethod
    def check_weight(weight):
        if weight and weight > 0:
            return True
        else:
            return False
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight):
        if Ingredient.check_weight(weight):
            self.__weight = weight
        else:
            raise ValueError

# Класс создание пиццы
class Pizza(Title):
    def __init__(self, title, ingredients):
        super().__init__(title)
        self.ingredients = ingredients
    
    def get_calories(self):
        all_calories = 0
        for ingredient in self.ingredients:
            all_calories += ingredient.get_calories()
        return all_calories
    
    def get_selfcost(self):
        all_selfcost = 0
        for ingredient in self.ingredients:
            all_selfcost += ingredient.get_selfcost()
        return all_selfcost
    
    def __str__(self):
        super().__str__()
        return f"{self.title} ({self.get_calories()} kkal) - {self.get_selfcost()} руб"


# Создаем продукты с указанием названия, калорийности продукта и его себестоимости
dough_product = Product('Тесто', 200, 20)
tomato_product = Product('Помидор', 100, 50)
cheese_product = Product('Сыр', 100, 120)

# Из продуктов создаем ингредиенты. Для каждого ингредиента указываем продукт, 
# из которого он состоит и вес продукта
dough_ingredient = Ingredient(dough_product, 300)
tomato_ingredient = Ingredient(tomato_product, 100)
cheese_ingredient = Ingredient(cheese_product, 150)

# Из ингредиентов создаем пиццу
pizza_margarita = Pizza('Маргарита', [dough_ingredient, tomato_ingredient, cheese_ingredient])
pizza_chessy = Pizza('Сырная',[ dough_ingredient, tomato_ingredient, cheese_ingredient, cheese_ingredient])
# Выводим экземпляр пиццы
print(pizza_margarita)
print(pizza_chessy)