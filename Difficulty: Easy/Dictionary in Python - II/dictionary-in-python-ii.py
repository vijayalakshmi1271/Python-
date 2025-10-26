def pair_sum(arr, sum):
    # code here
    seen = set()  
    for i in arr:
        needed = sum - i 
        
        if needed in seen:
            return True  
        seen.add(i)  
    return False  
