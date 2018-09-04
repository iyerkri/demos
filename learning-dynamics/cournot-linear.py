#! /usr/bin/env python

import numpy

# Pricing function is P(Q) = a - bQ
a = 9
b = 1

# Production cost c_i(q_i) = c_iq_i. The value of c_i is below.
c=[1,0.5]

# number of iterations
num_iter=25



# Each firms' quantity
quantity = numpy.zeros([num_iter,3])
quantity[0,0] = 3.6
quantity[0,1] = 0.1


# Best response function
# BR_i(q_{-i}) = \{ \frac{(a - c_i - q_{-i})^+}{2} \}

for i in range(1, num_iter):
    quantity[i,0] = max((a - c[0] - quantity[i-1,1])/2,0)
    quantity[i,1] = max((a - c[1] - quantity[i-1,0])/2,0)
    quantity[i,2] = i/num_iter 




# First two columns are production levels for the two firms, and the
# third column is the (normalized) number of iterations
numpy.savetxt("best-response",quantity)
