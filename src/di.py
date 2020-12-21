from injector import Injector,Module, singleton, provider
# from models.demo import Model
from controllers.main_ctl import Controller
from models.test_model import Model

class AppModule(Module):
    def __init__(self, event_loop, tk):
        self.__event_loop = event_loop
        self.__tk = tk


    @singleton
    @provider
    def provide_controller(self, model: Model) -> Controller:
        return Controller(self.__tk, model)

    @singleton
    @provider
    def provide_module(self) -> Model:
        return Model(self.__event_loop)

def get_controller(event_loop, tk):
    injector = Injector(AppModule(event_loop, tk))
    ctl = injector.get(Controller)
    return ctl