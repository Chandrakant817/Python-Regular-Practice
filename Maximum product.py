# I/P = [5,3,1,4,3,7,6,9,1]
# O/P = Maximum product is : (7,9)

ef max_product(arr):
    try:
        if len(arr) < 2:
            raise ValueError("Array must contain at least two elements")
        
        a = arr[0]
        b = arr[1]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if (arr[i]*arr[j]) > a*b:
                    a = arr[i]
                    b = arr[j]
        return a, b
        
    except Exception as e:
        return "Error:", e

arr = [5, 3, 1, 4, 3, 7, 6, 9, 1]
result = max_product(arr)
print(result)
