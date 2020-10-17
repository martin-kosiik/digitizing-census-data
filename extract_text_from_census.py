import pdfplumber
import os
import re
import numpy as np
import pandas as pd

working_directory = "C:/Users/marti/OneDrive/Plocha/RA_work/public_goods_and_ethnic_het"
os.chdir(working_directory)

pdf = pdfplumber.open("test.pdf")
page = pdf.pages[1]
table = page.extract_table()
pdf
print(table)

im = page.to_image()

table_text = """1 Bechyně 3 1 9 4 4 4 16 66 8 2 8 6 1 6 5 У 2 Benešov 36 23 35 15 18 31 36 356 29 13 12 29 28 31 33 4 3 Beroun 48 36 65 12 26 27 113 3.727 217 26 1.414 100 60 216 35 5 4 Brandýs nad Labem . . 301 98 1.183 61 252 166 262 1.142 100 142 26 76 15 53 145 6 5 Brod, Český ~ 86 46 86 61 187 376 95 450 28 26 12 22 16 14 59 7 6 Brod, Německý ~ . 33 19 23 13 38 22 67 109 8 7 1 7 7 14 5 8 7 Čáslav 67 47 76 41 95 109 118 324 19 10 11 35 39 13 36 9 8 Dobříš 12 6 14 5 7 10 23 199 30 11 21 7 8 17 7 10 9 Habry 8 3 17 23 22 19 26 98 4 3 2 3 13 14 4 11 10 Hora, Kutná ~ 79 81 63 48 74 160 105 375 22 6 8 51 32 41 29 12 11 Hořovice 24 28 28 11 18 23 54 987 124 12 260 68 53 84 28 13 12 Humpolec 15 8 15 8 13 10 36 102 7 3 7 18 2 3 4 14 13 Chotěboř 12 16 12 7 14 33 39 94 9 4 2 5 20 7 9 15 14 Janovice, Uhlířské ~ . . 24 7 13 9 11 24 30 161 21 5 5 16 16 5 11 16 15 Jílové 23 10 29 8 16 22 27 201 16 8 6 16 2 6 17 17 16 Kamenice nad Lipou . . 8 4 5 3 6 5 7 84 3 — 6 15 2 12 5 18 17 Karlín*) 102 34 474 39 104 92 108 964 37 291 20 46 11 34 63 19 18 Kolín 135 79 111 295 257 916 180 551 48 24 7 47 33 53 50 20 19 Kostelec nad Černými Lesy . 8 12 14 8 11 29 34 111 16 8 3 8 5 5 3 21 20 Kouřim 30 32 35 37 69 463 85 249 14 12 6 26 18 13 23 22 21 Královice, Dolní ~ . 13 13 5 5 5 8 14 110 9 7 1 6 7 7 7 23 22 Ledeč nad Sázavou . . . 11 10 19 11 17 18 29 120 4 1 2 5 13 5 11 24 23 Milevsko 13 2 9 1 2 2 9 112 9 6 2 9 4 7 12 25 24 Mirovice 5 1 4 2 1 — 13 74 9 4 7 9 7 8 7 26 25 Neveklov 4 2 10 2 2 6 9 75 4 2 — 8 3 12 4 27 26 Pacov 15 6 6 3 10 3 19 65 4 2 2 3 5 3 9 28 27 Pelhřimov 16 7 17 4 4 9 24 107 18 2 6 7 7 11 3 29 28 Počátky 2 2 7 2 2 5 7 66 5 3 4 10 2 4 2 30 29 Polná 4 8 4 — 5 5 13 21 — — — 3 4 1 1 31 Příbram 23 17 20 8 12 8 45 546 76 7 30 27 72 56 29 32 Přibyslav 3 12 1 3 6 5 16 35 3 — 3 2 2 1 1 33 Říčany*) 68 35 97 32 45 38 73 527 46 31 8 38 14 35 45 34 Sedlčany 4 4 9 4 4 5 14 169 12 6 5 11 5 10 26 35 Sedlec 7 5 13 2 1 5 27 105 8 2 3 8 9 3 9 36 Smíchov*) 46 14 120 16 25 45 112 2.920 434 436 44 81 29 74 95 37 Soběslav 7 2 11 7 8 9 11 64 5 2 8 10 4 6 3 38 Stoky 5 5 2 1 3 43 45 34 5 3 — 1 3 — 1 39 Tábor 30 31 27 7 23 16 58 401 22 7 12 82 30 27 18 40 Vlašim .... • . . . 30 13 12 4 11 16 35 169 15 5 7 19 10 11 18 41 Votice 22 7 14 5 8 4 38 167 10 4 10 17 19 8 6 42 Vožice, Mladá ~ . . . . 6 8 12 1 9 5 24 90 1 4 1 4 5 3 9 43 Zbraslav*) 53 35 78 34 38 33 84 769 57 39 54 63 19 38 48 44"""

