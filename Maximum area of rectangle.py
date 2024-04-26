# I/p => number = 8, [4,2,3,2,3,4,5,1]
# O/p => 8 Explanation:(4*2)
                

def max_area_of_rect(num,lenghts):
    try:
        arr = []
        for i in lenghts:
            if lenghts.count(i) >= 2 and i not in arr:
                arr.append(i)

        sum1 = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if (arr[i]*arr[j]) > sum1:
                    sum1 = arr[i]*arr[j]
        return sum1
        
    except exception as e:
        print("There is an Error in the Code")

# Taking input from user
num = int(input())
lenghts = list(map(int,input().split(",")))

result = max_area_of_rect(num,lenghts)
print("The maximum area of rectange is :",result)
