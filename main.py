# from pysat.formula import CNF
# from pysat.solvers import Solver
# sys and os are used to manipulate the system path so that files in the src directory can be imported with no issues!
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.prefAgent import PreferenceAgent





def main():
    """
        Main driver function for launching the PrefAgent system.

        Steps:
        1. Greets the user.
        2. Asks for two filenames: attributes and constraints.
        3. Initializes the PrefAgent with these files.
        4. Provides a looped menu to choose between Penalty Logic, Qualitative Logic, or Exit.
        5. Delegates further tasks (encoding, feasibility, etc.) to the PrefAgent's menu methods.
    """
    wellcomeMessage = """ 

    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓██████████████▓▒░░▒▓████████▓▒░      ░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░        ░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                     
     ░▒▓█████████████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░      ░▒▓█▓▒░ 



    ░▒▓████████▓▒░▒▓██████▓▒░                                                                                                           
       ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░                                                                                                          
       ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░                                                                                                          
       ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░                                                                                                          
       ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░                                                                                                          
       ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░                                                                                                          
       ░▒▓█▓▒░   ░▒▓██████▓▒░                                                                                                                                                                                                                            



    ░▒▓███████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░▒▓████████▓▒░                
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░                    
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░                    
    ░▒▓███████▓▒░░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒▒▓███▓▒░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░                    
    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░                    
    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░                    
    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░                    



    """
    print(f"\n{wellcomeMessage}")

    attrbutesFile = input("Enter the attributes file name: ").strip()
    constraintsFile = input("Enter the Hard constraints file name: ").strip();

    agent = PreferenceAgent(attrbutesFile, constraintsFile)


    while True:

        print("1. Penalty Logic")
        print("2. Qualitative Logic")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("You picked Penalty Logic.")
            prefFile = input("Enter the preference file name: ").strip()
            agent.loadPreferences(prefFile, logicType="penalty")
            agent.menuPenaltyLogic()
        elif choice == "2":
            print("You picked Qualitative Logic.")
            prefFile = input("Enter the preference file name: ").strip()
            agent.loadPreferences(prefFile, logicType="qualitative")
            agent.menuQualitativeLogic()
        elif choice == "3":
            print("Exiting the PrefAgent system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()