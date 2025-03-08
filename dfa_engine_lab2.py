"""
SIGMA alfpabet

states - f final, s starter

dict with transitions
"""

def verf_trans(line,sigma, states, transitions):
    if line[0] in states and line[2] in states and line[1] in sigma: # validation
                if line[0] not in transitions:
                    transitions[line[0]] = []
                transitions[line[0]].append([line[1],line[2]])


def constr_stare(sigma, states, transitions, Fstate,file_name):
    f = open(file_name)
    
    section = "End"
    f = f.read().splitlines()
    for line in f:
        line = line.split()
        

        if line[0]=='End':
            section = "End"
            

        if section == "Sigma":
            sigma.append(line[0])

        if section=="States":
           
            if len(line)==1:
                states.append(line[0])
            else:
                line[0] = line[0][:-1] #ca sa scap de virgula
                s = line[0]
                states.append(s)
                for i in range(1,len(line)): #in caz ca e si F si S
                    if line[i][0] == 'F':
                        Fstate.append(s)
                    if line[i][0] == 'S':
                        Sstate = s
                        
                
        if section == "Transitions":
            line = line[0].split(",")
            if verf_trans(line,sigma, states, transitions) == True:
                if line not in transitions:
                    transitions[line[0]] = []
                transitions[line[0]].append([line[1],line[2]])
                


        if line[0]=='Sigma:':
            section = "Sigma"

        if line[0]=='States:':
            section = "States"

        if line[0]=='Transitions:':
            section = "Transitions"
            

    return Sstate

                    
def afisare_stare(sigma, states, transition, Sstate, Fstate):
    print("Sigma:",sigma)
    print("States", states, f"start = {Sstate}, final = {Fstate}")
    print("Transitions:", transitions)
     
    
def verf_stare(secv,sigma,states,transitions,Sstate,Fstate):
    
    state = Sstate

    for i in range(len(secv)):
        element = secv[i]
        if element not in sigma:
            return "Reject"
        
        for trans_state in transitions[state]:
            if trans_state[0] == element:
                state = trans_state[1]

    if state in Fstate:
        return "Accept"
    else:
        return "Reject"


sigma =[]
states =[]
transitions ={}
Fstate = []
file_name=r"C:\Users\ioana\OneDrive\Documents\FMI\LFA\INPUTS\lab2_configs\1.6_l.txt"
Sstate = constr_stare(sigma, states, transitions, Fstate,file_name)

#afisare_stare(sigma, states, transitions, Sstate, Fstate)

#f=open(r"C:\Users\ioana\OneDrive\Documents\FMI\LFA\dfa_input.txt")
#secv=f.readline()
secv="01001"


validation = verf_stare(secv,sigma,states,transitions,Sstate,Fstate)
print(f"{secv} : {validation} ")




