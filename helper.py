import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import pickle
import csv




temp = pd.read_csv('Poisson_data_no_metal_07192019.csv', header=None).values
# el_ls = temp[0,:].tolist()
el_ls = []
#el_ls = ["","Code","Glass #","Author","Year","Trademark","Ag2O","AgI","Al","Al2O3","AlF3","AlN","As","As2O3","As2O5","As2S3","As2Se3","AsSe","B","B2O3","BaCl2","BaF2","BaO","BeF2","BeO","Bi2O3","BiCl3","Br","Ca","CaF2","CaO","Cd","CdCl2","CdF2","CdO","Ce2O3","CeF3","CeO2","Cl","Co3O4","CoO","Cr2O3","Cs2O","CsCl","CsF","Cu2O","CuO","Dy2O3","Er","Er2O3","ErF3","Eu","Eu2O3","EuF3","F","Fe","Fe2O3","FeO","Ga","Ga2O3","Ga2S3","Ga2Se3","GaF3","Gd2O3","GdF3","Ge","GeO2","GeS2","GeSe2","H2O","HfF4","HfO2","Hg","Ho2O3","I","InF3","K","K2O","K2S","K2SO4","KBr","KCl","KF","KHF2","La","La2O3","La2S3","LaF3","Li","Li2O","Li2S","Li2SO4","LiBr","LiCl","LiF","LiI","MgF2","MgO","Mn2O3","MnF2","MnO","MnO2","MoO2","MoO3","N","Na","Na2O","Na2S","Na2SO4","NaCl","NaF","NaPO3","Nb2O5","Nd","Nd2O3","NdF3","NH4NO3","NiO","O","OH","P","P2O5","Pb","PbCl2","PbF2","PbO","PdO","Pr2O3","Pr6O11","PrF3","Rb2O","RbF","Rh2O3","RuO2","S","Sb","Sb2O3","Sb2S3","Sc2O3","Se","Si","Si3N4","SiC","SiO2","Sm2O3","SnO","SnO2","SO2","SO3","Sr","SrCl2","SrF2","SrO","Ta2O3","Ta2O5","Tb2O3","TbF3","Te","TeO2","Th","ThF4","ThO2","TiO2","Tl","Tl2O","TlSe","Tm2O3","U","U3O8","UO2","V","V2O5","VO6","WO3","Y","Y2O3","Yb2O3","YbF3","YF3","ZnCl2","ZnF2","ZnO","ZnSO4","ZrF4","ZrO2","Young's modulus E (GPa)","Shear modulus G (GPa)","Poisson's ratio v"]
#compound_ls = ["Ag2O","AgI","Al","Al2O3","AlF3","AlN","As","As2O3","As2O5","As2S3","As2Se3","AsSe","B","B2O3","BaCl2","BaF2","BaO","BeF2","BeO","Bi2O3","BiCl3","Br","Ca","CaF2","CaO","Cd","CdCl2","CdF2","CdO","Ce2O3","CeF3","CeO2","Cl","Co3O4","CoO","Cr2O3","Cs2O","CsCl","CsF","Cu2O","CuO","Dy2O3","Er","Er2O3","ErF3","Eu","Eu2O3","EuF3","F","Fe","Fe2O3","FeO","Ga","Ga2O3","Ga2S3","Ga2Se3","GaF3","Gd2O3","GdF3","Ge","GeO2","GeS2","GeSe2","H2O","HfF4","HfO2","Hg","Ho2O3","I","InF3","K","K2O","K2S","K2SO4","KBr","KCl","KF","KHF2","La","La2O3","La2S3","LaF3","Li","Li2O","Li2S","Li2SO4","LiBr","LiCl","LiF","LiI","MgF2","MgO","Mn2O3","MnF2","MnO","MnO2","MoO2","MoO3","N","Na","Na2O","Na2S","Na2SO4","NaCl","NaF","NaPO3","Nb2O5","Nd","Nd2O3","NdF3","NH4NO3","NiO","O","OH","P","P2O5","Pb","PbCl2","PbF2","PbO","PdO","Pr2O3","Pr6O11","PrF3","Rb2O","RbF","Rh2O3","RuO2","S","Sb","Sb2O3","Sb2S3","Sc2O3","Se","Si","Si3N4","SiC","SiO2","Sm2O3","Sn","SnO","SnO2","SO2","SO3","Sr","SrCl2","SrF2","SrO","Ta2O3","Ta2O5","Tb2O3","TbF3","Te","TeO2","Th","ThF4","ThO2","TiO2","Tl","Tl2O","Tl2Se","TlSe","Tm2O3","U","U3O8","UO2","V","V2O5","VO6","WO3","Y","Y2O3","Yb2O3","YbF3","YF3","ZnCl2","ZnF2","ZnO","ZnSO4","ZrF4","ZrO2"]


