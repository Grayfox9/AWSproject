import pandas as pd
import numpy as np
import sys


file = pd.read_json(sys.stdin)
df = pd.read_json(sys, lines = True)
df.insert(0, column = 'ID', value = np.arange(1, len(df) + 1))
df.drop('reviewerName', axis = 1, inplace = True)
df.to_json(sys.stdout)

