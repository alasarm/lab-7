 #!/usr/bin/env python3
# Student ID: asarmiento6

def function1():
    global schoolName   # Declare schoolName as global
    schoolName = 'SICT'  # Modify global schoolName
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName   # Declare schoolName as global
    schoolName = 'SSDO'  # Modify global schoolName
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)  # Global schoolName
function1()
print('print() in main on schoolName:', schoolName)  # Should now be 'SICT'
function2()
print('print() in main on schoolName:', schoolName)  # Should now be 'SSDO'

