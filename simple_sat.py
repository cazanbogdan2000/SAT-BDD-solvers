import itertools

#functie care creeaza in parametrul satMatrix matricea necesara pentru sat
def matrixConstruct(clauses, satMatrix):
    # luam fiecare clauza in parte si obtinem literalii
    for clause in clauses:
        lineInMatrix = [0] * nrVariables
        clause = list(clause)

        clause.pop(0)
        clause.pop(len(clause) - 1)
        clause = "".join(clause)
        literals = clause.split("V")
        # "traducem" literalii, pentru a forma o matrice de intregi
        for literal in literals:
            if literal[0] != "~":
                col = int(literal)
                lineInMatrix[col - 1] = 1
            else:
                col = int(literal[1:])
                lineInMatrix[col - 1] = -1
        satMatrix.append(lineInMatrix)

if __name__ == "__main__":
    clauses = input().split("^")
    satMatrix = []
    nrVariables = 0
    nrClauses = 0
    #obitnem o lista de clauze din formula noastra
    for clause in clauses:
        literals = clause.split("V")
        if nrVariables < len(literals):
            nrVariables = len(literals)
    nrClauses = len(clauses)
    #construim matricea pentru sat
    matrixConstruct(clauses, satMatrix)
    #generam interpretarile si le verificam
    interpretations = list(itertools.product([-1, 1], repeat= nrVariables))
    satisfiable = 0
    for interpretation in interpretations:
        validClauses = 0
        for line in satMatrix:
            validate = 0
            for i in range(nrVariables):
               if line[i] == interpretation[i]:
                    validate = 1
                    break
            if validate == 1:
                validClauses += 1
            else:
                break
        if validClauses == nrClauses:
            satisfiable = 1
            break
        else:
            continue
    #resultat: 1 pentru satisfiabil, 0 altfel
    print(satisfiable)

