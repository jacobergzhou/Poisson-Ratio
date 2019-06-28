import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import pickle
el_ls = ["","Code","Glass #","Author","Year","Trademark","Ag2O","AgI","Al","Al2O3","AlF3","AlN","As","As2O3","As2O5","As2S3","As2Se3","AsSe","B","B2O3","BaCl2","BaF2","BaO","BeF2","BeO","Bi2O3","BiCl3","Br","Ca","CaF2","CaO","Cd","CdCl2","CdF2","CdO","Ce2O3","CeF3","CeO2","Cl","Co3O4","CoO","Cr2O3","Cs2O","CsCl","CsF","Cu2O","CuO","Dy2O3","Er","Er2O3","ErF3","Eu","Eu2O3","EuF3","F","Fe","Fe2O3","FeO","Ga","Ga2O3","Ga2S3","Ga2Se3","GaF3","Gd2O3","GdF3","Ge","GeO2","GeS2","GeSe2","H2O","HfF4","HfO2","Hg","Ho2O3","I","InF3","K","K2O","K2S","K2SO4","KBr","KCl","KF","KHF2","La","La2O3","La2S3","LaF3","Li","Li2O","Li2S","Li2SO4","LiBr","LiCl","LiF","LiI","MgF2","MgO","Mn2O3","MnF2","MnO","MnO2","MoO2","MoO3","N","Na","Na2O","Na2S","Na2SO4","NaCl","NaF","NaPO3","Nb2O5","Nd","Nd2O3","NdF3","NH4NO3","NiO","O","OH","P","P2O5","Pb","PbCl2","PbF2","PbO","PdO","Pr2O3","Pr6O11","PrF3","Rb2O","RbF","Rh2O3","RuO2","S","Sb","Sb2O3","Sb2S3","Sc2O3","Se","Si","Si3N4","SiC","SiO2","Sm2O3","Sn","SnO","SnO2","SO2","SO3","Sr","SrCl2","SrF2","SrO","Ta2O3","Ta2O5","Tb2O3","TbF3","Te","TeO2","Th","ThF4","ThO2","TiO2","Tl","Tl2O","Tl2Se","TlSe","Tm2O3","U","U3O8","UO2","V","V2O5","VO6","WO3","Y","Y2O3","Yb2O3","YbF3","YF3","ZnCl2","ZnF2","ZnO","ZnSO4","ZrF4","ZrO2","Young's modulus E (GPa)","Shear modulus G (GPa)","Poisson's ratio v"]

metal_ls = ["As","Al","B","Si","Ca","Cd","Er","Eu","Fe","Ga","Ge","Hg","K","La","Li","Na","Nd","Pb","Sn","Sr","Sb","Te","Sb","Th","Tl","U","V","Y"]
def convert_to_csv():
	"""
	convert an xlsx file to csv format and write to disk
	"""
	path = "data/Poisson_data_cleaned_06212019.xlsx"

	data_xls = pd.read_excel(path, index_col=None)
	data_xls.to_csv('Poisson_data_cleaned_06212019.csv', encoding='utf-8',header = None,index = False)


def read_csv():
	"""
	read an csv data return the a matrix 
	return:
		data: a matrix data representing all the row vectors in the csv data
	"""
	path = "Poisson_data_cleaned_06212019.csv"
	df = pd.read_csv(path)
	data = df.values
	#print(data)
	return data

def get_composition(compound,data):
	"""
	get the list of row vectors containing the specific compound
	param:
		compound: a string of representing compound name
		data: a matrix representation of the csv file
	return:
		result: a list of all the corresponding row vectors which has non zero entry of the given compound
	"""
	result = []
	if compound not in el_ls:
		print("ERROR: compound not in element list")
		exit()
	else:
		ind_col = el_ls.index(compound)
		col_vec = data[:,ind_col]
		ind_row = []
		for i in range(len(col_vec)):
			if col_vec[i] != 0:
				ind_row.append(i)
		
		for i in ind_row:
			result.append(data[i])
		result = np.array(result).tolist()
		return result

def get_glass(compound_number, data):
	"""
	get the list of row number that contains a specific number of compound
	param:
		compound_number: number of compound contained
		data: a matrix representation of the csv file
	return:
		glass: a list of all the corresponding row vector number which has the specfic number of compounds
	"""
	glass = []
	if compound_number > 181:
		print("ERROR: compound_number exceeds largest possible number")
		exit()
	for row in data:
		row = row.tolist()
		count = 0  
		for i in range(6,len(row)-3):
			if row[i] != 0.0:
				count = count + 1
			
		if count == compound_number:
			glass.append(row[0])
	return glass

