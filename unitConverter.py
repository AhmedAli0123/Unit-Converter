import streamlit as st

def convert(value, from_unit, to_unit, conversion_dict):
    return value * (conversion_dict[to_unit] / conversion_dict[from_unit])

st.title("Simple Unit Converter By Ahmed")

conversion_type = st.selectbox("Select conversion type", ["Length", "Weight"])

if conversion_type == "Length":
    units = {
                "meter": 1, 
                "kilometer": 0.001, 
                "centimeter": 100, 
                "millimeter": 1000, 
                "mile": 0.000621371, 
                "yard": 1.09361, 
                "foot": 3.28084, 
                "inch": 39.3701
            }
elif conversion_type == "Weight":
    units = {   
                "kilogram": 1, 
                "gram": 1000, 
                "milligram": 1e6, 
                "pound": 2.20462, 
                "lb": 2.20462
            }


value = st.number_input("Enter value")
from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units)


if st.button("Convert"):
    if value == 0:
        st.error("Please Enter the Value")
    else:    
        result = convert(value, from_unit, to_unit, units)
        st.success(f"{value} {from_unit} = {result} {to_unit}")
