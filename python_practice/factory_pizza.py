class Pizza:
    MEAT_PIZZA_TYPE = 0
    COMBINATION_PIZZA_TYPE = 1
    SEAFOOD_PIZZA_TYPE = 2
    def __init__( self ):
        self._price = None
    
    def getPrice( self ):
        return self._price

class MeatPizza( Pizza ):
    def __init__( self ):
        self._price = 8.50
    
class CombinationPizza( Pizza ):
    def __init__( self ):
        self._price = 9.50

class SeafoodPizza( Pizza ):
    def __init__( self ):
        self._price = 10.50

class PizzaFactory:
    def createPizza( self, pizza_type ):
        if pizza_type == Pizza.MEAT_PIZZA_TYPE:
            return MeatPizza()
        elif pizza_type == Pizza.COMBINATION_PIZZA_TYPE:
            return CombinationPizza()
        elif pizza_type == Pizza.SEAFOOD_PIZZA_TYPE:
            return SeafoodPizza()
        else:
            print("Unavailable pizza!")

if __name__ == '__main__':
    pizza1 = PizzaFactory().createPizza( 0 )
    #pizza1_price = pizza1.getPrice()
    #print(pizza_price)
    try:
        pizza2 = MeatPizza()
        print( type( pizza2 ) )
        print( pizza2.getPrice() )
    except:
        print("Error 2")
        
    pizza3 = MeatPizza()
    print( pizza3.getPrice() )