import pandas as pd
import os

os.chdir("path") ##Path of the main file
df = pd.read_excel("Hetero_Data.xlsx")
df = df[df["Fraction"]>=0.8]  ###Get data with fraction greater than equal to 0.6
print(df)
os.chdir("path") ##path to save the file
df.to_excel("Hetero_subset.xlsx")
os.chdir("path")  ##change path to read Hetero_subset file
df = pd.read_excel("Hetero_subset.xlsx")

pdb_list = set(df["PDB_id"])
pdb_list = list(pdb_list)

print(pdb_list)
chain_total_list = []
for PDB in pdb_list:
    chain_list = []
    for i in range(df.shape[0]):
         temp = df.iloc[i]
         pdb = temp["PDB_id"]
         chain = temp["Chain_id"]
         if PDB == pdb:
             chain_list.append(chain)
    uniq_chain = set(chain_list)
    uniq_chain = list(uniq_chain)
    chain_total_list.append(uniq_chain)

for i,j in zip(pdb_list,chain_total_list):
    print(i,"--",j)

data = {"PDB_id":pdb_list,"Chains":chain_total_list}
df_new = pd.DataFrame(data)
print(df_new)
print("-----------------------------------")
pdb_list_f1 = []
pdb_list_f2 = []
pdb_list_f3 = []
pdb_list_f4 = []
pdb_list_f5 = []
chain_id_f1 = []
chain_id_f2 = []
chain_id_f3 = []
chain_id_f4 = []
chain_id_f5 = []
seq_f1 = []
seq_f2 = []
seq_f3 = []
seq_f4 = []
seq_f5 = []

lr_f1 = []
lr_f2 = []
lr_f3 = []
lr_f4 = []
lr_f5 = []
hr_f1 = []
hr_f2 = []
hr_f3 = []
hr_f4 = []
hr_f5 = []
seq_type_f1 = []
seq_type_f2 = []
seq_type_f3 = []
seq_type_f4 = []
seq_type_f5 = []
frac_f1 = []
frac_f2 = []
frac_f3 = []
frac_f4 = []
frac_f5 = []
ss_f1 = []
ss_f2 = []
ss_f3 = []
ss_f4 = []
ss_f5 = []

