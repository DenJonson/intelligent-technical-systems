import numpy as np
import pandas as pd

def readFile (path):
  return pd.read_csv(path, ',')

def writeFile (path, arr, col=None):
  pd.DataFrame(arr, columns=col).to_csv(path)
  
f = readFile("taxi_zone_lookup.csv")

writeFile("zzz.csv", f)