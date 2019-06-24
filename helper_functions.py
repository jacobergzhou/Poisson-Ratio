# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:39:51 2019

@author: liubeisong
"""

import pandas as pd
import numpy as np
el_ls = ["","Code","Glass #","Author","Year","Trademark","Ag2O","AgI","Al","Al2O3","AlF3","AlN","As","As2O3","As2O5","As2S3","As2Se3","AsSe","B","B2O3","BaCl2","BaF2","BaO","BeF2","BeO","Bi2O3","BiCl3","Br","Ca","CaF2","CaO","Cd","CdCl2","CdF2","CdO","Ce2O3","CeF3","CeO2","Cl","Co3O4","CoO","Cr2O3","Cs2O","CsCl","CsF","Cu2O","CuO","Dy2O3","Er","Er2O3","ErF3","Eu","Eu2O3","EuF3","F","Fe","Fe2O3","FeO","Ga","Ga2O3","Ga2S3","Ga2Se3","GaF3","Gd2O3","GdF3","Ge","GeO2","GeS2","GeSe2","H2O","HfF4","HfO2","Hg","Ho2O3","I","InF3","K","K2O","K2S","K2SO4","KBr","KCl","KF","KHF2","La","La2O3","La2S3","LaF3","Li","Li2O","Li2S","Li2SO4","LiBr","LiCl","LiF","LiI","MgF2","MgO","Mn2O3","MnF2","MnO","MnO2","MoO2","MoO3","N","Na","Na2O","Na2S","Na2SO4","NaCl","NaF","NaPO3","Nb2O5","Nd","Nd2O3","NdF3","NH4NO3","NiO","O","OH","P","P2O5","Pb","PbCl2","PbF2","PbO","PdO","Pr2O3","Pr6O11","PrF3","Rb2O","RbF","Rh2O3","RuO2","S","Sb","Sb2O3","Sb2S3","Sc2O3","Se","Si","Si3N4","SiC","SiO2","Sm2O3","Sn","SnO","SnO2","SO2","SO3","Sr","SrCl2","SrF2","SrO","Ta2O3","Ta2O5","Tb2O3","TbF3","Te","TeO2","Th","ThF4","ThO2","Ti","TiO2","Tl","Tl2O","Tl2Se","TlSe","Tm2O3","U","U3O8","UO2","V","V2O5","VO6","WO3","Y","Y2O3","Yb2O3","YbF3","YF3","ZnCl2","ZnF2","ZnO","ZnSO4","Zr","ZrF4","ZrO2","Young's modulus E (GPa)","Shear modulus G (GPa)","Poisson's ratio v"]

def convert_to_csv():
	path = "Poisson_data_cleaned_06212019.xlsx"

	data_xls = pd.read_excel(path, index_col=None)
	data_xls.to_csv('Poisson_data_cleaned_06212019.csv', encoding='utf-8',header = None,index = False)

def read_csv():
	path = "Poisson_data_cleaned_06212019.csv"
	df = pd.read_csv(path)
	data = df.values
	#print(data)
	return data

def get_composition(compound,data):
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
    glass = []
    
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
    dict = {}
    for row in data:
        row = row.tolist()
        if row[0] == glass:
            for i in range(6,len(row)):
                if row[i] != 0.0:
                    dict[el_ls[i]] = row[i]
    return dict

if __name__ == "__main__":
    data = read_csv()
    data=np.array(data)
    res1 = get_composition("Al", data)
    print(res1)
    res2 = get_glass(1,data)
    print(res2)
    res3 = get_glass_info('# 1', data)
    print(res3)

    
    