# <h1>Predição de vendas das lojas Rossmann</h1>
![rossmann](https://user-images.githubusercontent.com/101605197/201553326-c854f2e0-8c6d-481e-b6c6-9545dfb79f0f.jpg)
</br>
<h2>O Problema de Negócio</h2>
Durante uma reunião mensal, foi decidido que cada loja Rossmann iria receber um orçamento para a reforma das lojas, contudo, esse orçmento seria diretamente proporcional a receita das vendas ao longo dos últimos meses.</br>
Por isso, pediu a equipe de Ciência de Dados uma predição das vendas para as próximas seis semanas a partir da data de entrega do projeto.
</br>
<h2>Dados</h2>
Os dados foram extraídos, tranformados, passaram pela Exploratory Data Analysis (EDA) e por fim, foram usados para o treinamento do modelo.
</br>
<i>Fonte</i>: https://www.kaggle.com/competitions/rossmann-store-sales/data
<h3>Descrição dos Atributos</h3>

|  Atributos | Descrição  |
|---|---|
| Store | Id da loja  |
| DayOfWeek  | Dia da semana em que a venda foi realizada |
| Date  | Data da venda  |
| Sales  |  Receita das vendas |
|  Customers |  Quantidade de clientes que frequentaram a loja no dia |
|  Open |  Se a loja estava aberta ou não: 0 = fechado, 1 = aberto |
|  Promo | Indica se a loja estava em alguma promoção no dia das vendas  |
|  StateHoliday |  Feriado Estadual |
|  SchoolHoliday |  Feriado Escolar |
| StoreType  |  Diferencia 4 tipos de loja: a, b, c, d  |
|  Assortment |  Tamanho do sortimento da loja |
|  CompetitionDistance |  Distância do competidor mais próximo |
| CompetitionOpenSinceMonth  |  Mês aproximado em que o competidor mais próximo abriu |
| CompetitionOpenSinceYear  | Ano em que o competidor mais próximo abriu  |
| Promo2  | Se a loja está participando de uma promoção consecutiva  |
| Promo2SinceWeek  | Descreve a semana no calendário em que a Promo2 iniciou  |
| Promo2SinceYear  |  Descreve o ano em que a Promo2 iniciou |
|  PromoInterval |  Descreve o intervalo de quando a Promo2 estava ativa |

</br>
<h2>Premissas do Negócio</h2>
<ul>
  <li>A quantidade de clientes não foi considerada para o treinamento do modelo, já que para predizer a quantidade de cliente seria necessário um outro projeto</li>
  <li>Lojas sem o valor de CompetitionDistance ('NA'), são lojas sem competidores próximos, por isso, foi considerado uma distância de 200.000 metros para o treinamento do modelo nesses casos.</li>
</ul>
</br>
<h2>Insights durante a EDA</h2>

Durante a EDA do projeto, alguns insights foram descobertos e podem trazer para o negócio.
</br>
<h3>Lojas com competidores mais próximos vendem mais</h3>

![competition_distance](https://user-images.githubusercontent.com/101605197/201554941-32084751-f7c8-42f3-9417-de3bf144d565.png)
</br>


<h3>Lojas com competidores a mais tempo vendem menos</h3>

![competition_time](https://user-images.githubusercontent.com/101605197/201555007-fe662a74-8cb1-4b6e-8871-edf8e59783ca.png)
</br>


<h3>Lojas abertas durante o feriado de Natal vendem menos do que em outros feriados</h3>

![holidays](https://user-images.githubusercontent.com/101605197/201555069-4fd4a653-fb75-4ce2-9f97-72bf7f35dd97.png)
</br>


<h3>Lojas com promoções ativas por mais tempo tendem a vender menos</h3>

![tendencia](https://user-images.githubusercontent.com/101605197/201555202-b4641f04-0c39-4663-9210-741d54c0ba96.png)
</br>


<h2>Modelo</h2>
Para a criação do modelo foram considerados os atributos da fase de EDA, que permitiu um conhecimento maior do negócio. Para isso, os atributos foram tratados para que o modelo pudesse ter a melhor performance.
As variáveis que não possuiam Distribuição Normal foram tratadas para que pudessem ter esse tipo de distribuição, além das variáveis cíclicas (como os meses do ano) serem tratadas para um melhor entendimento do algortimo.
</br>
Após essa etapa, foi utilizado o algoritmo Boruta para complementar a seleção das variáveis.
</br>

Foram testados 5 modelos que apresentaram as performances abaixo:


| Model Name  | MAE  | MAPE  | RMSE  |
|---|---|---|---|
| Average Model	  |  1354,80 | 0,46  | 1835.14  |
| Linear Regression  |  1867.09 |  0.29 | 2671.05  |
|  Lasso | 1891.70  | 0,29  |  2744.45 |
|  Random Forest Regressor | 677.55  | 0,10  | 1007,86  |
|  XGBoost Regressor | 868,95  | 0,13  | 1238,55  |
</br>

Os modelos tiveram os resultados abaixo após a etapa de Cross Validation:


| Model Name  | MAE  | MAPE  | RMSE  |
|---|---|---|---|
| Linear Regression  | 2081,73 +/- 295,63  | 0,3 +/- 0,02  |  2952,52 +/- 468,37 |
|  Lasso | 2116,38 +/- 341,5 | 0,29 +/- 0,01  | 3057,75 +/- 504,26  |
|  Random Forest Regressor |  837,68 +/- 218,12 | 0,12 +/- 0,02  | 1256,33 +/- 318,28 |
| XGBoost Regressor |  7047,94 +/- 587,59 | 0,95 +/- 0,0  | 7714,01 +/- 688,65 |
</br>

É posível notar que a Random Forest possui a melhor performance, contudo, foi escolhido o XGBoost, pois este modelo utiliza menos espaço em memória e apresenta uma performance próxima a Random Forest.
Após a escolha, foi realizada a etapa de Hyperparameter Finetune e o modelo passou a apresentar as performances abaixo:
</br>

| Model Name  | MAE  | MAPE  | RMSE  |
|---|---|---|---|
| XGBoost Regressor | 760,19 | 0,11 | 1088,54 |

</br>
<h2>Resultados e Entrega</h2>
Após o treinamento e avaliação da performance do modelo, o deploy foi feito no Heroku Cloud e permitiu que o CFO pudesse visualizar a predição das lojas.
Para facilitar essa visualização, foi criado um bot para que o CFO possa consultar a qualquer momento a predição da loja.
</br>

<i>Link para o bot</i>: https://t.me/rossman_prediction_bot
</br>

Para ter acesso a predição da loja, deve-se colocar "/" antes do número da loja. Exemplo: "/30".
