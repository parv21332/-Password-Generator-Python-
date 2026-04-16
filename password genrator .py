#password genrater 
import random
c="abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password=""
for i in range(6):
    password += random.choice(c)
print("your password :",password)