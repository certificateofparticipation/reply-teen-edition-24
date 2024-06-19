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

'''

The highly anticipated white truffle harvesting season has finally arrived!
We have two truffles dogs, Mia and Genga, ready for the task, each assigned to a specific plot of land
TM ia and TGenga containing numerous truffle trees. The two plot lands are represented as two list of
non-negative integer of length LM ia and LGenga where each value consists in the weight of truffle in that
position.
The two truffles dogs will have to go in a harvesting season which can last in days between Amin and
Amax included. During an harvesting day Mia and Genga can collect truffles from their respective plot
of land TM ia and TGenga in any order. Once a truffle is harvested it won’t be availabe anymore for the
next days in the season.
To keep the truffle habitat sustainable, it’s s crucial that each dogs not exceed a designated total weight
W for day of truffles, which must be consistent for both Mia and Genga. Moreover, for each day, both
dogs must harvest the same total weight of truffles.
Your goal is to find a possible configuration for the harvesting season, meaning to calculate a set of D
harvesting days, with D between Amin and Amax included, to collect the entire quantity of truffles T
available from both terrains and the order of collection for each day.
For each harvesting day you are required indicate, for both Mia and Genga, the set of truffles from TM ia
and TGenga harvested.
Please note that different valid solution can exists, in this case it’s enough to return one of them.

amin is min number of attempts in days
amax is max number of attempts in days
wmia is mia's weight
wgenga is genga's weight
lmia is length of mia's plot
lgenga is length of genga's plot
wmax is max truffle weight/day
d is harvesting strat day

Plan:
Collect same amt of truffles/day
harvest all truf
w should not exceed wmax
'''
# YOUR CODE HERE!

testcases = int(input())

for _ in range(testcases):  # Loop through test cases
    d = 0
    wmia = 0
    wgenga = 0
    out = []
    splitstats = input().split()
    amin = int(splitstats[0])
    amax = int(splitstats[1])
    lmia = int(splitstats[2])
    lgenga = int(splitstats[3])
    wmax = int(splitstats[4])
    miaplot = [int(x) for x in input().split()]  # Convert miaplot to integer list
    gengaplot = [int(x) for x in input().split()]  # Convert gengaplot to integer list
    def daily_harvest(d, out, miaplot, gengaplot):
        for i in miaplot:
            for j in gengaplot:
                if i == j:
                    print(i)
                    out.extend([i, 0, i, 0, 0])
                    print(out)
                    d+=1
                    miaplot.remove(i)
                    gengaplot.remove(j)
                    return
        if len(miaplot) == 1 or len(gengaplot) == 1:
            if len(miaplot) < len(gengaplot):
                out.extend([sum(miaplot), 0, gengaplot[0], gengaplot[1], 0])
                print(out)
                d+=1
            elif len(miaplot) > len(gengaplot):
                out.extend([gengaplot[0], gengaplot[1], 0, sum(miaplot), 0])
                print(out)
                d+=1
                    
    for i in range(min(len(miaplot),len(gengaplot))):
        print(str(i) + "time")
        daily_harvest(d, out, miaplot, gengaplot)
   


    
    #output("Case #{}: {}".format(_ + 1, out))
    print("Case #{}: {}".format(_ + 1, out))
        

                    
                    
    

# submit()
