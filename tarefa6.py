import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_lixo_eletronico = pd.read_csv("E15/desafio6_lixo_eletronico.csv")


"""
Iniciando Exploração dos dados do dataframe
"""
print(f'\nExtrutura do dataframe (linhas/colunas) \n{df_lixo_eletronico.shape}')
print('\n')

# exibindo dataframe
print(df_lixo_eletronico.sample(10))



"""
Descrição do tipo de dados registrados em cada coluna
"""
print('Informações gerais:')
print(df_lixo_eletronico.info())
print('\n\n')



"""
Exibindo estatisticas descritivas sobre o df 
"""
print(f'Estatisticas: \n{df_lixo_eletronico.describe().round(2)}')
print('\n\n')



"""
Confirmando valores nulos dentro do dataframe
"""
print(f'Valores nulos dentro do DataFrame: \n{df_lixo_eletronico.isnull().sum()}')
print('\n\n')

"""
O total de dados ausentes é 75 nas colunas:
Tipo_Eletronico = 15;
Origem = 15;
Destino_final = 15;
Peso_kg = 15;
Custo_Reciclagem_R$ = 15;
"""




"""
Verificando se há linhas compoletamentes duplicadas no dataframe
o df_duplicado foi criado com a finalidade única de verificação de duplicatas
"""
df_duplicado = df_lixo_eletronico 
print("Linhas duplicadas no dataframe")
if df_duplicado.duplicated().any():
    print(f"\nExistem {df_duplicado.duplicated().any().sum()} linhas totalmente duplicadas no arquivo.\n")
else:
    print("\nNão há linhas totalmente duplicadas no arquivo.\n")

"""
Confirmando valores duplicados na coluna ID
"""
print('Verificando valores duplicados na coluna ID ')
if df_lixo_eletronico['ID_Registro'].duplicated().any():
    print('Há valores duplicados: \n')
    print(df_lixo_eletronico['ID_Registro'].duplicated().sum())



"""
Explorando o dataframe podemos avaliar que em algumas colunas há inconsistências nos dados
como nas colunas: Tipo_Eletronico; Origem; Destino_Fianl; Peso_Kg; 
"""


"""
Verificando padronização de dados nas colunas 
"""

print(f"Verificando quantidade de descartes: \n{df_lixo_eletronico['Tipo_Eletronico'].value_counts()}\n")

print(f"Coluna Origem: \n{df_lixo_eletronico['Origem'].value_counts()}\n")

print(f"Coluna Destino Final: \n{df_lixo_eletronico['Destino_Final'].value_counts()}\n")

print(f"Coluna Nivel Tóxico: \n{df_lixo_eletronico['Nivel_Toxico'].value_counts()}\n")

print(f"Coluna Municiopio: \n{df_lixo_eletronico['Municipio'].value_counts()}\n")

print(f"Coluna Educação Ambiental: \n{df_lixo_eletronico['Educacao_Ambiental'].value_counts()}\n")




"""
Iniciando padronização de colunas 
Método .str.title() utilizado para deixar todas as células da coluna iniciando cada palavra com Máiusc.
Método .str.capitalize() para deixar a letra incial das células com letra Máiusc.
"""
df_lixo_eletronico_tratado = df_lixo_eletronico.copy()

"""
Tratando células duplicadas da coluna ID_Registro 
"""
df_lixo_eletronico_tratado['ID_Registro'] = range(1, len(df_lixo_eletronico) + 1)


# Padronização da coluna 'Tipo_Eletronico'
df_lixo_eletronico_tratado['Tipo_Eletronico'] = df_lixo_eletronico_tratado['Tipo_Eletronico'].str.capitalize()

# Na coluna Origem o dado da célula estava digitado de forma incorreta "urbano" será corrigido para "Urbana"
print(f"\n\nAntes da correção: \n{df_lixo_eletronico_tratado.iloc[20]}")

df_lixo_eletronico_tratado.loc[df_lixo_eletronico_tratado['ID_Registro'] == 21, 'Origem'] = 'Urbana'

print(f"\n\nDepois da correção: \n{df_lixo_eletronico_tratado.iloc[20]}\n\n")

# Padronização da coluna 'Destino_Final' 
df_lixo_eletronico_tratado['Destino_Final'] = df_lixo_eletronico_tratado['Destino_Final'].str.title()

