#Calculates optimum value of theta through gradient descent.

#we will minimize cost function for each weight individually.
#for example, if y_pred = w0 + w1x1 + w2x2 + ...wnxn,
#then we take Wi and keep all other weights constant, and minimize
#the cost function relative to that combination of weights.
#because the cost function is an nD "bowl" so we need to minimize each
#and every theta.

#because, for some combination of weights other than k, regardless of 
#whether the total value is minimum or not, the slope of the curve with respect
#to that particular weight should be minimum, as it is minimum globally,
#and if it is minimum globally then it should also be minimum locally.


import pandas as pd
import numpy as np
import matplotlib as plt
from math import sqrt

class BinGradientDescent(object):
   
    def __init__(self,X,Y,precision,iterations=int('inf'),wno=False):
        self.iter= iterations
        self.X = X
        self.Y = Y
        self.prec = precision
        if not wno:
            self.wno = X.shape[1]    #if argument not passed, it takes all the features 
            #as the weights in the equations.
        else:
            self.wno = wno
        
        #creating list of weights  
        self.W = pd.series([0] * wno)
    
    def fit(self):
        #applying gradient descent to every single theta.

        #choosing a random bias value initially.
        self.bias = 10
        for i in range(self.X.shape[1]):
            #apply gradient descent to each feature
            high, low = self.choose_high_low(i)
            self.grad_desc_theta(i,high,low)
            #modifies the weight list

    
    def grad_desc_theta(self,index,high,low):
        rows = self.X.shape[0]
        for it in range(self.iter):
            self.W[index] = (high+low)/2
            del_cost = 0
            for i in range(rows):
                y_pred = self.bias + np.dot(self.X.loc[i].values,self.W.values)
                del_cost += 2*((self.Y[i] - y_pred)*(self.X[index]))/rows\
                
            #now checking if it lies in the precision range:
            if (del_cost<self.prec or del_cost > -self.prec):
                #0 +- error 
                break
            else:
                #and now the binary search shift
                if(del_cost>0):
                    #meaning, that the point is in the right side of the graph:
                    high = self.W[index]
                else:
                    #meaning, that the point is in the left side of the graph:
                    low = self.W[index]
    
    def choose_high_low(self,index):
        rows = self.X.shape[0]
        for it in range(self.iter):
            del_cost = 0
            for i in range(rows):
                y_pred = self.bias + np.dot(self.X.loc[i].values,self.W.values)
                del_cost += 2*((self.Y[i] - y_pred)*(self.X[index]))/rows
                
            #now checking if this random point is a high or a low:
            if(del_cost>0):
                #means its a high
                #search for a low.
                pass
                #well at lower value of weight if the slope is high it means the graph is steep
                #thus we need to increase the weight by a certain value

                #calculate the slope for one instance.
                ind = 0
                y_pred2 = self.bias + np.dot(self.X.loc[ind].values,self.W.values)
                slope2 = 2*((self.Y[ind] - y_pred2)*(self.X[index]))/rows
                k =  np.dot(self.X.loc[ind].values,self.W.values) - self.X.loc[ind,index]*self.W[index] - y_pred2
                xi = (self.X.loc[ind,index])
                w1 = (-k + sqrt(k**2 + (4*xi*slope2)))/(2*(xi))
                w2 = (-k - sqrt(k**2 + (4*xi*slope2)))/(2*(xi))
                wnew = self.W
                wnew[index] = w2
                del_costw2 = 0
                for i in range(rows):
                    y_pred = self.bias + np.dot(self.X.loc[i].values,wnew.values)
                    del_costw2 += 2*((self.Y[i] - y_pred)*(self.X[index]))/rows
                if(del_costw2 > 0):
                    return((self.W[index],w2))
                else:
                    del_costw1 = 0
                    wnew[index] = w1
                    for i in range(rows):
                        y_pred = self.bias + np.dot(self.X.loc[i].values,wnew.values)
                        del_costw1 += 2*((self.Y[i] - y_pred)*(self.X[index]))/rows
                    if(del_costw2 > 0):
                        return((self.W[index],w2))
                    else:
                        pass
                        
    
    def check(self):
        pass
