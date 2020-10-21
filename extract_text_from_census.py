#import pdfplumber
import os
import re
import numpy as np
import pandas as pd

working_directory = "C:/Users/marti/OneDrive/Plocha/RA_work/public_goods_and_ethnic_het"
os.chdir(working_directory)

class DigiTable():
    def __init__(self, text=table_text):
        self.text = text
    def make_table(self, n_cols=14):
        replaced = re.sub(' (?=\d+|—)|(?<=\d|—) ', '×', self.text, flags=re.IGNORECASE)
        split_string = replaced.split(sep='×')
        n_rows = len(split_string)//n_cols
        list_of_rows = []
        for row in range(n_rows):
            list_of_rows.append(split_string[row*n_cols:(row+1)*n_cols])
        arr = np.array(list_of_rows)
        return pd.DataFrame(arr)

table_text = """95 — 20.664 — — 1 — — — — 20.760 543 21.303 547 — 13.900 — 12 1 — — — — 14.460 112 14.572 499.088 145 249.365 716 1.160 62 36 13 — 46 750.681 6.260 756.891 80 — 13.821 1 — — — — — — 13.902 93 13.995 24.663 3 10 1 38 — — — — — 24.715 150 24.865 20.669 — 18 — 1 — 1 — — — 20.689 49 20.738 20.767 1 8 — — — 2 '"T“ — — 20.778 72 20.850 6.477 2 5.284 6 25 5 1 i — 2 11.803 65 11.868 20.350 6 4.970 1 11 2 — — — — 25.340 169 25.509 570 — 8.487 3 6 — — — — 1 9.067 98 9.165 7.598 1 8.473 1 — — . — — — 16.073 162 16.235 224 1 15.602 1 4 2 — i — — 15.835 171 16.006 18.683 3 2.737 — 12 — 1 i — — 21.437 130 21.567 43.565 10 746 58 57 4 1 — — 3 44.444 275 44.719 18.819 1 64 — 1 1 2 -L — . 18.888 43 18.931 406 — 14.733 7 67 1 2 4 — 2 15.222 478 15.700 10.293 3 5.718 — 5 2 — — — 2 16.023 42 16.065 16.894 3 16 — 4 3 1 — — — 16.921 67 16.988 865 — 16.547 3 5 — — — — — 17.420 280 17.700 295 — 19.346 • 18 1 1 — — — 19.661 201 19.862 15.939 2 15 — — 1 — 2 — — 15.959 67 16.026 136.540 81 8.251 489 705 21 16 3 . 26 146.132 1.498 147.630 28.221 3 140 — 5 2 — — — — 28.371 81 28.452. 57 — 17.304 — 2 — — — — — 17.363 153 17.516 35.143 10 254 1 5 1 2 1 — 1 35.418 161 35.579 235 — 11.601 — — — 1 1 — 1 11.838 101 11.939 9.635 4 15.988 28 42 2 — — — 1 25.700 262 25.962 1.673 — 22.584 113 43 1 1 ; — 1 24.416 513 24.929 23.027 4 3.034 — 6 3 — — — 2 26.076 191 26.267 236 — 24.385 2 16 1 — — — — 24.640 256 24.896 29 — 9.662 —j ■ — — — — — 1 9.692 33 9.725 2.181 2 10.293 1 26 — 2 — — 3 12.508 160 12.668 11.947 1 9.189 — 44 1 — — — — 21.182 150 21.332 23.007 4 85 — 12 8 2 — — — 23.118 89 23.207 398.593 125 154.173 533 481 32 27 4 — 28 553.996 8.890 562.886 496 . . 16.009 — — — — — — 1 16.506 554 17.060 64.658 86 11.642 251 221 9 13 2 — 9 76.891 1.242 78.133 841 — 10.539 — 2 — — — — — 11.382 605 11.987 15.755 2 68 1 16 — — • — -r- 15.842 60 15.902 19.795 — 82 — 1 1 — — — 1 19.880 103 19.983 28.325 2 7.774 98 40 1 1 1 — — 36.242 386 36.628 1.599 — 13.718 — 25 — — — — 3 15.345 604 15.949 1.901 — 10.622 4 — — — — — — 12.527 64 12.591 2.798 . 15.630 2 6 1 — — — — 18.437 526 18.963 14.808 2 16.181 2 15 ; — — — 1 30.959 521 31.480 11.452 1 48 — — 1 — — — 2 11.504 65 11.569 9.818 — 4 — — — 1 — — — 9.823 39 9.862 14.272 — 446 2 — — — — — — 14.720 59 14.779 37.259 10 184 99 9 i 1 1 — 4 37.568 220 37.788 216 — 15.358 — 9 — — — — — 15.578 296 15.874 11.569 1 9.275 53 26 5 — — — — 20.909 254 21.163 28.823 3 64 — 9 2 1 — — 1 28.903 224 29.127 16.429 1 1.069 — — 1 — — — 3 17.503 138 17.641 27.293 7 2.326 38 13 4 4 — — 2 29.687 2.129 31.816 16.643 — 20 — 4 — — — — — 16.667 83 16.750 15.641 1 16 — 3 — — — — — 15.661 100 15.761 11.786 2 15.686 1 58 2 — — — — 27.535 207 27.742 22.988 5 41 — 1 2 6 — — 1 23.044 144 23.188 65 — 7.388 2 — 1 — — — — 7.456 162 7.618 23.363 2 38 — 23 1 — — — — 28.427 105 23.532"""
#replaced = re.sub('\d+( )\d+', '×', table_text)
#print(replaced)

