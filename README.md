## Intro

This repo aims at presenting different techniques for making time series prediction.

## Approach 1: ARIMA models & LSTM neural networks

(to do)

## Approach 2: Hankel Matrix and DMD algorithm

HankelMatrix_and_DMDalg__model.ipynb

In this approach we see the time data points as snapshots of an underlying non-linear dynamical system. First we build the time-delayed Hankel matrix in order to embed the system into a space where it behaves  similar to a linear system. We conclude that by observing the time-evolution of the principal components of the Hankel matrix.
Then, taking advantage of the "linear" behaviour of our system, we refer to the Dynamic Mode Decomposition (DMD) of the Hankel matrix in order to
determine the DMD nodes of the system and make predictions about future behaviour.

Useful Links
- Hankel matrix : https://en.wikipedia.org/wiki/Hankel_matrix
- DMD : https://en.wikipedia.org/wiki/Dynamic_mode_decomposition

Dataset: We consider a 35-year (Rhine) river level dataset where each time observation describes the water level at that time for multiple cities located across the river. The task is to build a model that predicts the river's future water level for each city. The dataset cannot be made public.