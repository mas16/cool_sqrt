# Hero's Method for Determining Square Roots

by Matt Stetz
Jan 2018

## Introduction

I was watching an MIT Open Courseware Lecture on YouTube and the professor introduced an algorithm for calculating square roots of non-negative numbers based on an iterative minimization routine. The algorithm originated in ancient Babylon circa 1 AD and is attributed to the mathematican Hero of Alexandria also known as Heron of Alexandria (better known for determining how to calculate the area of triangles).

The algorithm is based on a simple iterative routine:

* Define a number, x, that you wish to compute the square root of

* Make an initial guess, g, for the sqrt(x) that is an overestimate

* Calculate x/g

* average g and x/g to get a new g

* iterate until the difference between g^2 and x is minimized

## Instructions

This script asks the user to define some variable:

* X = numer you want to calculate the square root of

* GUESS = initial guess (should overestimate)

* ITERATIONS = number of iterations allowed before script quits (set arbitrarily high)

* PRECISION = the desired numerical precision as floating point decimal e.g. 0.001, 0.0000000001, etc.

## Output

The script will print the following output:

* Initial Guess

* Each new guess with every iteration

* Converged solution

* Square of the converged solution

* Image file of a plot of GUESS vs. Iteration number 

## Setting the Convergence Criterion

I have define convergence to be when GUESS^2 is in [X-PRECISION,X+PRECISION]
