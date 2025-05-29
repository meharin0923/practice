class MethodOverride(): 
    def fun1(self):
        print("i love python") 
class Child(MethodOverride):
    def fun1(self):
        super().fun1() 
ob=Child() 
ob.fun1() 