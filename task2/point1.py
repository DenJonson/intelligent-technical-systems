def triangle(num_of_symb_on_each_side):
  symb = "*" #символ
  num = num_of_symb_on_each_side+2 #количество ярусов

  for i in range(num):
    print(" "*(num-i) + symb*(i+(i-1)) + " "*(num-i))
    
triangle(3)