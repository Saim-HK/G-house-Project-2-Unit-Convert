import streamlit as st

def convert_units(value, from_unit, to_unit, conversion_dict):
    if from_unit in conversion_dict and to_unit in conversion_dict:
        return value * (conversion_dict[to_unit] / conversion_dict[from_unit])
    return None

length_units = {
    "Meters": 1,
    "Kilometers": 0.001,
    "Centimeters": 100,
    "Millimeters": 1000,
    "Miles": 0.000621371,
    "Yards": 1.09361,
    "Feet": 3.28084,
    "Inches": 39.3701
}

weight_units = {
    "Kilograms": 1,
    "Grams": 1000,
    "Milligrams": 1_000_000,
    "Pounds": 2.20462,
    "Ounces": 35.274
}

temperature_units = {
    "Celsius": "C",
    "Fahrenheit": "F",
    "Kelvin": "K"
}

st.title("Unit Converter")

# Choose conversion category
category = st.selectbox("Select Conversion Category", ["Length", "Weight", "Temperature"])

# Input value
value = st.number_input("Enter value", min_value=0.0, format="%.2f")

if category == "Length":
    from_unit = st.selectbox("From Unit", list(length_units.keys()))
    to_unit = st.selectbox("To Unit", list(length_units.keys()))
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit, length_units)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Weight":
    from_unit = st.selectbox("From Unit", list(weight_units.keys()))
    to_unit = st.selectbox("To Unit", list(weight_units.keys()))
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit, weight_units)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("From Unit", list(temperature_units.keys()))
    to_unit = st.selectbox("To Unit", list(temperature_units.keys()))

    def convert_temperature(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == "Celsius":
            return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
        elif from_unit == "Fahrenheit":
            return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")