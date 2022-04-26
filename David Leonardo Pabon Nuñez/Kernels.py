class Kernels():
  """
  Kernels
  """
  def __init__(self):
    pass
  def LinearKernel(self, x, y, t, c):
    import numpy as np
    Fx, Cx = x.shape
    Fy, Cy = y.shape
    if Fx == Fy:
      if Cx == Cy:
        OUT = np.zeros((Fx,Cx))
        for i in range(Fx):
          OUT[i,...] = (x[i,...]**t)*y[i,...]+c
        return OUT
      else:
        print("Las entradas deben tener el mismo tamaño")
    else:
      print("Las entradas deben tener el mismo tamaño")

  def PolinomialKernel(self, x, y, t, c, a, d):
    import numpy as np
    Fx, Cx = x.shape
    Fy, Cy = y.shape
    OUT = np.zeros((Fx,Cx))
    if Fx == Fy:
      if Cx == Cy:
        for i in range(Fx):
          OUT = np.zeros((Fx,Cx))
          X = x**T
          Z = a*X*y
          J = Z+c
          OUT[i,...] = J**d
        return OUT
      else:
        print("Las entradas deben tener el mismo tamaño")
      
      return OUT
    else:
      print("Las entradas deben tener el mismo tamaño")

  def GaussianKernel(self, x, y, s):
    import numpy as np
    Fx, Cx = x.shape
    Fy, Cy = y.shape
    OUT = np.zeros((Fx))
    if Fx == Fy:
      if Cx == Cy:
        for i in range(Fx):
          resta = x[i] - y[i]
          norm = np.linalg.norm(resta, ord=2)
          norm = norm**2
          div = -1*(norm/(2*s**2))
          k = np.exp(div)
          OUT[i] = k
        return OUT  
      else:
        print("Las entradas deben tener el mismo tamaño")
    else:
      print("Las entradas deben tener el mismo tamaño")

  def ExponentialKernel(self, x, y, s):
    import numpy as np
    Fx, Cx = x.shape
    Fy, Cy = y.shape
    OUT = np.zeros((Fx))
    if Fx == Fy:
      if Cx == Cy:
        for i in range(Fx):
          resta = x[i] - y[i]
          norm = np.linalg.norm(resta, ord=2)
          div = -1*(norm/(2*s**2))
          k = np.exp(div)
          OUT[i] = k
        return OUT  
      else:
        print("Las entradas deben tener el mismo tamaño")
    else:
      print("Las entradas deben tener el mismo tamaño")
  
  def LaplacianKernel(self, x, y, s):
    import numpy as np
    Fx, Cx = x.shape
    Fy, Cy = y.shape
    OUT = np.zeros((Fx))
    if Fx == Fy:
      if Cx == Cy:
        for i in range(Fx):
          resta = x[i] - y[i]
          norm = np.linalg.norm(resta, ord=2)
          div = -1*(norm/(s))
          k = np.exp(div)
          OUT[i] = k
        return OUT  
      else:
        print("Las entradas deben tener el mismo tamaño")
    else:
      print("Las entradas deben tener el mismo tamaño")
    
  def AnovaKernel(self,x,y,s,n,d):
    import numpy as np
    Fx, Cx = x.shape
    Fy, Cy = y.shape
    OUT = np.zeros((Fx))
    if Fx == Fy:
        for i in range(n):
          resta = x**n - y**n
          resta = resta**2
          resta = -1*s*resta
          resta = resta**d
          res = np.exp(resta)
          OUT = res
        return OUT 
    else:
      print("Las entradas deben tener el mismo tamaño")

  def HyperbolicKernel(self, x, y, a, t, c):
    import numpy as np
    Fx, Cx = x.shape
    Fy, Cy = y.shape
    OUT = np.zeros((Fx,Cx))
    if Fx == Fy:
      if Cx == Cy:  
        for i in range(Fx):
          X = a*(x[i,...]**t)*y[i,...]
          sum = X + c
          res = np.tanh(sum)
          OUT[i,...] = res
        return OUT
      else:
        print("Las entradas deben tener el mismo tamaño")
    else:
      print("Las entradas deben tener el mismo tamaño")
    
  def RaKernel(self, x, y, c):
    import numpy as np
    Fx, Cx = x.shape
    Fy, Cy = y.shape
    OUT = np.zeros((Fx))
    if Fx == Fy:
      if Cx == Cy:
        for i in range(Fx):
          resta = x[i] - y[i]
          num = np.linalg.norm(resta, ord=2)
          num = num**2
          dem = np.linalg.norm(resta, ord=2)
          dem = dem + c
          div = num / dem
          res = 1 - div
          return OUT
      else:
       print("Las entradas deben tener el mismo tamaño")
    else:
      print("Las entradas deben tener el mismo tamaño")

    def MuKernel(self, x, y, c):
      import numpy as np
      Fx, Cx = x.shape
      Fy, Cy = y.shape
      OUT = np.zeros((Fx))
      if Fx == Fy:
        if Cx == Cy:
          for i in range(Fx):
            resta = x[i] - y[i]
            num = np.linalg.norm(resta, ord=2)
            num = num**2
            res = num + c
            res = np.sqrt(res)
            return OUT
        else:
          print("Las entradas deben tener el mismo tamaño")
      else:
        print("Las entradas deben tener el mismo tamaño")

    def ImKernel():
      import numpy as np
      Fx, Cx = x.shape
      Fy, Cy = y.shape
      OUT = np.zeros((Fx))
      if Fx == Fy:
        if Cx == Cy:
          for i in range(Fx):
            resta = x[i] - y[i]
            num = np.linalg.norm(resta, ord=2)
            num = num**2
            dem = num + c
            dem = np.sqrt(dem)
            res = 1 / dem
            return OUT
        else:
          print("Las entradas deben tener el mismo tamaño")
      else:
        print("Las entradas deben tener el mismo tamaño")