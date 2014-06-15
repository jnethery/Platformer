__author__ = 'josiah'
import importlib

class Trigger():

    def __init__(self, trig_method, res_method, trig_params = None, res_params = None):
        self.trig_method = trig_method
        self.res_method = res_method
        self.trig_params = trig_params
        self.res_params = res_params

    def call_trigger(self):
        trig_method = self.get_method(self.trig_method)
        res_method = self.get_method(self.res_method)

        triggered = False
        if self.trig_params is not None:
            triggered = trig_method(self.trig_params)
        else:
            triggered = trig_method()
        if triggered:
            if self.res_params is not None:
                res_method(self.res_params)
            else:
                res_method()

    def get_method(self, method_name):
        components = method_name.split('.')
        module = '.'.join(components[:len(components) - 1])
        module = importlib.import_module(module)
        method = components[len(components) - 1]
        return getattr(module, method)
