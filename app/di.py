from injector import Binder, Module
from config import Config

class DIModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(Config, Config())
