#clasa in care ne construim un nod pentru arborele nostru
#campul data va contine un string ce reprezinta formula la momentul respectiv
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    #inserare a unui element in campul data
    def insertFormulae(self, currForm):
        clauses = []
        for clause in currForm:
            clauses.append("(" + "V".join(clause) + ")")
        self.data = "^".join(clauses)

#functie care verifica un nod terminal; aici se vede daca interpretarea este
#buna sau nu
def terminalNode(tree, formulae, value):
    for clause in formulae:
        if clause[0][0] == "~":
            if value == True:
                tree.right = Node(False)
                return 0
        else:
            if value == False:
                tree.left = Node(False)
                return 0
    if value == True:
        tree.right = Node(True)
    else:
        tree.left = Node(True)
    return 1

# functie principala, recursiva, care formeaza arborele bdd, si decide
# satisfiabilitatea formulei
# nivelul reprezinta totodata numarul de ordine al variabilei curente (pe nivelul
# 3 se afla variabila 3 sau ~3, de exp)
def bddTree(tree, formulae, level, value, nrVariables):
    currVariable = str(level)
    if level == nrVariables:
        return terminalNode(tree, formulae, value)
    i = 0
    currentFormulae = [x[:] for x in formulae]
    # daca suntem pe ramura din stanga al subarborelui curent, verificam formula
    # pentru respectiva variabila
    if value == False:
        while i < len(currentFormulae):
            literals = currentFormulae[i]
            if literals[0][0] == "~" and literals[0][1:] == currVariable:
                currentFormulae.pop(i)
                continue
            elif literals[0] == currVariable:
                if len(literals) == 1:
                    tree.left = Node(False)
                    return 0
                literals.pop(0)
                currentFormulae[i] = literals
                if len(literals) == 0:
                    currentFormulae.pop(i)
                    continue
            i += 1
    # daca suntem pe ramura din dreapta al subarborelui curent, verificam formula
    # pentru respectiva variabila
    else:
        while i < len(currentFormulae):
            literals = currentFormulae[i]
            if literals[0][0] == "~" and literals[0][1:] == currVariable:
                if len(literals) == 1:
                    tree.right = Node(False)
                    return 0
                literals.pop(0)
                currentFormulae[i] = literals
                if len(literals) == 0:
                    currentFormulae.pop(i)
                    continue
            elif literals[0] == currVariable:
                currentFormulae.pop(i)
                continue
            i += 1
    # construire nod stanga si apel pentru construire ramura stanga
    tree.left = Node([])
    tree.left.insertFormulae(currentFormulae)
    result = bddTree(tree.left, currentFormulae, level + 1, False, nrVariables)
    if result == 1:
        return 1
    # construire nod dreapta si apel pentru construire ramura dreapta
    tree.right = Node([])
    tree.right.insertFormulae(currentFormulae)
    result = bddTree(tree.right, currentFormulae, level + 1, True, nrVariables)
    if result == 1:
        return 1
    return 0

def main():
    clauses = input().split("^")
    formulae = []
    nrVariables = 0

    # obtinerea unei liste de clauze; o clauza este doar o lista de literali
    for clause in clauses:
        literals = clause.split("V")
        literals[0] = literals[0][1:]
        lastLiteral = literals[len(literals) - 1]
        lastLiteral = lastLiteral[:len(lastLiteral) - 1]
        literals[len(literals) - 1] = lastLiteral
        formulae.append(literals)
        if nrVariables < len(literals):
            nrVariables = len(literals)

    tree = Node("^".join(clauses))
    result1 = bddTree(tree, formulae, 1, False, nrVariables)
    #resultat: 1 pentru satisfiabil, 0 altfel
    if result1 == 0:
        result2 = bddTree(tree, formulae, 1, True, nrVariables)
        print(result2)
    else:
        print(result1)
    
if __name__ == "__main__":
    main()