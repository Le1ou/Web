def IsPalindrome(value):
  value_copy=value
  result = 0
  while(value!=0):
    digit = value%10
    result = result*10 + digit
    value=int(value/10)
  if(result==value_copy):
    return True
  else:
    return False
value = int(input("Введите число: "))
check = IsPalindrome(value)
print(check)