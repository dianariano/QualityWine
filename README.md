# QualityWine

Exercise to implement a wines quality classifier

DataSource link:  https://drive.google.com/file/d/1-oG5-kBt9xQ3Li4PEexpiA9_7RZhRM1f/view

## Instalation

Activate Python 3 environment and install requirements.

```bash
$ pip install --file requirements.txt
```

## Usage

```bash
python wineQuality.py 
```
or you can send the csv file to script
```bash
python wineQuality.py file_dir
```

#Questions

1. Como foi a definição da sua estratégia de modelagem?
   
   Para definição da estrategia de modelagem primeiro pensei no fluxo que o processo deveria ter, defini uma lista de passos principais a qual foi:

   - Leitura de arquivo de dados
   - Criação de dataset com os dados do arquivo
   - Analisis exploratoria de dados
   - Implementação de algoritmo de aprendizado
   - Avaliação de resultados predecidos pelo modelo

   No caminho de desenvolvimento trabalhei sobre funções desacopladas para uso em qualquer caso de data.
   No que tomou mais tempo e foi de maior importança foi a parte de analisis do dataset, dessa analisis dependia o dataset que seria usado no modelo e a escolha do modelo. Nesse passo fiz avaliação de tipos de dados que cada coluna tem, limpeza de dados invalidos, apresentação da descrição matematica dos valores numericos do dataset, remoção de dados duplicados e por ultimo visualização de distribuição dos valores de cada coluna. Atraves dessas informações consegui definir qual modelo de aprendizado seria melhor para o contexto de meus dados e reconhecimento de transformações e padronização dos valores para cada feature.

2. Como foi definida a função de custo utilizada?

    Pelo tipo de dados que o dataset tem como saida, dados discretos e finitos, e entradas independentes pensei no algoritmo de probabilidade de Naive Bayes, o algoritmo e rapido em relação a outros algoritmos de classificação e e usado principalmente quando o problema tem muitas classes. 

3. Qual foi o critério utilizado na seleção do modelo final?

4. Qual foi o critério utilizado para validação do modelo? Por que escolheu utilizar
este método?

5. Quais evidências você possui de que seu modelo é suficientemente bom?