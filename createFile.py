import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

from google.colab import files
uploaded = files.upload()

addi = pd.read_csv('ADDIND.BO.csv')
addi()

plt.figure(figsize=(12.5,4.5))
plt.plot(addi['Close'],lable = 'Addi')
plt.title('ADDI')
plt.xlabel('Time')
plt.ylable('Close Price')
plt.legend(loc = 'upper left')
plt.show()