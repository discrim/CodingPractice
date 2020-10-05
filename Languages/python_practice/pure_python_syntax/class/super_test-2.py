class father():
    def __init__(self, who):
        self.who = who

    def handsome(self):
        print("Handsome because I resemble {}".format(self.who))

class sister(father):
    def __init__(self, who, where):
        super().__init__(who)
        self.where = where

    def choice(self):
        print("I mean {}".format(self.where))

    def handsome(self):
        super().handsome()
        self.choice()

sis = sister("father", "face")
sis.handsome()
