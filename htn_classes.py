class Predicate:
    def __init__(self, name='', arity=0, params=[]):
        self.name = name
        self.arity = arity
        self.params = params
    
    def check(self, cond, x):
        return (x in self.params) ^ cond ^ 1
    
    def add(self, x):
        self.params.append(x)
        #print('added', x)
    
    def discard(self, x):
        if x in self.params:
            self.params.remove(x)
            #print('removed', x)
            
        

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


class State:
    def __init__(self, preds=dict()):
        self.preds = preds
        
    def copy(self):
        preds = dict()
        for pred_name in self.preds:
            pred = self.preds[pred_name]
            new_params = [param.copy() for param in pred.params]  
            new_name = pred.name
            new_arity = pred.arity
            new_pred = Predicate(pred.name, pred.arity, new_params)
            preds[pred.name] = new_pred
        return State(preds)
        

class method_node:
    def __init__(self, method, args):
        #print(method.name, args, 'method')
        self.method = method
        self.args = args
        self.subtasks = []
        self.consecutive = True
        for subtask in method.subtasks:
            #print(subtask[0].name)
            subtask_args = [args[i] for i in subtask[1]]
            self.subtasks.append(task_node(subtask[0], subtask_args))
            
            
class task_node:
    def __init__(self, task, args):
        #print(task.name, args, 'task')
        self.task = task
        self.args = args
        self.methods = []
        if self.task.primitive:
            self.methods.append(operator_node(task.methods[0], args))
        else:
            for method in task.methods:
                self.methods.append(method_node(method, args))
                
                
class operator_node:
    def __init__(self, operator, args):
        #print(operator.name, args, 'operator')
        self.method = operator
        self.args = args
        
    def apply_changes(self, state):
        #print(self.args, 'changes')
        #print(self.method.name, self.method.effects)
        for effect in self.method.effects:
            if effect[1]:
                state.preds[effect[0].name].add([self.args[i] for i in effect[2]])
            else:
                #print(effect[2], self.args)
                state.preds[effect[0].name].discard([self.args[i] for i in effect[2]])
        #for pred in state.preds:
         #   print(pred, state.preds[pred].params)
        #print()
            

class Problem:
    def __init__(self, name='', d_name='', obj=[], init_state=State(), goals=[]):
        self.name = name
        self.domain_name = d_name
        self.objects = obj
        self.init_state = init_state
        self.goals = goals