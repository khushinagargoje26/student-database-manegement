l=[]

class FileNotFoundError(Exception):
    pass
try:
    
    
    def add_student(l):
        student_id = int(input("Enter ID of the student: "))
        name = input("Enter name of the student: ")
        age = int(input("Enter age of the student: "))
        grade = int(input("Enter grade of the student: "))
        address = input("Enter address: ")
        data = [student_id, name, age, grade, address]
        l.append(data)
        print("Student added successfully.")
        
    def dlt_stud(l,id):
        for i in l:
                if(i[0]==id):
                    l.remove(i)
                    print("student data deleted sucessfully")

    def update_student(l,id):
        for student in l:
            if student[0]==id:
        
                c=input("enter the key you want to update")

        
                if(c=='name'):
                    student[1]=input("Enter name updated name")
                elif(c=='age'):
                    student[2]=input("enter the updated age")
                        
                elif(c=='grade'):
                    student[3]=input("enter the updated grade")
                        
                elif(c=='address'):
                    student[4]=input("enter the updated address")
                else:
                    print("Invalid key")
                return 
    def search_student(l, student_id):
                    
        for student in l:
            if student[0] == student_id:
                print("Student found:", student)
            else:
                print("Student with ID not found.",student_id)
                
    def save_to_file(l, filename="students.txt"):
        file=open(filename,'w')
        for s in l:
            file.write(f"{s[0]},{s[1]},{s[2]},{s[3]},{s[4]}\n")
        print("Data saved to file.")
        print("Current data in file:", l)

    def load_from_file(filename="student.txt"):
        
        
        file=open(filename,'r')
        for line in file:
            student = line.strip().split(',')
            student[0] = int(student[0])
            student[1]=student[1]
            student[2] = int(student[2])
            student[3] = int(student[3])
            l.append(student)
        return l


except ValueError:
    print("Enter valid Input")
except FileNotFoundError:
    print("Data loaded from file:",l)
