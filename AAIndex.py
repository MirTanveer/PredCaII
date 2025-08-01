#!/usr/bin/env python
# coding: utf-8

# In[1]:


#To create an AAIndex matrices of shape (L*531) where
#L is the max_length of the sequence in the dataset

import pandas as pd
import numpy as np
import seaborn


# In[4]:


from aaindex import aaindex1


# In[5]:


aaindex_ids = [
    "ANDN920101", "ARGP820101", "ARGP820102", "ARGP820103", "BEGF750101",
    "BEGF750102", "BEGF750103", "BHAR880101", "BIGC670101", "BIOV880101",
    "BIOV880102", "BROC820101", "BROC820102", "BULH740101", "BULH740102",
    "BUNA790101", "BUNA790102", "BUNA790103", "BURA740101", "BURA740102",
    "CHAM810101", "CHAM820101", "CHAM820102", "CHAM830101", "CHAM830102",
    "CHAM830103", "CHAM830104", "CHAM830105", "CHAM830106", "CHAM830107",
    "CHAM830108", "CHOC750101", "CHOC760101", "CHOC760102", "CHOC760103",
    "CHOC760104", "CHOP780101", "CHOP780201", "CHOP780202", "CHOP780203",
    "CHOP780204", "CHOP780205", "CHOP780206", "CHOP780207", "CHOP780208",
    "CHOP780209", "CHOP780210", "CHOP780211", "CHOP780212", "CHOP780213",
    "CHOP780214", "CHOP780215", "CHOP780216", "CIDH920101", "CIDH920102",
    "CIDH920103", "CIDH920104", "CIDH920105", "COHE430101", "CRAJ730101",
    "CRAJ730102", "CRAJ730103", "DAWD720101", "DAYM780101", "DAYM780201",
    "DESM900101", "DESM900102", "EISD840101", "EISD860101", "EISD860102",
    "EISD860103", "FASG760101", "FASG760102", "FASG760103", "FASG760104",
    "FASG760105", "FAUJ830101", "FAUJ880101", "FAUJ880102", "FAUJ880103",
    "FAUJ880104", "FAUJ880105", "FAUJ880106", "FAUJ880107", "FAUJ880108",
    "FAUJ880109", "FAUJ880110", "FAUJ880111", "FAUJ880112", "FAUJ880113",
    "FINA770101", "FINA910101", "FINA910102", "FINA910103", "FINA910104",
    "GARJ730101", "GEIM800101", "GEIM800102", "GEIM800103", "GEIM800104",
    "GEIM800105", "GEIM800106", "GEIM800107", "GEIM800108", "GEIM800109",
    "GEIM800110", "GEIM800111", "GOLD730101", "GOLD730102", "GRAR740101",
    "GRAR740102", "GRAR740103", "GUYH850101", "HOPA770101", "HOPT810101",
    "HUTJ700101", "HUTJ700102", "HUTJ700103", "ISOY800101", "ISOY800102",
    "ISOY800103", "ISOY800104", "ISOY800105", "ISOY800106", "ISOY800107",
    "ISOY800108", "JANJ780101", "JANJ780102", "JANJ780103", "JANJ790101",
    "JANJ790102", "JOND750101", "JOND750102", "JOND920101", "JOND920102",
    "JUKT750101", "JUNJ780101", "KANM800101", "KANM800102", "KANM800103",
    "KANM800104", "KARP850101", "KARP850102", "KARP850103", "KHAG800101",
    "KLEP840101", "KRIW710101", "KRIW790101", "KRIW790102", "KRIW790103",
    "KYTJ820101", "LAWE840101", "LEVM760101", "LEVM760102", "LEVM760103",
    "LEVM760104", "LEVM760105", "LEVM760106", "LEVM760107", "LEVM780101",
    "LEVM780102", "LEVM780103", "LEVM780104", "LEVM780105", "LEVM780106",
    "LEWP710101", "LIFS790101", "LIFS790102", "LIFS790103", "MANP780101",
    "MAXF760101", "MAXF760102", "MAXF760103", "MAXF760104", "MAXF760105",
    "MAXF760106", "MCMT640101", "MEEJ800101", "MEEJ800102", "MEEJ810101",
    "MEEJ810102", "MEIH800101", "MEIH800102", "MEIH800103", "MIYS850101",
    "NAGK730101", "NAGK730102", "NAGK730103", "NAKH900101", "NAKH900102",
    "NAKH900103", "NAKH900104", "NAKH900105", "NAKH900106", "NAKH900107",
    "NAKH900108", "NAKH900109", "NAKH900110", "NAKH900111", "NAKH900112",
    "NAKH900113", "NAKH920101", "NAKH920102", "NAKH920103", "NAKH920104",
    "NAKH920105", "NAKH920106", "NAKH920107", "NAKH920108", "NISK800101",
    "NISK860101", "NOZY710101", "OOBM770101", "OOBM770102", "OOBM770103",
    "OOBM770104", "OOBM770105", "OOBM850101", "OOBM850102", "OOBM850103",
    "OOBM850104", "OOBM850105", "PALJ810101", "PALJ810102", "PALJ810103",
    "PALJ810104", "PALJ810105", "PALJ810106", "PALJ810107", "PALJ810108",
    "PALJ810109", "PALJ810110", "PALJ810111", "PALJ810112", "PALJ810113",
    "PALJ810114", "PALJ810115", "PALJ810116", "PARJ860101", "PLIV810101",
    "PONP800101", "PONP800102", "PONP800103", "PONP800104", "PONP800105",
    "PONP800106", "PONP800107", "PONP800108", "PRAM820101", "PRAM820102",
    "PRAM820103", "PRAM900101", "PRAM900102", "PRAM900103", "PRAM900104",
    "PTIO830101", "PTIO830102", "QIAN880101", "QIAN880102", "QIAN880103",
    "QIAN880104", "QIAN880105", "QIAN880106", "QIAN880107", "QIAN880108",
    "QIAN880109", "QIAN880110", "QIAN880111", "QIAN880112", "QIAN880113",
    "QIAN880114", "QIAN880115", "QIAN880116", "QIAN880117", "QIAN880118",
    "QIAN880119", "QIAN880120", "QIAN880121", "QIAN880122", "QIAN880123",
    "QIAN880124", "QIAN880125", "QIAN880126", "QIAN880127", "QIAN880128",
    "QIAN880129", "QIAN880130", "QIAN880131", "QIAN880132", "QIAN880133",
    "QIAN880134", "QIAN880135", "QIAN880136", "QIAN880137", "QIAN880138",
    "QIAN880139", "RACS770101", "RACS770102", "RACS770103", "RACS820101",
    "RACS820102", "RACS820103", "RACS820104", "RACS820105", "RACS820106",
    "RACS820107", "RACS820108", "RACS820109", "RACS820110", "RACS820111",
    "RACS820112", "RACS820113", "RACS820114", "RADA880101", "RADA880102",
    "RADA880103", "RADA880104", "RADA880105", "RADA880106", "RADA880107",
    "RADA880108", "RICJ880101", "RICJ880102", "RICJ880103", "RICJ880104",
    "RICJ880105", "RICJ880106", "RICJ880107", "RICJ880108", "RICJ880109",
    "RICJ880110", "RICJ880111", "RICJ880112", "RICJ880113", "RICJ880114",
    "RICJ880115", "RICJ880116", "RICJ880117", "ROBB760101", "ROBB760102",
    "ROBB760103", "ROBB760104", "ROBB760105", "ROBB760106", "ROBB760107",
    "ROBB760108", "ROBB760109", "ROBB760110", "ROBB760111", "ROBB760112",
    "ROBB760113", "ROBB790101", "ROSG850101", "ROSG850102", "ROSM880101",
    "ROSM880102", "ROSM880103", "SIMZ760101", "SNEP660101", "SNEP660102",
    "SNEP660103", "SNEP660104", "SUEM840101", "SUEM840102", "SWER830101",
    "TANS770101", "TANS770102", "TANS770103", "TANS770104", "TANS770105",
    "TANS770106", "TANS770107", "TANS770108", "TANS770109", "TANS770110",
    "VASM830101", "VASM830102", "VASM830103", "VELV850101", "VENT840101",
    "VHEG790101", "WARP780101", "WEBA780101", "WERD780101", "WERD780102",
    "WERD780103", "WERD780104", "WOEC730101", "WOLR810101", "WOLS870101",
    "WOLS870102", "WOLS870103", "YUTK870101", "YUTK870102", "YUTK870103",
    "YUTK870104", "ZASB820101", "ZIMJ680101", "ZIMJ680102", "ZIMJ680103",
    "ZIMJ680104", "ZIMJ680105", "AURR980101", "AURR980102", "AURR980103",
    "AURR980104", "AURR980105", "AURR980106", "AURR980107", "AURR980108",
    "AURR980109", "AURR980110", "AURR980111", "AURR980112", "AURR980113",
    "AURR980114", "AURR980115", "AURR980116", "AURR980117", "AURR980118",
    "AURR980119", "AURR980120", "ONEK900101", "ONEK900102", "VINM940101",
    "VINM940102", "VINM940103", "VINM940104", "MUNV940101", "MUNV940102",
    "MUNV940103", "MUNV940104", "MUNV940105", "WIMW960101", "KIMC930101",
    "MONM990101", "BLAM930101", "PARS000101", "PARS000102", "KUMS000101",
    "KUMS000102", "KUMS000103", "KUMS000104", "TAKK010101", "FODM020101",
    "NADH010101", "NADH010102", "NADH010103", "NADH010104", "NADH010105",
    "NADH010106", "NADH010107", "MONM990201", "KOEP990101", "KOEP990102",
    "CEDJ970101", "CEDJ970102", "CEDJ970103", "CEDJ970104", "CEDJ970105",
    "FUKS010101", "FUKS010102", "FUKS010103", "FUKS010104", "FUKS010105",
    "FUKS010106", "FUKS010107", "FUKS010108", "FUKS010109", "FUKS010110",
    "FUKS010111", "FUKS010112", "MITS020101", "TSAJ990101", "TSAJ990102",
    "COSI940101", "PONP930101", "WILM950101", "WILM950102", "WILM950103",
    "WILM950104", "KUHL950101", "GUOD860101", "JURD980101", "BASU050101",
    "BASU050102", "BASU050103", "SUYM030101", "PUNT030101", "PUNT030102",
    "GEOR030101", "GEOR030102", "GEOR030103", "GEOR030104", "GEOR030105",
    "GEOR030106", "GEOR030107", "GEOR030108", "GEOR030109", "ZHOH040101",
    "ZHOH040102", "ZHOH040103", "BAEK050101", "HARY940101", "PONJ960101",
    "DIGM050101", "WOLR790101", "OLSK800101", "KIDA850101", "GUYH850102",
    "GUYH850104", "GUYH850105", "JACR890101", "COWR900101", "BLAS910101",
    "CASG920101", "CORJ870101", "CORJ870102", "CORJ870103", "CORJ870104",
    "CORJ870105", "CORJ870106", "CORJ870107", "CORJ870108", "MIYS990101",
    "MIYS990102", "MIYS990103", "MIYS990104", "MIYS990105", "ENGD860101",
    "FASG890101"
]


