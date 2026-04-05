from random import randint
from time import sleep
allChrStr = "ABCDEFGHIJKLMNOQPRSTUWXYZabcdefghijklmnoqprstuwxyz0123456789-_?*!'£#$&˜.,:;=+@<>|"
allChrList = list(allChrStr)
digitChrStr = "0123456789"
digitChrList = list(digitChrStr)
alphaChrStr = "ABCDEFGHIJKLMNOQPRSTUWXYZabcdefghijklmnoqprstuwxyz"
alphaChrList = list(alphaChrStr)
passwordType = Input("Enter password type(digit, alpha, all):")
password = []
passwordLength = int(Input("Enter password Length:"))
i = 0
while(i<4):
  if(passwordType == "digit"):
    password[i] = digitChrStr[randint(1, len(digitChrList))]
  else if(passwordType == "alpha"):
    password[i] = alphaChrStr[randint(1, len(alphaChrList))]
  else if(passwordType == "all"):
    password[i] = allChrStr[randint(1, len(allChrList))]
  else:
    print("Your input is not valid. Exiting int 10 seconds")
    sleep(10)
    exit()
  print("Password Generating:",password)
print("Password Generated:"+password)
