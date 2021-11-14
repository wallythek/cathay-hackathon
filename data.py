import pandas as pd
import random
import numpy as np

df = pd.DataFrame(index=range(1000), columns=['user_id', 'post_id', 'tags', 'gender', 'age'])

df['user_id'] = np.random.choice(list(range(100)), len(df))
df['post_id'] = df.index
df['gender'] = np.random.choice(list(['m', 'f']), len(df))
df['age'] = np.random.choice(list(['16-25','25-35', '35-50', '50+']), len(df))
df['tags'] = np.random.choice(list(['nature', 'travel', 'staycation', 'food', 'sport', 'fashion', 'luxury', 'yoga']), len(df))

df.to_csv('user_data.csv')