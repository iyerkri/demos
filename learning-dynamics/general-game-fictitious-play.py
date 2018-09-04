#! /usr/bin/env python
import numpy

# number of iterations
num_iter = 100

# payoff matrix for the two players in the 2x2 game
# first two rows are player 1's payoff matrix, and the last two player 2's
payoff_matrix = numpy.zeros([4,2])

# 'strategy' stores the strategy played in each time period
strategy = numpy.zeros([num_iter,3])

# 'empirical' stores the empirical distribution at each time period
empirical = numpy.zeros([num_iter,3])

# 'payoffs' stores the payoff for each player, assuming the other
# player plays according to the empirical distribution
payoffs = numpy.zeros([2,2])

# matching pennies
payoff_matrix[:2,:] = [ [1, -1], [-1, 1]]
payoff_matrix[2:,:] = [ [-1, 1], [1, -1]]

# coordination game
#payoff_matrix[:2,:] = [ [1, 0], [0, 2]]
#payoff_matrix[2:,:] = [ [2, 0], [0, 1]]
#strategy[0,1] = 1
#empirical[0,1] = 1

# prisoner's dilemma
# payoff_matrix[:2,:] = [ [-1, -10], [0, -5]]
# payoff_matrix[2:,:] = [ [-1, 0], [-10, -5]]
# strategy[0,0] = 1
# strategy[0,1] = 1
# empirical[0,0] = 1
# empirical[0,1] = 1


for i in range(1,num_iter):
    
    # calculate payoff of player 1 assuming the other player plays according to empirical dist.
    payoffs[0,0] = empirical[i-1,1]*payoff_matrix[0,0] + (1-empirical[i-1,1])*payoff_matrix[0,1]
    payoffs[1,0] = empirical[i-1,1]*payoff_matrix[1,0] + (1-empirical[i-1,1])*payoff_matrix[1,1]

    # calculate payoff of player 2 assuming the other player plays according to empirical dist.
    payoffs[0,1] = empirical[i-1,0]*payoff_matrix[2,0] + (1-empirical[i-1,0])*payoff_matrix[3,0]
    payoffs[1,1] = empirical[i-1,0]*payoff_matrix[2,1] + (1-empirical[i-1,0])*payoff_matrix[3,1]


    # player 1's best response
    if payoffs[0,0] < payoffs[1,0]:
        strategy[i,0] = 0
    elif payoffs[0,0] > payoffs[1,0]:
        strategy[i,0] = 1
    else:
        strategy[i,0] = strategy[i-1,0]


    # player 2's best response
    if  payoffs[0,1] < payoffs[1,1]:
        strategy[i,1] = 0
    elif payoffs[0,1] > payoffs[1,1]:
        strategy[i,1] = 1
    else:
        strategy[i,1] = strategy[i-1,1]


    # update the empirical distribution
    empirical[i,0] = ((i-1)*empirical[i-1,0] + strategy[i,0])/i
    empirical[i,1] = ((i-1)*empirical[i-1,1] + strategy[i,1])/i
        
    # store the (normalized) number of iterations
    strategy[i,2] = i/num_iter
    empirical[i,2] = i/num_iter

# save files
numpy.savetxt('strategy', strategy)
numpy.savetxt('empirical',empirical)
