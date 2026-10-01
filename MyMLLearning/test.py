import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

db = sns.load_dataset('penguins')

plt.figure(figsize=(4, 4))
sns.histplot(data=db, x = 'body_mass')
plt.show()