# Super calss
class Greet():
    def hello(self):
        print("yaho")

    def bye(self):
        print("goodbye")

# Sub class
class Greet2(Greet):
    # Over write hello method
    def hello(self, name = None):
        if name :
            print(f"Mr./Ms.{name}, Good to see you")
        else:
            super().hello()
            