# In[63]:


# # 3) Standard amino acids
# AA_LIST = list("ARNDCQEGHILKMFPSTWYV")

# # 4) Load all data from aaindex
# # Each record: aaindex1[code] → {'author':..., 'values': {AA: float,...}}
# records = aaindex1.record_codes()

# # 5) Build a dict: {ID: {AA: value}}
# aa_dict = {}
# for code in aaindex_ids:
#     rec = aaindex1[code]
#     vals = rec['values']
#     # ensure all 20 AAs are present
#     if all(aa in vals for aa in AA_LIST):
#         aa_dict[code] = [vals[aa] for aa in AA_LIST]
#     else:
#         raise ValueError(f"Index {code} is missing data for some amino acids")

# # 6) Function to encode a peptide sequence to an L×531 matrix
# def encode_sequence_L_531(sequence, aa_dict, aaindex_ids):
#     L = len(sequence)
#     F = len(aaindex_ids)  # should be 531
#     matrix = np.zeros((L, F), dtype=float)
#     seq = sequence.upper()
#     for i, aa in enumerate(seq):
#         if aa not in AA_LIST:
#             # leave zeros for unknown residues
#             continue
#         for j, code in enumerate(aaindex_ids):
#             matrix[i, j] = aa_dict[code][AA_LIST.index(aa)]
#     return matrix

