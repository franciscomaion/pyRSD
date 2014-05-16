"""
Simulation data for dark matter power spectra at 3 redshifts, z = 0, 0.509, 0.987

For more, see the detailed description of these simulations in Okumura et al. 2012.
"""

import os as _os

import numpy as np
from pyRSD import data_dir


__all__ = ['load',
           'P00_mu0_z_0_000',
           'P00_mu0_z_0_509',
           'P00_mu0_z_0_989',
           'P01_mu2_z_0_000',
           'P01_mu2_z_0_509',
           'P01_mu2_z_0_989',
           'Pdv_mu0_z_0_000',
           'Pdv_mu0_z_0_509',
           'Pdv_mu0_z_0_989',
           'P11_mu4_z_0_000',
           'P11_mu4_z_0_509',
           'P11_mu4_z_0_989', 
           'Pcc_z_0_509',
           'PcAs_z_0_509',
           'PsAsA_z_0_509',
           'PsAsB_z_0_509', 
           'PcAs_sat_replaced_z_0_509',
           'PsAsA_sat_replaced_z_0_509', 
           'PsAsB_sat_replaced_z_0_509',
           'Pgg_z_0_509']

#-------------------------------------------------------------------------------
def load(f):
    """
    Load the power spectrum data file located in the data directory.

    Parameters
    ----------
    f : string
        File name.

    Returns
    -------
    data : ndarray, shape (N, 2)
        Data loaded from pyRSD.data_dir. Columns are k, P(k)
    """
    return np.loadtxt(_os.path.join(data_dir, f))

#-------------------------------------------------------------------------------
# GALAXY SIM DATA
#-------------------------------------------------------------------------------
def Pcc_z_0_509():
    """
    The central-central auto spectrum at z = 0.509. It has 13 columns, as
    follows:

    1st: k
    2nd: P_cc^s(k,\mu=0.1)
    3rd: its error
    4th: P_cc^s(k,\mu=0.3)
    5th: its error
    ...
    10th: P_cc^s(k,\mu=0.9)
    11th: its error
    12th: P_cc^r(k)
    13th: its error
    """
    return load("galaxy/2-halo/pkmu_s_r_c_c_00020_30000_z005_1-3_02-13aaan")
#-------------------------------------------------------------------------------
def PcAs_z_0_509():
    """
    The cross spectrum of centrals with no sats and satellites at z = 0.509. 
    It has 13 columns, as follows: 

    1st: k
    2nd: P_cAs^s(k,\mu=0.1)
    3rd: its error
    4th: P_cAs^s(k,\mu=0.3)
    5th: its error
    ...
    10th: P_cAs^s(k,\mu=0.9)
    11th: its error
    12th: P_cAs^r(k)
    13th: its error
    """
    return load("galaxy/2-halo/pkmu_s_r_f_s_00020_30000_z005_1-3_02-13aaan")
#-------------------------------------------------------------------------------
def PsAsA_z_0_509():
    """
    The auto spectrum of satellites with no sats in the same halo at z = 0.509. 
    It has 13 columns, as follows:

    1st: k
    2nd: P_sAsA^s(k,\mu=0.1)
    3rd: its error
    4th: P_sAsA^s(k,\mu=0.3)
    5th: its error
    ...
    10th: P_sAsA^s(k,\mu=0.9)
    11th: its error
    12th: P_sAsA^r(k)
    13th: its error
    """
    return load("galaxy/2-halo/pkmu_s_r_i_i_00020_30000_z005_1-3_02-13aaan")
#-------------------------------------------------------------------------------
def PsAsB_z_0_509():
    """
    The cross spectrum of satellites with and without sats in the same halo 
    at z = 0.509. It has 13 columns, as follows: 

    1st: k
    2nd: P_sAsB^s(k,\mu=0.1)
    3rd: its error
    4th: P_sAsB^s(k,\mu=0.3)
    5th: its error
    ...
    10th: P_sAsB^s(k,\mu=0.9)
    11th: its error
    12th: P_sAsB^r(k)
    13th: its error
    """
    return load("galaxy/2-halo/pkmu_s_r_i_j_00020_30000_z005_1-3_02-13aaan")
#-------------------------------------------------------------------------------
def PcAs_sat_replaced_z_0_509():
    """
    The cross spectrum of centrals with no sats and satellites at z = 0.509,
    with satellite positions/velocities replaced by those of the halo. 
    It has 11 columns, as follows: 

    1st: k
    2nd: P_cAs^s(k,\mu=0.1)
    3rd: its error
    4th: P_cAs^s(k,\mu=0.3)
    5th: its error
    ...
    10th: P_cAs^s(k,\mu=0.9)
    11th: its error
    """
    return load("galaxy/2-halo/pkmu_s_f_v_00020_30000_z005_1-3_02-13aaan")
