In thie repo we consider a river level dataset across 15 German countries.

We build a predictor model using LSTM RNNs.

The code file is structured as follows :

1) The dataset

2) Preparing the data : deal with Nan values, normalize data, construct training+test set )

3) The model : hyper-parameters tuning by picking the final model (among 54 different ones) which has (a) very low validation loss 
AND (b) very small distance between its loss and validation loss final values.

Due to small computational power and in the interest of space, we do not cross-validate each candidate model. Of course, one could try so.

4) Predictions : we build a function which uses the final(optimal) model to make river level predictions.

5) An example
