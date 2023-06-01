class TryExec:

    def func1(self):
        self.func2()
        print('Regular work of method func1')


    def func2(self):
        self.func3()
        print('Regular work of method func2')



    def func3(self):
        100 / 0
        print('Regular work of method func3')


some_obj = TryExec()
some_obj.func1()