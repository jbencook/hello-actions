import math


def almost_pi(n_terms: int = 21) -> float:
    """Generate estimate of pi"""
    return (
        math.sqrt(12) *
        sum(((-3)**-k)/(2*k + 1) for k in range(n_terms))
    )
