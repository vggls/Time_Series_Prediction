## Intro

This repo aims at presenting different techniques for making time series prediction.

## Approach 1: ARIMA models & LSTM neural networks

- ARIMA_and_LSTM_models.ipynb
- lstm.py

Dataset: https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data

Each datapoint is a daily measurement of 4 features describing climate conditions. We first deal with outliers and the stationarity issue (use ADF test to detect and Differencing technique) and then build one ARIMA model for each feature and one multifeature LSTM model equipped with trend and seasonality features to tackle underfitting. We note that the current LSTM model is not fine tuned (*to do*). However, it still serves our comparison purposes between ARIMA and LSTM. 

#### --> Performance results 
We note that the LSTM outperforms ARIMA in all features.  
        
            | ----------- | ---- MAE ---- |  ----RMSE----- |    
            | feature     | ARIMA   LSTM  |  ARIMA   LSTM  |
            | meantemp    |  5.4    3.87  |   6.24   4.47  |
            | humidity    |  16.55  16.39 |   21.02  18.82 |
            | wind speed  |  3.03   2.94  |   3.92   3.74  |
            | meanpressure|  6.57   5.17  |   8.31   6.67  |
            ------------------------------------------------
            where MAE = Mean Absolute Error, RMSE = sqRt of Mean Squared Error

#### --> A short recap on theory basics
*(more detail to be added)*
   <p align="left">
     <img src="https://github.com/vggls/Time_Series_Prediction/assets/55101427/07720097-63b5-457a-b49d-217c9e734d13.png" height="360" width="500" />
     <img src="https://github.com/vggls/Time_Series_Prediction/assets/55101427/e71dc391-dc56-4118-94ef-e8ab45e586ef.png" height="670" width="500" />
   </p>
<!-- Good source article on ARIMA models: https://www.capitalone.com/tech/machine-learning/understanding-arima-models/ -->

## Approach 2: Hankel Matrix and DMD algorithm

- HankelMatrix_and_DMDalg__model.ipynb

Dataset: We consider a 35-year (Rhine) river level dataset where each time observation describes the water level at that time for multiple cities located across the river. The task is to build a model that predicts the river's future water level for each city. The dataset cannot be made public.

In this approach we see the time data points as snapshots of an underlying non-linear dynamical system. First we build the time-delayed Hankel matrix in order to embed the system into a space where it behaves  similar to a linear system. We conclude that by observing the time-evolution of the principal components of the Hankel matrix.
Then, taking advantage of the "linear" behaviour of our system, we refer to the Dynamic Mode Decomposition (DMD) of the Hankel matrix in order to
determine the DMD nodes of the system and make predictions about future behaviour.

Useful Links:
  - Hankel matrix : https://en.wikipedia.org/wiki/Hankel_matrix
  - DMD : https://en.wikipedia.org/wiki/Dynamic_mode_decomposition
