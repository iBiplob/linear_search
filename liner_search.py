def linear_search(the_value,target):
    n = len(the_value)
    for i in range(n):
        if the_value[i] == target:
            return True
    return False


li = [1,2,3,4,5,6,7]
tar = int(input("Enter target number: "))
print(linear_search(li,tar))