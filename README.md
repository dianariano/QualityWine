# QualityWine

Exercise to implement a wines classifier

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

## Questions

1. **Como foi a definição da sua estratégia de modelagem?**
   
   Para definição da estrategia de modelagem primeiro pensei no fluxo que o processo deveria ter, defini uma lista de passos principais a qual foi:

   - Leitura de arquivo de dados
   - Criação de dataset com os dados do arquivo
   - Analisis exploratoria de dados
   - Implementação de algoritmo de aprendizado
   - Avaliação de resultados predecidos pelo modelo

   No caminho de desenvolvimento trabalhei sobre funções desacopladas para uso em qualquer caso de data.
   No que tomou mais tempo e foi de maior importança foi a parte de analisis do dataset, dessa analisis dependia o dataset que seria usado no modelo e a escolha do modelo. Nesse passo fiz avaliação de tipos de dados que cada coluna tem, limpeza de dados invalidos, apresentação da descrição matematica dos valores numericos do dataset, remoção de dados duplicados e por ultimo visualização de distribuição dos valores de cada coluna. Atraves dessas informações consegui definir qual modelo de aprendizado seria melhor para o contexto de meus dados e reconhecimento de transformações e padronização dos valores para cada feature.

2. **Como foi definida a função de custo utilizada?**

    Pelo tipo de dados que o dataset tem como saida, dados discretos e finitos, e entradas independentes pensei numa função de custo que estivese relacionada a aprendizagem supervisionada e de classificação. O problema da a resposta só e preciso descobrir o relacionamento da saida com os dados de entrada. Uma vez que eu conhecer este relacionamento e possivel responder qualquer outro problema do mesmo tipo.

3. **Qual foi o critério utilizado na seleção do modelo final?**

    Foram usadas varios criterios para seleção do modelo final, primeiro em relação quantidade de classes de saida do problema, segundo distribuição de valores de entrada e por ultimo tempo de processamento.

4. **Qual foi o critério utilizado para validação do modelo? Por que escolheu utilizar este método?**

    Para o modelo desenvolvido decidi usar matriz de confusão, acurácia (Accuracy) e precisão estes são metodos que validam a porcentagem de precisão que o modelo tem sobre as predições do conjunto de dados de teste (20% do dataset foi usado no conjunto de dados de teste). A acuracia não leva em consideração o que é positivo e o que é negativo. Respeito a precisão eu usei ela para calcular a media ponderada de precisão para cada classe do dataset.

5. **Quais evidências você possui de que seu modelo é suficientemente bom?**

    As metricas de avaliação usadas ajudam a ver o desempenho do meu modelo no contexto de dados do dataset. Usar a matrix de confusão e uma analise global de acuracia mostra quais clases meu modelo erra mais na classificação, mas pelo contexto e o entendimento do problema e abordagem desenvolvida acredito que o modelo e suficientemente bom para predições de dados do mesmo contexto do dataset de treino. O dataset tem uma distribuição desigual de classes mas poderiamos melhorar o modelo criando uma agrupação de classes e a clasificação ser em tres os quais poderiam classificar o vinho como ruim, medio ou bom, isso ajuda a ter uma distribuição melhor naas classes do dataset e melhorar os valores das metricas de avaliação obtidas.