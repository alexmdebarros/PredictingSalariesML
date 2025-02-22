# -*- coding: utf-8 -*-
"""Análise salarial machine learning

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Df_DpzshtNZPuAYt6mZm7LKkAN4VA_4j

# Análise Salarial com Modelo de Regressão

Este projeto tem como objetivo analisar os dados salariais de uma base fictícia e construir um modelo de árvore de decisão para prever os salários com base em variáveis como idade, gênero, nível educacional e experiência.

## 1. Coleta de Dados

A base de dados utilizada (“SalaryData.csv”) possui a seguinte estrutura:

| Coluna              | Descrição                                     |
| ------------------- | --------------------------------------------- |
| Age                 | Idade do profissional                         |
| Gender              | Gênero do profissional (Male/Female)          |
| Education Level     | Nível de educação (Bachelor's, Master's, PhD) |
| Job Title           | Cargo ocupado (vou usar futuramente)          |
| Years of Experience | Anos de experiência                           |
| Salary              | Salário anual (em dólares)                    |
"""

import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import gdown

#link para baixar o df no drive
url = 'https://drive.google.com/uc?id=1Hdsc4JmZL_Aqdy2fPnuxBRt-Q5wLludF'
gdown.download(url, 'SalaryData.csv', quiet=False)

#abrindo dataframe
df = pd.read_csv('SalaryData.csv', sep=',')
df.head()

#verificando dados faltantes
df.isnull().sum()

#removendo linhas com dados faltantes
df = df.dropna()
df.isnull().sum()

#verificando colunas categóricas
df.info()

#removendo coluna Job Title
df.drop('Job Title', axis=1, inplace=True)

#calculando a contagem de cada gênero
gender_counts = df['Gender'].value_counts()

#criando o gráfico de barras
plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', data=df, hue='Gender', palette={'Female': 'pink', 'Male': 'blue'})
plt.title('Distribuição de Gênero')
plt.xlabel('Gênero')
plt.ylabel('Contagem')


#adicionando rótulos com as porcentagens
total = len(df)
for p in plt.gca().patches:
    percentage = '{:.1f}%'.format(100 * p.get_height() / total)
    x = p.get_x() + p.get_width() / 2 - 0.1
    y = p.get_height() + 2
    plt.annotate(percentage, (x, y), size=12)


plt.show()

"""No grafico acima podemos perceber que o publico masculino (52%) é um pouco maior que o feminino (48%).

Baseado nisso vamos agora gerar um grafico mostrando a média salarial baseada no sexo.
"""

#calculando a mediana salarial por gênero
mean_salary_by_gender = df.groupby('Gender')['Salary'].mean()

#criando o gráfico de barras
plt.figure(figsize=(8, 6))
sns.barplot(
    x=mean_salary_by_gender.index,
    y=mean_salary_by_gender.values,
    palette=['pink', 'blue']
)

# Adicionando os rótulos de valor acima das barras
for index, value in enumerate(mean_salary_by_gender.values):
    plt.text(
        x=index,
        y=value + 1000,
        s=f'${value:,.2f}',
        ha='center'
    )

#ajustando os títulos e rótulos
plt.title('Média Salarial por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Média Salarial')
plt.show()

"""No grafico acima percebemos que a média salarial do genero masculino é de 103.867,78 por ano enquanto o feminino é de 97.011,17, uma diferença de 6.856,61 que talvez possa ser influenciada pela quantidade maior de pessoas do sexo masculino."""

#grafico de distribuição salarial por  nivel de educação
plt.figure(figsize=(8, 6))
sns.boxplot(x='Education Level', y='Salary', data=df,hue='Education Level', palette='Set3')
plt.title('Distribuição Salarial por Nível de Educação')
plt.xlabel('Nível de Educação')
plt.ylabel('Salário')
plt.show()

#grafico média salarial por tempo de experiencia
plt.figure(figsize=(8, 6))
sns.lineplot(x='Years of Experience', y='Salary', data=df, color='blue')
plt.grid(True)
plt.title('Média Salarial por Anos de Experiência')
plt.xlabel('Anos de Experiência')
plt.ylabel('Média Salarial')
plt.show()

#grafico de média salarial por idade
plt.figure(figsize=(8, 6))
sns.lineplot(x='Age', y='Salary', data=df, color='blue')
plt.grid(True)
plt.title('Média Salarial por Idade')
plt.xlabel('Idade')
plt.ylabel('Média Salarial')
plt.show()

"""#2. Modelagem

"""

#criando o mapeamento para coluna Education Level
education_mapping = {
    "Bachelor's": 0,
    "Master's": 1,
    "PhD": 2
}

#mapeando os valores da coluna Education Level
df['Education Level'] = df['Education Level'].map(education_mapping)

#coluna Gender (masculino = 1, Feminino = 0)
gender_mapping = {
    "Male": 1,
    "Female": 0
}
df['Gender'] = df['Gender'].map(gender_mapping)

df.head()

#selecionando variáveis independentes e dependente
X = df[['Age', 'Gender', 'Education Level', 'Years of Experience']]
y = df['Salary']

#dividindo os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Tamanho do conjunto de treino:", X_train.shape)
print("Tamanho do conjunto de teste:", X_test.shape)

#criando o modelo de árvore de decisão
model = DecisionTreeRegressor(random_state=42)

#treinando o modelo
model.fit(X_train, y_train)

#previsões
y_pred = model.predict(X_test)

print("Previsões do modelo:", y_pred[:5])

#calculando métricas de avaliação
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("R² Score:", r2 * 100)

#comparação de valores reais vs. previstos
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color='green')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], '--r', linewidth=2)
plt.title('Valores Reais vs. Previstos')
plt.xlabel('Valores Reais')
plt.ylabel('Valores Previstos')
plt.show()

#prevendo salario de alguem com 10 anos de experiencia, 35 anos de idade e nivel de educação 1 mestrado
predict = pd.DataFrame({'Age': [35], 'Gender': [1], 'Education Level': [1], 'Years of Experience': [10]})
predicted_salary = model.predict(predict)

print("Salário previsto:", predicted_salary[0])