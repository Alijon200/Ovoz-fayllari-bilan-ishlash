# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fm3icj4-YWvvtbZRaNuTpJnwmW0Mbhyl
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.array([4,12])
y=np.array([50,400])
plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([-7,-6,-5,-4,-3,-2,0,2,3,4,5,6,7])
y=np.array([49,36,25,16,9,4,0,4,9,16,25,36,49])
plt.plot(x,y)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Yurak shakli uchun parametrik tenglamalar
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Grafikni chizish
plt.plot(x, y, color='red')
plt.title("Yurak shakli")
plt.axis('equal')  # O'qlarni tenglashtirish
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([45,23,12,5,15,])
mylabels=["English","Dasturlash","Tarix","Kimyo","Iqtisod"]
plt.pie(x,labels=mylabels)
plt.show()