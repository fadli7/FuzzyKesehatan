import pandas as pd
import numpy as np

df = pd.DataFrame(index=['Sangat Tinggi', 'sfsd', 'sfs'], dtype=np.int)

df['test'] = pd.Series([1, 0, 1], index=['Sangat Tinggi', 'sfsd', 'sfs'])

print(df)

yoga = 0.0
print(round(yoga))
print(type(yoga))