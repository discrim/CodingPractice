class Parent():    
    def sing_once( self ):
        print("LOUD VOICE !")

class Child( Parent ):
    def sing_once( self ):
        print("quite voice ~")
    
    def sing_twice( self ):
        # Want to call both Parent's sing_once and Child's sing_once
        self.sing_once()
        super().sing_once()
        
if __name__ == "__main__":
    p1 = Parent()
    c1 = Child()
    
    print("p1.sing_once(): ")
    p1.sing_once()
    
    print("\nc1.sing_once(): ")
    c1.sing_once()
    
    print("\nc1.sing_twice(): ")
    c1.sing_twice()