DigiTable(table_text).make_table(n_cols=13)



def make_table(text=table_text, n_cols=16):
    replaced = re.sub(' (?=\d+|—)|(?<=\d|—) ', '×', text, flags=re.IGNORECASE)
    split_string = replaced.split(sep='×')
    n_rows = len(split_string)//n_cols
    list_of_rows = []
    for row in range(n_rows):
        list_of_rows.append(split_string[row*n_cols:(row+1)*n_cols])

dtable = DigiTable(table_text)

ethnicity_df = pd.read_excel('digitized_results\ethnicity.xlsx', dtype = {'non-citizens': str})
ethnicity_df = pd.read_excel('digitized_results\ethnicity.xlsx', dtype = str)

num_vars = ethnicity_df.columns.tolist()[2:]
ethnicity_df[num_vars] = ethnicity_df[num_vars].apply(lambda x:  x.str.replace('.', '').str.replace(',', ''))

ethnicity_df.columns

ethnicity_df['polish'].apply(lambda x:  x.replace('.', '').replace(',', ''))

ethnicity_df = ethnicity_df.fillna(0)

ethnicity_df[num_vars] = ethnicity_df[num_vars].apply(lambda x: pd.to_numeric(x, errors='coerce').fillna(0).astype(int))

ethnicity_df.dtypes

diff = ethnicity_df['citizens in total'] + ethnicity_df['non-citizens'] - ethnicity_df['total inhabitans']

ethnicity_df.to_excel('digitized_results\ethnicity_export.xlsx', index=False)

np.abs(diff).sort_values(ascending=False)[:50]
replaced = re.sub(' (?=\d+|—)|(?<=\d|—) ', '×', table_text, flags=re.IGNORECASE)
print(replaced)

split_string = replaced.split(sep='×')

n_cols = 14
split_string[:14]

#split_string.__len__()
n_rows = len(split_string)//n_cols
list_of_rows = []
for row in range(n_rows):
    list_of_rows.append(split_string[row*n_cols:(row+1)*n_cols])

from scipy.stats import norm
(1 - norm.cdf(1.42)) *2

#list_of_rows
#741/18
#table_text.replace()
#table_text.split(' ')
arr = np.array(list_of_rows)
#print(arr)

pd.DataFrame(arr)
