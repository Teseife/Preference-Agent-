# PrefAgent System - README

## Overview
The PrefAgent system is a knowledge-based intelligent system designed to solve a preference problem. It collects user-specified binary attributes, hard constraints (in CNF), and preferences (using either penalty logic or qualitative choice logic) to reason about and identify optimal solutions. This project adheres to the specifications provided in the project documentation.

## Features
- **Encoding:** Converts all objects into binary codes based on the attributes file.
- **Feasibility Checking:** Uses PySAT to determine which objects satisfy the hard constraints.
- **Table Display:** Presents a table of feasible objects with computed penalties or satisfaction degrees.
- **Exemplification:** Randomly selects two feasible objects and compares their preference outcomes.
- **Omni-optimization:** Identifies all optimal feasible objects based on the chosen preference logic.

## Dependencies
- **Python 3.11** or later
- **PySAT**  
  Install via:
  ```bash
  pip install python-sat
    ```
- Additional python standard Libraries:
  - `random`
  - `itertools`
  - `sys`
  - `os`

```
Prefrence-Agent/
│
├── main.py
├── README.md                   
├── ExampleTestCase/      
│   ├── attributes.txt
│   ├── constraints.txt
│   ├── penaltylogic.txt
│   └── qualitativechoicelogic.txt
├── TestCase/             
│   ├── attributes.txt
│   ├── constraints.txt
│   ├── penaltylogic.txt
│   └── qualitativechoicelogic.txt
└── src/                  
    ├── utils.py
    ├── prefAgent.py
    ├── parser.py
    └── evaluator.py

  
```

## Usage
1. **install** the required dependencies.
    ```bash
    pip install -r requirements.txt
    ```

2. **Run the main script**:
   ```bash
   python main.py
   ```
3. **Input File Format**: 
   - When prompted, provide the path to the input files like so. 
   ```
    Enter the path to the attributes file: ExampleTestCase/attributes.txt
     ```
   - The system will read the attributes, constraints, and preferences from the specified files.

4. **Output**:
```
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



    
Enter the attributes file name: ExampleTestCase/attributes.txt
Enter the Hard constraints file name: ExampleTestCase/constraints.txt
1. Penalty Logic
2. Qualitative Logic
3. Exit
Choose an option: 1
You picked Penalty Logic.
Enter the preference file name: ExampleTestCase/penaltylogic.txt

 Choose an option:
1. Encoding
2. Feasibility checking
3. Show the Table
4. Exemplification
5. Omni-optimization
6. Back to previous menu
Enter your choice: 1
Encoding of Objects:
o0 - ice-cream, beer, beef
o1 - ice-cream, beer, fish
o2 - ice-cream, wine, beef
o3 - ice-cream, wine, fish
o4 - cake, beer, beef
o5 - cake, beer, fish
o6 - cake, wine, beef
o7 - cake, wine, fish

 Choose an option:
1. Encoding
2. Feasibility checking
3. Show the Table
4. Exemplification
5. Omni-optimization
6. Back to previous menu
Enter your choice: 2
Feasible Objects (6):

 Choose an option:
1. Encoding
2. Feasibility checking
3. Show the Table
4. Exemplification
5. Omni-optimization
6. Back to previous menu
Enter your choice: 3
+----------+---------------+--------------+---------------+
| encoding | fish AND wine | wine OR cake | total penalty |
+----------+---------------+--------------+---------------+
| o0       | 10            | 6            | 16            |
| o1       | 10            | 6            | 16            |
| o4       | 10            | 0            | 10            |
| o5       | 10            | 0            | 10            |
| o6       | 10            | 0            | 10            |
| o7       | 0             | 0            | 0             |
+----------+---------------+--------------+---------------+

 Choose an option:
1. Encoding
2. Feasibility checking
3. Show the Table
4. Exemplification
5. Omni-optimization
6. Back to previous menu
Enter your choice: 4
Exemplification:
Two randomly selected feasible objects are o5 and o0,
o5 is better than o0

 Choose an option:
1. Encoding
2. Feasibility checking
3. Show the Table
4. Exemplification
5. Omni-optimization
6. Back to previous menu
Enter your choice: 5
All optimal objects: o7

 Choose an option:
1. Encoding
2. Feasibility checking
3. Show the Table
4. Exemplification
5. Omni-optimization
6. Back to previous menu
Enter your choice: 5
All optimal objects: o7

 Choose an option:
1. Encoding
2. Feasibility checking
3. Show the Table
4. Exemplification
5. Omni-optimization
6. Back to previous menu
Enter your choice: 6
1. Penalty Logic
2. Qualitative Logic
3. Exit
Choose an option: 3
Exiting the PrefAgent system. Goodbye!
```
