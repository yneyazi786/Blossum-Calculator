#!/usr/bin/env python
# coding: utf-8

<<<<<<< HEAD
=======
# In[1]:
>>>>>>> 411cbaf71956485e7da00c897f46002b949b55bd
import streamlit as st
st.markdown("""
<style>
body {
    background-color: #121212;
    color: white;
}
h1 {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-weight: bold;
}
.stSelectbox > div {
    background-color: #2a2a2a;
    color: white;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)


<<<<<<< HEAD
# Minimal BLOSUM62 matrix
BLOSUM62 = {
"A":{"A":4, "R":-1, "N":-2, "D":-2, "C":0, "Q":-1, "E":-1, "G":0, "H":-2, "I":-1, "L":-1, "K":-1, "M":-1, "F":-2, "P":-1, "S":1, "T":0, "W":-3, "Y":-2, "V":0},
"R":{"A":-1, "R":5, "N":0, "D":-2, "C":-3, "Q":1, "E":0, "G":-2, "H":0, "I":-3, "L":-2, "K":2, "M":-1, "F":-3, "P":-2, "S":-1, "T":-1, "W":-3, "Y":-2, "V":-3},
"N":{"A":-2, "R":0, "N":6, "D":1, "C":-3, "Q":0, "E":0, "G":0, "H":1, "I":-3, "L":-3, "K":0, "M":-2, "F":-3, "P":-2, "S":1, "T":0, "W":-4, "Y":-2, "V":-3},
"D":{"A":-2, "R":-2, "N":1, "D":6, "C":-3, "Q":0, "E":2, "G":-1, "H":-1, "I":-3, "L":-4, "K":-1, "M":-3, "F":-3, "P":-1, "S":0, "T":-1, "W":-4, "Y":-3, "V":-3},
"C":{"A":0, "R":-3, "N":-3, "D":-3, "C":9, "Q":-3, "E":-4, "G":-3, "H":-3, "I":-1, "L":-1, "K":-3, "M":-1, "F":-2, "P":-3, "S":-1, "T":-1, "W":-2, "Y":-2, "V":-1},
"Q":{"A":-1, "R":1, "N":0, "D":0, "C":-3, "Q":5, "E":2, "G":-2, "H":0, "I":-3, "L":-2, "K":1, "M":0, "F":-3, "P":-1, "S":0, "T":-1, "W":-2, "Y":-1, "V":-2},
"E":{"A":-1, "R":0, "N":0, "D":2, "C":-4, "Q":2, "E":5, "G":-2, "H":0, "I":-3, "L":-3, "K":1, "M":-2, "F":-3, "P":-1, "S":0, "T":-1, "W":-3, "Y":-2, "V":-2},
"G":{"A":0, "R":-2, "N":0, "D":-1, "C":-3, "Q":-2, "E":-2, "G":6, "H":-2, "I":-4, "L":-4, "K":-2, "M":-3, "F":-3, "P":-2, "S":0, "T":-2, "W":-2, "Y":-3, "V":-3},
"H":{"A":-2, "R":0, "N":1, "D":-1, "C":-3, "Q":0, "E":0, "G":-2, "H":8, "I":-3, "L":-3, "K":-1, "M":-2, "F":-1, "P":-2, "S":-1, "T":-2, "W":-2, "Y":2, "V":-3},
"I":{"A":-1, "R":-3, "N":-3, "D":-3, "C":-1, "Q":-3, "E":-3, "G":-4, "H":-3, "I":4, "L":2, "K":-3, "M":1, "F":0, "P":-3, "S":-2, "T":-1, "W":-3, "Y":-1, "V":3},
"L":{"A":-1, "R":-2, "N":-3, "D":-4, "C":-1, "Q":-2, "E":-3, "G":-4, "H":-3, "I":2, "L":4, "K":-2, "M":2, "F":0, "P":-3, "S":-2, "T":-1, "W":-2, "Y":-1, "V":1},
"K":{"A":-1, "R":2, "N":0, "D":-1, "C":-3, "Q":1, "E":1, "G":-2, "H":-1, "I":-3, "L":-2, "K":5, "M":-1, "F":-3, "P":-1, "S":0, "T":-1, "W":-3, "Y":-2, "V":-2},
"M":{"A":-1, "R":-1, "N":-2, "D":-3, "C":-1, "Q":0, "E":-2, "G":-3, "H":-2, "I":1, "L":2, "K":-1, "M":5, "F":0, "P":-2, "S":-1, "T":-1, "W":-1, "Y":-1, "V":1},
"F":{"A":-2, "R":-3, "N":-3, "D":-3, "C":-2, "Q":-3, "E":-3, "G":-3, "H":-1, "I":0, "L":0, "K":-3, "M":0, "F":6, "P":-4, "S":-2, "T":-2, "W":1, "Y":3, "V":-1},
"P":{"A":-1, "R":-2, "N":-2, "D":-1, "C":-3, "Q":-1, "E":-1, "G":-2, "H":-2, "I":-3, "L":-3, "K":-1, "M":-2, "F":-4, "P":7, "S":-1, "T":-1, "W":-4, "Y":-3, "V":-2},
"S":{"A":1, "R":-1, "N":1, "D":0, "C":-1, "Q":0, "E":0, "G":0, "H":-1, "I":-2, "L":-2, "K":0, "M":-1, "F":-2, "P":-1, "S":4, "T":1, "W":-3, "Y":-2, "V":-2},
"T":{"A":0, "R":-1, "N":0, "D":-1, "C":-1, "Q":-1, "E":-1, "G":-2, "H":-2, "I":-1, "L":-1, "K":-1, "M":-1, "F":-2, "P":-1, "S":1, "T":5, "W":-2, "Y":-2, "V":0},
"W":{"A":-3, "R":-3, "N":-4, "D":-4, "C":-2, "Q":-2, "E":-3, "G":-2, "H":-2, "I":-3, "L":-2, "K":-3, "M":-1, "F":1, "P":-4, "S":-3, "T":-2, "W":11, "Y":2, "V":-3},
"Y":{"A":-2, "R":-2, "N":-2, "D":-3, "C":-2, "Q":-1, "E":-2, "G":-3, "H":2, "I":-1, "L":-1, "K":-2, "M":-1, "F":3, "P":-3, "S":-2, "T":-2, "W":2, "Y":7, "V":-1},
"V":{"A":0, "R":-3, "N":-3, "D":-3, "C":-1, "Q":-2, "E":-2, "G":-3, "H":-3, "I":3, "L":1, "K":-2, "M":1, "F":-1, "P":-2, "S":-2, "T":0, "W":-3, "Y":-1, "V":4},
}
=======
# Define amino acids and BLOSUM62 scores based on the image
amino_acids = ["C", "S", "T", "P", "A", "G", "N", "D",
               "E", "Q", "H", "R", "K", "M", "I", "L", "V", "F", "Y", "W"]

# Manually encode the matrix from the image
blosum = [
    [9, ],                       # C
    [-1, 4],                     # S
    [-1, 1, 5],                  # T
    [-3, -1, -1, 7],             # P
    [-1, 1, 0, -1, 4],           # A
    [-3, 0, -2, -1, 0, 6],       # G
    [-1, 1, 0, -2, -2, 0, 6],    # N
    [-2, -1, -1, -1, -2, -1, 1, 6],  # D
    [-3, -1, -1, -1, -1, -2, 0, 2, 5],  # E
    [-3, 0, -1, -1, -1, -2, 0, 0, 2, 5], # Q
    [-3, -1, -2, -2, -2, -2, 0, -1, 0, 1, 8], # H
    [-3, -1, -2, -3, -2, -2, 0, -2, 0, 1, 0, 5], # R
    [-3, -1, -1, -1, -1, -2, 0, -1, 1, 2, -1, 2, 5], # K
    [-1, -1, -1, -2, -1, -3, -2, -3, -2, 0, -1, -2, -1, 5], # M
    [-2, -1, -1, -3, -1, -4, -2, -4, -3, -2, -3, -2, -2, 2, 4], # I
    [-1, -2, -1, -4, -1, -4, -3, -4, -3, -2, -3, -3, -3, 3, 2, 4], # L
    [-1, -2, -0, -4, -0, -4, -3, -4, -3, -2, -3, -3, -2, 1, 3, 2, 4], # V
    [-2, -2, -2, -4, -2, -3, -3, -4, -3, -3, -1, -3, -3, 0, 1, 1, 1, 6], # F
    [-2, -2, -2, -3, -2, -3, -2, -3, -2, -3, 2, -2, -2, -1, -1, -1, 0, 3, 7], # Y
    [-2, -3, -3, -4, -3, -2, -4, -4, -3, -2, -2, -3, -2, -1, -1, -2, -2, 1, 4, 11], # W
]

# Convert lower triangle to full matrix
import numpy as np
blosum_matrix = np.zeros((20, 20), dtype=int)
for i in range(20):
    for j in range(i+1):
        blosum_matrix[i, j] = blosum[i][j]
        blosum_matrix[j, i] = blosum[i][j]

st.title("BLOSUM Score Calculator")

wt_aa = st.selectbox("Select wildtype amino acid:", amino_acids)
mut_aa = st.selectbox("Select mutated amino acid:", amino_acids)

i = amino_acids.index(wt_aa)
j = amino_acids.index(mut_aa)
score = blosum_matrix[i, j]

st.write(f"BLOSUM score for {wt_aa} → {mut_aa} = **{score}**")


# In[ ]:
>>>>>>> 411cbaf71956485e7da00c897f46002b949b55bd

# Streamlit app
st.set_page_config(page_title='BLOSUM Score Calculator', layout='centered')
st.title('BLOSUM62 Mutation Score Calculator')

wt = st.text_input('Wildtype amino acid (single-letter code)').upper().strip()
mut = st.text_input('Mutant amino acid (single-letter code)').upper().strip()

if st.button('Calculate'):
    if wt not in BLOSUM62 or mut not in BLOSUM62:
        st.error('Please enter valid one-letter amino acid codes (e.g., A, R, N, D, ...).')
    else:
        score = BLOSUM62[wt][mut]
        st.success(f'BLOSUM62 score for {wt} → {mut} is {score}')

st.markdown("This tool calculates the substitution score between a wildtype and mutated amino acid using the BLOSUM62 matrix.")
