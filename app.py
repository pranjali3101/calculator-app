import streamlit as st

# Title
st.set_page_config(page_title="Calculator App", page_icon="🧮")
st.title("🧮 Simple Calculator App")

# Input fields
num1 = st.number_input("Enter first number:", format="%f")
num2 = st.number_input("Enter second number:", format="%f")

# Select operation
operation = st.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Calculate button
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"✅ Result: {num1} + {num2} = {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"✅ Result: {num1} - {num2} = {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"✅ Result: {num1} × {num2} = {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"✅ Result: {num1} ÷ {num2} = {result}")
        else:
            st.error("❌ Error: Division by zero is not allowed!")
