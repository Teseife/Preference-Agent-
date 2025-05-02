def evaluateLiteral(literal, obj):
    """
    Evaluates a single a literal against a dictionary object
    :param literal: exmaple. "NOT value" or "fish"
    :param obj: example.{'drink': 'wine', 'main': 'steak', 'dessert': 'cake'...}
    :return: True of the given literal is satisfied by the object if not returns False
    """
    if literal.startswith("NOT "):
        value = literal[4:].strip()
        return value not in obj.values() # True
    else:
        value = literal.strip()
        return value in obj.values() # False


def evaluateClause(clause, obj):
    """
    Evaluates a clause (disjunction of literals) against a given object
    :param clause: This is a list of literals example. ["NOt fish", "NOT wine"]
    :param obj: example.{'drink': 'wine', 'main': 'steak', 'dessert': 'cake'...}
    :return: True if any of the literals in the clause is satisfied by the object Else False
    """
    return any(evaluateLiteral(literal, obj) for literal in clause)

def evaluateFormula(formula, obj):
    """
    A string based for a formula contaning AND, OR and NOT with no parenthesis
    it splits any whitespace and processes the tokens in a basic sequence.
    :param formula: example. "NOT fish AND NOT wine" or "fish OR wine"
    :param obj: example.{'drink': 'wine', 'main': 'steak', 'dessert': 'cake'...}
    :return: True if the formula is satisfied by the object else False
    """
    tokens = formula.split()
    if not tokens:
        return True
    def processTokens(tokens):
















        num = 0
        newTokens = []
        while num < len(tokens):
            if tokens[num] == "NOT":
                if num +1 < len(tokens):
                    newTokens.append(str( not evaluateLiteral(tokens[num+1], obj)))
                    num += 2
                else:
                    num += 1
            else:
                newTokens.append(tokens[num])
                num += 1
        return newTokens

    tokens = processTokens(tokens)

    if "AND" in tokens:
        parts = [token for token in tokens if token != "AND"]
        results = []
        for part in parts:
            if part == "True" or part == "False":
                results.append(part == "True")
            else:
                results.append(evaluateFormula(part, obj))
        return all(results)
    elif "OR" in tokens:
        parts = [token for token in tokens if token != "OR"]
        results = []
        for part in parts:
            if part == "True" or part == "False":
                results.append(part == "True")
            else:
                results.append(evaluateFormula(part, obj))
        return any(results)
    else:
        token = tokens[0]
        if token == "True":
            return True
        elif token == "False":
            return False
        else:
            return evaluateLiteral(token, obj)


