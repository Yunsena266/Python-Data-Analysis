import pandas as pd
import statistics
import matplotlib
import matplotlib.pyplot as plt
datas_population=pd.read_csv("countries_population.txt",header=None, encoding='Windows-1251')
popul_countries=(datas_population[1])
print("average value",statistics.mean(popul_countries))
print("mediana",statistics.median_high(popul_countries))
print("standard deviation",statistics.stdev(popul_countries))