for PDB, chains in zip(pdb_list,chain_total_list):
    chains = sorted(chains)
    a = len(chains)
    if a==1:
        print(PDB, "--", chains, "--", a)
        for i in range(df.shape[0]):
            temp = df.iloc[i]
            pdb = temp["PDB_id"]
            chain = temp["Chain_id"]
            seq = temp["SEQUENCE"]
            lr = temp["Low_range"]
            hr = temp["High_range"]
            seq_type = temp["SEQUENCE_TYPE"]
            ss = temp["SECONDARY_STRUCTURE"]
            frac = temp["Fraction"]
            if PDB == pdb and chains[0] == chain:
                pdb_list_f1.append(PDB)
                chain_id_f1.append(chain)
                seq_f1.append(seq)
                lr_f1.append(lr)
                hr_f1.append(hr)
                seq_type_f1.append(seq_type)
                ss_f1.append(ss)
                frac_f1.append(frac)
    if a==2:
        print(PDB, "--", chains, "--", a)
        for i in range(df.shape[0]):
            temp = df.iloc[i]
            pdb = temp["PDB_id"]
            chain = temp["Chain_id"]
            seq = temp["SEQUENCE"]
            lr = temp["Low_range"]
            hr = temp["High_range"]
            seq_type = temp["SEQUENCE_TYPE"]
            ss = temp["SECONDARY_STRUCTURE"]
            frac = temp["Fraction"]
            if PDB == pdb and chains[0]==chain:
                pdb_list_f1.append(PDB)
                chain_id_f1.append(chain)
                seq_f1.append(seq)
                lr_f1.append(lr)
                hr_f1.append(hr)
                seq_type_f1.append(seq_type)
                ss_f1.append(ss)
                frac_f1.append(frac)
            if PDB == pdb and chains[1]==chain:
                pdb_list_f2.append(PDB)
                chain_id_f2.append(chain)
                seq_f2.append(seq)
                lr_f2.append(lr)
                hr_f2.append(hr)
                seq_type_f2.append(seq_type)
                ss_f2.append(ss)
                frac_f2.append(frac)
    if a==3:
        print(PDB, "--", chains, "--", a)
        for i in range(df.shape[0]):
            temp = df.iloc[i]
            pdb = temp["PDB_id"]
            chain = temp["Chain_id"]
            seq = temp["SEQUENCE"]
            lr = temp["Low_range"]
            hr = temp["High_range"]
            seq_type = temp["SEQUENCE_TYPE"]
            ss = temp["SECONDARY_STRUCTURE"]
            frac = temp["Fraction"]
            if PDB == pdb and chains[0]==chain:
                pdb_list_f1.append(PDB)
                chain_id_f1.append(chain)
                seq_f1.append(seq)
                lr_f1.append(lr)
                hr_f1.append(hr)
                seq_type_f1.append(seq_type)
                ss_f1.append(ss)
                frac_f1.append(frac)
            if PDB == pdb and chains[1]==chain:
                pdb_list_f2.append(PDB)
                chain_id_f2.append(chain)
                seq_f2.append(seq)
                lr_f2.append(lr)
                hr_f2.append(hr)
                seq_type_f2.append(seq_type)
                ss_f2.append(ss)
                frac_f2.append(frac)
            if PDB == pdb and chains[2]==chain:
                pdb_list_f3.append(PDB)
                chain_id_f3.append(chain)
                seq_f3.append(seq)
                lr_f3.append(lr)
                hr_f3.append(hr)
                seq_type_f3.append(seq_type)
                ss_f3.append(ss)
                frac_f3.append(frac)
    if a==4:
        print(PDB, "--", chains, "--", a)
        for i in range(df.shape[0]):
            temp = df.iloc[i]
            pdb = temp["PDB_id"]
            chain = temp["Chain_id"]
            seq = temp["SEQUENCE"]
            lr = temp["Low_range"]
            hr = temp["High_range"]
            seq_type = temp["SEQUENCE_TYPE"]
            ss = temp["SECONDARY_STRUCTURE"]
            frac = temp["Fraction"]
            if PDB == pdb and chains[0]==chain:
                pdb_list_f1.append(PDB)
                chain_id_f1.append(chain)
                seq_f1.append(seq)
                lr_f1.append(lr)
                hr_f1.append(hr)
                seq_type_f1.append(seq_type)
                ss_f1.append(ss)
                frac_f1.append(frac)
            if PDB == pdb and chains[1]==chain:
                pdb_list_f2.append(PDB)
                chain_id_f2.append(chain)
                seq_f2.append(seq)
                lr_f2.append(lr)
                hr_f2.append(hr)
                seq_type_f2.append(seq_type)
                ss_f2.append(ss)
                frac_f2.append(frac)
            if PDB == pdb and chains[2]==chain:
                pdb_list_f3.append(PDB)
                chain_id_f3.append(chain)
                seq_f3.append(seq)
                lr_f3.append(lr)
                hr_f3.append(hr)
                seq_type_f3.append(seq_type)
                ss_f3.append(ss)
                frac_f3.append(frac)
            if PDB == pdb and chains[3]==chain:
                pdb_list_f4.append(PDB)
                chain_id_f4.append(chain)
                seq_f4.append(seq)
                lr_f4.append(lr)
                hr_f4.append(hr)
                seq_type_f4.append(seq_type)
                ss_f4.append(ss)
                frac_f4.append(frac)
    if a==5:
        print(PDB, "--", chains, "--", a)
        for i in range(df.shape[0]):
            temp = df.iloc[i]
            pdb = temp["PDB_id"]
            chain = temp["Chain_id"]
            seq = temp["SEQUENCE"]
            lr = temp["Low_range"]
            hr = temp["High_range"]
            seq_type = temp["SEQUENCE_TYPE"]
            ss = temp["SECONDARY_STRUCTURE"]
            frac = temp["Fraction"]
            if PDB == pdb and chains[0]==chain:
                pdb_list_f1.append(PDB)
                chain_id_f1.append(chain)
                seq_f1.append(seq)
                lr_f1.append(lr)
                hr_f1.append(hr)
                seq_type_f1.append(seq_type)
                ss_f1.append(ss)
                frac_f1.append(frac)
            if PDB == pdb and chains[1]==chain:
                pdb_list_f2.append(PDB)
                chain_id_f2.append(chain)
                seq_f2.append(seq)
                lr_f2.append(lr)
                hr_f2.append(hr)
                seq_type_f2.append(seq_type)
                ss_f2.append(ss)
                frac_f2.append(frac)
            if PDB == pdb and chains[2]==chain:
                pdb_list_f3.append(PDB)
                chain_id_f3.append(chain)
                seq_f3.append(seq)
                lr_f3.append(lr)
                hr_f3.append(hr)
                seq_type_f3.append(seq_type)
                ss_f3.append(ss)
                frac_f3.append(frac)
            if PDB == pdb and chains[3]==chain:
                pdb_list_f4.append(PDB)
                chain_id_f4.append(chain)
                seq_f4.append(seq)
                lr_f4.append(lr)
                hr_f4.append(hr)
                seq_type_f4.append(seq_type)
                ss_f4.append(ss)
                frac_f4.append(frac)
            if PDB == pdb and chains[4]==chain:
                pdb_list_f5.append(PDB)
                chain_id_f5.append(chain)
                seq_f5.append(seq)
                lr_f5.append(lr)
                hr_f5.append(hr)
                seq_type_f5.append(seq_type)
                ss_f5.append(ss)
                frac_f5.append(frac)

