def printFizzBuzz(var):
  if(var <= 0):
    print('varは正の整数を入れること')
  elif (var % 15 == 0):
    print('FizzBuzz')
  elif(var % 5 == 0):
    print('Buzz')
  elif(var % 3 == 0):
    print('Fizz')
  else:
    print(var)

printFizzBuzz(15)
printFizzBuzz(5)
printFizzBuzz(3)
printFizzBuzz(100)
printFizzBuzz(1233)
printFizzBuzz(1)
printFizzBuzz(0)
printFizzBuzz(-22)