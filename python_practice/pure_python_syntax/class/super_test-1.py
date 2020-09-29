class father():     # Parent
    def handsome(self):
        print("Father is handsome!")

class brother(father):  # brother inherits father
    ''' Son '''

class sister(father):   # sister inherits father
    def pretty(self):
        print("Sister is pretty!")

    def handsome(self):
        super().handsome()  # Inherited
        print("Sister is handsome!")

bro = brother()
bro.handsome()

sis = sister()
sis.handsome()
sis.pretty()
