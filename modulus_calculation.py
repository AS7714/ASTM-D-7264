import numpy as np

def calculate_stress_strain(sample_data, width_beam, thickness_beam):
    support_span = 96  # mm
    stresses = (3 * (sample_data['Load'] * 1000) * support_span) / (4 * width_beam * thickness_beam**2)
    strains = (4.36 * sample_data['Deflectometer'] * thickness_beam) / (support_span**2)
    return stresses, strains

def calculate_youngs_modulus(corrected_strains, corrected_stresses):
    linear_start = np.where(corrected_strains > 0.001)[0][0]
    linear_end = np.where(corrected_strains > 0.003)[0][0]
    
    p = np.polyfit(corrected_strains[linear_start:linear_end], corrected_stresses[linear_start:linear_end], 1)
    youngs_modulus = p[0] / 1000  # Convert to GPa
    return youngs_modulus, p
