import pandas as pd
import matplotlib.pyplot as plt

# Load the observational data
input_file = '/home/sohaib/Downloads/table_WASP-107-b-Welbanks-et-al.-2024 (1).tsv'
output_file = '/home/sohaib/Desktop/masterthesis/wasp107MIR.dat'



try:
    # Load the data and specify the first row as the header
    spectrum_data = pd.read_csv(input_file, sep='\t', header=0)
    
    # Rename columns for clarity
    spectrum_data.columns = ['Wavelength', 'Rp_Rs', 'Error']
    
    # Convert columns to numeric
    spectrum_data['Wavelength'] = pd.to_numeric(spectrum_data['Wavelength'], errors='coerce')
    spectrum_data['Rp_Rs'] = pd.to_numeric(spectrum_data['Rp_Rs'], errors='coerce')
    spectrum_data['Error'] = pd.to_numeric(spectrum_data['Error'], errors='coerce')
    
    # Drop rows with invalid (NaN) values
    spectrum_data = spectrum_data.dropna()
    
    # Square the Rp/Rs column to compute Transit Depth
    spectrum_data['Transit_Depth'] = spectrum_data['Rp_Rs']**2
    
    # Reorganize columns for output
    spectrum_data = spectrum_data[['Wavelength', 'Transit_Depth', 'Error']]
    
    # Save the processed data to the output file
    spectrum_data.to_csv(output_file, sep=' ', index=False, header=False)
    
    print(f"Updated observational data saved to: {output_file}")
except Exception as e:
    print(f"An error occurred: {e}")


import numpy as np

# Define file names with the .dat extension
nir_file = '/home/sohaib/Desktop/masterthesis/wasp107.dat'
mir_file = '/home/sohaib/Desktop/masterthesis/wasp107MIR.dat'
output_file = '/home/sohaib/Desktop/masterthesis/wasp107_NIR+MIR.dat'

# Load data from the .dat files.
# Adjust delimiter if your data is not whitespace-delimited.
nir_data = np.loadtxt(nir_file)
mir_data = np.loadtxt(mir_file)

# Combine the two datasets by vertically stacking them.
combined_data = np.vstack((nir_data, mir_data))

# Sort the combined data by the wavelength (assuming column 0 is wavelength).
sorted_data = combined_data[np.argsort(combined_data[:, 0])]

# Save the combined, sorted data back to a .dat file.
np.savetxt(output_file, sorted_data, fmt='%.6e')

print(f"Combined spectrum saved to {output_file}")
