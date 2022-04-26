class Triangular_superior():
  """
  Triangular superior de una matrix F*C
  """
  def __init__(self):
    pass
  def TrianSup(self, x):
    import numpy as np
    F, C = x.shape
    OUT = np.zeros((F,C))
    for i in range(F):
      OUT[i,i:C]=M[i,i:C]
    return OUT