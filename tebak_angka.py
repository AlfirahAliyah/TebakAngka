import streamlit as st
import random

def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

st.title('Tebak Angka!')

angka_rahasia = generate_random_number(1, 100)

tebakan = st.number_input('Masukkan tebakan Anda:', min_value=1, max_value=100)

if st.button('Cek Tebakan'):
    if tebakan < angka_rahasia:
        st.error('Terlalu rendah!')
    elif tebakan > angka_rahasia:
        st.error('Terlalu tinggi!')
    else:
        st.success('Selamat! Tebakan Anda benar!')