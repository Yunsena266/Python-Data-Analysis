import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
info=pd.read_csv ("RussianSerials.txt")
print("Size of table",info.shape)
print(info.describe(include='all'));

