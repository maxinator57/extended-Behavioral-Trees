from htn_classes import *

def eBT_go(opline):
    d = 0
    res = []
    left = opline.copy()
    done = [False] * len(opline)
    for d in range(len(opline)):
        if done[d]:
            continue
        cur_block = [opline[d]]
        for i in range(d + 1, len(opline)):
            if not done[i]:
                ch_order_ok = True
                for j in range(d, i):
                    ch_order_ok = ch_order_ok and swap_check(opline[i],opline[j])
                if ch_order_ok:
                    cur_block.append(opline[i])
                    done[i] = True
        res.append(cur_block)
    return res
                    

def swap_check(a, b):
    op_node_a = a[0].methods[a[1] - 1]
    op_node_b = b[0].methods[b[1] - 1]
    return preconds_ok(a[2], op_node_b) and preconds_ok(b[2], op_node_a) and not pm_intersection(op_node_a, op_node_b)


def preconds_ok(state, op_node):
    res = True
    for precond in op_node.method.preconds:
        args = [op_node.args[i] for i in precond[2]]
        pred = state.preds[precond[0].name]
        res = res and pred.check(precond[1], args)
    return res


def pm_intersection(op_node_a, op_node_b):
    a_plus = []
    a_minus = []
    b_plus = []
    b_minus = []    
    for effect in op_node_a.method.effects:
        if effect[1]:
            a_plus.append([effect[0].name] + [op_node_a.args[i] for i in effect[2]])
        else:
            a_minus.append([effect[0].name] + [op_node_a.args[i] for i in effect[2]])
    for effect in op_node_b.method.effects:
        if effect[1]:
            b_plus.append([effect[0].name] + [op_node_b.args[i] for i in effect[2]])
        else:
            b_minus.append([effect[0].name] + [op_node_b.args[i] for i in effect[2]])
    for a in a_plus:
        for b in b_minus:
            if a == b:
                return False
    for a in a_minus:
        for b in b_plus:
            if a == b:
                return False
    return True