# HELPER FUNCTIONS
# Use these functions to quickly get your inputs from your input file,
# and write your outputs to an output file.

# The name of your input file.
file_input_name = "input.txt"
# The name of your output file.
file_output_name = "output.txt"

IGNORE_ME_file_input = open(file_input_name, 'r')
IGNORE_ME_file_output = open(file_output_name, 'w')
IGNORE_ME_file_output_storage = []

# Get the next line from your input file.
# You may optionally pass a string argument for debug print statements. This parameter can be skipped.
# Example:
# cases = input()
# length = input("Length of the box")
def input(ignored=None):
    if ignored != None:
        print("Reading {}".format(ignored))
    return IGNORE_ME_file_input.readline().strip()

# Write a string to your output file.
# You must pass a string argument to be written to the file.
# Example:
# output("Case #{}: {}".format(case, result))
def output(output):
    print("Writing line: {}".format(output))
    IGNORE_ME_file_output_storage.append(output + "\n")

# Saves your output file and makes it ready for submission.
# You must put this at the end of your code.
# Do not pass any arguments.
def submit():
    IGNORE_ME_file_output_storage[-1] = IGNORE_ME_file_output_storage[-1].strip()
    IGNORE_ME_file_output.writelines(IGNORE_ME_file_output_storage)
    IGNORE_ME_file_output.close()
    print("Saved and finished! Send your output file called {}".format(file_output_name))
#
# Good luck!
# ----------------------------------------------------
"""
PLAN:
## Coding Plan for Mikado Game
**1. Define Functions:**
* `get_data(n)`: This function takes the total number of sticks (n) as input and prompts the user to enter the dependency rules (stick x positioned over stick y) one by one.
It should store these rules in a dictionary where the key is the "under" stick (y) and the value is a list of "above" sticks (x).
* `remove_sticks(n, rules)`: This function takes the number of sticks (n) and the dependency rules dictionary as input. This will be the core logic to find the removal order.
**2. `remove_sticks` Function Breakdown:**
* **Initialize Variables:**
    * `removal_order`: An empty list to store the order of stick removal.
    * `remaining_sticks`: A set containing all stick numbers (initially {0, 1, ..., n-1}).
* **Loop until all sticks are removed:**
    * `removed_in_iteration`: Flag to check if any sticks were removed in this loop.
    * Iterate through a copy of `remaining_sticks` (to avoid modifying the original while iterating).
        * Check if the current stick has any dependencies in the rules dictionary.
            * If no dependencies exist (stick not in `rules`) or all dependencies are already removed (check if each dependency is present in `removal_order`), 
            remove the current stick:
                * Add the stick to `removal_order`.
                * Remove the stick from `remaining_sticks`.
                * Set `removed_in_iteration` to True.
* **Error Handling:**
    * After the loop, if `removed_in_iteration` is False, it means no stick could be removed and there must be a cycle in dependencies. Raise a `ValueError` indicating this.
* **Return:**
    * Return the final `removal_order` list.
**3. Main Script:**
* Get the number of sticks (n) from the user.
* Call `get_data(n)` to get the dependency rules dictionary.
* Call `remove_sticks(n, rules)` to find the removal order.
* Print the removal order in a user-friendly format.
This coding plan outlines the structure of the program with separate functions for data collection and core logic. You can then fill in the specific details of each function
using the chosen programming language (Python in this case).
"""
def remove_sticks(n, datalist):
    removal_order = []
    nlist = []
    nylist = []
    remaining_sticks = datalist
    def p1(num, numlist):
        for x in numlist:
            if num < i:
                pass
            else:
                return False
        return True
    for y in datalist:
        for p in y:
            nylist.append(p)
    #print(datalist)
    print(remaining_sticks)
    for i in range(n):
        nlist.append(i)
    for l in remaining_sticks:
        #print(l, "debug3")
        #print(first_stick, "debug3")
        #removal order: if not in list at all (following order of pred)-> if only in l[0] -> if no more r3
        for num in nlist:
            index = remaining_sticks.index(l)
            if (num != l[0]) and (num != l[1]) and (p1(num, nylist)): #first
                print(remaining_sticks)
                del remaining_sticks[index]
                removal_order.append(num)
                print(removal_order)
            elif (num == l[0]) and (num != l[1]):
                print(remaining_sticks)
                del remaining_sticks[index]
                removal_order.append(num)
                print(removal_order)
                
            elif len(remaining_sticks) ==1:
                removal_order.append(num)
                print(removal_order)
    return removal_order

#this code when outputted
t = int(input())
for i in range(t):
    datalist=[]
    nm = input()
    nm = nm.split(" ")
    n = int(nm[0])
    m = int(nm[1])
    for times in range(m):
        datas = []
        data = input() #possbiel error
        data = data.split(" ")
        for o in data:
            o = int(o)
            datas.append(o)
            #print(datas)
        datalist.append(datas)
        #print(datalist)
    removal_order = remove_sticks(n, datalist)
    #print(removal_order)
for case in range(t):
    output("Case #{}: {}".format(case + 1, removal_order))  
submit()     

# Example usage
"""
N = 5  # Number of sticks
rules = [(1, 0), (2, 1), (3, 2), (4, 3)]  # Example precedence rules
removal_order = find_order(N, rules)
print("Removal order:", removal_order)
"""
