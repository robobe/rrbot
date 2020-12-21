from injector import Injector,Module, singleton, provider

class BusinessLogic:
    def __init__(self, data):
        self.data = data

    def do_stuff(self):
        
        print(f'the api returned a result: {self.data}')

class AppModule(Module):
    def __init__(self, data):
        self.__data = data
    
    @singleton
    @provider
    def provide_business_logic(self) -> BusinessLogic:
        return BusinessLogic(data=self.__data)

if __name__ == '__main__':
    data = "hello di"
    injector = Injector(AppModule(data))
    logic = injector.get(BusinessLogic)
    logic.do_stuff()