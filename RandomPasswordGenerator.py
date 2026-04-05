from random import randint
chrStr = "ABCDEFGHIJKLMNOQPRSTUWXYZabcdefghijklmnoqprstuwxyz0123456789-_?*!'£#$&˜.,:;=+@<>|"
chrList = list(chrStr)
password = []
passwordLength = 4
i = 0
while(i<4):
  password[i] = chrStr[randint(1, len(chrList))]
  print("Password Generating:",password)
print("Password Generated:"+password)
