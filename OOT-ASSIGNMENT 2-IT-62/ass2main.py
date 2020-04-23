"""
DOCSTRING
THIS IS MAIN APPLICATION ,IN WHICH MENU IS GIVEN FOR USER . USER SELECT ONE CHOICE, 
THEN MODULE CALL IS DONE ACCORDING TO  USER SELECTION

"""
from ass2submodule import * # IMPORT THE ASS2SUBMODULE PROGRAM WHICH CONTAINS CODE FOR OPERATIONS

   
def main(): # START OF MAIN MODULE

    choice=0
    
    
    while True: # START OF WHILE LOOP
        print("\n")
        print("Select the option: \n")
        print("1. Add") 
        print("2. Search")
        print("3. Delete")
        print("4. Update")
        print("5. Display")
        print("6. Number of students")
        print("7. Exit\n")
        choice = int(input())
        
        # CHOICE SELECTED BY USER WILL BE COMPARE AND CALL MODULE ACCORDINGLY
        if choice == 1:
            Student.addStudent()
        elif choice == 2:
            Student.search()
        elif choice == 3:
            Student.delStudent()
        elif choice == 4:
            Student.update()
        elif choice == 5:
            Student.display()
        elif choice == 6:
            Student.count()
            
        elif choice == 7:
            break
        else:
            print("\nWrong Choice choosed.........") # EXECUTE WHEN USER SELECT THE OTHER OPTION WHICH IS NOT GIVEN IN MENU
    # END OF WHILE LOOP
    


main() # CALL TO MAIN MODULE