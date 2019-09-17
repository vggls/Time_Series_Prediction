# time_series_prediction_hankel_and_dmd

In this repo we consider the free "Air Passengers" time series dataset which is available on Kaggle.

The task is to build a prediction model. 

Instead of using RNNs, which seem to be one of the most common approaches, here we see the data points as snapshots of an underlying
non-linear dynamical system. First we build the time-delayed Hankel matrix in order to embed the system into another one which is 
close to a linear system. We conclude that by observing the time-evolution of the principal components of the Hankel matrix.

Then, taking advantage of the "linear" behaviour of our system, we refer to the Dynamic Mode Decomposition of the Hankel matrix in order to
determine the DMD modes of the system and make predictions about the future behaviour of our system.


Remark
Looking at the results in the end of the notebook we observe that the model does not seem to work perfectly close to the actual data points.
Any corrections and remarks are more than welcome !
However, in any case, this short repo could be seen as a chance to get an idea of both the Hankel matrix and the DMD algorithm and
its use for making predictions.
