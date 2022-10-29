import numpy as np
import pandas as pd

class NNClassifier:
  def __init__ (self):
    pass
  
  classList = []
  
  def addClass(self, path):
    f = pd.read_csv(path)
    f = np.array(f)
    self.classList.append(f)
    

Classifier = NNClassifier()

Classifier.addClass("task2\\point3\\taxi_zone_lookup.csv")
print(Classifier)