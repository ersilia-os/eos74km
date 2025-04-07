# imports
import os
import csv
import sys
import numpy as np
import joblib
from mhfp.encoder import MHFPEncoder
from rdkit.Chem import CanonSmiles

# variables
root = os.path.dirname(os.path.abspath(__file__))
checkpoints_dir = os.path.abspath(os.path.join(root, "..", "..",  "checkpoints"))

# load the model
model = joblib.load(os.path.join(checkpoints_dir, "mhfp6_rf.joblib"))
label_classes = model.classes_.tolist()
label_classes = [str(l).replace("-", "_") for l in label_classes]

# instantiate the fingerprint encoder
mhfp_encoder = MHFPEncoder(n_permutations=2048, seed=42)  # MHFP6 fingerprint
ecbl_mhfp6_fingerprints = []  # This is not used

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# calculate encodings
R = []
idxs = []
for i, smiles in enumerate(smiles_list):
    can_smiles = CanonSmiles(smiles)
    if not can_smiles:
        continue
    R.append(mhfp_encoder.encode(can_smiles, radius=3))
    idxs.append(i)
R = np.array(R)
idxs = set(idxs)

# run model
y = model.predict_proba(R)
print(y)

# assemble the output
outputs = []
empty_output = [None]*len(label_classes)
j = 0  # len(y) != len(smiles_list)
for i, idx in enumerate(smiles_list):
    if i in idxs:
        outputs.append(y[j])
        j += 1
    else:
        outputs.append(empty_output)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(label_classes)  # header
    for o in outputs:
        writer.writerow(o)
