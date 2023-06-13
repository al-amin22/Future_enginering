#future engineering
'''
tahap-tahap dalam proses futere enginering
1. memproses nilai kosong (na/nan)
2. variabel yang berhubungan dengan waktu
3. variabel yang tidak berdistribusi normal
4. menghilangkan varibel jarang untuk tipe katagori
5. merubah format data dtring ke numerik untuk tipe katagorri
6. menyamakan rentang data nilai untuk beberapa variabel

'''

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action='ignore')

#mengimpor data set
data_asli = pd.read_csv('harga_rumah.csv') 
dataku = pd.read_csv('harga_rumah.csv') 

#membagi menjadi dua data yaitu training dan test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(dataku, dataku['SalePrice'],
                                                    test_size = 0.1, random_state = 10)
#mengatasi data kosong untuk tipe data katagori
kolom_na_kategori = [kolom for kolom in dataku.columns if dataku[kolom].isnull().sum()
                     >0 and dataku[kolom].dtypes == 'object']
#MENGHITUNG DATA KATOGORI YANG KOSONG
dataku[kolom_na_kategori].isnull().mean()*100

#mengganti data kosong untuk tipe katagori dengan kategori kosong
x_train[kolom_na_kategori] = x_train[kolom_na_kategori].fillna('kosong')
x_test[kolom_na_kategori] = x_test[kolom_na_kategori].fillna('kosong')

#memastikan tidak ada data kosong untuk tipe katagori di training test
x_train[kolom_na_kategori].isnull().sum()
x_test[kolom_na_kategori].isnull().sum()

#mendeteksi data kosong untuk tipe data numerik
kolom_na_numerik = [kolom for kolom in dataku.columns if dataku[kolom].isnull().sum()
                    >0 and dataku[kolom].dtypes != 'object']
dataku[kolom_na_numerik].isnull().mean()*100

#mengganit data kosong numerik dengan modus atau nilai terbanyak
for kolom in kolom_na_numerik:
    #menghitung modus
    hitung_modus = x_train[kolom].mode()[0]
    #menambahkan kolom baru mendeteksi data kosong per barisnya
    x_train[kolom +'_na']= np.where(x_train[kolom].isnull(), 1, 0)
    x_test[kolom +'_na']= np.where(x_test[kolom].isnull(), 1, 0)
    x_train[kolom] = x_train[kolom].fillna(hitung_modus)
    x_test[kolom] = x_test[kolom].fillna(hitung_modus)
    
#mendeteksi tidak ada data kosong 
x_train[kolom_na_numerik].isnull().sum()
x_test[kolom_na_numerik].isnull().sum()