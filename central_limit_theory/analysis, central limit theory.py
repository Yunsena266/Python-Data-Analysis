#TASK: In the group of 30 people in the ages from 18 to 30 the experiment of measuring of dna level
# was made. Evaluate the middle value of dna level in the all general sets (find the confidence
# interval including this parameter).

#central limit theory

import math
import pandas
import matplotlib.pyplot as plt
import statistics as st
import numpy as np
datas_level_DNA=[102,100,98,99,88,103,101,105,105,107,108,
                 105,107,99,95,107,102,106,98,101,100,101,96,108,101,89,94,96,104,100,103]
n=len(datas_level_DNA)
mean_levelDNA=st.mean(datas_level_DNA)
sd=st.stdev(datas_level_DNA)
print("mean average of dna level", mean_levelDNA)
print("standard deviation of dna level",sd)
se=sd/math.sqrt(n) #standard mean mistake
extreme_right_value=mean_levelDNA+1.96*sd;
extreme_left_value=mean_levelDNA-1.96*sd;
print("The confident interval from: "+str(extreme_left_value)+" to "+str(extreme_right_value))



