# Ref https://www.youtube.com/watch?v=6Kb22Rebx9g&t=1s
import gurobipy as gp
from gurobipy import *

try:
    D=['Doctor1','Doctor2','Doctor3','Doctor4','Doctor5','Doctor6']
    P=['Patient1','Patient2','Patient3','Patient4','Patient5','Patient6']
    
    combinations,hr=multidict({
    ('Doctor1','Patient1'):52,
    ('Doctor1','Patient2'):100,
    ('Doctor1','Patient3'):74,
    ('Doctor1','Patient4'):143,
    ('Doctor1','Patient5'):99,
    ('Doctor1','Patient6'):60,
    
    ('Doctor2','Patient1'):150,
    ('Doctor2','Patient2'):76,
    ('Doctor2','Patient3'):122,
    ('Doctor2','Patient4'):66,
    ('Doctor2','Patient5'):96,
    ('Doctor2','Patient6'):90,
    
    ('Doctor3','Patient1'):112,
    ('Doctor3','Patient2'):142,
    ('Doctor3','Patient3'):54,
    ('Doctor3','Patient4'):130,
    ('Doctor3','Patient5'):112,
    ('Doctor3','Patient6'):75,
    
    
    ('Doctor4','Patient1'):130,
    ('Doctor4','Patient2'):95,
    ('Doctor4','Patient3'):150,
    ('Doctor4','Patient4'):112,
    ('Doctor4','Patient5'):88,
    ('Doctor4','Patient6'):50,
    
    
    ('Doctor5','Patient1'):118,
    ('Doctor5','Patient2'):83,
    ('Doctor5','Patient3'):52,
    ('Doctor5','Patient4'):111,
    ('Doctor5','Patient5'):56,
    ('Doctor5','Patient6'):95,
    
    ('Doctor6','Patient1'):144,
    ('Doctor6','Patient2'):90,
    ('Doctor6','Patient3'):72,
    ('Doctor6','Patient4'):102,
    ('Doctor6','Patient5'):55,
    ('Doctor6','Patient6'):100,
     
    
    })
    
    m = Model('all-doctors')
    
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
