import streamlit as st

# Title of the app
st.title("Unit Converter")

# Sidebar for unit selection
unit_type = st.sidebar.selectbox("Select Unit Type", ["Length", "Weight", "Temperature"])

# Conversion functions
def convert_length(value, from_unit, to_unit):
    length_conversions = {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Inch": 39.3701,
        "Foot": 3.28084,
        "Yard": 1.09361,
        "Mile": 0.000621371
    }
    return value * (length_conversions[to_unit] / length_conversions[from_unit])

def convert_weight(value, from_unit, to_unit):
    weight_conversions = {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1e6,
        "Pound": 2.20462,
        "Ounce": 35.274
    }
    return value * (weight_conversions[to_unit] / weight_conversions[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
        else:
            return value
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        return value

# Main content
value = st.number_input("Enter the value to convert", value=1.0)

if unit_type == "Length":
    length_units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Inch", "Foot", "Yard", "Mile"]
    from_unit = st.selectbox("From", length_units)
    to_unit = st.selectbox("To", length_units)
    result = convert_length(value, from_unit, to_unit)

elif unit_type == "Weight":
    weight_units = ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"]
    from_unit = st.selectbox("From", weight_units)
    to_unit = st.selectbox("To", weight_units)
    result = convert_weight(value, from_unit, to_unit)

elif unit_type == "Temperature":
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From", temperature_units)
    to_unit = st.selectbox("To", temperature_units)
    result = convert_temperature(value, from_unit, to_unit)

# Display the result
st.write(f"Converted value: {result:.2f} {to_unit}")