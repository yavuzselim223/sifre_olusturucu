import random


charachters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("Şifreniz kaç karakterden oluşsun istiyorsunuz?"))


password = ""
for i in range(uzunluk):
    password += random.choice(charachters)
    
    
print("Sizin için oluşturduğum şifre:",password)

