##For assigning terminal or middle interactions
import pandas as pd
df = pd.read_excel("Hetero_interaction.xlsx")

pdb_list = set(df["PDB_id"])
pdb_list = list(pdb_list)

print(len(pdb_list))

interaction_list = []
for i in range(df.shape[0]):
       temp = df.iloc[i]
       pdb = temp["PDB_id"]
       lr =  temp["Low_range"]
       hr = temp["High_range"]
       pos_c1 = temp["Position_c1"]
       pos_c2 = temp["Position_c2"]
       for j in pdb_list:
           if j==pdb:
             print(pdb_list)
             if (pos_c1==lr and pos_c2==lr) or (pos_c1==hr and pos_c2==hr):
                           interaction_list.append("T")
             else:
               interaction_list.append("M")


df["T/M_interaction"] = interaction_list

df.to_excel("Hetero_interaction_v2.xlsx")