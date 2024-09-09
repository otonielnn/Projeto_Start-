# Analise de vulnerabilidade e prioridade de riscos em ambiente de TI
## Objetivo
- Coletar dados de vulnerabilidades a partir de varreduras de segurança.
- Analisar esses dados para avaliar a gravidade e a probabilidade das vulnerabilidades.
- Priorizar as vulnerabilidades com base em impacto potencial e risco associado.
- Gerar relatórios e dashboards para visualizar as vulnerabilidades e suas priorizações.

## Ferramentas
- [OpenVAS](https://greenbone.github.io/docs/latest/22.4/container/index.html)
- Python com as bibliotecas (Pandas, Statsmodels, Matplotlib, Seaborn)
- [Docker](https://www.docker.com/)

## Como executar?
- Instale as bibliotecas listasdas no requirements.txt com o commando:

    ```bash
    pip install -r requirements.txt
    ```

    ou

    ```bash
    pip install pandas statsmodels matplotlib seaborn
    ```

- Subindo container docker seguindo [documentação da comunidade do Greenbone](https://greenbone.github.io/docs/latest/22.4/container/index.html)

- Crie uma pasta chamada `data` ou rode o arquivo `analise_vunerabilidade.py` para criar a pasta.

- adicione o arquivo `.csv` gerado pelo GreenBone, renomeando para `openvas_scan_results.csv`