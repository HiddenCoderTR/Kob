from random import randint
from time import sleep

allChrStr = "ABCDEFGHIJKLMNOQPRSTUWXYZabcdefghijklmnoqprstuwxyz0123456789-_?*!'£#$&˜.,:;=+@<>|"
digitChrStr = "0123456789"
alphaChrStr = "ABCDEFGHIJKLMNOQPRSTUWXYZabcdefghijklmnoqprstuwxyz"

# Python'da input küçük harfle yazılır
passwordType = input("Enter password type (digit, alpha, all): ").lower()
passwordLength = int(input("Enter password Length: "))

password = []
i = 0

while i < passwordLength: # 4 yerine kullanıcının istediği uzunluk
    if passwordType == "digit":
        # randint yerine random.choice kullanmak çok daha pratiktir ama senin mantığınla gidelim:
        password.append(digitChrStr[randint(0, len(digitChrStr) - 1)])
    elif passwordType == "alpha":
        password.append(alphaChrStr[randint(0, len(alphaChrStr) - 1)])
    elif passwordType == "all":
        password.append(allChrStr[randint(0, len(allChrStr) - 1)])
    else:
        print("Your input is not valid. Exiting in 10 seconds")
        sleep(10)
        exit()
    
    i += 1 # i++ yerine Python'da bu kullanılır
    # Listeyi ekrana basarken güzel gözükmesi için "".join kullanılır
    print("Password Generating: " + "".join(password))

print("Final Password: " + "".join(password))
