import sys
if len(sys.argv) != 4:
    print("Usage: python employedetails.py <name> <rollno> <id> <salary>")
    sys.exit(1)
name =  sys.argv[1]
experience = sys.argv[2]
id = sys.argv[3]
salary = sys.argv[4]

print("employee name is",name)
print("experience is",experience)
print("id is",id)
print("salary is",salary)