table_text_2 = """Hlavní město Praha . . 3.801 2.896 4.826 1.640 2.684 2.738 6.082 36.097 3.565 1.965 1.804 2.863 1.216 3.228 2.565 Župa I. Praha 1.441 829 2.804 862 1.483 2.829 2.180 17.096 1.516 1.186 2.046 1024 654 971 935 Bechyně 3 1 9 4 4 4 16 66 8 2 8 6 1 6 5 Benešov 36 23 35 15 18 31 36 356 29 13 12 29 28 31 33 Beroun 48 36 65 12 26 27 113 3.727 217 26 1.414 100 60 216 35 Brandýs nad Labem . . 301 98 1.183 61 252 166 262 1.142 100 142 26 76 15 53 145 Brod, Český ~ 86 46 86 61 187 376 95 450 28 26 12 22 16 14 59 Brod, Německý ~ . 33 19 23 13 38 22 67 109 8 7 1 7 7 14 5 Čáslav 67 47 76 41 95 109 118 324 19 10 11 35 39 13 36 Dobříš 12 6 14 5 7 10 23 199 30 11 21 7 8 17 7 Habry 8 3 17 23 22 19 26 98 4 3 2 3 13 14 4 Hora, Kutná ~ 79 81 63 48 74 160 105 375 22 6 8 51 32 41 29 Hořovice 24 28 28 11 18 23 54 987 124 12 260 68 53 84 28 Humpolec 15 8 15 8 13 10 36 102 7 3 7 18 2 3 4 Chotěboř 12 16 12 7 14 33 39 94 9 4 2 5 20 7 9 Janovice, Uhlířské ~ . . 24 7 13 9 11 24 30 161 21 5 5 16 16 5 11 Jílové 23 10 29 8 16 22 27 201 16 8 6 16 2 6 17 Kamenice nad Lipou . . 8 4 5 3 6 5 7 84 3 — 6 15 2 12 5 Karlín*) 102 34 474 39 104 92 108 964 37 291 20 46 11 34 63 Kolín 135 79 111 295 257 916 180 551 48 24 7 47 33 53 50 Kostelec nad Černými Lesy . 8 12 14 8 11 29 34 111 16 8 3 8 5 5 3 Kouřim 30 32 35 37 69 463 85 249 14 12 6 26 18 13 23 Královice, Dolní ~ . 13 13 5 5 5 8 14 110 9 7 1 6 7 7 7 Ledeč nad Sázavou . . . 11 10 19 11 17 18 29 120 4 1 2 5 13 5 11 Milevsko 13 2 9 1 2 2 9 112 9 6 2 9 4 7 12 Mirovice 5 1 4 2 1 — 13 74 9 4 7 9 7 8 7 Neveklov 4 2 10 2 2 6 9 75 4 2 — 8 3 12 4 Pacov 15 6 6 3 10 3 19 65 4 2 2 3 5 3 9 Pelhřimov 16 7 17 4 4 9 24 107 18 2 6 7 7 11 3 Počátky 2 2 7 2 2 5 7 66 5 3 4 10 2 4 2 Polná 4 8 4 — 5 5 13 21 — — — 3 4 1 1 Příbram 23 17 20 8 12 8 45 546 76 7 30 27 72 56 29 Přibyslav 3 12 1 3 6 5 16 35 3 — 3 2 2 1 1 Říčany*) 68 35 97 32 45 38 73 527 46 31 8 38 14 35 45 Sedlčany 4 4 9 4 4 5 14 169 12 6 5 11 5 10 26 Sedlec 7 5 13 2 1 5 27 105 8 2 3 8 9 3 9 Smíchov*) 46 14 120 16 25 45 112 2.920 434 436 44 81 29 74 95 Soběslav 7 2 11 7 8 9 11 64 5 2 8 10 4 6 3 Stoky 5 5 2 1 3 43 45 34 5 3 — 1 3 — 1 Tábor 30 31 27 7 23 16 58 401 22 7 12 82 30 27 18 Vlašim .... • . . . 30 13 12 4 11 16 35 169 15 5 7 19 10 11 18 Votice 22 7 14 5 8 4 38 167 10 4 10 17 19 8 6 Vožice, Mladá ~ . . . . 6 8 12 1 9 5 24 90 1 4 1 4 5 3 9 Zbraslav*) 53 35 78 34 38 33 84 769 57 39 54 63 19 38 48"""

replaced = re.sub('\d+( )\d+', '×', table_text)
print(replaced)


replaced = re.sub(' (?=\d+|—)|(?<=\d|—) ', '×', table_text_2, flags=re.IGNORECASE)
print(replaced)

split_string = replaced.split(sep='×')

n_cols = 16
split_string[:17]

split_string.__len__()
n_rows = len(split_string)//n_cols
list_of_rows = []
for row in range(n_rows):
    list_of_rows.append(split_string[row*n_cols:(row+1)*n_cols])

list_of_rows
741/18
table_text.replace()
table_text.split(' ')
arr = np.array(list_of_rows)
print(arr)

pd.DataFrame(arr)
