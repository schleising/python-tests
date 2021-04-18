import numpy as np
import pandas as pd
import csv
from pathlib import Path

print(np.log(np.exp(10)))

with open(Path('output/test.csv'), 'w', encoding='utf8') as csvFile:
    writer = csv.DictWriter(csvFile, ['Col1', 'Col2', 'Col3'])
    writer.writeheader()

    for i in range(10):
        j = i * 10
        writer.writerow({
            'Col1': j + 1,
            'Col2': j + 2,
            'Col3': j + 3,
        })

df = pd.read_csv(Path('output/test.csv'))

print(df)