# Padronização da coluna 'Nivel_Toxico'
df_lixo_eletronico_tratado['Nivel_Toxico'] = df_lixo_eletronico_tratado['Nivel_Toxico'].str.capitalize()

# Padronização da coluna 'Municipio'
df_lixo_eletronico_tratado['Municipio'] = df_lixo_eletronico_tratado['Municipio'].str.capitalize()

#Padronização da coluna 'Educacao_Ambiental'
df_lixo_eletronico_tratado['Educacao_Ambiental'] = df_lixo_eletronico_tratado['Educacao_Ambiental'].str.capitalize()



"""
Iniciando o tratamento de valores ausentes subtituindo pela média de cada aparelho (Peso, Custo de reciclagem) 
"""
# Coluna 'Tipo_Eletronico' - valores ausentes substituidos por 'Desconhecido'
df_lixo_eletronico_tratado['Tipo_Eletronico'] = df_lixo_eletronico_tratado['Tipo_Eletronico'].fillna('Desconhecido')

# Coluna 'Origem' - valores ausentes substituidos por 'Desconhecida'
df_lixo_eletronico_tratado['Origem'] = df_lixo_eletronico_tratado['Origem'].fillna('Desconhecida')

# Coluna 'Destino_Final' - valores ausentes substituidos por 'Desconhecido'
df_lixo_eletronico_tratado['Destino_Final'] = df_lixo_eletronico_tratado['Destino_Final'].fillna('Desconhecido')

# Agrupa a coluna 'Tipo_Eletronico' e agrega pela média do peso de cada tipo eletrônico
# Coluna 'Peso_kg' - valores ausentes substituidos pela média de cada Tipo_Eletronico 
medias_peso_por_tipo = df_lixo_eletronico_tratado.groupby('Tipo_Eletronico')['Peso_kg'].mean()
df_lixo_eletronico_tratado['Peso_kg'] = df_lixo_eletronico_tratado['Peso_kg'].fillna(df_lixo_eletronico_tratado['Tipo_Eletronico'].map(medias_peso_por_tipo))

# Agrupa a coluna 'Tipo_Eletronico' e agrega pela média do custo de reciclagem de cada tipo eletrônico
# Coluna 'Custo_Reciclagem_R$' - valores ausentes substituidos pela média de cada Tipo_Eletronico
medias_custo_reciclagem_por_tipo = df_lixo_eletronico_tratado.groupby('Tipo_Eletronico')['Custo_Reciclagem_R$'].mean()
df_lixo_eletronico_tratado['Custo_Reciclagem_R$'] = df_lixo_eletronico_tratado['Custo_Reciclagem_R$'].fillna(df_lixo_eletronico_tratado['Tipo_Eletronico'].map(medias_custo_reciclagem_por_tipo))

# Confirmando tratamento de valores ausentes
print(f"Colunas do Datraframe após os tratamentos: \n{df_lixo_eletronico_tratado.isnull().sum()}\n\n")



"""
Iniciando análise de distribuição e frequência
"""

"""
Exibição dos Gráficos e tabelas de frequência
"""
# Frequência de cada tipo de eletrônico
freq_tipo_eletronico = df_lixo_eletronico_tratado['Tipo_Eletronico'].value_counts()
percent_tipo_eletronico = df_lixo_eletronico_tratado['Tipo_Eletronico'].value_counts(normalize=True) * 100 # calculando a porcentagem dos tipos eletronicos
"""
Criando um dataframe para exibir a tabela de frequência de cada tipo de eletrônico e sua porcentagem
"""
tabela_tipo_eletronico = pd.DataFrame({
    'Contagem': freq_tipo_eletronico,
    'Percentual (%)': percent_tipo_eletronico.round(2)
})
print("\nTabela de frequência por Tipo de Eletrônico:")
print(tabela_tipo_eletronico)

# Gráfico de barras para Tipo de Eletrônico
plt.figure(figsize=(12, 6))
sns.barplot(x=freq_tipo_eletronico.index, y=freq_tipo_eletronico.values, hue=freq_tipo_eletronico,palette='viridis', legend=False)
plt.title('Frequência de Descarte por Tipo de Eletrônico')
plt.xlabel('Tipo de Eletrônico')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("freq_tipo_eletronico.png") 



