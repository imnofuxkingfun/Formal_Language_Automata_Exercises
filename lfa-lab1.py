
"""
SIGMA alfpabet

states - f final, s starter

dict with transitions

PYTHON NOTEBOOKS
LATEX overleaf.con
"""

def constr_stare():
    f = open(r"C:\Users\ioana\OneDrive\Documents\FMI\LFA\dfa_config.txt")
    global sigma 
    sigma= []
    global states
    states=[]
    global Fstate
    Fstate = []
    global Sstate
    global transitions
    transitions = {}
    ok = 0
    f = f.read().splitlines()
    for line in f:
        line = line.split()
        

        if line[0]=='End':
            ok = 0
            

        if ok==1:
            sigma.append(line[0])

        if ok==2:
            if len(line)==1:
                states.append(line[0])
            else:
                line[0] = line[0][:-1] #ca sa scap de virgula
                s = line[0]
                states.append(s)
                for i in range(1,len(line)): #in caz ca e si F si S
                    if line[i] == 'F':
                        Fstate.append(s)
                    if line[i] == 'S':
                        Sstate = s
                
        if ok == 3:
            line = line[0].split(",")
            if line[0] in states and line[2] in states and line[1] in sigma: # validation
                if line[0] not in transitions:
                    transitions[line[0]] = []
                transitions[line[0]].append([line[1],line[2]])


        if line[0]=='Sigma:':
            ok=1

        if line[0]=='States:':
            ok = 2

        if line[0]=='Transitions:':
            ok = 3
            if len(Fstate)==1:
                Fstate = Fstate[0]


    
constr_stare()

print("Sigma:",sigma)
print("States", states, f"start = {Sstate}, final = {Fstate}")
print("Transitions:", transitions)


