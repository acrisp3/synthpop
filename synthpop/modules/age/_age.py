"""
The base class for age distribution modules.
"""

__all__ = ["Age", ]
__date__ = "2022-06-27"
__version__ = '1.0.0'

from abc import ABC, abstractmethod
from types import ModuleType
import numpy as np
from .. import const, default_sun

class Age(ABC):
    """
    The Age base class. 
    """

    def __init__(self, sun: ModuleType = None,
            coord_trans: ModuleType = None,
            logger: ModuleType = None,
            **kwargs):
        """
        Initialize the Age class.
        """

        #: name for age distribution
        self.age_func_name = 'None' 
        #: solar parameters
        self.sun = sun if sun is not None else default_sun
        #: coordinate transformation module
        self.coord_trans = coord_trans #: coordinate transformation module
        #: logger module
        self.logger = logger 

    @abstractmethod
    def draw_random_age(self, N: int = None) -> np.ndarray or float:
        """
        Generate a random age from the distribution

        Parameters
        ----------
        N : int, None, optional
            if N is set to an integer, an array with N random ages is returned
        
        Returns
        -------
        random_age : ndarray or float [Gyr]
            array of random ages
        """
        raise NotImplementedError('No age subclass set')

    @abstractmethod
    def average_age(self) -> float:
        """
        Returns the average age of the distribution
        """
        raise NotImplementedError('No age subclass set')

    @abstractmethod
    def get_maximum_age(self) -> float:
        """
        Returns the maximum age generated by the distribution
        if there is no maximum, it should return None.
        """
        return None