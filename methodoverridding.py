class MethodOverride(): 
    def fun1(self):
        print("i hate you") 
class Child(MethodOverride):
    def fun2(self):
        print("i love you")
ob=Child() 
ob.fun1() 
ob.fun2()