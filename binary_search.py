import random 

def binary_search(list_numbers, number): 
    list_numbers = sorted(list_numbers)
    attempts, low, high = 0,  0, len(list_numbers) - 1
    
    while low <= high: 
        attempts += 1
        middle = int((low + high) / 2)
        kick = list_numbers[middle]

        if kick == number: 
            return attempts, number 
        
        elif kick > number: 
            high = kick 
        else: 
            low = kick 
    else: 
        return None  
    

if __name__ == '__main__': 
    numbers = [i for i in range(0, 256)]
    
    response = binary_search(numbers, random.randint(0, 255))
    print(response)