correct_cmp = ["Ag2O","Al2O3","AlF3","As2O3","As2O5","B2O3","BaCl2","BaF2","BaO","BeF2",
"BeO","Bi2O3","BiCl3","CaF2","CaO","CdCl2","CdF2","CdO","Ce2O3","CeF3","CeO2","Co3O4","CoO",
"Cr2O3","Cs2O","CsCl","CsF","Cu2O","CuO","Dy2O3","Er2O3","ErF3","Eu2O3","EuF3","Fe2O3",
"FeO","Ga2O3","GaF3","Gd2O3","GdF3","GeO2","H2O","HfF4","HfO2","Ho2O3","InF3","K2O",
"KCl","KF","KHF2","La2O3","LaF3","Li2O","LiCl","LiF","MgF2","MgO","Mn2O3","MnF2","MnO",
"MnO2","MoO2","MoO3","Na2O","NaCl","NaF","Nb2O5","Nd2O3","NdF3","NiO","OH","P2O5","PbCl2",
"PbF2","PbO","PdO","Pr2O3","Pr6O11","PrF3","Rb2O","RbF","Rh2O3","RuO2","Sb2O3","Sc2O3",
"SiO2","Sm2O3","SnO","SnO2","SO2","SO3","SrCl2","SrF2","SrO","Ta2O3","Ta2O5","Tb2O3","TbF3",
"TeO2","ThF4","ThO2","TiO2","Tl2O","Tm2O3","U3O8","UO2","V2O5","VO6","WO3","Y2O3","Yb2O3",
"YbF3","YF3","ZnCl2","ZnF2","ZnO","ZrF4","ZrO2"]

stupid_cmp = ["K2SO4","Li2SO4","Na2SO4","NaPO3","NH4NO3","ZnSO4"]

metal_ls = ["As","Al","B","Si","Ca","Cd","Er","Eu","Fe","Ga","Ge","Hg","K","La","Li","Na","Nd","Pb","Sn","Sr","Sb","Te","Sb","Th","Tl","U","V","Y"]
def convert_to_csv():
	"""
	convert an xlsx file to csv format and write to disk
	"""
	path = "Error_detection_07232019.xlsx"

	data_xls = pd.read_excel(path, index_col=None)
	data_xls.to_csv('Error_detection_07232019.csv', encoding='utf-8',index = False)

def read_csv():
    """
	read an csv data return the a matrix 
	return:
		data: a matrix data representing all the row vectors in the csv data
	"""
    #path = "Poisson_data_cleaned_06212019.csv"
    #path = "test_data.csv"
    #path = "Poisson_data_cleaned_07162019.csv"
    path = "test_raw_data_07252019.csv"
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
		for i in range(6,len(row)-5):
			if row[i] != 0.0:
				count = count + 1
			
		if count == compound_number:
			glass.append(row[0])
	return glass


def plot_frequency(data):
    """
	function to plot the occurances of glasses with a specific number of compounds
	param:
		data: a matrix representation of the csv file
	"""
    frequency = []
    xpos = []
    for i in range(1, 7):
        y = len(get_glass(i,data))
        frequency.append(y)
        xpos.append(i)
    
    plt.bar(xpos, frequency)
    plt.ylabel("number of occurances")
    plt.xlabel("number of compounds")
    plt.show()

    
def get_glass_info_subscript(glass, data):
    dic = get_glass_compound_info(glass, data)
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    
    total = ""
    for key in dic:
        content = '(' + str(key) + ')' + str(dic[key]) + ' '
        #content = content.translate(SUB)
        total = total + content
    return total

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
			for i in range(7,len(row)):
				if row[i] != 0.0:
					dict[el_ls[i]] = row[i]
	return dict

def get_glass_compound_info(glass, data):
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
            for i in range(6,len(row)-5):
                if row[i] != 0.0:
                    dict[el_ls[i]] = row[i]
    return dict

