#!/usr/bin/env python
# coding: utf-8

# In[1]:
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




