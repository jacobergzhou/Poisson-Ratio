import numpy as np
from helper import get_glass_info
import pickle
import pandas as pd

def read_csv():
    """
	read an csv data return the a matrix 
	return:
		data: a matrix data representing all the row vectors in the csv data
	"""
    path = "Poisson_data_no_metal_07192019.csv"
    #path = "test_data.csv"
    df = pd.read_csv(path,header = None)
    data = df.values
    #print(data)
    return data

def generate_num(ls,data):
	num = []
	for j in ls:
		compound = get_glass_info(j,data)
		num.append(compound["Poisson's ratio v"])
	return num


def std_check(num_ls,compound_ls):
    result = []
    for ls in num_ls:
        temp = []
        out_ind = num_ls.index(ls)
        std = np.nanstd(ls)
        mean = np.nanmean(ls)
        cut_off = std * 3
        lower_limit = mean - cut_off
        upper_limit = mean + cut_off
        for outlier in ls:
            if outlier > upper_limit or outlier < lower_limit:
                in_ind = ls.index(outlier)
                temp.append(compound_ls[out_ind][in_ind])
        if len(temp) != 0:
            result.append(temp)
    return result

def median(a, l, r): 
    n = r - l + 1
    n = (n + 1) // 2 - 1
    return n + l 
  
# Function to calculate Q1 and Q3 of the IQR 
def IQR(a, n):   
    result = []
    a.sort()   
    # Index of median of entire data 
    mid_index = median(a, 0, n)   
    # Median of first half 
    Q1 = a[median(a, 0, mid_index)]   
    # Median of second half 
    Q3 = a[median(a, mid_index + 1, n)]   
    # IQR calculation 
    result.append(Q1)
    result.append(Q3)
    return result

def IQR_check(num_ls, compound_ls):
    
    outlier = []
    for i in range(0, len(num_ls)):
        if len(num_ls[i]) <= 2:
            continue
        temp_lst = []
        iqr_range = IQR(num_ls[i], len(num_ls[i]))
        iqr = iqr_range[1] - iqr_range[0]
        bound_left = iqr_range[0] - 1.5*iqr
        bound_right = iqr_range[1] + 1.5*iqr
        for j in range(0, len(num_ls[i])):
            if num_ls[i][j] < bound_left or num_ls[i][j] > bound_right:
                temp_lst.append(same_compound_ls[i][j])
        if len(temp_lst) != 0:
            outlier.append(temp_lst)
    
    return outlier

if __name__ == "__main__":
	# data = read_csv()
    with open('same_compound_ls.pkl','rb') as f:	
        same_compound_ls = pickle.load(f)
	# poisson_ls = []
	# for i in same_compound_ls:
	# 	num = generate_num(i,data)
	# 	poisson_ls.append(num)
	# with open('poisson_data.pkl','wb') as f:
	#  	pickle.dump(poisson_ls,f)
    with open('young_data.pkl','rb') as f:	
        poisson_ls = pickle.load(f)

    result = std_check(poisson_ls,same_compound_ls)
    print(result)
    result1 = IQR_check(poisson_ls,same_compound_ls)
    print(result1)


