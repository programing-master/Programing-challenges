# This algorithm takes an integer number positive as a parameter and generates all possible combinations
# of numbers that sum up to the given number using a backtracking approach.
# 

def sum_generate(target):
    if target < 0 or not isinstance(target,int):
        return
    result=[]
    def backtracking(surplus,combination,start):
         if surplus == 0:
             result.append(combination[:])
             return
         for num in range(start,target + 1):
             if num > surplus:
                 break
             combination.append(num)
             backtracking(surplus - num,combination,num)
             combination.pop()
                
    backtracking(target,[],1)
    return result

print(sum_generate(2))
print()
print(sum_generate(-4))