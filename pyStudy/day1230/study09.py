# *
# **
# ***
# ****
# *****

for i in range(5):
    for j in range(i+1):
        print("*",end='');
    print()


#           *           1
#          ***          3   
#         *****         5
#        *******        7
#       *********       9

for i in range(1,6):
    for j in range(6-i):
        print(" ",end="");
    for j in range(i*2-1):
        print("*",end="");
    print();