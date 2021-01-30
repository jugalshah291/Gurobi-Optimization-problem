#Ref:https://www.youtube.com/watch?v=6Kb22Rebx9g&t=1s
import gurobipy as gp
from gurobipy import *

try:
    D=['Doctor4','Doctor5']
    P=['Patient1','Patient2']
    
    combinations,hr=multidict({
    ('Doctor4','Patient1'):130,
    ('Doctor4','Patient2'):95,
    ('Doctor5','Patient1'):118,
    ('Doctor5','Patient2'):83
    })
    
    m = Model('few-doctors')
    
    # Add variables
    x=m.addVars(combinations,name='map')

    #doctor constraints
    doctor=m.addConstrs((x.sum(d,'*')==1 for d in D),'doctor')
    
    #patient constraints
    patients=m.addConstrs((x.sum('*',p)==1 for p in P),'patient')
    
    
    # Set objective function
    m.setObjective(x.prod(hr),GRB.MINIMIZE)
    # Add constraints

    # Solve model
    m.optimize()
    
    for v in m.getVars():
        print('%s %g'%(v.varName,v.x))
    
    print('obj: %g'% m.objVal)
    
 
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
