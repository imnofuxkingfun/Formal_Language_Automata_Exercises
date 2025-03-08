
def read_config(f):
    rules = {}
    variables = set()
    terminals = set()
    start_var = None
    ok=1
    
    for line in f:
        line = line.strip("\n")
        if ok == 1:
            if line[0] != '#' and line != "End":
                l = line.split("->")
                if len(l) != 2:
                    ok = 0 

                var = l[0].strip()

                # aici var ar trebui sa fie neaparat doar O litera mare
                if len(var) == 1 or var.isupper() == True:
                    variables.add(var)
                else:
                    ok = 0

                if start_var is None:
                    start_var = var
                
                if var not in rules:
                    rules[var] = []
                
                rules_list = l[1].split("|")
                for r in rules_list:
                    r = r.strip()
                    rules[var].append(r)
                    if r != "epsilon":
                        for t in r:
                            #impartim sirul - va fi ori terminal ori variabila
                            t = t.strip()
                            if t.isupper(): #litera mare -> variabila
                                variables.add(t)
                            else:
                                terminals.add(t)
                    else:
                        terminals.add(r)
            else:
                break
        else:
            break

    return variables, terminals, start_var, rules, ok

def configCFG(file):

    f = open(file)
    variables, terminals, start_var, rules, ok = read_config(f)
        
    if start_var not in variables or start_var is None:
        ok = 0
        
    return variables, terminals,start_var, rules, ok

def show_config(terminals, variables, start_var, rules):
    print("Terminals: ",terminals)
    print("Variables: ",variables)
    print("Start Variable: ", start_var)
    print("Rules: ", rules)

def verf_secv(secv, variables, terminals, start_var, rules):
    for element in secv:
        if element not in terminals:
            return "Reject"
    return "Accept"

filename = r"C:\Users\ioana\OneDrive\Documents\FMI\LFA\INPUTS\lab4_configs\2.4a.txt"
variables, terminals, start_var, rules, ok = configCFG(filename)
if ok==0:
    print("Invalid CFG configuration")
else:
    show_config(terminals, variables, start_var, rules)
    secv="011010"
    print("t",terminals)
    validation = verf_secv(secv, variables, terminals, start_var, rules)
    print(f"{secv} : {validation} ")







    