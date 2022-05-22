# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    df=pd.read_csv('data.csv', sep=',')

#    print(df["Date"].unique())
    print(df["Region"].unique())

    print('\tilk ülkeyi giriniz:')

    x = input()

    print('\tikinci ülkeyi giriniz:')

    y = input()

    df1 = df.query("Region == @x")
    df2 = df.query("Region == @y")

    z = 0
    benzerlik = {}
    #print(df2["Region"])

    '''for i in df1:
        for j in df2:
            if(i[1] == j[1] and i[5] == j[5]):
                benzerlik[z] += 1
        z += 1'''
    for date in df1["Date"].unique():
        df11 = df1.query("Date == @date")
        df22 = df2.query("Date == @date")
        if date[9] == '0':
            print(date)
            for i, rowi in df11.iterrows():
                for j, rowj in df22.iterrows():
                    if(rowi[1] == rowj[1] and rowi[5] == rowj[5]):
                        tarih = datetime.strptime(rowi["Date"], '%Y-%m-%d')
                        tarih = tarih.toordinal()
                        if tarih in benzerlik:
                            benzerlik[tarih] = benzerlik[tarih] + 1
                        else:
                            benzerlik[tarih] = 1



    X = np.array(list(benzerlik.keys()))
    Y = np.array(list(benzerlik.values()))

#    print(X)
#    print(Y)

    xreshaped = np.reshape(X,(-1,1))
    yreshaped = np.reshape(Y,(-1,1))

    model = LinearRegression()
    model.fit(xreshaped, yreshaped)
    modelscore = model.score(xreshaped, yreshaped)

    prediction_date = "2018-01-09"
    print("Tahmin edilecek tarih = " + prediction_date)


    guess = datetime.strptime(prediction_date, '%Y-%m-%d')
    guess = guess.toordinal()

    guessreshaped = np.reshape(guess, (-1,1))

    prediction = model.predict(guessreshaped)

    print("\nTahmin Edilen Benzerlik")
    print(prediction)

    print("\nModel Başarısı")
    print(modelscore)


    plt.scatter(xreshaped, yreshaped, color = "red")
    plt.plot(xreshaped, model.predict(xreshaped), color = "blue", linewidth = 3)

    plt.xticks(())
    plt.yticks(())

    plt.show()
 #   print(benzerlik)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/