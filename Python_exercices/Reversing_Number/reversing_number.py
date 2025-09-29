'''
* Create a program that reverses an integer number
* For example, if the input is 123 the output would be 321

'''
def reversing(number):
        print(number % 10,end='')
        if number > number % 10:
            reversing(number // 10)
    

reversing(123)
print()
reversing(456)
print()
reversing(996)

