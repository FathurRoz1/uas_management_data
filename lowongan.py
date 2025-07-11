import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Baca data
df = pd.read_csv('job_postings.csv')

# Konversi kolom waktu
df['first_seen'] = pd.to_datetime(df['first_seen'], errors='coerce')
df['last_processed_time'] = pd.to_datetime(df['last_processed_time'], errors='coerce')

# Statistik dasar
print("Jumlah baris:", len(df))
print("Jumlah kolom:", len(df.columns))
print("Kolom unik:")
print(df.nunique())

# Cek missing values
print("\nMissing values:")
print(df.isnull().sum())

# Pekerjaan per negara (Top 10)
top_countries = df['search_country'].value_counts().head(10)
print("\nTop 10 negara dengan lowongan terbanyak:")
print(top_countries)

# Visualisasi negara
plt.figure(figsize=(10,6))
top_countries.plot(kind='bar', color='skyblue')
plt.title('Top 10 Negara dengan Lowongan Terbanyak')
plt.ylabel('Jumlah Lowongan')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Distribusi job_type
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='job_type', order=df['job_type'].value_counts().index)
plt.title('Distribusi Jenis Pekerjaan (Job Type)')
plt.xlabel('Job Type')
plt.ylabel('Jumlah')
plt.tight_layout()
plt.show()

# Distribusi job_level
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='job_level', order=df['job_level'].value_counts().index)
plt.title('Distribusi Level Pekerjaan')
plt.xlabel('Job Level')
plt.ylabel('Jumlah')
plt.tight_layout()
plt.show()

# 10 Jabatan paling sering muncul
top_titles = df['job_title'].value_counts().head(10)
print("\nTop 10 Jabatan (job_title) paling sering:")
print(top_titles)

# Tren lowongan dari waktu 'first_seen'
jobs_per_month = df.set_index('first_seen').resample('M').size()

plt.figure(figsize=(10,6))
jobs_per_month.plot()
plt.title('Tren Jumlah Lowongan per Bulan')
plt.ylabel('Jumlah Lowongan')
plt.xlabel('Bulan')
plt.tight_layout()
plt.show()

# Top perusahaan yang posting pekerjaan
top_companies = df['company'].value_counts().head(10)
print("\nTop 10 Perusahaan dengan Lowongan Terbanyak:")
print(top_companies)

# Simpan versi bersih (opsional)
# df_clean = df.dropna(subset=['job_title', 'search_country'])
# df_clean.to_csv('cleaned_ai_jobs.csv', index=False)
