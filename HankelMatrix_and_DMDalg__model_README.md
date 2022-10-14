# README

We consider a 35-year river level dataset and the task is to build a prediction model. 

Instead of using RNNs, which seem to be one of the most common approaches, here we see the data points as snapshots of an underlying
non-linear dynamical system. First we build the time-delayed Hankel matrix in order to embed the system into a space where it behaves  similar to a linear system. We conclude that by observing the time-evolution of the principal components of the Hankel matrix.

Then, taking advantage of the "linear" behaviour of our system, we refer to the Dynamic Mode Decomposition (DMD) of the Hankel matrix in order to
determine the DMD modes of the system and make predictions about the future behaviour of our system.

Useful Links
- Hankel matrix : https://en.wikipedia.org/wiki/Hankel_matrix
- DMD : https://en.wikipedia.org/wiki/Dynamic_mode_decomposition
