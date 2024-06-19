import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Name
#Description
st.sidebar.title("Data analysis application")
st.write("Load CSV file and fill the empties")
# Step 1 Load CSV file
uploaded_file = st.file_uploader('Load CSV-file', type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(5))
else:
    st.stop()


# Step 2 Cheak the the empty ent.
missed_values = df.isna().sum()
missed_values = missed_values[missed_values > 0]

if len(missed_values) > 0:
    st.write("Number of empties value in dataframe", len(missed_values))
    st.write(missed_values)
    fig, ax = plt.subplots()
    sns.barplot(x=missed_values.index, y=missed_values.values)
    ax.set_title("empties in columns")
    st.pyplot(fig)
else:
    st.write("There is no any empties in data")
    st.stop()

df_filled = df[missed_values.index].copy()
# <Step 3 Fill the empties
if len(missed_values) !=0:
    button = st.button("Fill empties")
    if button:

        df_filled = df[missed_values.index].copy()

        for col in df_filled.columns:
            if df_filled[col].dtype =="object":
                df_filled[col] = df_filled[col].fillna(df_filled[col].mode()[0])
            else:
                df_filled[col] = df_filled[col].fillna(df_filled[col].median())

        st.write(df_filled.head(5))
# Load free fra empties CSV-file
st.download_button(label="DOwnload CSV -file",
                   data=df_filled.to_csv(),
                     file_name='filed.csv',
                     mime='txt/csv')