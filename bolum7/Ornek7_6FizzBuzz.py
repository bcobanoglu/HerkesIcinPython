# -*- coding: UTF-8 -*- 
#FizzBuzz Oyunu
def fizzBuzz():
    for x in range(1, 101):
        if x % 15 == 0:
            print('FizzBuzz', end=',')
        elif x % 3 == 0:
            print('Fizz', end=',')
        elif x % 5 == 0:
            print('Buzz')
        else:
            print(x,end=',')
#Ana program
if __name__ == '__main__':
    fizzBuzz()
