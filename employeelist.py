#------------------------------EMPLOYEE LIST------------------------------

employees=["Darsh","Aarushi","Mark","John","Rohit","Amit","Sakshi","Riya","Ankit","Nisha","Diksha"]

print("\nPrinting all employees in the list:")

for employee in employees:
    print(employee)

print("\nPrinting every second employee in the list:")

for i in range(0, len(employees),2):
    print(employees[i])

name=input("\nEnter the name of the employee to check if they are in the list: ")
if name in employees:
    print(name, "is in the employee list.")
else:
    print(name, "is not in the employee list.")

print("\n")

salary=int(input("Enter the salary to check for employees: "))
age=int(input("Enter the age to check for employees: "))
department=input("Enter the department to check for employees: ")
id=int(input("Enter the ID to check for employees: "))

data=[{"id": 1, "name": "Darsh", "age": 25, "department": "ECE", "salary": 500000},
      {"id": 2, "name": "Aarushi", "age": 28, "department": "ECE", "salary": 600000},
      {"id": 3, "name": "Mark", "age": 30, "department": "Finance", "salary": 70000},
      {"id": 4, "name": "John", "age": 35, "department": "IT", "salary": 80000},
      {"id": 5, "name": "Rohit", "age": 32, "department": "HR", "salary": 75000},
      {"id": 6, "name": "Amit", "age": 29, "department": "Finance", "salary": 65000},
      {"id": 7, "name": "Sakshi", "age": 27, "department": "IT", "salary": 55000},
      {"id": 8, "name": "Riya", "age": 31, "department": "HR", "salary": 70000},
      {"id": 9, "name": "Ankit", "age": 26, "department": "Finance", "salary": 60000},
      {"id": 10, "name": "Nisha", "age": 33, "department": "IT", "salary": 75000},
      {"id": 11, "name": "Diksha", "age": 34, "department": "HR", "salary": 80000}]

print("\n")

for i in data:
    if i["salary"] >= salary:
        print(i["name"], "has a salary greater than or equal to", salary)
    if i["salary"] < salary:
        print(i["name"], "has a salary less than", salary)

print("\n")

for i in data:
    if i["age"] >= age:
        print(i["name"], "is at least", age, "years old.")
    if i["age"] < age:
        print(i["name"], "is not yet", age, "years old.")

print("\n")

for i in data:
    if i["department"] == department:
        print(i["name"], "works in the", department, "department.")
    else:
        print("ERROR, Please write in all caps.")
        break 

print("\n")

for i in data:
    if i["id"] == id:
        print(i["name"], "has the ID number", id)