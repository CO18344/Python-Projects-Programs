import pandas as pd
df = pd.read_json(r'D:\E\Satvik\Programs\Python\Covid19\covid19\active.json')
df.to_csv(r'D:\E\Satvik\Programs\Python\Covid19\covid19\active1.csv')
