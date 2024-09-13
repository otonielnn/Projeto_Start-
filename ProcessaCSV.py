import pandas as pd

# Caminho do arquivo CSV
csv_path = 'C:/Users/Lucas Luiz/Desktop/report-ce0b29f5-860b-4996-93a7-b1b85adfd53a.csv'

# Carregar o CSV
df = pd.read_csv(csv_path)

# Nomes das colunas atuais
print("Colunas atuais:", df.columns.tolist())

# Definir novos nomes de colunas (deve haver 26 nomes aqui, um para cada coluna)
df.columns = ['IP', 'Hostname', 'Port', 'Port_Protocol', 'CVSS', 'Severity', 'QoD', 'Solution_Type', 'NVT_Name', 'Summary', 'Specific_Result', 'NVT_OID', 'CVEs', 'Task_ID', 'Task_Name', 'Timestamp', 'Result_ID', 'Impact', 'Solution', 'Affected_Software/OS', 'Vulnerability_Insight', 'Vulnerability_Detection_Method', 'Product_Detection_Result', 'BIDs', 'CERTs', 'Other_References']

# Visualizar as primeiras linhas do DataFrame para confirmar
print(df.head())

# Salvar o DataFrame limpo em um novo arquivo CSV
df.to_csv('C:/Users/Lucas Luiz/Desktop/clean_greenbone_report.csv', index=False)