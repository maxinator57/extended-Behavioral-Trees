class Predicate:
    def __init__(self, name='', arity=0, params=set()):
        self.name = name
        self.arity = arity
        self.params = params
    
    def check(self, cond, x):
        return (x in self.params) ^ cond ^ 1
    
    def discard(self, x):
        self.params.discard(x)
        

class Task:
    def __init__(self, name='', primitive=True, methods=[]):
        self.name = name
        self.primitive = primitive
        self.methods = methods
        
    
class Method:
    def __init__(self, name='', taskname='', taskparams=[], preconds=[], subtasks=[]):
        self.name = name
        self.taskname = taskname
        self.taskparams = taskparams
        self.preconds = preconds
        self.subtasks = subtasks


class Operator:
    def __init__(self, name='', taskname='', taskparams=[], preconds=[], effects=[]):
        self.name = name
        self.taskname = taskname
        self.taskparams = taskparams
        self.preconds = preconds
        self.effects = effects


class Domain:
    def __init__(self, name='', preds=dict(), tasks=dict()):
        self.name = name
        self.preds = preds
        self.tasks = tasks


class Problem:
    def __init__(self, name='', obj=[], start=[], goal=[]):
        self.name = name
        self.obj = obj
        self.start = start
        self.goal = goal