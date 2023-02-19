import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a pandas DataFrame
df = pd.read_csv('your_data_file.csv')

def main():
    # Set the title and subtitle of the app
    st.title("Business Data Visualization")
    st.subheader("Sales data for 2022")

    # Show a scatter plot of SellPrice vs Margin
    fig, ax = plt.subplots()
    ax.scatter(df['SellPrice'], df['Margin'])
    ax.set_xlabel('Sell Price')
    ax.set_ylabel('Margin')
    st.pyplot(fig)

    # Show a histogram of the SellPrice column
    fig, ax = plt.subplots()
    ax.hist(df['SellPrice'], bins=10)
    ax.set_xlabel('Sell Price')
    ax.set_ylabel('Count')
    st.pyplot(fig)

    # Show a bar chart of the total sales per SKU
    sales_by_sku = df.groupby('Sku')['SaleInvoice'].count()
    fig, ax = plt.subplots()
    ax.bar(sales_by_sku.index, sales_by_sku.values)
    ax.set_xticklabels(sales_by_sku.index, rotation=90)
    ax.set_xlabel('SKU')
    ax.set_ylabel('Number of Sales')
    st.pyplot(fig)

if __name__ == "__main__":
    main()
