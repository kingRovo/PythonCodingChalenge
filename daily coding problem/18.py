def printMax(arr, n, k): 
    max = 0
    
    for i in range(n - k + 1): 
        max = arr[i] 
        for j in range(1, k): 
            if arr[i + j] > max: 
                max = arr[i + j] 
        print(str(max) + " ", end = "") 
  

if __name__=="__main__": 
    arr = [10,5,2,7,8,7] 
    n = len(arr) 
    k = 3
    printMax(arr, n, k)
        

        
    
