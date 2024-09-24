from time import time


# Декоратор
class AppRoute:
    def __init__(self, routes, url):
        self.routes = routes
        self.url = url


    def __call__(self, cls):
        self.routes[self.url] = cls()
        print(cls)


# Декоратор
class Debug:
    def __init__(self, name):
        self.name = name

    def __call__(self, cls):
        def timeit(method):
            def timed(*args, **kw):
                ts = time()
                result = method(*args, **kw)
                te = time()
                delta = te - ts
                print(f'debug --> {self.name} method took {delta:2.2f} ms')
                return result

            return timed

        return timeit(cls)


#func()
#obj = MyClass()
#obj()