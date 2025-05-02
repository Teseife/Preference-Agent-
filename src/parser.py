

def parse_attributes(fileName):
    """
    Parses an attribute file:
    attributesName: value1, value2
    :param fileName: path to file to parse
    :return: Dictionary of attributes in the form of {'attributeName': (value1, value2)}
    """
    attributes = {}
    with open(fileName, 'r') as file:
        for line in file:
            line = line.strip()
            if ":" in line:
                key, value = line.split(":",1)
                value = value.strip().split(",")
                value = [v.strip() for v in value]
                if len(value) != 2:
                    raise ValueError(f"Attribute {key} does not have exactly 2 values.")
                attributes[key.strip()] = (value[0], value[1])
    return attributes

def parse_constraints(fileName):
    """
    Parses a constraint file:
    where each line is one clause in the CNF
    example: "Not soup OR NOT ice-cream"
    :param fileName: path to the constraint file
    :return: a list of clauses, where each clause is a list of literal strings
            example: [["Not soup", "NOT ice-cream"], ["NOT wine", "NOT beer"]]
    """
    constraints = []
    with open(fileName, 'r') as file:
        for line in file:
            line = line.strip()
            literals = [lit.strip() for lit in line.split("OR")]
            constraints.append(literals)
    return constraints

def parse_preferences(fileName,logicType = "penalty"):
    """
    Parses a preference file in one of two formats:
    1. Penalty: "formula, penalty integer"
    2. Qualitative: "betterThing BT worseThing IF condition"

    :param fileName: path to the preference file
    :param logicType: "penalty" or "qualitative"
    :return: a list of preferences in the form of dictionaries
            For penalty: [{"formula": "fish and wine", "penalty": 10}]
            For qualitative: [{"better": "fish", "worse": "beef", "condition": "wine"}]
    """
    with open(fileName, 'r') as file:
        preferences = []
        for line in file:
           line = line.strip()
           if logicType == "penalty":
               preference = line.split(",")
               if len(preference) != 2:
                   continue
               formula = preference[0].strip()
               penalty = int(preference[1].strip())
               preferences.append({"formula":formula, "penalty":penalty})
           elif logicType == "qualitative":
               if "BT" in line:
                   beforeIF = line.split("IF")
                   rulePart = beforeIF[0].strip()
                   condition = ""
                   if len(beforeIF) > 1:
                       condition = beforeIF[1].strip()
                   if "BT" in rulePart:
                       better, worse = rulePart.split("BT")
                       preferences.append({"better":better.strip(),
                                           "worse":worse.strip(),
                                           "condition":condition  })
    return preferences


