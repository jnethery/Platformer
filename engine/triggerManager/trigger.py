__author__ = 'josiah'
import importlib

class Trigger():

    def __init__(self, triggerMethod, resultMethod, triggerParams = None, resultParams = None):
        self.triggerMethod = triggerMethod
        self.resultMethod = resultMethod
        self.triggerParams = triggerParams
        self.resultParams = resultParams

    def callTrigger(self):
        triggerMethod = self.getMethod(self.triggerMethod)
        resultMethod = self.getMethod(self.resultMethod)

        triggered = False
        if self.triggerParams is not None:
            triggered = triggerMethod(self.triggerParams)
        else:
            triggered = triggerMethod()
        if triggered:
            if self.resultParams is not None:
                resultMethod(self.resultParams)
            else:
                resultMethod()

    def getMethod(self, methodName):
        components = methodName.split('.')
        module = '.'.join(components[:len(components) - 1])
        module = importlib.import_module(module)
        method = components[len(components) - 1]
        return getattr(module, method)

def hello():
    print 'hello'

def test():
    return True
