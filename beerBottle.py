for nums in range(99,0,-1) :
    if nums == 1:
        print (nums, "bottle of beer on wall..")
        print (nums, "bottle of beer..")
        print ("Take one down .. pass it around..")
    else:
        print (nums, "bottles of beer on wall..")
        print (nums, "bottles of beer..")
        print ("Take one down .. pass it around..")
    new_num = nums -1
    if new_num ==0:
        print ("No bottle of beer on wall")
    elif new_num ==1:
        print (new_num, "bottle of beer on wall")
    else:
        print (new_num, "bottles of beer on wall")
    print()
    
    
