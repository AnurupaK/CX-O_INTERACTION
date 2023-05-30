#####For merging
import pandas as pd

df1 = pd.read_excel("Hetero_chain1.xlsx")
df2 = pd.read_excel("Hetero_chain2.xlsx")

merged_df = pd.merge(df1, df2, on=["PDB_id", "SEQUENCE", "Range_num","Low_range","High_range"])

print(merged_df)
merged_df.to_excel("Hetero_merged.xlsx")


##For getting interactions
import pandas as pd
import os

os.chdir("E:/INTERACTION_FOLDER/HETERODIMER/HETERODIMERS_CSV_FILES/NEW_HETERO_CSVs")
df = pd.read_excel(
    "E:/INTERACTION_FOLDER(1+0.8+0.6)/HETERODIMER_INTERFACE(1+0.8+0.6)/ORI_FILES/CHAINS/Hetero_merged.xlsx")

csv_list = os.listdir()
print(csv_list)
for csv in csv_list:
    a = csv[0:6]
    b = csv[7:12]
    c = csv[-3:]

residue_c1_list = []
residue_c2_list = []
atom_c1_list = []
atom_c2_list = []
r_dist_list = []
pdb_list = []
seq_list = []
seq_type_list = []
lr_list = []
hr_list = []
r_num_list = []
chain_c1_list = []
ss_c1_list = []
frac_c1_list = []
Int_num_c1_list = []
chain_c2_list = []
ss_c2_list = []
frac_c2_list = []
Int_num_c2_list = []
pos_c1_list = []
pos_c2_list = []

for i in range(df.shape[0]):
    temp = df.iloc[i]
    pdb = temp["PDB_id"]
    seq = temp["SEQUENCE"]
    seq_type = temp["Sequence_type"]
    lr = temp["Low_range"]
    hr = temp["High_range"]
    r_num = temp["Range_num"]
    chain_c1 = temp["Chain_id_c1"]
    ss_c1 = temp["Secondary_structure_c1"]
    frac_c1 = temp["Fraction_c1"]
    int_num_c1 = temp["Int_number_c1"]
    int_num_c1_list = int_num_c1.split(",")
    chain_c2 = temp["Chain_id_c2"]
    ss_c2 = temp["Secondary_structure_c2"]
    frac_c2 = temp["Fraction_c2"]
    int_num_c2 = temp["Int_number_c2"]
    int_num_c2_list = int_num_c2.split(",")
    common_int_num = set(int_num_c1_list).intersection(set(int_num_c2_list))
    for csv in csv_list:
        a = csv[0:6]
        b = csv[7:12]
        c = csv[-3:]
        if c == "csv" and pdb == a and seq == b:
            print(a + " found with " + b)
            df_csv = pd.read_csv(csv)
            for j in range(df_csv.shape[0]):
                temp2 = df_csv.iloc[j]
                Pos_c1 = temp2["Pos_c1"]
                Pos_c2 = temp2["Pos_c2"]
                atom_c1 = temp2["Atom_c1"]
                atom_c2 = temp2["Atom_c2"]
                res_c1 = temp2["Residue_c1"]
                res_c2 = temp2["Residue_c2"]
                r_dist = temp2["r_distance"]
                for num in common_int_num:
                    num = float(num)
                    if num == Pos_c1 and num == Pos_c2:
                        residue_c1_list.append(res_c1)
                        residue_c2_list.append(res_c1)
                        atom_c1_list.append(atom_c1)
                        atom_c2_list.append(atom_c2)
                        r_dist_list.append(r_dist)
                        lr_list.append(lr)
                        hr_list.append(hr)
                        r_num_list.append(r_num)
                        pdb_list.append(pdb)
                        seq_list.append(seq)
                        seq_type_list.append(seq_type)
                        chain_c1_list.append(chain_c1)
                        chain_c2_list.append(chain_c2)
                        frac_c1_list.append(frac_c1)
                        frac_c2_list.append(frac_c2)
                        ss_c1_list.append(ss_c1)
                        ss_c2_list.append(ss_c2)
                        Int_num_c1_list.append(int_num_c1_list)
                        Int_num_c2_list.append(int_num_c2_list)
                        pos_c1_list.append(Pos_c1)
                        pos_c2_list.append(Pos_c2)

data = pd.DataFrame({"PDB_id": pdb_list, "SEQUENCE": seq_list, "Sequence_type": seq_type_list, "Low_range": lr_list,
                     "High_range": hr_list,
                     "Range_num": r_num_list, "Chain_c1": chain_c1_list, "Chain_c2": chain_c2_list,
                     "Secondary_structure_c1": ss_c1_list, "Secondary_structure_c2": ss_c2_list,
                     "Fraction_c1": frac_c1_list, "Fraction_c2": frac_c2_list,
                     "Int_number_c1": Int_num_c1_list, "Int_number_c2": Int_num_c2_list, "Position_c1": pos_c1_list,
                     "Position_c2": pos_c2_list, "Residue_c1": residue_c1_list,
                     "Residue_c2": residue_c2_list, "Atom_c1": atom_c1_list, "Atom_c2": atom_c2_list,
                     "r_distance": r_dist_list})

data['Int_number_c1'] = [str(x).strip('[]') for x in data['Int_number_c1']]
data['Int_number_c2'] = [str(x).strip('[]') for x in data['Int_number_c2']]
data['Int_number_c1'] = data['Int_number_c1'].str.replace("'", "")
data['Int_number_c2'] = data['Int_number_c2'].str.replace("'", "")

print(data)
os.chdir("E:/INTERACTION_FOLDER(1+0.8+0.6)/HETERODIMER_INTERFACE(1+0.8+0.6)/ORI_FILES/CHAINS")
data.to_excel("Hetero_interaction.xlsx")
