import numpy as np


# -----------------------------------------
# Calibration constant for given element (K) where
# K_reference = A_reference/C_reference
# -----------------------------------------

def calibration_constant(peak_area, activity_bq_kg,
                        peak_area_error, activity_error_bq_kg):

    K = peak_area / activity_bq_kg

    sigmaK = abs(K) * np.sqrt(
        (peak_area_error / peak_area)**2 +
        (activity_error_bq_kg / activity_bq_kg)**2
    )

    return K, sigmaK



# -----------------------------------------
# Activity concentration
# C_activity = A_activity/K_reference
# -----------------------------------------

def activity_concentration(peak_area, peak_area_error,
                           K, sigmaK):

    C = peak_area / K

    sigmaC = abs(C) * np.sqrt(
        (peak_area_error / peak_area)**2 +
        (sigmaK / K)**2
    )

    return C, sigmaC



# -----------------------------------------
#  Absorbed Dose Rate D
# -----------------------------------------

def absorbed_dose(Cu, Cth, Ck):# Cu=U activity concentration, Cth=Th activity concentration, Ck=K activity concentration

    D = (0.462 * Cu +0.604 * Cth +0.0417 * Ck)

    return D



def dose_error(sCu, sCth, sCk):# sCu=sigma of u activity concentration, sCth=sigma of th activity concentration, sCk=sigma of k activity concentration

    return np.sqrt((0.462*sCu)**2 +(0.604*sCth)**2 +(0.0417*sCk)**2)



# -----------------------------------------
# Annual Effective Dose Equivalent (AEDE)
# -----------------------------------------

def annual_effective_dose(D):# in mSv/year

    return D * 0.008760 * 0.7 * 0.2



def annual_effective_dose_error(sigmaD):# in mSv/year

    return sigmaD * 0.00876 * 0.7 * 0.2



# -----------------------------------------
# Radium Equivalent(Ra_eq)
# -----------------------------------------

def radium_equivalent(Cu, Cth, Ck):# radium equivalent activity concentration (Bq/kg) where Cu=U activity concentration, Cth=Th activity concentration, Ck=K activity concentration

    return (Cu +1.43*Cth +0.077*Ck)


def radium_error(sCu, sCth, sCk):# sCu=sigma of u activity concentration(error), sCth=sigma of th activity concentration(error), sCk=sigma of k activity concentration(error)

    return np.sqrt(sCu**2 +(1.43*sCth)**2 +(0.077*sCk)**2)



# -----------------------------------------
# External Hazard Index
# -----------------------------------------

def hazard_index(Cu, Cth, Ck):# Cu=U activity concentration, Cth=Th activity concentration, Ck=K activity concentration

    return (Cu/370 +Cth/259 +Ck/4810 )

#------------------------------------
# internal hazard index
#-------------------------------------

def int_hazard_index(Cu, Cth, Ck):
    return(Cu/185 +Cth/370 +Ck/4810)

#-------------------------------------------
#excess lifetime cancer risk
# AEDE is converted from mSv/year to Sv/year
#-------------------------------------------

def ELCR(AEDE):

    AEDE_Sv = AEDE * 10**-3

    lifetime = 70
    risk_factor = 0.057

    return AEDE_Sv * lifetime * risk_factor



#---------------------------
#activity utilization index
#---------------------------

def AUI(Cu, Cth, Ck):

    return (Cu/150 + Cth/100 + Ck/1500)