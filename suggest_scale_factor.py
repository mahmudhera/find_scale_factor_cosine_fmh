"""
Suggest a scale factor given
- num of elements in sets
- desired error
- desired confidence
"""

import math
from scipy.stats import norm


def get_min_scale_factor2(n1, n2, size_intersection, error, confidence):
    c = norm.ppf(confidence/2+0.5)
    p = size_intersection

    a = c**2 * ( (n1-p)*(n2-p)/(n1*n2) )**0.5
    b = c * ( ( (n1-p)/(n1*p) )**0.5 + ( (n2-p)/(n2*p) )**0.5 )
    c = -error

    x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)

    print(1.0/(1.0+x1), 1.0/(1.0+x2))
    exit(-1)



def get_min_scale_factor(n1, n2, error, confidence):
    epsilon = error * 2 / 5
    q = 6.0 / (1.0 - confidence)
    log_q = math.log(q)
    min_scale_factor = 3.0 * log_q / ( min(n1, n2) * epsilon**2 )
    return min(min_scale_factor, 1.0)

if __name__ == '__main__':
    n1 = 1000000
    n2 = 1000000
    error = 0.1
    confidence = 0.9
    print(get_min_scale_factor(n1, n2, error, confidence))

    get_min_scale_factor2(n1, n2, 100000, error**2, confidence)


