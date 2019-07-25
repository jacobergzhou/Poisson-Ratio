import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import pickle
import csv

temp = pd.read_csv('Poisson_data_no_metal_07192019.csv', header=None).values
el_ls = temp[0,:].tolist()
#el_ls = ["","Code","Glass #","Author","Year","Trademark","Ag2O","AgI","Al","Al2O3","AlF3","AlN","As","As2O3","As2O5","As2S3","As2Se3","AsSe","B","B2O3","BaCl2","BaF2","BaO","BeF2","BeO","Bi2O3","BiCl3","Br","Ca","CaF2","CaO","Cd","CdCl2","CdF2","CdO","Ce2O3","CeF3","CeO2","Cl","Co3O4","CoO","Cr2O3","Cs2O","CsCl","CsF","Cu2O","CuO","Dy2O3","Er","Er2O3","ErF3","Eu","Eu2O3","EuF3","F","Fe","Fe2O3","FeO","Ga","Ga2O3","Ga2S3","Ga2Se3","GaF3","Gd2O3","GdF3","Ge","GeO2","GeS2","GeSe2","H2O","HfF4","HfO2","Hg","Ho2O3","I","InF3","K","K2O","K2S","K2SO4","KBr","KCl","KF","KHF2","La","La2O3","La2S3","LaF3","Li","Li2O","Li2S","Li2SO4","LiBr","LiCl","LiF","LiI","MgF2","MgO","Mn2O3","MnF2","MnO","MnO2","MoO2","MoO3","N","Na","Na2O","Na2S","Na2SO4","NaCl","NaF","NaPO3","Nb2O5","Nd","Nd2O3","NdF3","NH4NO3","NiO","O","OH","P","P2O5","Pb","PbCl2","PbF2","PbO","PdO","Pr2O3","Pr6O11","PrF3","Rb2O","RbF","Rh2O3","RuO2","S","Sb","Sb2O3","Sb2S3","Sc2O3","Se","Si","Si3N4","SiC","SiO2","Sm2O3","SnO","SnO2","SO2","SO3","Sr","SrCl2","SrF2","SrO","Ta2O3","Ta2O5","Tb2O3","TbF3","Te","TeO2","Th","ThF4","ThO2","TiO2","Tl","Tl2O","TlSe","Tm2O3","U","U3O8","UO2","V","V2O5","VO6","WO3","Y","Y2O3","Yb2O3","YbF3","YF3","ZnCl2","ZnF2","ZnO","ZnSO4","ZrF4","ZrO2","Young's modulus E (GPa)","Shear modulus G (GPa)","Poisson's ratio v"]
#compound_ls = ["Ag2O","AgI","Al","Al2O3","AlF3","AlN","As","As2O3","As2O5","As2S3","As2Se3","AsSe","B","B2O3","BaCl2","BaF2","BaO","BeF2","BeO","Bi2O3","BiCl3","Br","Ca","CaF2","CaO","Cd","CdCl2","CdF2","CdO","Ce2O3","CeF3","CeO2","Cl","Co3O4","CoO","Cr2O3","Cs2O","CsCl","CsF","Cu2O","CuO","Dy2O3","Er","Er2O3","ErF3","Eu","Eu2O3","EuF3","F","Fe","Fe2O3","FeO","Ga","Ga2O3","Ga2S3","Ga2Se3","GaF3","Gd2O3","GdF3","Ge","GeO2","GeS2","GeSe2","H2O","HfF4","HfO2","Hg","Ho2O3","I","InF3","K","K2O","K2S","K2SO4","KBr","KCl","KF","KHF2","La","La2O3","La2S3","LaF3","Li","Li2O","Li2S","Li2SO4","LiBr","LiCl","LiF","LiI","MgF2","MgO","Mn2O3","MnF2","MnO","MnO2","MoO2","MoO3","N","Na","Na2O","Na2S","Na2SO4","NaCl","NaF","NaPO3","Nb2O5","Nd","Nd2O3","NdF3","NH4NO3","NiO","O","OH","P","P2O5","Pb","PbCl2","PbF2","PbO","PdO","Pr2O3","Pr6O11","PrF3","Rb2O","RbF","Rh2O3","RuO2","S","Sb","Sb2O3","Sb2S3","Sc2O3","Se","Si","Si3N4","SiC","SiO2","Sm2O3","Sn","SnO","SnO2","SO2","SO3","Sr","SrCl2","SrF2","SrO","Ta2O3","Ta2O5","Tb2O3","TbF3","Te","TeO2","Th","ThF4","ThO2","TiO2","Tl","Tl2O","Tl2Se","TlSe","Tm2O3","U","U3O8","UO2","V","V2O5","VO6","WO3","Y","Y2O3","Yb2O3","YbF3","YF3","ZnCl2","ZnF2","ZnO","ZnSO4","ZrF4","ZrO2"]
         
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
    #path = "Poisson_data_cleaned_06212019.csv"
    #path = "test_data.csv"
    #path = "Poisson_data_cleaned_07162019.csv"
    path = "Poisson_data_no_metal_07192019.csv"
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
            for i in range(1,len(row)-2):
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
		for i in range(6 , len(row)-5):
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
    """
	find the glasses in the same family and export their information to a csv called "Output.csv"
	param:
		compound_lst: a list of strings representing the compounds of that family
		data: a matrix representation of the csv file
	return:
		dc_lst: a list of dictionaries representing the information of the glasses in the same family
	"""
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


