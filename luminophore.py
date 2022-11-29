import numpy as np
import pandas as pd

def get_absorption(file, low, high):
    df = pd.read_csv(file)
    
    absorption_x = df['Absorption wavelength (nm)'].values
    absorption = df['normalized Absorption'].values
    
    absorption_x = absorption_x[~np.isnan(absorption_x)]
    absorption = absorption[~np.isnan(absorption)]

    min_absorption = np.min(absorption_x)
    max_absorption = np.max(absorption_x)
    print(min_absorption, max_absorption)
    
    min_wave = 200
    max_wave = 1001
    
    if min_wave < min_absorption:
        extra_wave = np.arange(min_wave, min_absorption)
        extra_data = np.zeros(int(min_absorption-min_wave)) + absorption[0]
        absorption_x = np.concatenate([extra_wave, absorption_x])
        absorption = np.concatenate([extra_data, absorption])

    if max_wave > max_absorption:
        extra_wave = np.arange(max_absorption+1, max_wave)
        extra_data = np.zeros(int(max_wave-max_absorption-1)) + absorption[-1]
        absorption_x = np.concatenate([absorption_x, extra_wave])
        absorption = np.concatenate([absorption, extra_data])
        
    df2 = pd.DataFrame({'wavelength': absorption_x, 'spectrum':absorption})
    
    data = df2[(df2['wavelength']>=low) & (df2['wavelength']<high)]['spectrum']
    
    return data

def get_emission(file, low, high):
    df = pd.read_csv(file)
    
    emission_x = df['emission wavelength (nm)'].values
    emission = df['Normalized emission'].values
    
    emission_x = emission_x[~np.isnan(emission_x)]
    emission = emission[~np.isnan(emission)]

    min_emission = np.min(emission_x)
    max_emission = np.max(emission_x)
    print(min_emission, max_emission)
    
    min_wave = 200
    max_wave = 1001

    if min_wave < min_emission:
        extra_wave = np.arange(min_wave, min_emission)
        extra_data = np.zeros(int(min_emission-min_wave)) + emission[0]
        emission_x = np.concatenate([extra_wave, emission_x])
        emission = np.concatenate([extra_data, emission])

    if max_wave > max_emission:
        extra_wave = np.arange(max_emission+1, max_wave)
        extra_data = np.zeros(int(max_wave-max_emission-1)) + emission[-1]
        emission_x = np.concatenate([emission_x, extra_wave])
        emission = np.concatenate([emission, extra_data])
        
    df2 = pd.DataFrame({'wavelength': emission_x, 'spectrum':emission})
    
    data = df2[(df2['wavelength']>=low) & (df2['wavelength']<high)]['spectrum']
    
    return data