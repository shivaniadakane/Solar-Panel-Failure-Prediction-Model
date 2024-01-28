
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


col_names = ['Time', 'Ipv', 'Vpv', 'Vdc', 'ia', 'ib', 'ic', 'va', 'vb', 'vc', 'Iabc','If', 'Vabc', 'Vf', 'label']

faulty = pd.DataFrame(columns = col_names)
non_faulty = pd.DataFrame(columns = col_names)

for num in range(1,8):
    df1 = pd.read_csv(r"D:\DS Project\datasets\CSV_Files\CSV_Files\F{}L.csv".format(num))
    df1['label'] = np.full((len(df1),1), 'F'.format(num))
    faultyL = pd.concat([faulty, df1], ignore_index = True)
    
    df2 = pd.read_csv(r"D:\DS Project\datasets\CSV_Files\CSV_Files\F{}M.csv".format(num))
    df2['label'] = np.full((len(df2),1), 'F'.format(num))
    faultyM = pd.concat([faulty, df2], ignore_index = True)
    
a = df1.head()    
b = df2.head()    
    
num = 0
df3 = pd.read_csv(r"D:\DS Project\datasets\CSV_Files\CSV_Files\F{}L.csv".format(num))
df3['label'] = np.full((len(df3),1), 'NF'.format(num))
non_faultyL = pd.concat([non_faulty, df3], ignore_index = True)
    
df4 = pd.read_csv(r"D:\DS Project\datasets\CSV_Files\CSV_Files\F{}M.csv".format(num))
df4['label'] = np.full((len(df4),1), 'NF'.format(num))
non_faultyM = pd.concat([non_faulty, df4], ignore_index = True)



c = df3.head()    
d = df4.head()


df1f = faultyL.iloc[::1000,:]
df2f = faultyM.iloc[::1000,:]
df3n = non_faultyL.iloc[::1000,:]
df4n = non_faultyM.iloc[::1000,:]


df1.iloc[::200,:].to_csv(r"D:\DS Project\Pre-processed data\df1.csv",index=False)
df2.iloc[::200,:].to_csv(r"D:\DS Project\Pre-processed data\df2.csv",index=False)
df3.iloc[::200,:].to_csv(r"D:\DS Project\Pre-processed data\df3.csv",index=False)
df4.iloc[::200,:].to_csv(r"D:\DS Project\Pre-processed data\df4.csv",index=False)


faulty_con = pd.concat([df1, df2], axis=0, join='inner')
non_faulty_con = pd.concat([df3, df4], axis=0, join='inner')

faulty_data = non_faulty_con.sample(n = 3000)
non_faulty_data = faulty_con.sample(n = 7000)


solar_data = pd.concat([faulty_data, non_faulty_data], axis=0, join='inner')


solar_data.iloc[::].to_csv(r"D:\DS Project\Pre-processed data\Solar_data.csv",index=False)