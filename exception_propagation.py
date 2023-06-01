class TryExec:

    def func1(self):
        try:
            self.func2()
        except ZeroDivisionError:
            print('The occurrence of an error in the method func1')
        print('Regular work of method func1')


    def func2(self):
        try:
            self.func3()
        except ZeroDivisionError:
            print('The occurrence of an error in the method func2')
        print('Regular work of method func2')


    def func3(self):
        try:
            100 / 0
        except ZeroDivisionError:
            print('The occurrence of an error in the method func3')
        print('Regular work of method func3')


some_obj = TryExec()
some_obj.func1()