class AccessModifier:
    def __init__(self):
        self.public_variable = "Public variable"
        self.__private_variable = "Private variable"
    
    def public_method(self):
        print("Public method")
    
    def __private_method(self):
        print("Private method")
    
    def get_private_variable(self):
        return self.__private_variable

def main():
    instance = AccessModifier()
    instance.public_method()
    try:
        instance.__private_method()
    except:
        print("Error")
    print(instance.get_private_variable())
    try:
        print(instance.__private_variable)
    except:
        print("Error")
        
if __name__ == '__main__':
    main()