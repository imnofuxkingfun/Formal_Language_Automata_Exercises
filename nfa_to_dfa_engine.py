"""
States-become the combinatie of each state with the others, plus null one
we determine start and accept:
start -> reacheable from S by travelling across empty arrows, and S itself
any that contain F will become F

we determine the transitions: cominations! :v
->nu merge nimic in el, si nu e nici S, se sterge
"""
import itertools


#verificare daca tranzitiile sunt corecte
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

#afisare stare pt verificare                 
def afisare_stare(sigma, states, transitions, Sstate, Fstate):
    print("Sigma:",sigma)
    print("States", states, f"start = {Sstate}, final = {Fstate}")
    print("Transitions:", transitions)
     

def nfa_to_dfa(sigma, states, transitions, Sstate, Fstate):
    #starile noi
    newStates=states.copy()
    for i in range(2,len(states)+1):
        combinations = list(itertools.combinations(states,i))
        for i in range(len(combinations)):
            newStates.append(combinations[i])

    newFState=[]
    for state in newStates:
        for finalState in Fstate:
            if finalState == state or finalState in state:
                newFState.append(state)
                
    #starea initiala + epsilon - !!epsilon == E3? maybe
    newSstate = []
    newSstate.append(Sstate)
    s = Sstate
    while s!=-1:
        for i in range(len(transitions[s])):
            if transitions[s][i][0] == 'E3':
                s = transitions[s][i][1]
                newSstate.append(s)
                break
        s=-1
    newSstate = tuple(newSstate)

    #tranzitiile noi
    newTransitions={}
    for stare in newStates:
        if stare not in newTransitions:
            newTransitions[stare] =[]
        #ajunge in starea combinata cu toata starile in care se ajungea
        if type(stare) is tuple:
            for caz in sigma:
                destination = set()
                for st in stare:
                    for trans in transitions[st]:
                        if trans[0] == caz:
                            destination.add(trans[1])
                            aux  = trans[1]
                            for nulltrans in transitions[aux] :
                                if nulltrans[0] == 'E3':
                                    destination.add(nulltrans[1])
                                    aux = nulltrans[1]
                destination = tuple(sorted(destination))
                if destination != ():
                    newTransitions[stare].append([caz,destination])
        else:
            for caz in sigma:
                destination = set()
                for trans in transitions[stare]:
                    if trans[0] == caz:
                        destination.add(trans[1])
                        aux  = trans[1]
                        for nulltrans in transitions[aux] :
                            if nulltrans[0] == 'E3':
                                destination.add(nulltrans[1])
                                aux = nulltrans[1]

                destination = tuple(sorted(destination))
                if destination != ():
                    newTransitions[stare].append([caz,destination])
    
    #stergem tranzitiile cu epsilon
    for state in newStates:
        for trans in newTransitions[state]:
            if trans[0] == 'E3':
                newTransitions[state].remove(trans)
    sigma.remove('E3')

    #de facut -> stare noua, nula, cand o stare nu are un caz sigma
    for state in newStates:
        usedsigma=[]
        for trans in newTransitions[state]:
            usedsigma.append(trans[0])
        for caz in sigma:
            if caz not in usedsigma:
                newTransitions[state].append([caz,'null']) 
            
    newTransitions['null'] =[]
    for caz in sigma:
        newTransitions['null'].append([caz,'null'])
    newStates.append('null')
    
    #stergem starile in care nu ajunge nimic
    
    
    usedStates=[]
    usedStates.append(newSstate)
    for state in newStates:
        if state!='null':
            for trans in newTransitions[state]:
                usedStates.append(trans[1])
    usedStates=set(usedStates)
    usedStates = tuple(usedStates)

    newStatesCopy = newStates.copy()
    for state in newStatesCopy:
        if state!='null':
            copystate = tuple(state)
            if copystate not in usedStates :
                del newTransitions[state]
                newStates.remove(state)
                if state in newFState:
                    newFState.remove(state)
    
    return newStates, newTransitions, newSstate, newFState

#reject // accept  
def verf_stare(secv,sigma,states,transitions,Sstate,Fstate):
        
    state = Sstate

    for i in range(len(secv)):
        element = secv[i]
        if element not in sigma:
            return "Reject"
        
        for trans_state in transitions[state]:
            if trans_state[0] == element:
                state = trans_state[1]
                if len(state) == 1:
                    state = state[0]

    if state in Fstate:
        return "Accept"
    else:
        return "Reject"

sigma =[]
states =[]
transitions ={}
Fstate = []
file_name=r"C:\Users\ioana\OneDrive\Documents\FMI\LFA\INPUTS\nfa_simple_config.txt"
Sstate = constr_stare(sigma, states, transitions, Fstate, file_name)


afisare_stare(sigma, states, transitions, Sstate, Fstate)
print()
states,transitions,Sstate,Fstate=nfa_to_dfa(sigma, states, transitions, Sstate, Fstate)
afisare_stare(sigma,states,transitions, Sstate, Fstate)
print()
print(verf_stare("bba",sigma,states,transitions,Sstate,Fstate))