import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("dashboard/main_data.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Start Date", df['dteday'].min())
end_date = st.sidebar.date_input("End Date", df['dteday'].max())
filtered_df = df[(df['dteday'] >= pd.Timestamp(start_date)) & (df['dteday'] <= pd.Timestamp(end_date))]

# Dashboard Title
st.title("🚲 Bike Sharing Dashboard")
st.markdown("### Analisis Penyewaan Sepeda Berbasis Data")

# KPI Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Penyewaan", f"{filtered_df['cnt'].sum():,}")
col2.metric("Rata-rata Harian", f"{filtered_df['cnt'].mean():,.0f}")
col3.metric("Penyewaan Maksimum", f"{filtered_df['cnt'].max():,}")

# Tren Penyewaan Sepeda
st.subheader("📈 Tren Penyewaan Sepeda")
fig_trend = px.line(filtered_df, x='dteday', y='cnt', title="Tren Penyewaan Sepeda Harian", labels={'cnt': 'Jumlah Penyewaan'})
st.plotly_chart(fig_trend, use_container_width=True)

# Analisis Cuaca vs Penyewaan
st.subheader("🌤️ Pengaruh Cuaca terhadap Penyewaan")
fig_weather = px.box(filtered_df, x='weathersit', y='cnt', title="Distribusi Penyewaan Berdasarkan Cuaca",
                      labels={'cnt': 'Jumlah Penyewaan', 'weathersit': 'Kondisi Cuaca'})
st.plotly_chart(fig_weather, use_container_width=True)

# Perbandingan Hari Kerja vs Akhir Pekan
st.subheader("📊 Perbandingan Penyewaan: Hari Kerja vs Akhir Pekan")
filtered_df['is_weekend'] = filtered_df['weekday'].apply(lambda x: 'Weekend' if x in [0, 6] else 'Weekday')
fig_weekend = px.bar(filtered_df.groupby('is_weekend')['cnt'].mean().reset_index(), x='is_weekend', y='cnt',
                     title="Rata-rata Penyewaan Sepeda: Weekday vs Weekend", labels={'cnt': 'Jumlah Penyewaan'})
st.plotly_chart(fig_weekend, use_container_width=True)

# Clustering Manual
st.subheader("🔍 Clustering Penggunaan Sepeda")
bins = [0, 2000, 4000, 6000, 10000]
labels = ['Rendah', 'Sedang', 'Tinggi', 'Sangat Tinggi']
filtered_df['cluster_usage'] = pd.cut(filtered_df['cnt'], bins=bins, labels=labels)
fig_cluster = px.histogram(filtered_df, x='cluster_usage', title="Distribusi Clustering Berdasarkan Penggunaan",
                           labels={'cluster_usage': 'Kategori Penggunaan'})
st.plotly_chart(fig_cluster, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Made by Hubbal Habbaza for Dicoding Data Analysis Final Project Submission")
