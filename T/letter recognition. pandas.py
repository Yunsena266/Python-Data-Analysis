import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
datas=pd.read_csv("mnist_train.csv",header=None)
print(datas.shape)
columnss=['label']
for i in range(784):
    columnss.append(f"px_{i}")
datas.columns=columnss
size_of_image=28
matrix_datas=datas.values
digit=matrix_datas[0,:]
digit=digit[1:]
print(digit.shape);
image=digit.reshape(28,28)
print(image.shape)
plt.plot(image,color='k')
plt.show()


