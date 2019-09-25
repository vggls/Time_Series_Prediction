# time_series_prediction_hankel_and_dmd

We consider a river level dataset and the task is to build a prediction model. 

Instead of using RNNs, which seem to be one of the most common approaches, here we see the data points as snapshots of an underlying
non-linear dynamical system. First we build the time-delayed Hankel matrix in order to embed the system into a space where it behaves  
similar to a linear system. We conclude that by observing the time-evolution of the principal components of the Hankel matrix.

Then, taking advantage of the "linear" behaviour of our system, we refer to the Dynamic Mode Decomposition of the Hankel matrix in order to
determine the DMD modes of the system and make predictions about the future behaviour of our system.
