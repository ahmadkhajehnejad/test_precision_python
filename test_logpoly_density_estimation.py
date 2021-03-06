import numpy as np
import logpoly.tools
from logpoly.model import Logpoly
from logpoly.tools import compute_SS

x = np.load('./data/synthetic.npy')
min_x = np.min(x, axis=0)
max_x = np.max(x, axis=0)
x = logpoly.tools.scale_data(x, min_x, max_x)

n = len(x)
poly_degree = 18
SS = compute_SS(x, poly_degree)
logpoly_density_estimator = Logpoly()
logpoly_density_estimator.fit(SS, n)

print(np.sum(logpoly_density_estimator.logpdf(x)))
print(logpoly_density_estimator.logZ)

print(np.sum( np.exp( logpoly_density_estimator.logpdf( np.arange(0, 1, 0.001) ) ) ) / 1000)