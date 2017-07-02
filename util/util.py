import pandas as pd
import numpy as np
from random import sample


def random_sampling(dataset, diff=50, max_n_no_alarm=1000, max_n_alarm = 1000, verbose=False):
    
    """
    dataset : one of the five campagnes
    diff : range of sampling for alarm data
    max_n_alarm: first max_n_alarm will be sampled
    balance: if true, alarm and no alarm dateset will have the same capacity
    
    """
    alarms = ["CQ 32306 XH01", "CQ 32306 XH03", "CQ 32306 XH05"]
    
    
    df = dataset

    
    # sample alarm data
    # subset with alarm
    xh1 = df[df['CQ 32306 XH01']==1]
    xh2 = df[df['CQ 32306 XH03']==1]
    xh3 = df[df['CQ 32306 XH05']==1]
    
    #diff = 300
    
    # get index of alarm subset
    sampled_alarm_index = []
    xh_l = xh1.index.values.tolist()+xh2.index.values.tolist()+xh3.index.values.tolist()

    # sample alarm data index
    for i in xh_l:
        start = i-diff
        end = i+diff
        for j in range(start, end):
            if j not in sampled_alarm_index:
                sampled_alarm_index.append(j)
                if len(sampled_alarm_index)>=max_n_alarm:
                    break
        if len(sampled_alarm_index)>=max_n_alarm:
            break


    sampled_alarm = df.iloc[sampled_alarm_index, :]
    sampled_alarm_index = pd.Index(sampled_alarm_index)
    
    
    # get index of no alarm subset
    sampled_no_alarm_index = df.index.difference(sampled_alarm_index)

    #period = 15
    # sample no alarm data index
    temp_list = sampled_no_alarm_index.values.tolist()
    sampled_no_alarm_index=[]
    if len(temp_list)<max_n_no_alarm:
        print('max_n_no_alarm is larger than the total number of no alarm records')
    else:
        sampled_no_alarm_index = sample(temp_list, max_n_no_alarm)
    
    sampled_no_alarm = df.iloc[sampled_no_alarm_index, :]
    sampled_df = pd.concat([sampled_no_alarm, sampled_alarm], axis=0)

    if verbose:
        print("shape of input dataset:")
        print(df.shape)
        print("shape of sampled data without alarm:")
        print(sampled_no_alarm.shape)
        print("shape of sampled data with alarm:")
        print(sampled_alarm.shape)
        print( "diff:"+str(diff))
    
    return sampled_df


def list_diff(l1,l2):
    l2 = set(l2)
    return [item for item in l1 if item not in l2]

def define_inf(df, replace=1000):
    
    df = df.replace(np.inf, replace)
    df = df.replace(-np.inf, -replace)
    return df
