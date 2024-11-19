"""
Extinction Law from Damineli et al (2016), derived to be representative
of the Galactic plane, |b|<5 deg.

Valid from 0.4-4.8 microns.

Source DOI: 10.1093/mnras/stw2122
"""

__all__ = ["Damineli2016", ]
__author__ = "M.J. Huston"
__date__ = "2024-04-18"
__license__ = "GPLv3"
__version__ = "1.0.0"

from ._extinction import ExtinctionLaw
import numpy as np


class Damineli2016(ExtinctionLaw):
    """
    Good for 0.4-4.8 microns.
    """

    def __init__(self, **kwargs):
        self.extinction_law_name = 'Damineli2016'
        self.law_ref_wavelength = 2.159
        self.min_wavelength = 0.4
        self.max_wavelength = 4.8

    def Alambda_Aref(self, eff_wavelength: float) -> float:
        """
        Given an effective wavelength lambda_eff, calculate the relative extinction A_lambda/A_V

        Parameters
        ----------
        eff_wavelength : float
            Effective Wavelength of the filter for which the extinction should be determined.
            in micrometer
        """

        x = np.log10(2.159/eff_wavelength)
        Alam_AKs = 10**(-0.015 + 2.330*x + 0.522*x**2 - 3.001*x**3 + 2.034*x**4)

        return Alam_AKs