# Frequência de cada origem 
freq_origem = df_lixo_eletronico_tratado['Origem'].value_counts()
percent_origem = df_lixo_eletronico_tratado['Origem'].value_counts(normalize=True) * 100 # Calculando a porcentagem das origens
"""
Criando um dataframe para exibir a tabela de origem dos eletrônicos e sua porcentagem
"""
tabela_origem = pd.DataFrame({
    'Contagem': freq_origem,
    'Percentual (%)': percent_origem.round(2)
})
print("\nTabela de frequência por Origem:")
print(tabela_origem)


# Gráfico de barras para Origem
plt.figure(figsize=(10, 5))
sns.barplot(x=freq_origem.index, y=freq_origem.values, hue=freq_origem, palette='plasma', legend=False)
plt.title('Frequência de Descarte por Origem')
plt.xlabel('Origem')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("freq_origem.png") 




"""
Iniciando ánalise temporal de descarte
"""

# Alterando o tipo de dado da coluna 'Data_Descarte' para datetime
df_lixo_eletronico_tratado['Data_Descarte'] = pd.to_datetime(df_lixo_eletronico_tratado['Data_Descarte'])
# Criação das colunas 'Mes_Descarte' e 'Ano_Descarte'
df_lixo_eletronico_tratado['Ano_Descarte'] = df_lixo_eletronico_tratado['Data_Descarte'].dt.year
df_lixo_eletronico_tratado['Mes_Descarte'] = df_lixo_eletronico_tratado['Data_Descarte'].dt.month

"""
Preparando os dados para cada gráfico 
"""
# Dados gráfico geral anual
descartes_anuais = df_lixo_eletronico_tratado['Ano_Descarte'].value_counts().sort_index()

# Dados gráfico de sazonalidade mensal
nomes_meses_pt = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
descartes_mensais_agg = df_lixo_eletronico_tratado['Mes_Descarte'].value_counts().sort_index()
descartes_mensais_agg.index = nomes_meses_pt

# Dados ráfico de 2025
df_2025 = df_lixo_eletronico_tratado[df_lixo_eletronico_tratado['Ano_Descarte'] == 2025]
descartes_2025_mensal = df_2025['Mes_Descarte'].value_counts()
volume_mensal_2025 = pd.Series(0, index=range(1, 13))
volume_mensal_2025.update(descartes_2025_mensal)
volume_mensal_2025.index = nomes_meses_pt


"""
Criação das figuras para o subplot
"""
plt.style.use('seaborn-v0_8-whitegrid')
fig = plt.figure(figsize=(18, 12))
# fig.suptitle('Dashboard de Análise Temporal do Descarte Eletrônico', fontsize=22, weight='bold')


# Definindo o layout dos subplots
"""
Um grid de 2x2: O primeiro gráfico ocupará a linha superior inteira
Os outros dois ocuparão a segunda linha, em colunas separadas
"""
ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=2)   # Gráfico anual
ax2 = plt.subplot2grid((2, 2), (1, 0))              # Gráfico Gráfico de Sazonalidade
ax3 = plt.subplot2grid((2, 2), (1, 1))              # Gráfico de 2025

# Plotando no primeiro subplot (ax1): Tendência Anual
sns.lineplot(x=descartes_anuais.index, y=descartes_anuais.values, marker='o', ax=ax1, color='darkblue')
ax1.set_title('Gráfico Geral: Tendência Anual de Descarte', fontsize=16, weight='bold', pad=15)
ax1.set_xlabel('Ano', fontsize=12)
ax1.set_ylabel('Total de Descartes', fontsize=12)
ax1.xaxis.set_major_locator(plt.MaxNLocator(integer=True)) # Garante que os valores do eixo Y sejam inteiros

# Plotando no segundo subplot (ax2): Sazonalidade Mensal
sns.lineplot(x=descartes_mensais_agg.index, y=descartes_mensais_agg.values, marker='s', linestyle='--', ax=ax2, color='green', sort=False)
ax2.set_title('Sazonalidade (Todos os Anos)', fontsize=16, weight='bold', pad=15)
ax2.set_xlabel('Mês', fontsize=12)
ax2.set_ylabel('Total Acumulado', fontsize=12)

