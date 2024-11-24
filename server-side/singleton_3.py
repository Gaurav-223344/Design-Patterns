"""
Pattern name - SingleTon
Pattern type - Creational Design Pattern
"""


# Solution - 3
class SingletonDecorator(object):
    def __init__(self, klass):
        self.klass = klass
        self.instance = None
        
    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.klass(*args,**kwargs)
        return self.instance

# to use for every classes of an application
class StandardSingletonDecorator(object):
    def __init__(self, klass):
        self.klass = klass
        self.instances = {}
        
    def __call__(self, *args, **kwargs):
        if self.klass not in self.instances:
            self.instances[self.klass] = self.klass(*args,**kwargs)
        return self.instances[self.klass]


@StandardSingletonDecorator
class Logger(object):
    def __init__(self):
        self.start = None

    def write(self, message):
        if self.start:
            print(self.start, message)
        else:
            print(message)

if __name__ == "__main__":
    logger1 = Logger()
    logger1.start = "# >"
    print("Logger 1", logger1)
    logger1.write("Logger1 object is created.")

    logger2 = Logger()
    logger2.start = "$ >"
    print("Logger 2", logger2)
    logger1.write("Logger2 object is created.")
    
    print("logger1.start ", logger1.start )
    