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
		cut_off = std * 2
		lower_limit = mean - cut_off
		upper_limit = mean + cut_off
		for outlier in ls:
			if outlier > upper_limit or outlier < lower_limit:
				in_ind = ls.index(outlier)
				temp.append(compound_ls[out_ind][in_ind])
				result.append(temp)
	return result

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
		young_ls = pickle.load(f)

	result = std_check(young_ls,same_compound_ls)
	print(result)


