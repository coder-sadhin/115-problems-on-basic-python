# problem: 6. Data Type Checker: Write a Python function that takes a variable as input 
# and returns the data type of the variable as a string (e.g., “int”, “float”, “str”, “list”, etc.).

# value=list(input())
# print(type(value))
# value=list(input())
# print(type(value))

intiger=int(input())
found_pair = False
for root in range(2,intiger):
    for pwr in range(1,6):

# intiger=int(input())
# found_pair = False
# for root in range(2,intiger):
#     for pwr in range(1,6):

        if root**pwr == intiger:
            found_pair = True
            break
    if found_pair:
            break
if found_pair:
    print("Root: ", root, " & Power: " , pwr)
else:
     print("No pair integar exits")
    