# # 7) Example usage:
# sequence = "ACDEFGHIKLMNPQXXXXXXXXXXXXXXX"  # length 20
# X = encode_sequence_L_531(sequence, aa_dict, aaindex_ids)
# print("Shape:", X.shape)  # → (L, 531)


# In[62]:


# # 3) Standard amino acids
# AA_LIST = list("ARNDCQEGHILKMFPSTWYV")

# # 4) Load all data from aaindex
# # Each record: aaindex1[code] → {'author':..., 'values': {AA: float,...}}
# records = aaindex1.record_codes()

# # 5) Build a dict: {ID: {AA: value}}
# aa_dict = {}
# for code in aaindex_ids:
#     rec = aaindex1[code]
#     vals = rec['values']
#     # ensure all 20 AAs are present
#     if all(aa in vals for aa in AA_LIST):
#         aa_dict[code] = [vals[aa] for aa in AA_LIST]
#     else:
#         raise ValueError(f"Index {code} is missing data for some amino acids")

# # 6) Function to encode a peptide sequence to an L×531 matrix
# def encode_sequence_L_531(sequence, aa_dict, aaindex_ids):
#     L = len(sequence)
#     F = len(aaindex_ids)  # should be 531
#     matrix = np.zeros((L, F), dtype=float)
#     seq = sequence.upper()
#     for i, aa in enumerate(seq):
#         if aa not in AA_LIST:
#             # leave zeros for unknown residues
#             continue
#         for j, code in enumerate(aaindex_ids):
#             matrix[i, j] = aa_dict[code][AA_LIST.index(aa)]
#     return matrix

