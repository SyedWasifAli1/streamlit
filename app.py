import streamlit as st

def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        "meters": {"feet": 3.28084, "kilometers": 0.001, "miles": 0.000621371},
        "feet": {"meters": 0.3048, "kilometers": 0.0003048, "miles": 0.000189394},
        "kilograms": {"grams": 1000, "pounds": 2.20462},
        "grams": {"kilograms": 0.001, "pounds": 0.00220462},
        "celsius": {"fahrenheit": lambda c: (c * 9/5) + 32},
        "fahrenheit": {"celsius": lambda f: (f - 32) * 5/9}
    }
    
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        factor = conversion_factors[from_unit][to_unit]
        return factor(value) if callable(factor) else value * factor
    else:
        return "Invalid conversion"

st.title("Unit Converter")

# User Input
value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
from_unit = st.selectbox("From Unit:", ["meters", "feet", "kilograms", "grams", "celsius", "fahrenheit"])
to_unit = st.selectbox("To Unit:", ["meters", "feet", "kilograms", "grams", "celsius", "fahrenheit"])

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.write(f"Converted Value: {result} {to_unit}")