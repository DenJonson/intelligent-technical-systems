symb = "0x`" #символ
num = 10 #количество ярусов

for i in range(num):
  print(" "*(num-i) + symb*(i+(i-1)) + " "*(num-i))
