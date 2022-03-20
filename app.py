import streamlit as st
import pandas as pd

#DEbe poderse registrr un usuario con su nombre y buscalo en el selectbox para poder guardar
#sus efluentes y ultimos labroatorios
st.image("WAPP.png")
nombres=(['Alonso','Fernando'])
Registro=st.text_input("Nombre")
names=nombres.append(Registro)

@st.cache(allow_output_mutation=True)
def get_data():
    return []

user_id = st.text_input("User ID")
foo = st.slider("foo", 0, 100)
bar = st.slider("bar", 0, 100)

if st.button("Add row"):
    get_data().append({"UserID": user_id, "foo": foo, "bar": bar})

st.write(pd.DataFrame(get_data()))
