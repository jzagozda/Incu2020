def AddOddNumbers(a):
    final_result = 0
    for i in range(a):
        result = i+(i+1) 
        print("Number ",i+1,": ",result)        
        final_result += result
    return final_result
AddOddNumbers(5)
print(AddOddNumbers(5))