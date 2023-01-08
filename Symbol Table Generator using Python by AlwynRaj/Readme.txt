Symbol Table Generator using Python by AlwynRaj

Symbol Table Constructor using Python. A Symbol Table consists of all the Variable names, the Datatypes, the Initial Values, the Function names, Arguments, and their Returntypes. This Program generates a symbol table for a C-like programming language.
 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
Algorithm:
Step 1: Get the Input program from the user.
Step 2: Tokenize the Input program.
Step 3: Now Traverse the Entire Token list to check for datatypes, if found store it in a variable.
Step 4: Check for identifiers, If found store them in a variable.
Step 5: Check for ',' Commas, if found append the Datatype and value 0 into their respective lists.
Step 6: Check for ';' Semicolons, if found append all the collected data into their respective lists.
Step 7: Now Separate the Variables from the Function declaration. ( The 'Values' in the Values list has '()' in them to identify them and separate them)
Step 8: Use any means to create a table. Here I used Pretty table Module to create a table. 
 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
Advantages :
1. It is easy to understand. 
2. Easy to implement.
3. It Can be further optimized.
4. Flexible.

Disadvantages :
1. Not optimized.
2. Large space complexity.
3. Too many loops affect the program's performance.
