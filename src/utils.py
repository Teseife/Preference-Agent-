import itertools

def encodeObj(attributes):
    """
    Generates all possible combinations of attributes.
    Where each attribute is listed value is encoded as bit=1, and the second as bit=0
    :param attributes: A dictionary of attributes in the form of {'attributeName': (value1, value2)}
    :return: A list of (code,obj) pairs, where:
            code = o1, o2, o3, ... oN
            obj = {'attributeName': value}
    """
    objs = []
    keys = list(attributes.keys())

    for bits in itertools.product([0,1], repeat=len(keys)):
        obj = {}

        for key, bit in zip(keys, bits):
            val = attributes[key][0] if bit == 1 else attributes[key][1]
            obj[key] = val
        num = 0
        for bit in bits:
            num = (num << 1) | bit
        code = f"o{num}"
        objs.append((code, obj))
    return objs

def displayTable(headers, data):
    """
    Prints an ASCII table to the given data

    :param headers: list of column headings
    :param data: list of rows, where each row is a list of strings
    :return: Prints the table to the console
    """

    colWidths = [max(len(cell) for cell in col) for col in zip(headers,*data)]

    sepLine = "+-" + "-+-".join("-"*width for width in colWidths) + "-+"
    headerLine = "| " + " | ".join(f"{header:{width}}" for header, width in zip(headers, colWidths)) + " |"

    print(sepLine)
    print(headerLine)
    print(sepLine)

    for row in data:
        rowLine = "| " + " | ".join(f"{cell:{width}}" for cell, width in zip(row, colWidths)) + " |"
        print(rowLine)















    print(sepLine)
