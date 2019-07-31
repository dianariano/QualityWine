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

    Para o modelo desenvolvido decidi usar matriz de confusão, e acurácia (Accuracy), são metodos que validam a porcentagem de precisão que o modelo faz nas predições sobre o conjunto de dados de teste (20% do dataset foi usado no conjunto de dados de teste). A acuracia não leva em consideração o que é positivo e o que é negativo. 
    
    do dataset  a proporção de casos que foram corretamente previstos, sejam eles verdadeiro positivo ou verdadeiro negativo. Em nosso exemplo: 65/100 = 0,65
    
     Modelos de classificação de aprendizado de máquina podem ser validados por técnicas como validação cruzada, onde os dados são divididos em conjuntos de teste e treinamento e medidas apropriadas como precisão são calculadas para ambos os conjuntos de dados e comparadas. Para além da precisão, sensibilidade (Avaliação Positiva Verdadeira) e especificidade (Avaliação Negativa Verdadeira) podem prover modos de modelos de avaliação. De forma similar, Avaliações Positivas Falsas assim como Avaliações Negativas Falsas poder ser computadas. Curvas Receptoras de Operação (CRO) em conjunto com a Área em baixo da CRO (AUC) oferecem ferramentas adicionais para a classificação de modelos de avaliação. Graus maiores de AUC estão associados a um modelo de melhor performance


5. **Quais evidências você possui de que seu modelo é suficientemente bom?**