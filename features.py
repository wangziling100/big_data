import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kurtosis

## feature functions

### element-wise feature functions
def ef_log(data, columns=None, label=None):
    """
    an element-wise feature
    
    log10 on each element
    """
    if label is not None:
        target = data[label]
        
    if columns is None:
        columns = data.columns.tolist()
   
    r_data = pd.DataFrame( np.log10(data[columns].values))
    
    r_data.columns = ['log_'+i for i in columns]
    
    if label is not None:
        r_data = pd.concat([ r_data, target ], axis=1)
    
    return r_data

### column feature functions    
def cf_mean_window(data, window=4, columns=None, label=None ):
    """
    compute rolling std for all columns which contain "ifft"
    
    Parameters
    ----------
    
    data : table to operate on
    window : size of rolling/sliding window
    column_key : identifier for columns to use for computation
    label : name of class variable column (which is kept if label is not None)
        
    """

    if label is not None:
        target = data[label]
    if columns is None:
        columns = data.columns.tolist()
    
    r_data = data[columns].rolling(window=window, axis=0).mean()
    # rename
    r_data.columns = ["cf_mean_"+x for x in columns]
     
    
    if label is not None:
        r_data = pd.concat([ r_data, target ], axis=1)
    
    return r_data 
    

def cf_std_window(data, window=4, columns=None, label=None ):
    """
    compute rolling std for all columns which contain "ifft"
    
    Parameters
    ----------
    
    data : table to operate on
    window : size of rolling/sliding window
    column_key : identifier for columns to use for computation
    label : name of class variable column (which is kept if label is not None)
        
    """

    if label is not None:
        target = data[label]
    if columns is None:
        columns = data.columns.tolist()
    
    r_data = data[columns].rolling(window=window, axis=0).std()
    # rename
    r_data.columns = ["cf_std_"+x for x in columns]
    
    
    if label is not None:
        r_data = pd.concat([ r_data, target ], axis=1)
    
    return r_data   


def cf_var_window(data, window=4, columns=None, label=None ):
    """
    compute rolling var for all columns which contain "ifft"
    
    Parameters
    ----------
    
    data : table to operate on
    window : size of rolling/sliding window
    column_key : identifier for columns to use for computation
    label : name of class variable column (which is kept if label is not None)
        
    """

    if label is not None:
        target = data[label]
    if columns is None:
        columns = data.columns.tolist()
   
    
    r_data = data[columns].rolling(window=window, axis=0).var()
    # rename
    r_data.columns = ["cf_var_"+x for x in columns]
    
    r_data = pd.concat([ r_data, target ], axis=1)
    
    return r_data



def cf_diff(data, columns=None, label=None):
    """
    computes the diff for each column
    
    useful for removing signal distortions which are system error artifacts and not an actual
    environmental effect in the signal
    """
    
    if label is not None:
        target = data[label]
    if columns is None:
        columns = data.columns.tolist()
    
    
    
    r_data = pd.DataFrame(np.diff(data[columns].values, axis=0))

    r_data.columns = ["cf_diff_"+x for x in columns]
    

    if label is not None:
        r_data = pd.concat([ r_data, target ], axis=1)
        
        
    return r_data



def cf_kurtosis_window(data,window=10, columns=None, label=None):
    """
    kurtosis accross window
    """
    
    if label is not None:
        target = data[label]
    if columns is None:
        columns = data.columns.tolist()
    
    
    r_data = data[columns].rolling(window=window, axis=0).kurt()
    # rename
    r_data.columns = ["cf_kurt_"+x for x in columns]
    
    if label is not None:
        r_data = pd.concat([ r_data, target ], axis=1)
    
    return r_data
    
def cf_skew_window(data,window=10, columns=None, label=None):
    """
    skew accross window
    """
    
    if label is not None:
        target = data[label]
    if columns is None:
        columns = data.columns.tolist()
    
    
    r_data = data[columns].rolling(window=window, axis=0).skew()
    # rename
    r_data.columns = ["cf_skew_"+x for x in columns]
    
    if label is not None:
        r_data = pd.concat([ r_data, target ], axis=1)
    
    return r_data
    
def cf_max_window(data,window=4, columns=None, label=None):
    
    
    if label is not None:
        target = data[label]
    if columns is None:
        columns = data.columns.tolist()
    
    
    r_data = data[columns].rolling(window=window, axis=0).max()
    # rename
    r_data.columns = ["cf_max_"+x for x in columns]
    
    if label is not None:
        r_data = pd.concat([ r_data, target ], axis=1)
    
    return r_data

def cf_min_window(data,window=4, columns=None, label=None):
    
    
    if label is not None:
        target = data[label]
    if columns is None:
        columns = data.columns.tolist()
    
    
    r_data = data[columns].rolling(window=window, axis=0).min()
    # rename
    r_data.columns = ["cf_min_"+x for x in columns]
    
    if label is not None:
        r_data = pd.concat([ r_data, target ], axis=1)
    
    return r_data




