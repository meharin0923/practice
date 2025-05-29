class gf():
    def fun3(self):
         print("c")
class f(gf):
    def fun1(self):
        print("a")
class s(gf):
    def fun2(self):
        print("b")
class gf(f,s):
    def fun4(self):
        print("girl")
ob=gf()
#ob.fun2()
#ob.fun1()
#ob.fun3()
ob.fun4()