def get_glass_info(glass, data):
    """
	get the composition information of a specific glass
	param:
		glass: index of the glass (e.g. '# 305')
		data: a matrix representation of the csv file
	return:
		dict: a dictionary of the glass composition
	"""
    dict = {}
    for row in data:
        row = row.tolist()
        if row[0] == glass:
            for i in range(6,len(row)):
                if row[i] != 0.0:
                    dict[el_ls[i]] = row[i]
    return dict

def get_metal_glass(data):
	"""
	get the list of row vectors that contains only metal element
	param:
		data: a matrix representation of the csv file
	return:
		result: a list of all the corresponding row vector number which only consists of metals
	"""
	result = []
	for row in data:
		temp = True
		row = row.tolist()
		for i in range(6 , len(row)-3):
			if (row[i] != 0.0) and (el_ls[i] not in metal_ls):
				temp = False
		if temp == True:
			result.append(row)
	return result

def plot_helper(data):
	"""
	helper function to get the dictionary of the number of occurances of all the compounds in the dataset
	param:
		data: a matrix representation of the csv file
	return:
		el_dict: a dictionary of the number of occurances of all the compounds in the dataset
	"""
	el_dict = {}
	for row in data:
		row = row.tolist()
		for i in range(6, len(row) - 3):
			if row[i] != 0.0:
				if el_ls[i] not in el_dict:
					el_dict[el_ls[i]] = 1
				else:
					el_dict[el_ls[i]] += 1
	return el_dict

# def check(data):
# 	num = 0
# 	for compound in el_ls[5:189]:
# 		ind_col = el_ls.index(compound)
# 		col_vec = data[:,ind_col]
# 		ind_row = []
# 		zero_vec = True
# 		for i in range(len(col_vec)):
# 			if col_vec[i] != 0:
# 				zero_vec = False
# 		if zero_vec == True:
# 			num += 1
# 	print(num)

def get_glass_info(glass, data):
	"""
	get the composition information of a specific glass
	param:
		glass: index of the glass (e.g. '# 305')
		data: a matrix representation of the csv file
	return:
		dict: a dictionary of the glass composition
	"""
	dict = {}
	for row in data:
		row = row.tolist()
		if row[0] == glass:
			for i in range(6,len(row)):
				if row[i] != 0.0:
					dict[el_ls[i]] = row[i]
	return (glass,dict)
	

def plot_hist(el_dict):
	"""
	function to plot the barchart of the most common compounds
	param:
		el_dict: a dictionary of the number of occurances of all the compounds in the dataset
	"""
	c = Counter(el_dict)
	ls = c.most_common(10)
	cnt = []
	compound = []
	for i in range(len(ls)):
		cnt.append(ls[i][1])
		compound.append(ls[i][0])
	ypos = np.arange(len(compound))
	plt.xticks(ypos,compound)
	plt.ylabel("number of occurances")
	plt.title("Most Common Compounds")
	plt.bar(ypos,cnt)
	plt.show()


def duplicate_helper(data):
	"""
	function to return a dictionary with only nonzero values
	param:
		data: a matrix representation of the csv file
	return:
		data_ls: list of dictionary with only nonzero values
	"""
	data_ls = []
	for row in data:
		row = row.tolist()
		path = row[0]
		glass,dict = get_glass_info(path,data)
		data_ls.append((glass,dict))
	return data_ls

def check_duplicate(data_ls):
	"""
	function to check the duplicate of the row vectors
	param:
		data_ls: list of dictionary with only nonzero values
	return:
		duplicate_ls: a list of lists where each sublist represent the No. of the glass that has the same compounds
	"""
	duplicate = {}
	for i in data_ls:

		dict = i[1]
		sum = 0
		for key in dict:
			if key != "Young's modulus E (GPa)" and key != "Shear modulus G (GPa)" and key != "Poisson's ratio v":
				scalar = 1
				for j in key:
					scalar *= (ord(j)+0.1)
					#print(scalar)
				val = (scalar) * dict[key]
				sum += val
		if sum not in duplicate:
			duplicate[sum] = [i[0]]
		else:
			duplicate[sum].append(i[0])
	# print(duplicate)
	duplicate_ls = []
	for key in duplicate:
		if len(duplicate[key]) > 1:
			duplicate_ls.append(duplicate[key])
	with open('duplicate_ls.pkl','wb') as f:
 		pickle.dump(duplicate_ls,f)
	return duplicate_ls

if __name__ == "__main__":

	data = read_csv()
	data = np.array(data)
	print(len(data))
	# data_ls = duplicate_helper(data)
	# with open('data_ls.pkl','wb') as f:
	#  	pickle.dump(data_ls,f)
	# with open('data_ls.pkl','rb') as f:	
	# 	data_ls = pickle.load(f)
	# duplicate_ls = check_duplicate(data_ls)

	with open('duplicate_ls.pkl','rb') as f:	
		duplicate_ls = pickle.load(f)
	print(len(duplicate_ls))


	

