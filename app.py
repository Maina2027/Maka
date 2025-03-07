import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
# Generate random time series data
st.header("Anything")
time_series = np.random.randn(100)

if st.button("Test this"):
  # Plot the time series
  plt.plot(time_series)
  plt.title("Random 100-Unit Time Series")
  plt.xlabel("Time")
  plt.ylabel("Value")
  st.pyplot(plt.gcf())
