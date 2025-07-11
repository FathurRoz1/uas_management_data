import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data
df = pd.read_csv('ai_job_trends_dataset.csv')

# Menampilkan 5 data pertama
print(df.head())
print(df.dtypes)

# Cek missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Bersihkan angka: hapus simbol $, % jika ada — (tidak perlu di file ini tapi bisa kamu aktifkan)
# df['Median Salary (USD)'] = df['Median Salary (USD)'].replace('[\$,]', '', regex=True).astype(float)

# Konversi tipe data numerik (jika belum otomatis)
numeric_cols = ['Median Salary (USD)', 'Experience Required (Years)', 'Job Openings (2024)', 
                'Projected Openings (2030)', 'Remote Work Ratio (%)', 'Automation Risk (%)', 'Gender Diversity (%)']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Rata-rata gaji berdasarkan industri
avg_salary_industry = df.groupby('Industry')['Median Salary (USD)'].mean().sort_values(ascending=False)
print("\nRata-rata gaji per industri:")
print(avg_salary_industry)

# Visualisasi: Top 10 Industri dengan Gaji Tertinggi
avg_salary_industry.head(10).plot(kind='bar', title='Top 10 Industri dengan Median Gaji Tertinggi')
plt.ylabel('Median Salary (USD)')
plt.tight_layout()
plt.show()

# Visualisasi: Rasio kerja remote vs risiko otomatisasi
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Remote Work Ratio (%)', y='Automation Risk (%)', hue='Industry')
plt.title('Remote Work vs Automation Risk by Industry')
plt.tight_layout()
plt.show()

# Visualisasi: Distribusi Gender Diversity
plt.figure(figsize=(8, 6))
sns.histplot(df['Gender Diversity (%)'], bins=20, kde=True)
plt.title('Distribusi Gender Diversity (%)')
plt.tight_layout()
plt.show()

# Tabel: 5 pekerjaan dengan pembukaan tertinggi di 2030
top_openings = df.sort_values('Projected Openings (2030)', ascending=False)[
    ['Job Title', 'Industry', 'Projected Openings (2030)']].head(5)
print("\nTop 5 pekerjaan dengan proyeksi pembukaan tertinggi di 2030:")
print(top_openings)

# Optional: Simpan versi bersih ke CSV baru
# df.to_csv('ai_job_trends_cleaned.csv', index=False)
