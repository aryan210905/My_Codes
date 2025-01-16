class Library:
    def __init__(self):
        self.l = []
        self.noOfBooks = len(self.l)
    def addBook(self,bookName):
        self.l.append(bookName)
        self.noOfBooks = self.noOfBooks + 1
        print(f"\nSuccessfully added {bookName} in the system")
        print(f"Currently there are {self.noOfBooks} books in the system")
    def removeBook(self,bookName):
        if(len(self.l) == 0):
            print("\nNo books in the system")
        else:
            self.l.remove(bookName)
            self.noOfBooks = self.noOfBooks - 1
            print(f"\nSuccessfully removed {bookName} from the system")
            print(f"Currently there are {self.noOfBooks} books in the system")
    def displayAllBooks(self):
        if(len(self.l) == 0):
            print("\nNo books in the system")
        else:
            print("Here are the available books in the library")
            print(self.l)
            print("\n")
    
class Student(Library):
    authority = "Student"
    def __init__(self):
        self.studentList = []
        self.noOfStudents=0
    def addStudent(self,newStudentId,newStudentName):
        self.newStudentId = newStudentId
        self.newStudentName = newStudentName
        self.noOfStudents += 1
    def removeStuent(self,studentId):
        self.studentList.remove(studentId)
        self.noOfStudents -= 1       
obj = Library()
print("Menu:")
print("1. Add Book")
print("2. Remove Book")
print("3. Print all books")
print("4. Exit system\n")
while(1):
    task = int(input("\nEnter task: "))
    match task:
        case 1:
            a = input("Enter book name to be added: ")
            obj.addBook(a)
        case 2:
            a = input("Enter book name to be removed: ")
            obj.removeBook(a)
        case 3:
            obj.displayAllBooks()
        case 4:
            raise SystemExit
        case _:
            print("Invalid input")


