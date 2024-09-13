from sqlalchemy import create_engine
import pandas as pd

# Configurações de conexão
username = 'root'
password = ''  
host = 'localhost'
database = 'projeto_vulnerabilidade'

# Crie a string de conexão
connection_string = f'mysql+pymysql://{username}:{password}@{host}/{database}'

# Crie o engine
engine = create_engine(connection_string)

# Carregar o CSV em um DataFrame
df = pd.read_csv('C:/Users/Lucas Luiz/Desktop/clean_greenbone_report.csv')

# Importar o DataFrame para a tabela MySQL
df.to_sql('vulnerabilities', con=engine, if_exists='replace', index=False)