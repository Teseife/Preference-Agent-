import itertools
import random
from itertools import count

# NEW: these two lines import PySAT's CNF and Solver
from pysat.formula import CNF
from pysat.solvers import Solver

from parser import parse_constraints, parse_preferences, parse_attributes
from utils import encodeObj, displayTable
from evaluator import evaluateClause, evaluateFormula

class PreferenceAgent:
    """
    A preference agent that can evaluate preferences and constraints:
        - A set of binary attributes (from the given files)
        - A set of constraints (from the given file)
        - A set of preferences (from the given file)
        - Methods to evaluate the preferences and constraints and omni-optimization
    """

    def __init__(self, attributesFile, constraintsFile):
        """
        Constructor for the PreferenceAgent class.

        :param attributesFile: path to the file containing the attributes
        :param constraintsFile: path to the file containing the constraints
        """
        # Parse attributes via your parser
        self.attributes = parse_attributes(attributesFile)

        # Parse constraints as text (kept for reference) but we won't rely on them in `satisfiesConstrants` anymore
        self.constraints = parse_constraints(constraintsFile)

        # Generate all objects (encodeObj is presumably your old approach)
        self.objs = encodeObj(self.attributes)

        # Build a dictionary from "attribute-value" to a unique integer literal
        # or, equivalently, from "actual string (wine, fish, etc.)" to an int.
        self.valueMap = self.buildValueMap(self.attributes)

        # Convert your constraints file to a PySAT CNF
        # so we can solve them with PySAT
        self.constraintsCNF = self.parseConstraintsPySAT(constraintsFile)

        # We keep self.preferences for penalty or qualitative logic
        self.preferences = []

        # Now we do feasibility check via PySAT
        self.feasibleObj = self.checkFeasibilityPySAT()

        self.logicalType = None

    # -------------------------------------------------------------------------
    # NEW UTILITY: buildValueMap
    # -------------------------------------------------------------------------
    def buildValueMap(self, attributes_dict):
        """
        Creates a mapping from each possible value (like 'wine' or 'beef')
        to a unique integer variable for PySAT.

        Example scheme:
         - For each attribute, we get a new variable ID.
         - The first attribute's two values => +varID, -varID
         - Then we increment varID for the next attribute, etc.

        :param attributes_dict: from parse_attributes, e.g.
              { 'dissert': ('cake','ice-cream'),
                'drink': ('wine','beer'),
                'main':  ('fish','beef') }
        :return: A dict from string -> int. e.g. 'wine' -> 2, 'beer' -> -2, ...
        """
        value_map = {}
        var_id = 1
        for attr, (val1, val2) in attributes_dict.items():
            # We'll say val1 -> +var_id, val2 -> -var_id
            value_map[val1] = var_id
            value_map[val2] = -var_id
            var_id += 1
        return value_map

    # -------------------------------------------------------------------------
    # NEW UTILITY: parseConstraintsPySAT
    # -------------------------------------------------------------------------
    def parseConstraintsPySAT(self, constraintsFile):
        """
        Reads the constraints file, line by line, building a PySAT CNF object.
        Each line is a single disjunction. Example: 'NOT wine OR NOT ice-cream'

        We'll parse each literal, turn it into an integer based on self.valueMap,
        and handle 'NOT ' by flipping the sign.

        :param constraintsFile: path to your .txt constraints file
        :return: A PySAT CNF object containing all constraints
        """
        cnf = CNF()
        with open(constraintsFile, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                # Example line: "NOT wine OR NOT ice-cream"
                parts = [part.strip() for part in line.split("OR")]
                clause = []
                for p in parts:
                    if p.startswith("NOT "):
                        val = p[4:].strip()  # e.g. "wine"
                        # If valueMap says 'wine' -> 2, then NOT wine => -2
                        # But if valueMap says 'wine' is +2 => that means "wine" is the 'val1' of "drink"
                        # So "NOT wine" => literal = - (+2) => -2
                        literal = -self.valueMap[val]
                    else:
                        # e.g. "wine"
                        literal = self.valueMap[p]
                    clause.append(literal)
                cnf.append(clause)
        return cnf

    # -------------------------------------------------------------------------
    # NEW: checkFeasibilityPySAT replaces the old checkFeasibility
    # -------------------------------------------------------------------------
    def checkFeasibilityPySAT(self):
        """
        Loops over all encoded objects. For each object, tries to see if
        constraintsCNF + the unit clauses for that object's assignment
        is satisfiable. If yes, it's feasible.

        :return: a list of (code, obj) pairs that are feasible.
        """
        feasible = []
        for code, obj in self.objs:
            if self.isFeasibleWithPySAT(obj):
                feasible.append((code, obj))
        return feasible

    def isFeasibleWithPySAT(self, obj):
        """
        Given a single object (dict of {attr: chosen_value}),
        we create a solver, add the constraints, then add unit clauses
        for each chosen_value. If satisfiable => True, else False.

        :param obj: e.g. {'dissert': 'cake', 'drink': 'wine', 'main': 'fish'}
        :return: bool
        """
        with Solver(name='g3') as solver:
            # Add the constraints from your main constraints cnf
            solver.append_formula(self.constraintsCNF)

            # Now add this object's assignment as unit clauses
            # e.g. "dissert = cake" => if 'cake' maps to +1, we add [1]
            for attr, val in obj.items():
                lit = self.valueMap[val]
                solver.add_clause([lit])

            return solver.solve()

    # -------------------------------------------------------------------------
    # (Kept only for reference, but we are NOT using it for feasibility now)
    # -------------------------------------------------------------------------
    def checkFeasibility(self):
        """
        OLD manual method, no longer used.
        You can keep it around if you want for debugging,
        or remove it if you’re sure you don’t need it.
        """
        feasibleObj = []
        for code, obj in self.objs:
            if self.satisfiesConstrants(obj):
                feasibleObj.append((code, obj))
        return feasibleObj

    def satisfiesConstrants(self, obj):
        """
        OLD manual approach.
        We won't call this if we're using PySAT for feasibility.
        But you can keep it as a fallback or remove it.

        :param obj: a dictionary of attributes
        :return: True if the object satisfies all constraints else False
        """
        for clause in self.constraints:
            if not evaluateClause(clause, obj):
                return False
        return True

    # -------------------------------------------------------------------------
    # Preferences-Related (unchanged from your original)
    # -------------------------------------------------------------------------
    def loadPreferences(self, preferencesFile, logicType):
        """
        Loads the preferences from the given file
        :param preferencesFile: path to the file containing the preferences
        :param logicType: "penalty" or "qualitative"
        """
        self.preferences = parse_preferences(preferencesFile, logicType)
        self.logicalType = logicType

    def taskEncoding(self):
        """
        Displays the table of objects
        """
        print("Encoding of Objects:")
        for code, obj in self.objs:
            values = [obj[key] for key in self.attributes.keys()]
            print(f"{code} - {', '.join(values)}")

    def taskFeasibility(self):
        """
        Displays how many feasible objects we have.
        (Now, feasibleObj is determined by PySAT.)
        """
        countFeasible = len(self.feasibleObj)
        print(f"Feasible Objects ({countFeasible}):")

    def taskShowTable(self):
        """
        Displays the table of feasible objects with each preference rule's penalty
        and the total penalty at the end (Penalty Logic).
        """
        tableData = []
        headers = ["encoding"]
        for rule in self.preferences:
            headers.append(rule["formula"])
        headers.append("total penalty")

        for code, obj in self.feasibleObj:
            row = [code]
            totalPenalty = 0
            for rule in self.preferences:
                if evaluateFormula(rule["formula"], obj):
                    penalty = 0
                else:
                    penalty = rule["penalty"]
                row.append(str(penalty))
                totalPenalty += penalty
            row.append(str(totalPenalty))
            tableData.append(row)

        displayTable(headers, tableData)

    def taskExemplification(self):
        """
        Randomly pick two feasible objects and compare their total penalties (Penalty Logic).
        """
        print("Exemplification:")
        if len(self.feasibleObj) < 2:
            print("No feasible objects found.")
            return
        obj1 = random.choice(self.feasibleObj)
        obj2 = random.choice(self.feasibleObj)

        while obj1 == obj2:
            obj2 = random.choice(self.feasibleObj)

        print(f"Two randomly selected feasible objects are {obj1[0]} and {obj2[0]},")

        total1 = sum(
            0 if evaluateFormula(rule["formula"], obj1[1]) else rule["penalty"]
            for rule in self.preferences
        )
        total2 = sum(
            0 if evaluateFormula(rule["formula"], obj2[1]) else rule["penalty"]
            for rule in self.preferences
        )

        if total1 < total2:
            print(f"{obj1[0]} is better than {obj2[0]}")
        elif total1 > total2:
            print(f"{obj2[0]} is better than {obj1[0]}")
        else:
            print("and they are equivalent in preference.")

    def taskOmniOptimization(self):
        """
        Finds all feasible objects with minimal total penalty
        and prints them as the "optimal" set (Penalty Logic).
        """
        if not self.feasibleObj:
            print("No feasible objects found.")
            return

        objPenalty = []
        for code, obj in self.feasibleObj:
            totalP = sum(
                0 if evaluateFormula(rule["formula"], obj) else rule["penalty"]
                for rule in self.preferences
            )
            objPenalty.append((code, obj, totalP))

        minPenalty = min(item[2] for item in objPenalty)
        optimalObjs = [item[0] for item in objPenalty if item[2] == minPenalty]

        if optimalObjs:
            print("All optimal objects: " + ", ".join(optimalObjs))
        else:
            print("No optimal objects found.")

    def qualitativeScore(self, obj):
        """
        Produces a 'score vector' for a given object, comparing how it stands on each
        qualitative rule under an optional condition.
        """
        scores = []
        for rule in self.preferences:
            condition = rule.get("condition")
            if condition == "" or evaluateFormula(condition, obj):
                better = evaluateFormula(rule["better"], obj)
                worse = evaluateFormula(rule["worse"], obj)
                if better and not worse:
                    scores.append(1)
                elif worse and not better:
                    scores.append(-1)
                else:
                    scores.append(0)
            else:
                scores.append(0)
        return scores

    def compareObjectsQualitative(self, obj1, obj2):
        """
        Compares two objects based on their qualitative scores.
        :return: 1 if obj1 is better, -1 if obj2 is better, 0 if they are incomparable
        """
        score1 = self.qualitativeScore(obj1)
        score2 = self.qualitativeScore(obj2)

        better = False
        worse = False

        for s1, s2 in zip(score1, score2):
            if s1 > s2:
                better = True
            elif s1 < s2:
                worse = True

        if better and not worse:
            return 1
        elif worse and not better:
            return -1
        else:
            return 0

    def taskExemplificationQualitative(self):
        """
        Randomly pick two feasible objects and compare them in Qualitative Choice Logic.
        """
        if len(self.feasibleObj) < 2:
            print("No feasible objects found for exemplification.")
            return

        obj1 = random.choice(self.feasibleObj)
        obj2 = random.choice(self.feasibleObj)

        while obj1 == obj2:
            obj2 = random.choice(self.feasibleObj)

        print(f"Two randomly selected feasible objects are {obj1[0]} and {obj2[0]},")
        cmp_result = self.compareObjectsQualitative(obj1[1], obj2[1])

        if cmp_result == 1:
            print(f"{obj1[0]} is better than {obj2[0]}")
        elif cmp_result == -1:
            print(f"{obj2[0]} is better than {obj1[0]}")
        else:
            print("and they are incomparable in preference.")

    def taskOmniOptimizationQualitative(self):
        """
        In Qualitative Choice Logic, an object is 'optimal' if no other object strictly dominates it.
        We check all pairs of feasible objects and see which ones are undominated.
        """
        if not self.feasibleObj:
            print("No feasible objects found.")
            return

        optimalObjs = []
        for code1, obj1 in self.feasibleObj:
            dominated = False
            for code2, obj2 in self.feasibleObj:
                if obj1 != obj2:
                    if self.compareObjectsQualitative(obj2, obj1) == 1:
                        dominated = True
                        break
            if not dominated:
                optimalObjs.append(code1)

        if optimalObjs:
            print("All optimal objects: " + ", ".join(optimalObjs))
        else:
            print("No optimal objects found.")

    def menuPenaltyLogic(self):
        """
        A menu to display the options for the user
        """
        while True:
            print("\n Choose an option:")
            print("1. Encoding")
            print("2. Feasibility checking")
            print("3. Show the Table")
            print("4. Exemplification")
            print("5. Omni-optimization")
            print("6. Back to previous menu")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.taskEncoding()
            elif choice == "2":
                self.taskFeasibility()
            elif choice == "3":
                self.taskShowTable()
            elif choice == "4":
                self.taskExemplification()
            elif choice == "5":
                self.taskOmniOptimization()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again:")

    def menuQualitativeLogic(self):
        """
        A menu to display the options for the user
        """
        while True:
            print("\n Choose an option:")
            print("1. Encoding")
            print("2. Feasibility checking")
            print("3. Show the Table")
            print("4. Exemplification")
            print("5. Omni-optimization")
            print("6. Back to previous menu")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.taskEncoding()
            elif choice == "2":
                self.taskFeasibility()
            elif choice == "3":
                self.taskShowTable()
            elif choice == "4":
                self.taskExemplificationQualitative()
            elif choice == "5":
                self.taskOmniOptimizationQualitative()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again:")
