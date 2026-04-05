from random import randint
allChrStr = "ABCDEFGHIJKLMNOQPRSTUWXYZabcdefghijklmnoqprstuwxyz0123456789-_?*!'£#$&˜.,:;=+@<>|"
allChrList = list(allChrStr)
digitChrStr = "0123456789"
digitChrList = list(digitChrStr)
passwordType = Input("Enter password type(digit, alpha, all):")
password = []
passwordLength = int(Input("Enter password Length:"))
i = 0
while(i<4):
  password[i] = allChrStr[randint(1, len(allChrList))]
  print("Password Generating:",password)
print("Password Generated:"+password)
