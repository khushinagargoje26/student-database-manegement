

import studentdatabase_system as stud
l=stud.load_from_file()



while True:
    choice=int(input("Enter 1 to  Add Student\nEnter 2 to delete student \nEnter 3 to update student\nEnter 4 to search student\nEnter 5 to display all students\nEnter 6 to Exit \nChoose an option:"))

        
    if choice == 1:
        stud.add_student(l)
            

    elif choice==2:
        id=int(input("enter id which you want to delete"))
        stud.dlt_stud(l,id)
        

    elif choice==3:
        id=int(input("Enter id  which you want to update"))
        stud.update_student(l,id)
        print("update succesfull")

    elif choice==4:
            
        id=int(input("enter  student_id which you want to search"))
        print(id)
        stud.search_student(l,id)
    elif choice == 5:
        print(l)
        


    elif choice==6:
        print("EXIT")
        break