def get_metal_glass(data,dict):
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
		ind = row[0]
		sub_dict = dict[ind]
		score = 0
		for key in sub_dict:
			if key in correct_cmp:
				score += 1

		if score == 0:
			result.append(ind)
			print(ind)
			print(sub_dict)
			print("\n")
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



	data = read_csv()
	data = np.array(data)
	# print(len(data))
	# res = get_glass_info("# 304",data)
	# print(res)
	# data_ls = duplicate_helper(data)

def is_in(elm, lst):
    """
	function to check whether an element is a member of a list
	param:
		elm: the element we want to check
        lst: the list
	return:
		result: the boolean(True or False) representing whether the element is the member
	"""
    result = False
    for i in lst:
        if elm == i:
            result = True
            break
    
    return result
        
       
def get_compound(data):
    """
	function to get the composition information of all the glasses
	param:
		data: a matrix representation of the csv file
	return:
		result_lst: a list of lists the ith list representing the compounds that the ith glass has
	"""
    
    result_lst = []
    for row in data:
        row = row.tolist()
        temp_lst = []
        for i in range(6,len(row)-5):
            if row[i] != 0.0:
                temp_lst.append(el_ls[i])
        result_lst.append(temp_lst)
    return result_lst

def find_same_glasses_helper(data, lst):
    """
	a helper function to find the same glasses within a group of glasses with same compounds
	param:
		data: a matrix representation of the csv file
        lst: a list of glasses with same compounds
	return:
		result_lst: list of same glasses
	"""
    #glasses_names = data[:0].tolist()
    amount_lst = []
    for glass in lst:
        temp_lst = []
        dic = get_glass_compound_info(glass, data)
        for key in dic.keys():
            temp_lst.append(dic[key])
        amount_lst.append(temp_lst)
    #print(amount_lst)
    
    result_lst = []
    remove_lst = []
    for i in range(0, len(amount_lst) - 1):
        if i >= len(amount_lst) - 1:
            break
        if is_in(i, remove_lst):
            continue
        
        temp_lst = []
        temp_lst.append(lst[i])
        flag = False
        
        for j in range(i+1, len(amount_lst)):
            if j >= len(amount_lst):
                break
            
            if amount_lst[i] == amount_lst[j]:
                temp_lst.append(lst[j])
                remove_lst.append(j)
                flag = True
            
        if flag:
            result_lst.append(temp_lst)
    
    #print("result_lst: ")
    #print(result_lst)
    return result_lst   

def check_if_all_zero(data):
    result_lst = []
    for row in data:
        All_zero = True
        row = row.tolist()
        for i in range(6, len(row)):
            if row[i] != 0:
                All_zero = False
                break
        
        if All_zero:
            result_lst.append(row[0])
     
    return result_lst           

def is_subset(big_lst, small_lst):
    result = True
    for i in small_lst:
        if is_in(i,big_lst) == False:
            result = False
            break
    return result

def find_family(compound_lst, data):
    glass_names = data[:,0].tolist()
    compounds = get_compound(data)
    result = []
    for i in range(len(compounds)):
        if is_subset(compound_lst, compounds[i]):
            result.append(glass_names[i])
    return result

def export_dic_to_csv(compound_lst, data):
    family = find_family(compound_lst, data)
    dic_lst = []
    for i in family:
        temp_dic = {}
        temp_dic["glass_name"] = i
        
        glass_info = get_glass_info(i, data)
        keys = []
        for key in glass_info:
            keys.append(key)
        
        temp_dic["Code"] = glass_info["Code"]
        temp_dic["Glass #"] = glass_info["Glass #"]
        temp_dic["Author"] = glass_info["Author"]
        temp_dic["Year"] = glass_info["Year"]
        temp_dic["Trademark"] = glass_info["Trademark"]
        
        
        for compound in compound_lst:
            if is_in(compound, keys) == False:
                temp_dic[compound] = 0
            else:
                temp_dic[compound] = glass_info[compound]
        temp_dic["Young's modulus E (GPa)"] = glass_info["Young's modulus E (GPa)"]
        temp_dic["Shear modulus G (GPa)"] = glass_info["Shear modulus G (GPa)"]
        temp_dic["Poisson's ratio v"] = glass_info["Poisson's ratio v"]
        
        dic_lst.append(temp_dic)
    
    csv_columns = []
    for key in dic_lst[0]:
        csv_columns.append(key)
    csv_file = "Output.csv"
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dic_lst:
            writer.writerow(data)
    return dic_lst

            
                      
