import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from keras.optimizers import Adam    

def lstm_train_val_data(dataframe):

    scaler = MinMaxScaler(feature_range=(-1, 1))

    df = dataframe.copy()
    df.index = df.index.strftime('%Y-%m-%d')
    train_indices = df.index[df.index.str.contains('|'.join(['2013', '2014', '2015']))]
    val_indices = df.index[df.index.str.contains('2016')]

    scaled_training = scaler.fit_transform(df.loc[train_indices])
    scaled_val = scaler.transform(df.loc[val_indices])

    x_train, y_train = scaled_training[:-1,:], scaled_training[1:,:]
    x_train = np.reshape(x_train, (x_train.shape[0], 1, x_train.shape[1]))
    y_train = np.reshape(y_train, (y_train.shape[0], 1, y_train.shape[1]))

    x_val, y_val= scaled_val[:-1,:], scaled_val[1:,:]
    x_val = np.reshape(x_val, (x_val.shape[0], 1, x_val.shape[1]))
    y_val = np.reshape(y_val, (y_val.shape[0], 1, y_val.shape[1]))

    return x_train, y_train, x_val, y_val, scaler

class model():

    def __init__(self, x_train, y_train, x_val, y_val):

        self.x_train = x_train
        self.y_train = y_train
        self.x_val = x_val
        self.y_val = y_val

    def fit(self):

        #Build the LSTM model
        model = Sequential()
        model.add(LSTM(256, return_sequences=True, input_shape=(self.x_train.shape[1], self.x_train.shape[2])))
        model.add(Dropout(0.2))
        model.add(LSTM(128, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(64, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(64, return_sequences=False))
        model.add(Dropout(0.2))
        model.add(Dense(64))
        model.add(Dropout(0.2))
        model.add(Dense(32))
        model.add(Dense(self.x_train.shape[2]))

        # Compile the model
        opt = Adam(learning_rate=0.001)
        model.compile(optimizer=opt, loss='mean_squared_error')

        #Train the model
        model.fit(self.x_train, self.y_train, batch_size=128, epochs=10, 
                  validation_data=(self.x_val, self.y_val))

        return model