if __name__ == "__main__":
    data = read_csv()
    data = np.array(data)
    
    ls1 = export_dic_to_csv(['AlF3', 'BaF2', 'CaF2', 'MgF2', 'PbF2', 'YbF3'], data)
    #print(ls1)
    
    #ls = find_family(['K2O','MoO3', 'P2O5'],data)
    #print(ls)

    #ls = check_if_all_zero(data)
    #print(ls)
    #print(len(data))
    #plot_frequency(data)
    #lst2 = find_same_compound_glasses(data)
    #print(lst2)
    #lst = find_same_glasses(data)
    #print(lst[0])
    #print(lst)
    #glass_names = data[:,0].tolist()
    #print(glass_names)
    #print(test_find_same_glass2(data))
    # data_ls = duplicate_helper(data)
	# with open('data_ls.pkl','wb') as f:
	#  	pickle.dump(data_ls,f)
	# with open('data_ls.pkl','rb') as f:	
	# 	data_ls = pickle.load(f)
	# duplicate_ls = check_duplicate(data_ls)
    
    with open('duplicate_ls.pkl','rb') as f:
        duplicate_ls = pickle.load(f)
    #print(len(duplicate_ls))
    
'''    
    # create the error_detection csv
    glass_names = data[:,0].tolist()
    lst = []
    for i in glass_names:
        lst.append(get_glass_info_subscript(i, data))
    csv_input = pd.read_csv('Poisson_data_no_metal_07192019.csv')
    csv_input['glass_comp'] = lst
    csv_input.to_csv('output.csv', index=False)
    print(lst)
'''

'''  
    with open("Poisson_data_no_metal_07192019.csv", 'r') as csvinput:
        with open("output.csv", 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator = '\n')
            reader = csv.reader(csvinput)
            
            all = []
            row = next(reader)
            row.
'''    
    
    

'''   
    lst = find_same_glasses(data)
    print(lst)
    f = open("result.txt","w")
    for i in lst:    
        for j in i:
            f.write('-------------------------------------------------------------------------------')
            f.write('-------------------------------------------------------------------------------')
            for k in j:
                dic = get_glass_info(k, data)
                f.write(k)
                f.write(str(dic))
                f.write('\n')
    f.close()
    
    
    ls1 = find_same_compound_glasses(data)
    f1 = open("result1.txt", "w")
    for i in ls1:
        for j in i:
            f1.write('-------------------------------------------------------------------------------')
            f1.write('-------------------------------------------------------------------------------') 
            dic = get_glass_info(j,data)
            #print(dic)
            f1.write(j)
            f1.write(str(dic))
            f1.write('\n')
    f1.close()
'''
           



	

