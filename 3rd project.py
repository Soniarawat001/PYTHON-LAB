"""make a miniproject for series of no. by taking input 
from user such as starting point, ending point, updation, 
choice for horizontal/vertical and also take choice for 
printing the no. reverse/forword order"""

starting_point = int(input(
    "enter your starting digit:"
))
ending_point = int(input(
    "enter your ending digit:"
))
steping_value= int(input(
    "enter the gap value:"
))
way= input(
    " enter the way of your series \n h for horizontal\n v for vertical \n here:"
)
order= input(
    "enter the order of your series\n f for forword\n r for reverse \n here:"
)
if(order=="f"):
    for i in range(starting_point,ending_point+1,steping_value):
        if(way=="h"): 
            print(i,end=" ")
        else:
            print(i)
else:
    for i in range(ending_point,starting_point-1,-steping_value):
        if(way=="h"): 
            print(i,end=" ")
        else:
            print(i)



