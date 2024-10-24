def toe_correction(strains, stresses):
    linear_start = next(i for i, v in enumerate(strains) if v > 0.001)
    linear_end = next(i for i, v in enumerate(strains) if v > 0.003)

    p = np.polyfit(strains[linear_start:linear_end], stresses[linear_start:linear_end], 1)
    
    x_intercept = -p[1] / p[0]
    
    corrected_strains = strains - x_intercept
    positive_indices = corrected_strains >= 0
    corrected_strains = corrected_strains[positive_indices]
    corrected_stresses = stresses[positive_indices]
    
    youngs_modulus = p[0] / 1000  # Convert to GPa
    return corrected_strains, corrected_stresses, youngs_modulus
