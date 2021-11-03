"""Perceptron Class

Returns:
    [python Object]: returns model object
"""

import numpy as np
import pandas as pd

import logging
# logging_str = " [ %(asctime)s:%(levelname)s:%(module)s ] : %(message)s"
# logging.basicConfig(level=logging.INFO,format=logging_str)

from tqdm import  tqdm

class Perceptron:
  def __init__(self):
    self.weights = None
    self.eta = 0.01
    self.epochs = 1
    self.error=0

  def activationFunction(self,input):
    z = np.dot(input,self.weights)
    return np.where(z>0,1,0)

  def fit(self,X,y,eta=0.01,epochs=1):
    self.eta=eta
    self.epochs=epochs

    X_with_bias = np.c_[X,-np.ones((len(X),1))]
    self.weights = np.random.randn(X_with_bias.shape[1])* 1e-4

    for i in tqdm(range(0,self.epochs),total=self.epochs,desc="training model"):
      y_hat = self.activationFunction(X_with_bias)
      self.error = y-y_hat
      self.weights = self.weights + self.eta * np.dot(X_with_bias.T, self.error)
      logging.info(f'At Epochs {i+1} Weights :{self.weights} ; Error : {sum(self.error*self.error)}')

      logging.info("--"*20)

  def predict(self, X):
    X_with_bias = np.c_[X, -np.ones((len(X), 1))]
    return self.activationFunction(X_with_bias)
    