def shifting(sf, shift:int):
    sf['cons_T-'+str(shift)] = sf['consumption'].shift(periods=shift, freq='H')
    return sf

temp_df = df.filter(items=['consumption'])
day_temp_df = df.filter(items=['consumption'])

#week
for i in range(24, 168+1):
    temp_df = shifting(temp_df, i)
temp_df = temp_df.drop(['consumption'], axis=1)

#day
for i in range(24, 48+1):
    day_temp_df = shifting(day_temp_df, i)
day_temp_df = day_temp_df.drop(['consumption'], axis=1)

#columns added
df['day_mean'] = day_temp_df.mean(axis=1, skipna=True)
df['week_mean'] = temp_df.mean(axis=1, skipna=True)

df = df.fillna(0)
df.tail(3)