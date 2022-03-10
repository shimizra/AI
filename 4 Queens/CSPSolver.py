'''
 Completed by Shimon Mizrahi 203375563. 
  As you can see after completing the heuristics calculation, I chose to solve(100):
  and it's calculate after a few second, instead of a lot of time. 
'''

import CSProblem
import copy

def solve(n):
    CSProblem.present(backtrack(CSProblem.create(n)))

def backtrack(p):
    var=next_var(p, MRV=True)# MRV-Most constrained variable or Minimum Remaining Values
    if var==None:
        return p
    dom=sorted_domain(p, var, LCV=False)# LCV-least constraining value
    for i in dom:
        bu=copy.deepcopy(p)
        CSProblem.assign_val(bu, var, i)
        propagate_constraints(bu, var)
        bu=backtrack(bu)
        if CSProblem.is_solved(bu):
            return bu
    return p

def sorted_domain(p, var, LCV=True):
    if LCV==False:
        return CSProblem.domain(p,var)
    # influence_list = will be store the count of vars that erased.
    influence_list = []
    # for ecah option in var row at p:
    for item in range(len(p[1][var])):
        influence_list.append([p, var, p[1][var][item]])
    # dictionary = p[1][var][:] (row at p ) is the key, influence_list is the value;
    dictionary = dict(zip(p[1][var][:], influence_list))
    # sort dictionary by value for recive the firsy key => min influence row at p.
    min_var = sorted(dictionary.items(), key=lambda item: item[1])[0][1] 
    return min_var

def num_of_del_vals(l):
#l=[problem, the variable, the val. assigned to the var.]
#returns the num. of vals. erased from vars domains after assigning x to v
    count=0
    for inf_v in CSProblem.list_of_influenced_vars(l[0], l[1]):
        for i in CSProblem.domain(l[0], inf_v):
            if not CSProblem.is_consistent(l[0], l[1], inf_v, l[2], i):
                count+=1
    return count
        
def next_var(p, MRV=True):
#p is the problem
#MRV - Minimum Remained Values
#Returns next var. to assign
#If MRV=True uses MRV heuristics
#If MRV=False returns first non-assigned var.
    v=CSProblem.get_list_of_free_vars(p)
    if MRV==False:
        if v==[]:
            return None
        else:
            return v[0]
    # if v==[] than no next var 
    if v==[]:
            return None
    # max_option = max of option + 1.
    max_option = len(p[0])+1
    # result = to index of minimum option.
    result = 0
    # forech item we serch the minimum option.
    for item in v:
        current = CSProblem.domain_size(p, item)
        # if we find min option.
        if current < max_option:
            # swap.
            max_option = current
            # store the max constrained.
            result = item
    # return max constrained.
    return result
    
           
def propagate_constraints(p, v):
    for i in CSProblem.list_of_influenced_vars(p, v):
        for x in CSProblem.domain(p, i):
            if not CSProblem.is_consistent(p, i, v, x, CSProblem.get_val(p, v)):
                CSProblem.erase_from_domain(p, i, x)
        
    
    
solve(100)


        