# Plotando no terceiro subplot (ax3): Descarte em 2025
sns.lineplot(x=volume_mensal_2025.index, y=volume_mensal_2025.values, marker='D', linestyle=':', ax=ax3, color='purple', sort=False)
ax3.set_title('Volume Mensal de Descartes em 2025', fontsize=16, weight='bold', pad=15)
ax3.set_xlabel('Mês', fontsize=12)
ax3.set_ylabel('Total de Descartes', fontsize=12)
ax3.yaxis.set_major_locator(plt.MaxNLocator(integer=True))


# Ajustando o layout para evitar sobreposição
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("dashboard_temporal.png")




"""
Iniciando agregação por municipio
"""
# Definindo reciclagens formais e informais =
destino_formal = ['Reciclagem Formal', 'Cooperativa', 'Reuso', 'Doação']
destino_informal = ['Aterro Controlado', 'Lixão', 'Rio']

def classificando_destino(destino):
    if destino in destino_formal:
        return 'Formal'
    elif destino in destino_informal:
        return 'Informal'
    else:
        return 'Não Classificado'

df_lixo_eletronico_tratado['Tipo_Destino'] = df_lixo_eletronico_tratado['Destino_Final'].apply(classificando_destino)

# Agrupando por município e calculando métricas
agg_municipio = df_lixo_eletronico_tratado.groupby('Municipio').agg(
    Total_Residuos_Descartados_kg=('Peso_kg', 'sum'),
    Media_Peso_Eletronicos_kg=('Peso_kg', 'mean')
).round(2)

# Calculando proporçao de destinos formais e informais
destino_counts = df_lixo_eletronico_tratado.groupby(['Municipio', 'Tipo_Destino']).size().unstack(fill_value=0)
destino_total = destino_counts.sum(axis=1)

# Evitando divisões por zero
destino_counts['Proporcao_Formal_%'] = (destino_counts.get('Formal', 0) / destino_total * 100).round(2)
destino_counts['Proporcao_Informal_%'] = (destino_counts.get('Informal', 0) / destino_total * 100).round(2)


# Combinando agregações
tabela_municipios = pd.concat([agg_municipio, destino_counts], axis=1).fillna(0)

# Classificando tabela por total de residuos descartados
tabela_municipios_ordenada = tabela_municipios.sort_values(by='Total_Residuos_Descartados_kg', ascending=False)

# Exibindo tabela ordenada
print("Tabela Agregada por Município:")
print(tabela_municipios_ordenada)

"""
Visualizando 
"""
# Barra horizontal de descartes
plt.figure(figsize=(12, 10))
sns.barplot(x='Total_Residuos_Descartados_kg', y=tabela_municipios_ordenada.index, data=tabela_municipios_ordenada, palette='viridis', hue=tabela_municipios_ordenada.index, dodge=False)
# plt.title('Total de Resíduos Descartados por Município (kg)', fontsize=16, weight='bold')
plt.xlabel('Total de Resíduos (kg)', fontsize=12)
plt.ylabel('Município', fontsize=12)
plt.legend([],[], frameon=False)
plt.tight_layout()
plt.savefig("total_descarte_municipio.png")


# Tabela comparativa de descartes
tabela_comparativa_destinos = tabela_municipios_ordenada[['Formal', 'Informal']].sort_values(by='Formal', ascending=False)
print("\nTabela Comparativa de Destinos Formais e Informais:")
print(tabela_comparativa_destinos)

# Barra horizontal comparativa de descartes formais e informais de municipios
tabela_comparativa_destinos.plot(kind='barh', figsize=(14, 12), colormap='plasma', width=0.8)
# plt.title('Comparação de Descarte Formal vs. Informal por Município', fontsize=16, weight='bold')
plt.xlabel('Número de Descartes', fontsize=12)
plt.ylabel('Município', fontsize=12)
plt.legend(title='Tipo de Destino')
plt.gca().invert_yaxis() # Para acertar a ordem das tabelas
plt.tight_layout()
plt.savefig("comparativo_destino_municipio.png")




"""
Iniciando cruzaemento entre tipo de eletrônico e destino
"""
# Criando a tabela cruzada
tabela_cruzada = pd.crosstab(df_lixo_eletronico_tratado['Tipo_Eletronico'], df_lixo_eletronico_tratado['Destino_Final'])