#-------------------------------------------------------------------------------
def PsAsA_sat_replaced_z_0_509():
    """
    The auto spectrum of satellites with no sats in the same halo at z = 0.509,
    with satellite positions/velocities replaced by those of the halo.  
    It has 11 columns, as follows:

    1st: k
    2nd: P_sAsA^s(k,\mu=0.1)
    3rd: its error
    4th: P_sAsA^s(k,\mu=0.3)
    5th: its error
    ...
    10th: P_sAsA^s(k,\mu=0.9)
    11th: its error
    """
    return load("galaxy/2-halo/pkmu_s_w_w_00020_30000_z005_1-3_02-13aaan")
#-------------------------------------------------------------------------------
def PsAsB_sat_replaced_z_0_509():
    """
    The cross spectrum of satellites with and without sats in the same halo 
    at z = 0.509, with satellite positions/velocities replaced by those of 
    the halo.  It has 11 columns, as follows:

    1st: k
    2nd: P_sAsB^s(k,\mu=0.1)
    3rd: its error
    4th: P_sAsB^s(k,\mu=0.3)
    5th: its error
    ...
    10th: P_sAsB^s(k,\mu=0.9)
    11th: its error
    """
    return load("galaxy/2-halo/pkmu_s_w_z_00020_30000_z005_1-3_02-13aaan")
#-------------------------------------------------------------------------------
def Pgg_z_0_509():
    """
    The full galaxy power spectrum in redshift space at z = 0.509. 
    It has 11 columns, as follows:

    1st: k
    2nd: P_gg^s(k,\mu=0.1)
    3rd: its error
    4th: P_gg^s(k,\mu=0.3)
    5th: its error
    ...
    10th: P_gg^s(k,\mu=0.9)
    11th: its error
    """
    return load("galaxy/full/lrgmu_gg_z005aaa")
    
#-------------------------------------------------------------------------------
# DARK MATTER SIM DATA
#-------------------------------------------------------------------------------
def P00_mu0_z_0_000():
    """
    The P00 dark matter term with mu^0 angular dependence at z = 0.000
    """
    return load("dark_matter/pkmu_P00_mu0_z_0.000.dat")

def P00_mu0_z_0_509():
    """
    The P00 dark matter term with mu^0 angular dependence at z = 0.509
    """
    return load("dark_matter/pkmu_P00_mu0_z_0.509.dat")

def P00_mu0_z_0_989():
    """
    The P00 dark matter term with mu^0 angular dependence at z = 0.989
    """
    return load("dark_matter/pkmu_P00_mu0_z_0.989.dat")
    
#-------------------------------------------------------------------------------
def P01_mu2_z_0_000():
    """
    The P01 dark matter term with mu^2 angular dependence at z = 0.000
    """
    return load("dark_matter/pkmu_P01_mu2_z_0.000.dat")

def P01_mu2_z_0_509():
    """
    The P01 dark matter term with mu^2 angular dependence at z = 0.509
    """
    return load("dark_matter/pkmu_P01_mu2_z_0.509.dat")
    
def P01_mu2_z_0_989():
    """
    The P01 dark matter term with mu^2 angular dependence at z = 0.989
    """
    return load("dark_matter/pkmu_P01_mu2_z_0.989.dat")

#-------------------------------------------------------------------------------
def Pdv_mu0_z_0_000():
    """
    The Pdv dark matter term with mu^0 angular dependence at z = 0.000
    """
    return load("dark_matter/pkmu_Pdv_mu0_z_0.000.dat")

def Pdv_mu0_z_0_509():
    """
    The Pdv dark matter term with mu^0 angular dependence at z = 0.509
    """
    return load("dark_matter/pkmu_Pdv_mu0_z_0.509.dat")
    
def Pdv_mu0_z_0_989():
    """
    The Pdv dark matter term with mu^0 angular dependence at z = 0.989
    """
    return load("dark_matter/pkmu_Pdv_mu0_z_0.989.dat")

#-------------------------------------------------------------------------------
def P11_mu4_z_0_000():
    """
    The P11 dark matter term with mu^4 angular dependence at z = 0.000
    """
    return load("dark_matter/pkmu_P11_mu4_z_0.000.dat")

def P11_mu4_z_0_509():
    """
    The P11 dark matter term with mu^4 angular dependence at z = 0.509
    """
    return load("dark_matter/pkmu_P11_mu4_z_0.509.dat")
    
def P11_mu4_z_0_989():
    """
    The P11 dark matter term with mu^4 angular dependence at z = 0.989
    """
    return load("dark_matter/pkmu_P11_mu4_z_0.989.dat")

#-------------------------------------------------------------------------------
