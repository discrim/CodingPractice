class Family:
    lastname = 'Kim'    # Class variable
    
    def intro(self):
        print('This is ' + self.lastname + '\'s family.')

print("Family.lastname: ", Family.lastname)

a = Family()
b = Family()

print("a.lastname: ", a.lastname)
print("b.lastname: ", b.lastname)
a.intro()

print("Execute Family.lastname = 'Park'")
Family.lastname = 'Park'

print("a.lastname: ", a.lastname)
print("b.lastname: ", b.lastname)

print("id(Family.lastname): ", id(Family.lastname))
print("id(a.lastname): ", id(a.lastname))
print("id(b.lastname): ", id(b.lastname))