def find_same_glasses(data):
    """
	function to find the same glasses(same compounds and same amount)
	param:
		data: a matrix representation of the csv file
	return:
		result_lst: list of same glasses
	"""
    #glass_names = data[:,0].tolist()
    glasses_lst = find_same_compound_glasses(data)
    result_lst = []
    for glasses in glasses_lst:
        temp_lst = find_same_glasses_helper(data, glasses)
        if len(temp_lst) != 0:
            print(temp_lst)
            result_lst.append(temp_lst)
    
    return result_lst
  

def find_same_compound_glasses(data):
    """
	function to get the glasses with the same compounds
	param:
		data: a matrix representation of the csv file
	return:
		result_glasses: a list of lists where the glasses with the same compounds are in the same inner list
	"""
    glass_names = data[:,0].tolist()
    compound_lst = get_compound(data)        
    
    lst = []
    remove_lst = []
    for i in range(0,len(compound_lst)-1):
        if i >= len(compound_lst)-1:
            break
        if is_in(i, remove_lst):
            continue
        temp_lst = []
        temp_lst.append(i)
        flag = False
        
        for j in range(i+1, len(compound_lst)):
            if j >= len(compound_lst):
                break

            if compound_lst[i] == compound_lst[j]:
                temp_lst.append(j)
                remove_lst.append(j)
                flag = True
            
        if flag:
            #print(temp_lst)
            lst.append(temp_lst)
    
    result_glasses = []
    for i in lst:
        temp_lst = []
        for j in i:
            temp_lst.append(glass_names[j])
        result_glasses.append(temp_lst)
    return result_glasses

def get_header():
	"""
	get the list of header in the csv
	"""
	path = "Non_metal_07242019.csv"
	df = pd.read_csv(path,header = None)
	data = df.values
	el_ls = data[0].tolist()
	return el_ls

def get_dict_of_dict(data):
	print(el_ls)
	nested_dict = {}
	for row in data:
		row = row.tolist()
		ind = row[0]
		dict = get_glass_info(ind,data)
		nested_dict[ind] = dict
	return nested_dict
		

if __name__ == "__main__":
    # data = read_csv()
    # data = np.array(data)
    
    # ls1 = export_dic_to_csv(['K2O','MoO3', 'P2O5'], data)
    # #print(ls1)
    
    # ls = find_family(['K2O','MoO3', 'P2O5'],data)
  
    
    # with open('duplicate_ls.pkl','rb') as f:
    #     duplicate_ls = pickle.load(f)

    el_ls = get_header()
    # print(el_ls)
    # # print(metal_ls)
    # data = read_csv()   
    # nested_dict = get_dict_of_dict(data)     
    # # with open('nested_dict.pkl','wb') as f:
    # #     pickle.dump(nested_dict,f)
    # # with open('nested_dict.pkl','rb') as f:
    # #     nested_dict = pickle.load(f)
    # res = get_metal_glass(data,nested_dict)
    # print(res)

    # csvfile = "Non_metal_07252019.csv"
    # with open(csvfile, 'w') as csvfile:
    #     writer = csv.writer(csvfile, delimiter=',')
    #     writer.writerow(el_ls)
    #     for row in data:
    #         row = row.tolist()
    #         if row[0] not in res:
    #             writer.writerow(row)
    path1 = "Non_metal_07242019.csv"
    df = pd.read_csv(path1)
    data_0724 = df.values
    path2 = "Non_metal_07252019.csv"
    df = pd.read_csv(path2)
    data_0725 = df.values
    ind_0724 = []
    ind_0725 = []
    res = []
    for row in data_0724:
    	row = row.tolist()
    	ind_0724.append(row[0])
    for row in data_0725:
    	row = row.tolist()
    	ind_0725.append(row[0])
    for i in ind_0724:
    	if i not in ind_0725:
    		print(i)
    		print(get_glass_info(i,data_0724))
    		print("\n")
    # for i in ind_0725:
    # 	if i not in ind_0724:
    # 		print(i)
    # 		print(get_glass_info(i,data_0725))
    # 		print("\n")


 