print(pdb_list_f1,chain_id_f1,seq_f1,lr_f1,hr_f1,seq_type_f1,frac_f1,ss_f1)
print(pdb_list_f2,chain_id_f2,seq_f2,lr_f2,hr_f2,seq_type_f2,frac_f2,ss_f2)
print(pdb_list_f3,chain_id_f3,seq_f3,lr_f3,hr_f3,seq_type_f3,frac_f3,ss_f3)
print(pdb_list_f4,chain_id_f4,seq_f4,lr_f4,hr_f4,seq_type_f4,frac_f4,ss_f4)
print(pdb_list_f5,chain_id_f5,seq_f5,lr_f5,hr_f5,seq_type_f5,frac_f5,ss_f5)

dr1 = {"PDB_id":pdb_list_f1,"SEQUENCE":seq_f1,"Chain_id":chain_id_f1,"Low_range":lr_f1,"High_range":hr_f1,"Sequence_type":seq_type_f1,"Secondary_structure":ss_f1,"Fraction":frac_f1}
df1 = pd.DataFrame(dr1)
dr2 = {"PDB_id":pdb_list_f2,"SEQUENCE":seq_f2,"Chain_id":chain_id_f2,"Low_range":lr_f2,"High_range":hr_f2,"Sequence_type":seq_type_f2,"Secondary_structure":ss_f2,"Fraction":frac_f2}
df2 = pd.DataFrame(dr2)
dr3 = {"PDB_id":pdb_list_f3,"SEQUENCE":seq_f3,"Chain_id":chain_id_f3,"Low_range":lr_f3,"High_range":hr_f3,"Sequence_type":seq_type_f3,"Secondary_structure":ss_f3,"Fraction":frac_f3}
df3 = pd.DataFrame(dr3)
dr4 = {"PDB_id":pdb_list_f4,"SEQUENCE":seq_f4,"Chain_id":chain_id_f4,"Low_range":lr_f4,"High_range":hr_f4,"Sequence_type":seq_type_f4,"Secondary_structure":ss_f4,"Fraction":frac_f4}
df4 = pd.DataFrame(dr4)
dr5 = {"PDB_id":pdb_list_f5,"SEQUENCE":seq_f5,"Chain_id":chain_id_f5,"Low_range":lr_f5,"High_range":hr_f5,"Sequence_type":seq_type_f5,"Secondary_structure":ss_f5,"Fraction":frac_f5}
df5 = pd.DataFrame(dr5)

print("Chain length:1")
print(df1)
print("Chain length:2")
print(df2)
print("Chain length:3")
print(df3)
print("Chain length:4")
print(df4)
print("Chain length:5")
print(df5)

df1.to_excel("Hetero_chain1.xlsx")
df2.to_excel("Hetero_chain2.xlsx")
df3.to_excel("Hetero_chain3.xlsx")
df4.to_excel("Hetero_chain4.xlsx")
df5.to_excel("Hetero_chain5.xlsx")

##Note: Generally we should get two chains. There are rare events we will get more than two seperated chains.
