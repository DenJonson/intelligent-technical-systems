import numpy as np
import pandas as pd

class NNClassifier:
  def __init__ (self):
    pass
  
  classList = []
  
  def addClass(self, className, path):
    f = pd.read_csv(path)
    self.classList.append([className, np.array(f)])
  
  
