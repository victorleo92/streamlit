import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Define a function to create a chart
def create_chart():
    # Generate some sample data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Create a line plot of the data
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Business Visualization')

    # Return the chart as a PNG image
    return fig

# Define the Streamlit app
def main():
    # Set the title and subtitle of the app
    st.title("Business Visualization App")
    st.subheader("Using Streamlit and Matplotlib")

    # Create a chart and display it
    chart = create_chart()
    st.pyplot(chart)

# Run the Streamlit app
if __name__ == '__main__':
    main()
