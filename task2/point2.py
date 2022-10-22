def histDistance (hist1, hist2):
  if len(hist1) != len(hist2):
    print("Гистограммы должны быть соразмерны!")
    return 0
  hist_len = len(hist1)
  distance = 0
  for i in range(0, hist_len):
    distance += (hist1[i] - hist2[i])**2
  distance **= 0.5 
  return distance
