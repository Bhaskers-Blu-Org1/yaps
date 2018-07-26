import sys
import os
sys.path.append(os.path.abspath(os.path.join('..', 'yaps')))

from yaps.lib import int, real, uniform, bernoulli
import yaps as yaps

@yaps.model
def coin(x: int(lower=0, upper=1)[10]):
    theta: real(lower=0, upper=1) is uniform(0, 1)
    for i in range(10):
        x[i] is bernoulli(theta)


flips = [0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
print(coin.stan_code)

fit = yaps.infer(coin(x=flips),
                iter=1000)
print(fit)