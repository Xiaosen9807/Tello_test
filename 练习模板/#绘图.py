#绘图
#%%
#%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#ts=pd.Series(np.random.randn(10,5))

ts=pd.DataFrame(
    np.random.rand(5),
    columns=['number'],
    index=[1,2,3,4,5]
    )

print(ts)
ts.plot.pie(subplots=True)
plt.grid(True)
plt.show()
# %%

ts.plot.pie(subplots=True)
plt.grid(True)
plt.show()
# %%
