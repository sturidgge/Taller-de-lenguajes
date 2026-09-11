import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import squarify

df = pd.read_csv('python_chart/issues.csv')

print(df.head())

print(df)

print("Cantidad de valores nulos: ", df.isnull().sum())

print("cantidad de valores duplicados: ", df.duplicated().sum())

print(df.info())

print(df["name"].unique())

df["name"] = df["name"].str.lower()

print(df["name"].unique())

print(df[df["name"] == "python"])

print(df[df["name"] == "ruby"])



plt.figure(figsize=(12,6))
sns.barplot(
    data=df.head(8),
    x="name",
    y="count",
    hue="name",       # asignamos hue
    palette="viridis",
    legend=False          # evita mostrar leyenda duplicada
)
plt.title("Lenguajes con mas Count tercer trimestre de 2011")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12,6))
sns.barplot(
    data=df,
    x="name",
    y="count",
    hue="name",       # asignamos hue
    palette="viridis",
    legend=False          # evita mostrar leyenda duplicada
)
plt.title("Lenguajes con mas Counts")
plt.xticks(rotation=45)
plt.show()

df_agrupado = df.groupby('name')['count'].sum()

plt.figure(figsize=(12,8))
squarify.plot(sizes=df_agrupado, label=df_agrupado.index, alpha=.8)
plt.title("Proporción de count por Lenguaje (2011)")
plt.axis('off')
plt.show()