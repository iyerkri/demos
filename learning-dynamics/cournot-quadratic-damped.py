#! /usr/bin/env python

import numpy

# Pricing function is P(Q) = a - bQ
a = 9
b = 1

# Production cost c_i(q_i) = c_i(q_i)^2. The value of c_i is below.
c=[1,0.5]

# number of iterations
num_iter=25



# Each firms' quantity
quantity = numpy.zeros([num_iter,3])
quantity[0,0] = 8.0
quantity[0,1] = 4.5


# Best response function
# BR_i(q_{-i}) = \{ \frac{(a - q_{-i})^+}{2+c_i} \}

# Damping factor
alpha = 0.2

for i in range(1, num_iter):
    quantity[i,0] = (1-alpha)*quantity[i-1,0] + alpha*max((a  - quantity[i-1,1])/(2+c[0]),0)
    quantity[i,1] = (1-alpha)*quantity[i-1,1] + alpha*max((a  - quantity[i-1,0])/(2+c[1]),0)
    quantity[i,2] = i/num_iter 

# First two columns are production levels for the two firms, and the
# third column is the (normalized) number of iterations
numpy.savetxt("best-response",quantity)
