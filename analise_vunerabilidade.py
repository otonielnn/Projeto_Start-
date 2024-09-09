import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels.api as sm

# Carregar Dados
data = pd.read_csv("data/openvas_scan_results.csv")

# Verificar os Dados
print(data.head())
print(data.info())

# Mapeamento e Verificação da Severidade
severity_mapping = {'Low': 1, 'Medium': 2, 'High': 3}
data['Severity'] = data['Severity'].map(severity_mapping)

print('---')
print(data['Severity'].unique())
print('---')
print(data['Severity'].isna().sum())
print('---')
print(data['Severity'].value_counts())
print('---')
print(data[['Severity']].head())
print('---')

# Verificando se há valores NaN após o mapeamento
if data['Severity'].isna().all():
    raise ValueError('Todos os valores na coluna \'Severity\' são NaN após o mapeamento. Verifique os dados de entrada')

# Subistituição de NaN na coluna 'Severity' com a moda:
severity_mode = data['Severity'].mode()
if not severity_mode.empty:
    data['Severity'].fillna(severity_mode[0])
else:
    raise ValueError('Não há moda disponível para a coluna \'Severity\'. Verifique os dados de entrada.')

# Conversão de CVSS e Substituição de NaN
data['CVSS'] = pd.to_numeric(data['CVSS'], errors='coerce')
data['CVSS'] = data['CVSS'].fillna(data['CVSS'].median())

# Cálculo do Pontuação de Risco e Classificação
data['risk_score'] = data['Severity'] * data['CVSS']

data_sorted = data.sort_values(by="risk_score", ascending=False)

def classify_priority(row):
    if row["risk_score"] > 75:
        return "Alta"
    elif row["risk_score"] > 50:
        return "Média"
    else:
        return "Baixa"

data_sorted["priority"] = data_sorted.apply(classify_priority, axis=1)

# Análise Estatística
X = data_sorted[["Severity", "CVSS"]]
y = data_sorted["risk_score"]

# removendo os não númericos
valid_rows = ~X.isna().any(axis=1) & ~y.isna()
X = X[valid_rows]
y = y[valid_rows]

# verificando se X e Y não estão vazios
if X.empty or y.empty:
    raise ValueError('Os dados para X ou y estão vazios. Verifique os dados de entrada')

# Verificando se há valores infinitos
if X.isin([float('inf')]).any().any() or X.isin([float('-inf')]).any().any() or y.isin([float('inf')]).any() or y.isin([float('-inf')]).any():
    raise ValueError('X ou y contém valores infinitos.')

# Adicionando constante
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

# Resumo do modelo
print(model.summary())

# Gráficos
plt.figure(figsize=(14, 8))
ax = sns.barplot(x="priority", y="risk_score", data=data_sorted, estimator='mean')
plt.title("Distribuição de Vulnerabilidades por Prioridade")
plt.xlabel("Prioridade")
plt.ylabel("Pontuação de Risco")

# Adicionando rótulos nas barras
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{height:.2f}', (p.get_x() + p.get_width() / 2., height), 
                ha='center', va='center', 
                xytext=(0, 5), textcoords='offset points')

# Adicionando identificação das vulnerabilidades na imagem
for i, row in enumerate(data_sorted.iterrows()):
    index, row = row
    ax.annotate(row["NVT Name"], 
                (i, row["risk_score"]),
                ha='center', va='center', 
                xytext=(0, -25), textcoords='offset points', 
                fontsize=8, rotation=0)  # Ajuste a fonte e a rotação conforme necessário


# Verificando se  diretorio 'Data' existe e criando se necessario
if not os.path.exists('data'):
    os.makedirs("data")

# Salvando imagem
plt.savefig("data/priority_distribution.png")
plt.show()

# Salvar Dados Processados
data_sorted.to_csv("data/results_analysis.csv", index=False)