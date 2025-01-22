import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("📊 Data Visualization Example")

data = pd.DataFrame({
    'x': np.linspace(0, 10, 100),
    'y': np.sin(np.linspace(0, 10, 100))
})

st.write("Here’s a simple line chart:")
st.line_chart(data)

st.write("Matplotlib plot:")
fig, ax = plt.subplots()
ax.plot(data['x'], data['y'], label="y = sin(x)")
ax.set_title("Matplotlib Example")
ax.legend()
st.pyplot(fig)
