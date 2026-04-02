# This Level A1
password = "1234"
chrStr = "ABCDEFGHIJKLMNOQPRSTUWXYZabcdefghijklmnoqprstuwxyz0123456789-_?*!'£#$&˜.,:;=+@<>|"
chrList = list(chrStr)
print(chrList)

numStr = "0123456789"
numList = list(numList)
unknownPassword = ['0', '0', '0', '0']
i = 0
while(True):
  if(PasswordControl(unknownPassword)):
    Break
  i= i+1
  ln = 0
  while(ln<4):
    unknownPassword[ln] += 1
    

print("Access Succesful. Current Password:" + unknownPassword) 

def PasswordControl (uPassword):
  if(string(uPassword) == password):
    return True
  else:
    return False
