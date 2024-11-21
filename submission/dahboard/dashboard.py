import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import calendar
from datetime import datetime

# Load dataset
df_day = pd.read_csv('Day.csv')  # Ganti dengan path file dataset day
df_hour = pd.read_csv('Hour.csv')  # Ganti dengan path file dataset hour

# Convert date columns to datetime
df_day['dteday'] = pd.to_datetime(df_day['dteday'])

# Sidebar for navigation
st.sidebar.title("Bike Sharing Dashboard")
st.sidebar.markdown("Navigasi untuk melihat analisis berbeda.")
page = st.sidebar.radio("Pilih Halaman", ['Summary', 'Analisis Waktu', 'Analisis Hari & Musim', 'Analisis Cuaca'])

# Filter Tanggal
st.sidebar.subheader("Filter Data")
start_date = st.sidebar.date_input("Start Date", df_day['dteday'].min())
end_date = st.sidebar.date_input("End Date", df_day['dteday'].max())

# Filter data based on date range
filtered_data = df_day[(df_day['dteday'] >= pd.to_datetime(start_date)) & (df_day['dteday'] <= pd.to_datetime(end_date))]

# Summary Page
if page == 'Summary':
    st.title("Ringkasan Statistik Bike Sharing")

    # Scorecards
    total_rentals = filtered_data['cnt'].sum()
    avg_registered = filtered_data['registered'].mean()
    avg_casual = filtered_data['casual'].mean()
    registered_share = (filtered_data['registered'].sum() / total_rentals) * 100
    casual_share = (filtered_data['casual'].sum() / total_rentals) * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rentals", f"{total_rentals:,}")
    col2.metric("Avg Registered Users", f"{avg_registered:.2f}")
    col3.metric("Avg Casual Users", f"{avg_casual:.2f}")

    col4, col5 = st.columns(2)
    col4.metric("Registered Share (%)", f"{registered_share:.1f}%")
    col5.metric("Casual Share (%)", f"{casual_share:.1f}%")

    st.markdown("---")
    st.markdown("Ringkasan ini didasarkan pada data yang difilter.")

# Time Analysis Page
elif page == 'Analisis Waktu':
    st.title("Distribusi Pengguna Berdasarkan Jam")
    hour = df_hour.groupby('hr')[['registered', 'casual']].mean()
    fig1 = px.line(hour, x=hour.index, y=['registered', 'casual'], 
                   labels={'x': 'Jam', 'value': 'Rata-Rata Pengguna', 'variable': 'Tipe Pengguna'},
                   title='Distribusi Rata-Rata Pengguna Registered dan Casual Berdasarkan Jam')
    st.plotly_chart(fig1)

# Day and Season Analysis Page
elif page == 'Analisis Hari & Musim':
    st.title("Analisis Hari dan Musim")
    
    # Perbandingan Pengguna Berdasarkan Hari
    st.subheader("Perbandingan Pengguna Berdasarkan Hari")
    fig2, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weekday', y='registered', data=filtered_data, label='Registered Users', color='#B83A14', width=0.5, errorbar=None, ax=ax)
    sns.barplot(x='weekday', y='casual', data=filtered_data, label='Casual Users', color='#231650', width=0.5, errorbar=None, ax=ax)
    ax.set_title('Comparison between Registered and Casual Users by Day')
    ax.set_xlabel('Hari')
    ax.set_ylabel('Rata-Rata Pengguna')
    ax.legend()
    st.pyplot(fig2)

    # Distribusi Pengguna Berdasarkan Musim
    st.subheader("Distribusi Pengguna Berdasarkan Musim")
    season_total = filtered_data.groupby('season')['cnt'].sum()
    fig3, ax = plt.subplots(figsize=(8, 8))
    ax.pie(season_total, labels=season_total.index, autopct='%1.1f%%', colors=sns.color_palette('Spectral'))
    ax.set_title('Distribusi Jumlah Peminjaman Berdasarkan Musim')
    st.pyplot(fig3)

# Weather Analysis Page
elif page == 'Analisis Cuaca':
    st.title("Analisis Pengguna Berdasarkan Cuaca")
    fig4, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weathersit', y='registered', data=filtered_data, label='Registered Users', color='#f6ae2d', width=0.5, errorbar=None, ax=ax)
    sns.barplot(x='weathersit', y='casual', data=filtered_data, label='Casual Users', color='#33658A', width=0.5, errorbar=None, ax=ax)
    ax.set_title('Comparison between Registered and Casual Users by Weather Condition')
    ax.set_xlabel('Kondisi Cuaca')
    ax.set_ylabel('Rata-Rata Pengguna')
    ax.legend()
    st.pyplot(fig4)

# Footer Section
st.sidebar.markdown("---")
st.sidebar.markdown("**Dashboard dibuat oleh Data Analyst.**")