# Exibindo tabela
print("Tabela Cruzada: Tipo de Eletrônico vs. Destino Final")
print(tabela_cruzada)

# Visualizando os resultados no mapa de calor
plt.figure(figsize=(16, 10))
heatmap = sns.heatmap(tabela_cruzada, annot=True, fmt="d", cmap="YlGnBu", linewidths=.5)
# plt.title('Heatmap: Relação entre Tipo de Eletrônico e Destino Final', fontsize=18, weight='bold')
plt.ylabel('Tipo de Eletrônico', fontsize=12)
plt.xlabel('Destino Final', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig("heatmap_tipo_destino.png")




"""
Iniciando análise de relação de educação ambiental e destino de risiduo
"""

# Definir as categorias de descarte formal e informal conforme as instruções do usuário
destinos_formais = ["Cooperativa", "Reciclagem formal", "Aterro controlado",]
destinos_informais = ["Lixão", "Rio" "Desconhecido"]

# Criar uma coluna para indicar se o descarte é formal ou informal
df_lixo_eletronico_tratado["Tipo_Descarte"] = df_lixo_eletronico_tratado["Destino_Final"].apply(
    lambda x: "Formal" if x in destinos_formais else ("Informal" if x in destinos_informais else "Outro")
)

# Agrupar os dados por município e pela existência de programas de educação ambiental
# e calcular a proporção de descarte formal e informal

df_agrupado = df_lixo_eletronico_tratado.groupby(["Municipio", "Educacao_Ambiental", "Tipo_Descarte"]).size().unstack(fill_value=0)

# Calcular as proporções
df_agrupado_proporcao = df_agrupado.apply(lambda x: x / x.sum(), axis=1)

# Resetar o índice para que "Municipio" e "Educacao_Ambiental" se tornem colunas
df_agrupado_proporcao = df_agrupado_proporcao.reset_index()

# Renomear colunas para clareza
df_agrupado_proporcao.columns.name = None

# Exibir os primeiros resultados do agrupamento
print("\nProporção de Descarte por Município e Educação Ambiental (Corrigido):")
print(df_agrupado_proporcao.head())

# --- Geração de gráficos separados para 'Sim' e 'Não' em 'Educacao_Ambiental' ---

# Paleta de cores personalizada
sns.set_palette(sns.color_palette('viridis', n_colors=2))

for educacao_status in ["Sim", "Não"]:
    df_filtered = df_agrupado_proporcao[df_agrupado_proporcao["Educacao_Ambiental"] == educacao_status]

    if not df_filtered.empty:
        plt.figure(figsize=(18, 10))

        # Melt o dataframe para facilitar a plotagem com seaborn
        df_plot = df_filtered.melt(id_vars=["Municipio", "Educacao_Ambiental"], var_name="Tipo_Descarte", value_name="Proporcao")

        # Filtrar apenas os tipos de descarte "Formal" e "Informal" para o gráfico
        df_plot_filtered = df_plot[df_plot["Tipo_Descarte"].isin(["Formal", "Informal"])]

        ax = sns.barplot(x="Municipio", y="Proporcao", hue="Tipo_Descarte", data=df_plot_filtered, dodge=False)

        # Adicionar valores numéricos nas barras, ajustando a posição para evitar sobreposição
        for container in ax.containers:
            for i, patch in enumerate(container.patches):
                value = patch.get_height()
                if value > 0.01:
                    ax.text(patch.get_x() + patch.get_width() / 2,
                            patch.get_y() + patch.get_height() / 2,
                            f'{value:.2f}',
                            ha='center', va='center',
                            color='black', fontsize=9)

        # plt.title(f"Proporção de Descarte Formal vs. Informal por Município (Educação Ambiental: {educacao_status})")
        plt.xlabel("Município")
        plt.ylabel("Proporção")
        plt.xticks(rotation=90)
        plt.legend(title="Tipo de Descarte")
        plt.tight_layout()
        plt.savefig("educacao_ambiental.png")




"""
Iniciando análise se correlação entre origem e tipo de eletrônicos
"""
from scipy.stats import chi2_contingency

# 1. Tabela de Contingência (Frequências Observadas)
contingency_table = pd.crosstab(df_lixo_eletronico_tratado['Origem'], df_lixo_eletronico_tratado['Tipo_Eletronico'])

# 2. Teste Qui-Quadrado
"""
Realiza o teste do Qui-Quadrado de independência em uma tabela de contingência (tabela com contagem de categorias).
chi2: valor da estatística do teste,
p_value: probabilidade de os dados ocorrerem ao acaso (quanto menor, mais significativa a relação),
dof: graus de liberdade (depende do tamanho da tabela),
expected_frequencies: valores esperados se as variáveis fossem independentes.
"""
chi2, p_value, dof, expected_frequencies = chi2_contingency(contingency_table)
"""
Transforma a matriz de frequências esperadas (vinda do chi2_contingency) em um DataFrame, para facilitar visualização e análise.
"""
expected_frequencies_df = pd.DataFrame(expected_frequencies, index=contingency_table.index, columns=contingency_table.columns)

# 3. Contribuição de cada célula para a estatística Qui-Quadrado
"""
Calcula quanto cada célula da tabela observada contribui para o valor total da estatística Qui-Quadrado.
Ajuda a entender quais categorias têm maior diferença entre o observado e o esperado.
"""
chi2_contribution = (contingency_table - expected_frequencies_df)**2 / expected_frequencies_df

# 4. Gráfico de Barras Empilhadas Proporcional
proportions = contingency_table.div(contingency_table.sum(axis=1), axis=0)

# Exibir tabelas no console para clareza
print("--- Tabela de Frequências Observadas ---")
print(contingency_table)
print("\n" + "="*50 + "\n")
print("--- Tabela de Frequências Esperadas ---")
print(expected_frequencies_df.round(2))
print("\n" + "="*50 + "\n")
print("--- Resultados do Teste Qui-Quadrado ---")
print(f"Estatística Qui-Quadrado: {chi2:.4f}")
print(f"P-valor: {p_value:.4f}")
print(f"Graus de Liberdade: {dof}")
print("\n" + "="*50 + "\n")

# 5. Criação das visualizações com subplots
fig, axes = plt.subplots(2, 2, figsize=(20, 16))
# fig.suptitle('Análise da Relação entre Origem e Tipo de Lixo Eletrônico', fontsize=20)

# Gráfico 1: Mapa de Calor das Frequências Observadas
sns.heatmap(contingency_table, annot=True, cmap='viridis', fmt='d', ax=axes[0, 0], linewidths=.5)
axes[0, 0].set_title('Mapa de Calor: Frequências Observadas', fontsize=14)
axes[0, 0].set_xlabel('Tipo de Eletrônico')
axes[0, 0].set_ylabel('Origem')

# Gráfico 2: Mapa de Calor da Contribuição para o Qui-Quadrado
sns.heatmap(chi2_contribution, annot=True, cmap='Reds', fmt='.2f', ax=axes[0, 1], linewidths=.5)
axes[0, 1].set_title('Mapa de Calor: Contribuição para o Qui-Quadrado', fontsize=14)
axes[0, 1].set_xlabel('Tipo de Eletrônico')
axes[0, 1].set_ylabel('Origem')

# Gráfico 3: Gráfico de Barras Empilhadas Proporcional
proportions.plot(kind='barh', stacked=True, ax=axes[1, 0], colormap='tab20')
axes[1, 0].set_title('Distribuição Proporcional dos Tipos de Eletrônicos por Origem', fontsize=14)
axes[1, 0].set_xlabel('Proporção')
axes[1, 0].set_ylabel('Origem')
axes[1, 0].legend(title='Tipo de Eletrônico', bbox_to_anchor=(1, 1), loc='upper left')

# Gráfico 4: Mapa de Calor das Frequências Esperadas
sns.heatmap(expected_frequencies_df, annot=True, cmap='coolwarm', fmt='.2f', ax=axes[1, 1], linewidths=.5)
axes[1, 1].set_title('Mapa de Calor: Frequências Esperadas (Hipótese de Independência)', fontsize=14)
axes[1, 1].set_xlabel('Tipo de Eletrônico')
axes[1, 1].set_ylabel('Origem')


plt.tight_layout(rect=[0, 0.03, 1, 0.96])
plt.savefig("dashboard_qui_quadrado.png")