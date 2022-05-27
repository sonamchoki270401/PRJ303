import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
from sklearn import preprocessing


def model_api(test):
    df = pd.read_csv(
        "/Users/sonamchoki/Desktop/WEATHER FORECAST/seattle_weather.csv", index_col="date")
    df.index = pd.to_datetime(df.index)

    # Label Encoding
    ladel_encoding = preprocessing.LabelEncoder()
    ladel_encoding.fit(df[['weather']])
    new_y = ladel_encoding.transform(df[['weather']])

    new_ydf = pd.DataFrame(data=new_y, columns=['weather'], index=df.index)
    new_df = pd.concat([df.iloc[:, :-1], new_ydf], axis=1)

    Q1 = new_df.precipitation.quantile(0.25)
    Q3 = new_df.precipitation.quantile(0.75)
    IQR = Q3 - Q1
    upperlimit = Q3 + (IQR * 1.5)
    lowerlimit = Q1 - (IQR * 1.5)

    new_df[(new_df.precipitation < lowerlimit) |
           (new_df.precipitation > upperlimit)]
    newdf = new_df[(new_df.precipitation > lowerlimit) &
                   (new_df.precipitation < upperlimit)]

    Q1 = new_df.wind.quantile(0.25)
    Q3 = new_df.wind.quantile(0.75)
    IQR = Q3 - Q1
    upperlimit = Q3 + (IQR * 1.5)
    lowerlimit = Q1 - (IQR * 1.5)

    new_df[(new_df.wind < lowerlimit) | (new_df.wind > upperlimit)]
    newdf = new_df[(new_df.wind > lowerlimit) & (new_df.wind < upperlimit)]

    X = newdf.iloc[:, :-1]
    y = newdf.iloc[:, -1]

    from sklearn.model_selection import train_test_split
    xtrain, xtest, ytrain, ytest = train_test_split(
        X, y, test_size=0.25, random_state=5)

    #from sklearn.ensemble import RandomForestClassifier

    #model = RandomForestClassifier(n_estimators= 50,min_samples_leaf=50)
   # model.fit(xtrain, ytrain)
    from sklearn.linear_model import LogisticRegression

    Logre = LogisticRegression(random_state=0)
    Logre.fit(xtrain, ytrain)
    #result_pre = model.predict(np.reshape(test,(1, -1)))
    y_hat = Logre.predict(np.reshape(test, (1, -1)))
    return "The predicted weather is : ", str(ladel_encoding.inverse_transform(y_hat)[0])

    # return "The predicted weather is : ",ladel_encoding.inverse_transform(result_pre)[0]
