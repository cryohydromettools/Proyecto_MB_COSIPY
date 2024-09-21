import numpy as np
import xarray as xr
import datetime
import os
import pandas as pd
import matplotlib.pyplot as plt
import dateutil
import glob


hgt_aws = 5236.00

#lat_aws = -62.67154536205238
#lon_aws = -60.35032693570448

g       = 9.80665

files = sorted(glob.glob('../../data/input/ERA5/Chuecon_ERA5_*.nc'))
ds = xr.open_mfdataset(files).mean(('latitude','longitude'))

file_out = '../../data/input/Taller/Chuecon_ERA5.csv'
print(ds)

#breakpoint()

hgt_era  = (float(ds['z'][0].values))/g
print('')
print('Grid ele')

print(hgt_era)
df_nc = ds[['z','d2m','sp','ssrd','t2m','tcc','tp', 'sf', 'u10','v10','strd']].to_dataframe()

df_nc['t2m'] = df_nc['t2m'].values + (hgt_aws - hgt_era) * -0.006
df_nc['d2m'] = df_nc['d2m'].values + (hgt_aws - hgt_era) * -0.005

#print(df_nc)

# relative humidity

T0 = 273.16 # K
a1 = 611.21 # Pa
a3 = 17.502 # K
a4 = 32.19  # K
R_dry = 287.0597 # Kg^-1 K^-1
R_vap = 461.5250 # Kg^-1 K^-1

T  = df_nc['t2m'].values
Td = df_nc['d2m'].values
P  = df_nc['sp'].values
T_e_sat = a1 * np.exp(a3* ((T - T0)/(T - a4)))
T_q_sat = ((R_dry/R_vap)*T_e_sat)/(P - (1 - (R_dry/R_vap)) * T_e_sat)
Td_e_sat = a1 * np.exp(a3* ((Td - T0)/(Td - a4)))
Td_q_sat = ((R_dry/R_vap)*Td_e_sat)/(P - (1 - (R_dry/R_vap)) * Td_e_sat)
RH    = 100 * Td_e_sat/T_e_sat
RH[RH > 100]  = 100.0
RH[RH <   0]  = 0.0

df_nc['rh'] = RH

# solar radiation
SWin    = df_nc['ssrd']/3600
SWin[SWin < 0] = 0.0
df_nc['SWin'] = SWin

# long radiation
LWin    = df_nc['strd']/3600
#LWin[LWin < 0] = 0.0
df_nc['LWin'] = LWin

# pressure
df_nc['press']    = df_nc['sp']/100
SLP = df_nc['press'].values / np.power((1 - (0.0065 * hgt_era) / (288.15)), 5.255)
df_nc['press'] = SLP * np.power((1 - (0.0065 * hgt_aws)/(288.15)), 5.22) 

# wind speed to 2 from 10 m
U10 = np.sqrt((df_nc['u10'].values)**2 + (df_nc['v10'].values)**2)
df_nc['u2'] = U10 * (np.log(2/(2.12*1000))/np.log(10/(2.12*1000)))

# total precipitation
tp          = df_nc['tp'].values
tp[tp < 0]  = 0.0
df_nc['tp'] = tp*1000

# total precipitation
sf          = df_nc['sf'].values
sf[sf < 0]  = 0.0
df_nc['sf'] = sf


df_nc = df_nc[['SWin','LWin', 't2m','rh','u2','tp', 'press','tcc']] # 'sf',

df_nc .columns = ['G','LWin', 'T2','RH2','U2','RRR', 'PRES','N'] # 'SNOWFALL',
df_nc.index.names = ['TIMESTAMP'] 
print(df_nc)


df_nc.to_csv(file_out, sep=',')
