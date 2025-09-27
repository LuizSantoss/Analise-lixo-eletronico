# ♻️ Dashboard de Análise de Lixo Eletrônico 📊  
<br>

## 🚀 Sobre o Projeto

Essa análise nasceu da necessidade de entender melhor como o lixo eletrônico é descartado. A partir de um conjunto de dados, mergulhamos em um processo completo de **limpeza, análise e visualização** para descobrir padrões e tendências ocultas.

O grande objetivo é transformar dados brutos em insights valiosos que possam:

  - Apoiar a tomada de decisões estratégicas em empresas de reciclagem.
  - Inspirar a criação de políticas públicas mais eficientes.
  - Otimizar campanhas de coleta e conscientização. 🌱


## 🛠️ Tecnologias Utilizadas


  * **Linguagem:** `Python`
  * **Análise e Manipulação de Dados:**
      * `Pandas`: Essencial para a estruturação, limpeza e manipulação dos dados.
      * `Scipy`: Utilizada para realizar análises estatísticas robustas, como o teste Qui-Quadrado.
  * **Visualização de Dados:**
      * `Matplotlib`: A base para a criação dos nossos gráficos.
      * `Seaborn`: Deixou nossos gráficos mais bonitos, informativos e estatisticamente ricos.

## 🗺️ Etapas da Jornada


#### 1\. Exploração Inicial 🧭

  * Começamos carregando os dados de um arquivo `.csv`.
  * Fizemos uma primeira "investigação" para entender a estrutura, os tipos de dados e as primeiras estatísticas.

#### 2\. Limpeza e Pré-processamento 🧹

  * **Valores Nulos:** Tratamos os dados ausentes de forma inteligente. Em vez de simplesmente apagar, preenchemos valores categóricos com "Desconhecido" e dados numéricos (como peso e custo) com a média correspondente ao seu tipo, mantendo a integridade dos dados.
  * **Inconsistências:** Padronizamos textos (letras maiúsculas e erros de digitação\! 👋) para garantir que tudo fosse contado corretamente.
  * **Duplicatas:** Para garantir que cada registro fosse único, geramos um novo ID para cada um.

#### 3\. Análise e Visualização 📈


  * **O que mais descartamos?**

      * **Gráfico:** Frequência de Descarte por Tipo de Eletrônico.
      * **💡 Insight:** Descobrimos quais categorias, como celulares e computadores, são as campeãs de descarte. Isso ajuda a direcionar a logística de reciclagem\!

  * **De onde vem tanto lixo?**

      * **Gráfico:** Frequência de Descarte por Origem.
      * **💡 Insight:** Mapeamos os principais geradores (residencial, comercial) para guiar a criação de parcerias e políticas focadas.

  * **Quando descartamos mais?**

      * **Gráfico:** Tendências Anuais e Sazonalidade Mensal.
      * **💡 Insight:** Identificamos picos de descarte ao longo do ano. Perfeito para saber a hora certa de lançar uma campanha de coleta\! 🗓️

  * **Quais cidades lideram o descarte?**

      * **Gráfico:** Total de Resíduos por Município (kg).
      * **💡 Insight:** Apontamos as áreas geográficas que mais precisam de atenção e infraestrutura, como novos ecopontos.

  * **O descarte está sendo feito da forma correta?**

      * **Gráfico:** Comparativo de Descarte Formal vs. Informal.
      * **💡 Insight:** Conseguimos medir a eficácia das políticas locais e identificar municípios que precisam de um "empurrãozinho" para combater o descarte inadequado.

  * **Para onde vai cada tipo de eletrônico?**

      * **Gráfico:** Mapa de Calor (Heatmap) da relação Tipo vs. Destino.
      * **💡 Insight:** Revelamos padrões interessantes, como itens de baixo valor indo para lixões. Uma informação poderosa para criar estratégias de coleta específicas por produto.

  * **Educação ambiental funciona mesmo? 🤔**

      * **Gráfico:** Descarte Formal vs. Informal em cidades com e sem programas de educação.
      * **💡 Insight:** Sim\! Comprovamos que a conscientização leva a um descarte muito mais correto e responsável.

  * **Existe alguma relação estatística entre a origem e o tipo de lixo?**

      * **Gráfico:** Análise de Associação com Qui-Quadrado.
      * **💡 Insight:** Confirmamos estatisticamente o que suspeitávamos: a origem (ex: residencial) tem uma forte conexão com o tipo de eletrônico descartado.

## ▶️ Como Executar o Projeto

1.  **Pré-requisitos:** Garanta que você tenha o Python e as bibliotecas (`pandas`, `matplotlib`, `seaborn`, `scipy`) instaladas.
    ```bash
    pip install pandas matplotlib seaborn scipy
    ```
2.  **Organize os arquivos:** Coloque o script `analise.py` e o arquivo de dados `lixo_eletronico.csv` na mesma pasta.
3.  **Execute o script:** Abra o terminal, navegue até a pasta e rode o comando:
    ```bash
    python analise.py
    ```
4.  **A mágica acontece:** O script irá processar tudo e salvará os gráficos como arquivos `.png` no mesmo diretório. ✨
5.  **Visualize o resultado:** Por fim, abra o arquivo `index.html` em seu navegador preferido para ver o dashboard completo com todos os gráficos e análises.

-----

