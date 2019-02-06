class Object:
    def __init__(self, name):
        self.name = name

class Predicate:
    def __init__(self, name='', arity=0, params=set()):
        self.name = name
        self.arity = arity
        self.params = params
    
    def check(self, cond, x):
        return (x in self.params) ^ cond ^ 1
    
    def discard(self, x):
        self.params.discard(x)
        
    
class Action:
    def __init__(self, name='', preconds=[], effects=[]):
        self.name = name
        self.preconds = preconds
        self.effects = effects
    

class Domain:
    def __init__(self, name='', preds=dict(), acts=[]):
        self.name = name
        self.preds = preds
        self.acts = acts


class Problem:
    def __init__(self, name='', obj=[], start=[], goal=[]):
        self.name = name
        self.obj = obj
        self.start = start
        self.goal = goal