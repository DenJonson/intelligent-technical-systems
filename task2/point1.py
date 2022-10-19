def triangle(a):
  symb = "*" #символ
  num = a+2 #количество ярусов

  for i in range(num):
    print(" "*(num-i) + symb*(i+(i-1)) + " "*(num-i))
    
triangle(3)