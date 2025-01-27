# Análise Salarial com Modelo de Regressão

Este projeto tem como objetivo analisar os dados salariais de uma base fictícia e construir um modelo de árvore de decisão para prever os salários com base em variáveis como idade, gênero, nível educacional e experiência.

## 1. Coleta de Dados

A base de dados utilizada (“SalaryData.csv”) possui a seguinte estrutura:

| Coluna              | Descrição                                     |
| ------------------- | --------------------------------------------- |
| Age                 | Idade do profissional                         |
| Gender              | Gênero do profissional (Male/Female)          |
| Education Level     | Nível de educação (Bachelor's, Master's, PhD) |
| Years of Experience | Anos de experiência                           |
| Salary              | Salário anual (em dólares)                    |

A coluna `Job Title` foi descartada devido ao alto número de valores únicos, o que poderia introduzir ruído no modelo e dificultar a interpretação dos resultados mas futuramente pretendo trabalhar em cima dessa coluna e aperfeiçoar o modelo.

## 1.1. Gráficos Gerados

![dist-por-genero](https://github.com/alexmdebarros/PredictingSalariesML/blob/main/dist-por-genero.png)

No grafico acima podemos perceber que o publico masculino (52%) é um pouco maior que o feminino (48%).
Baseado nisso gerei um grafico mostrando a média salarial por sexo.

![media-por-genero](https://github.com/alexmdebarros/PredictingSalariesML/blob/main/media-por-genero.png)

No grafico acima percebemos que a média salarial do genero masculino é de 103.867,78 por ano enquanto o feminino é de 97.011,17, uma diferença de 6.856,61 que talvez possa ser influenciada pela quantidade maior de pessoas do sexo masculino.

![dist-por-nivel-academico](https://github.com/alexmdebarros/PredictingSalariesML/blob/main/distr-por-nivel-academico.png)

O gráfico mostra a importância da educação como um fator determinante para a remuneração. Profissionais com pós-graduação (mestrado e doutorado) tendem a ter salários mais elevados e uma menor dispersão salarial em comparação aos bacharéis. No entanto, profissionais com nivel mais alto com PhD tendem a ter maiores salários mas com uma dispersão maior.

![dist-por-tempo](https://github.com/alexmdebarros/PredictingSalariesML/blob/main/media-por-tempo.png)

O gráfico demonstra que a experiência é um fator importante para a remuneração, mas não o único. Perceber isso em alguns picos de alta principalmente acima dos 15 anos de experiência.

![dist-por-idade](https://github.com/alexmdebarros/PredictingSalariesML/blob/main/media-por-idade.png)

O gráfico demonstra que a idade é um fator que influencia a remuneração, com a tendência de aumento da média salarial talvez ligada também ao tempo de experiência.

## 2. Modelagem

A modelagem foi baseada nas seguintes etapas:

### 2.1. Tratamento de Dados Categóricos

- A coluna `Education Level` foi convertida para valores numéricos:

  - Bachelor's: 0
  - Master's: 1
  - PhD: 2

- A coluna `Gender` foi convertida para valores binários:

  - Male: 1
  - Female: 0

### 2.2. Divisão dos Dados

Os dados foram divididos em:

- Conjunto de treino (80%)
- Conjunto de teste (20%)

### 2.3. Modelo Utilizado

Foi utilizado um modelo de regressão baseado em árvores de decisão, implementado com a biblioteca `sklearn`.

### 2.4. Métricas de Avaliação

As seguintes métricas foram calculadas:

- **Mean Absolute Error (MAE)**: Média dos erros absolutos.
- **Mean Squared Error (MSE)**: Média dos erros ao quadrado.
- **R² Score**: Qualidade do ajuste do modelo.

## 3. Resultados

### 3.1. Métricas do Modelo

- **MAE**: 9428.57
- **MSE**: 231101568.41
- **R² Score**: 90.36

Os resultados indicam que o modelo conseguiu capturar uma boa parte da variabilidade dos salários, apresentando um R² de aproximadamente 90%, o que é um desempenho muito satisfatório.

### 3.2. Visualização

O gráfico abaixo compara os valores reais e previstos pelo modelo:

![download (5)](https://github.com/user-attachments/assets/77476656-c26d-445c-ba83-d363f87990f2)

O gráfico "Reais vs. Previstos" demonstra que o modelo de árvore de decisão apresenta uma boa capacidade de previsão dos salários, com poucas dispersões. A análise desse gráfico auxilia na avaliação da performance do modelo e na identificação de possíveis áreas de aprimoramento.

## 4. Conclusão

- **Conclusão:** O modelo apresentou um desempenho robusto, com um R² elevado e métricas de erro dentro de uma faixa aceitável. As variáveis idade, gênero, nível educacional e anos de experiência mostraram-se preditoras relevantes para o salário.
A análise revela como características individuais, como idade e nível educacional, estão fortemente relacionadas aos salários. Profissionais com maior experiência e formação avançada (como mestrado e doutorado) tendem a receber salários mais elevados, enquanto o impacto do gênero ainda é perceptível em algumas faixas salariais. Essa visualização dos dados permite que empresas identifiquem potenciais desigualdades e promovam estratégias mais justas de remuneração.
Além disso, o modelo criado oferece uma ferramenta prática para prever salários com base em características facilmente mensuráveis, auxiliando tanto os gestores quanto os profissionais de recursos humanos na tomada de decisões estratégicas.

## 6. Execução do Projeto

Para reproduzir este projeto:

1. Instale as bibliotecas necessárias:
   ```bash
   pip install pandas scikit-learn matplotlib
   ```
2. Execute o script Python com os códigos fornecidos.
3. Verifique os resultados no terminal e nos gráficos gerados.

## 7. Repositório GitHub

Todos os códigos e visualizações estão disponíveis no repositório GitHub.


