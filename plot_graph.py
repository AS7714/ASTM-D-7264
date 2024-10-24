import matplotlib.pyplot as plt

def plot_stress_strain(corrected_strains, corrected_stresses, maxstrain, maxstress, youngs_modulus, sample_name, sample_folder):
    plt.figure()
    plt.plot(corrected_strains, corrected_stresses, label='Stress-Strain Curve', linewidth=1.5)
    plt.plot(maxstrain, maxstress, 'ro', label='Max Stress', markersize=8, linewidth=1.5)
    
    plt.xlabel('Strain')
    plt.ylabel('Stress (MPa)')
    plt.title(f'Toe-Corrected Stress-Strain Curve - {sample_name}')
    
    linear_strains = np.linspace(0, max(corrected_strains), 100)
    linear_stresses = youngs_modulus * 1000 * linear_strains
    plt.plot(linear_strains, linear_stresses, 'r--', label='Linear Region', linewidth=1.5)
    
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(sample_folder, f'{sample_name}_Toe_Corrected_Stress_Strain_Curve.png'))
    plt.close()
