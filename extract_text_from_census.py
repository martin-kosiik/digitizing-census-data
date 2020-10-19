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


table_text = """Polička 23.278 4 8.709 — 3 — 1 — — 1 31.996 314 32.310 Přelouč 22.438 3 42 1 3 1 1 1 — — 22.490 129 22.619 Skuteč 20.765 5 19 — — — — — — — 20.789 91 2U.880 Üsti nad Orlicí 29.714 8 4.903 2 17 16 2 14 — — 34.676 191 34.867 Žamberk 28.328 9 258 45 — 7 4 — — 1 28.652 131 28.783 Župa III. Hradec Králové. . . . 360.024 131 141.805 446 294 82 14 1 — 26 502.823 3.933 506.756 Broumov 1.957 — 24.747 2 10 5 — — — — 26.721 640 27.361 Bydžov, Nový ~ 31.464 5 90 — 13 1 — — — 1 31.574 98 31.672 Dvůr Králové nad Labem .... 17.670 6 11.862 8 41 — — — — — 29.582 234 29.816 Hořice 29.651 3 120 1 11 3 1 — ■ 1—’ 29.790 73 29.863 Hostinné 1.280 — 17.197 — 14 7 — — — 1 18.499 196 18.695 Hradec Králové 57.868 61 414 96 7 5 4 — — 8 58.463 365 58.828 Chlumec nad Cidlinou 23.901 8 51 1 — 2 — — — — 23.963 94 24.057 Jaroměř 31.203 14 2.752 310 2 7 4 — — — 34.292 432 34.724 Maršov 165 — 8.802 — — 1 — — — ‘ 8.968 105 9.073 Město, Nové ~ nad Metují . . . 17.891 3 4.229 1 — 2 — — — — 22.126 98 22.224 Náchod 38.259 8 352 1 124 7 3 — — 2 38.756 199 38.955 Nechanice 17.813 2 10 1 — — — — — — 17.826 127 17.953 Opočno 24.299 9 139 • 1 3 — — — 1 24.452 95 24.547 Police nad Metují 11.351 1 202 — — — — — — — 11.554 57 11.611 Rokytnice v Ori. Horách .... 823 — 12.448 1 8 1 — — — — 13.281 193 13.474 Rychnov nad Kněžnou 20.452 4 269 1 — 1 1 — — 2 20.730 93 20.823 Skalice, Česká ~ 13.644 2 121 ' — 1 — ' — 3 13.771 42 13.813 Teplice nad Metují 427 — 11.067 1 5 — — — — - 11.500 86 11.586 Trutnov 3.925 1 37.926 19 54 25 1 — — 6 41.957 507 42.464 Üpice 14.874 4 329 7 4 4 — 1 — — 15.223 41 15.264 Žacléř 1.107 — 8.678 1 — 7 — — — 2 9.795 158 9.953 Župa IV. Mladá Boleslav .... 500.746 226 224.715 538 386 93 28 6 — 46 726.784 9.033 735.817 Bělá pod Bezdězem 11.309 3 2.195 1 — 3 — — — — 13.511 81 13.592 Benátky, Nové ~ 28.780 7 205 41 — — — — — 4 29.037 495 29.532 Boleslav, Mladá ~ 48.476 69 542 200 19 5 4 1 — 5 49.321 384 49.705 Brod, Železný ~ 22.584 5 260 — — 1 1 — — — 22.851 56 22.907 Dub, Český ~ 12.680 1 1.106 2 — — — — — — 13.789 41 13.830 Frýdlant 1.166 1 29.478 7 5 3 1 — — 2 30.663 927 31.590 Hradiště, Mnichovo ~ 24.160 11 229 1 — 2 2 — — 2 24.407 147 24.554 Jablonec nad Nisou 7.089 6 51.416 4 95 16 — L_ — 5 58.631 1.271 59.902 Jičín 31.565 13 448 84 9 7 4 4 — 4 32.138 159 32.297 Jilemnice 22.438 5 1.141 — — — 2 — — — 23.586 39 23.625 Libáň 19.850 3 59 11 4 1 — — — 1 19.929 124 20.053 Liberec 15.170 35 78.268 85 157 21 6 — — 7 93.749 3.017 96.766 v tom: Liberec město 4.894 14 27.929 38 130 9 3 — — 3 33.020 1.965 34.985 Lomnice nad Popelkou 16.955 1 51 3 — — 2 — — ] 17.013 29 17.042 Mělník 43.351 18 138 2 11 7 2 — — — 43.529 262 43.791 Městec Králové 20.244 1 28 12 14 1 — — — — 20.300 100 20.400 Město, Nové ~ pod Smrkem . . 271 — 9.083 — — 3 — — — — 9.357 278 9.635 Nymburk 32.878 22 111 2 26 5 — — — 3 33.047 249 33.296 Рака, Nová ~ 27.986 2 2.377 1 6 1 — — — — 30.373 72 30.445 Poděbrady 30.378 9 53 4 — 3 — — — 2 30.449 217 30.666 Rokytnice nad Jizerou 974 — 7.023 — 1 — — — — — 7.998 62 8.060 Semily 16.956 1 275 1 2 — — — — 1 17.236 45 17.281 Sobotka 15.387 1 27 1 — 4 — — — 2 15.422 55 15.477 Tanvald 6.671 3 19.268 1 — 3 4 — — 3 25.953 352 26.305 Turnov 30.810 8 373 71 9 6 — 1 __ . 2 31.280 160 31.440 Vrchlabí 2.160 — 20.074 1 23 1 — — — 1 22.260 396 22.650 Vysoké nad Jizerou 10.458 1 487 3 5 — — — — 1 10.955 15 10.970 Župa V. Česká Lipa 59.524 110 489.129 567 606 185 18 3 1 74 550.217 15.894 566.111 Benešov nad Plouínicí 200 20.732 1 1 20.934 132 21.066 Bor u České Lípy . I 1.794 1 18.320 2 1 10 — — — — 20.128 372[ 20.500"""

#replaced = re.sub('\d+( )\d+', '×', table_text)
#print(replaced)

def make_table(text=table_text, n_cols=16):
    replaced = re.sub(' (?=\d+|—)|(?<=\d|—) ', '×', text, flags=re.IGNORECASE)
    split_string = replaced.split(sep='×')
    n_rows = len(split_string)//n_cols
    list_of_rows = []
    for row in range(n_rows):
        list_of_rows.append(split_string[row*n_cols:(row+1)*n_cols])

dtable = DigiTable(table_text)
DigiTable(table_text).make_table()



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
