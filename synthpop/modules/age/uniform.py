""" A uniform age distribution """

__all__ = ["Uniform", ]
__author__ = "S. Johnson"
__date__ = "2022-07-06"
__license__ = "GPLv3"
__version__ = "1.0.0"

import numpy as np
from ._age import Age

class Uniform(Age):
    """
    Uniform subclass of Age base class. This subclass is for Populations that
    have ages characterized by a uniform distribution between two bounds. 
    """

    def __init__(self, low_bound: float, high_bound: float, **kwargs):
        super().__init__(**kwargs)
        #: age distribution name
        self.age_func_name = 'uniform'
        #: lower age limit in Gyr
        self.low_bound = low_bound
        #: upper age limit in Gyr
        self.high_bound = high_bound

    def draw_random_age(self, N: float or None = None) -> np.ndarray or float:
        """
        Generate a random age or ages from a uniform distribution

        Parameters
        ----------
        N : int, None, optional
            if N is set to an integer, an array with N random ages is returned

        Returns
        -------
        age : ndarray, float [Gyr]
            single age or numpy array of N ages in gigayears
        """
        return np.random.uniform(self.low_bound, self.high_bound, N)

    def average_age(self) -> float:
        """Return the average age of the population"""
        return (self.low_bound + self.high_bound) / 2.0

    def get_maximum_age(self) -> float:
        """ Return the maximum age that can be generated by the distribution."""
        return self.high_bound