# # 7) Example usage:
# sequence = "MKLTCVVIVAVLFLTACQLITADDSRSTQRHRALRSTTKLSMSTRCKPPGSKCSPSMRDCCTTCISYTKRCRKYYN"  # length L
# X = encode_sequence_L_531(sequence, aa_dict, aaindex_ids)
# print("Shape:", X.shape)  # → (L, 531)


# In[24]:


# === Step 3: Collect sequences ===
fasta_path = "../Combined_Calcium_cdhit.fasta"
sequences = []
seq_ids = []

for record in SeqIO.parse(fasta_path, "fasta"):
    seq = str(record.seq).upper()
    sequences.append(seq)
    seq_ids.append(record.id)

# === Step 4: Find the longest sequence ===
max_len = max(len(seq) for seq in sequences)
print(f"Longest sequence length: {max_len}")


# In[22]:


# === Step 5: Encode and pad sequences ===
def encode_sequence_L_531(sequence, aa_dict, aaindex_ids, max_len):
    L = len(sequence)
    F = len(aaindex_ids)
    matrix = np.zeros((max_len, F), dtype=float)
    for i, aa in enumerate(sequence):
        if aa not in AA_LIST:
            continue  # unknown/ambiguous aa → leave row as zeros
        for j, code in enumerate(aaindex_ids):
            matrix[i, j] = aa_dict[code][AA_LIST.index(aa)]
    return matrix


# In[26]:


# === Step 6: Process all sequences ===
features_all = []

for seq_id, seq in zip(seq_ids, sequences):
    matrix = encode_sequence_L_531(seq, aa_dict, aaindex_ids, max_len)
    features_all.append((seq_id, matrix))

print(f"Processed {len(features_all)} sequences to shape ({max_len}, 531).")


# In[64]:


import os
import re

#Save the matrices along with the seq_ids
os.makedirs("AAindex_matrices", exist_ok=True)

def sanitize_filename(name):
    return re.sub(r'[\/:*?"<>|]', '_', name)

for seq_id, mat in features_all:
    safe_id = sanitize_filename(seq_id)
    np.save(f"AAindex_matrices/{safe_id}.npy", mat)


# In[68]:


# #Encode and save without Seq_IDs
# # === Read sequences from FASTA ===
# fasta_path = "../Combined_Calcium_cdhit.fasta"
# sequences = []

# for record in SeqIO.parse(fasta_path, "fasta"):
#     sequences.append(str(record.seq).upper())

# # === Find longest sequence length ===
# max_len = max(len(seq) for seq in sequences)
# print(f"Longest sequence length: {max_len}")

# # === Encode and pad sequences ===
# def encode_and_pad(sequence, aa_dict, aaindex_ids, max_len):
#     L = len(sequence)
#     F = len(aaindex_ids)
#     matrix = np.zeros((max_len, F), dtype=float)
#     for i, aa in enumerate(sequence):
#         if aa not in AA_LIST:
#             continue  # skip unknown residues
#         for j, code in enumerate(aaindex_ids):
#             matrix[i, j] = aa_dict[code][AA_LIST.index(aa)]
#     return matrix


# In[69]:


# # === Create list of padded matrices (no IDs, no AAindex labels) ===
# matrices = []

# for seq in sequences:
#     mat = encode_and_pad(seq, aa_dict, aaindex_ids, max_len)
#     matrices.append(mat)

# print(f"Total matrices created: {len(matrices)}")
# print(f"Each matrix shape: {matrices[0].shape}")  # Should be (max_len, 531)


# In[1]:


#print(features_all)


# In[2]:


#features_all[0][1].shape


# In[4]:


#type(features_all)

