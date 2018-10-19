'''
Hero's Method

Cool algorithm to calculate a square root
Without using sqrt function
Developed in ancient Babylon by Hero
Circa the 1st Century AD

Hero's method is an interative minimization algorithm:
Let x be some number you wish to calculate the square root of
Let g be an initial guess of the sqrt(x) such that g >> sqrt(x)
x/g will underestimate sqrt(x)
Therefore the average of g and x/g will be closer to sqrt(x) than
either g or x

By Matt Stetz
01/2018
'''

#####################################
#Import Libraries

from __future__ import division
import numpy as np
import pylab as plt

#####################################
#User input below:

#Number you want to calculate the square root of:
X = 25698309433

#Initial Guess (Overstimate Square Root)
GUESS = 700000 

#Number of Iterations
ITERATIONS = 1000000000

#Desired numerical precision
PRECISION = 0.001

#####################################

#function to perform hero's method
def hero(x,guess,iterations,precision):
     i = 0
     guess_log = [guess]
     counter_log = [i]
     print ('Inital guess: '+str(guess)+'\n')
     #check convergence with while loop to avoid memory limits
     #for large number of iterations
     while i <= iterations:
          #this conditional style is supported in Python
          if x-precision < guess**2 < x+precision:
               print ('\nSolution Found = '+str(guess))
               print ('Solution Squared = '+str(guess**2))
               break
          #new guess
          else:
               guess = (guess+(x/guess))/2.0
               guess_log.append(guess)
               counter_log.append(i)
               print ('New guess '+str(i+1)+': '+str(guess))
               i += 1
     return guess_log,counter_log

#visualize results
def plot(guess_log,counter_log,x):
     correct_sqrt = np.sqrt(x)
     x_axis = np.linspace(-1, 1.1*len(guess_log), len(guess_log))
     y_axis = np.ones(len(guess_log))*correct_sqrt
     plt.plot(counter_log, guess_log,'ok')
     plt.plot(x_axis, y_axis, '--r', linewidth=2.0, label='Correct Answer')
     plt.axis([-1, max(x_axis), -0.1*max(guess_log), 1.1*max(guess_log)])
     plt.xlabel('Iterations')
     plt.ylabel('Guess')
     plt.legend(loc = 'upper right')
     plt.show()
     return 0

if __name__ == '__main__':
     GUESS_LOG,COUNTER_LOG = hero(X,GUESS,ITERATIONS,PRECISION)
     plot(GUESS_LOG,COUNTER_LOG,X)
