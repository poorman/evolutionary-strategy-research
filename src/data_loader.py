import pandas as pd
import numpy as np

def load_synthetic_data(n_rows=1000):
    print("Loading synthetic data")
    data = pd.DataFrame({
        "price": np.cumsum(np.random.randn(n_rows)) + 100
    })
    return data
