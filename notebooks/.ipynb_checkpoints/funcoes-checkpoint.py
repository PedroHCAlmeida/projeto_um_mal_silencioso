import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re
from functools import wraps

def limpa_casos_h(dados:pd.DataFrame, hep:str):
    
    '''
    Função que recebe um dataset com dados sobre casos relacionado à um tipo de hepatite e realiza algumas transformações:
        
        Retira as colunas que agrupam diversos anos, coluna 'Total' e coluna '1999-2006'
        Retira a segunda linha do dataframe que se refere à taxa de incidência e, primeiramente serão usados apenas os dados de casos totais para juntar os dados recentes e mais antigos
        Transforma a disposição da tabela, transformando as colunas em apenas uma coluna('Ano') atribuindo o vírus da hepatite(A,B,C) como nome da coluna de valores numéricos
        Retira a primeira linha que antes se referia ao nome da variável numérica('Casos')
        Transforma o tipo de dados da coluna 'Ano' em inteiro e a coluna com os dados numéricos para float(podem haver valores nulos) para depois facilitar a manipulação e evitar problemas  
        
    Parâmetros:
        
        dados : DataFrame onde estão os dados mais recentes dos casos de hepatite, tipo : pd.DataFrame
        hep : o vírus da hepatite que o DataFrame se refere, tipo : str
    
    Retorno:
        
        dados : DataFrame com todas as limpezas realizadas, tipo : pd.DataFrame
    '''
    
    dados = dados.drop(columns=['Total', '1999-2006'])
    dados = dados.drop(index=1)
    dados = pd.melt(dados, var_name='Ano', value_name=hep)
    dados = dados.drop(0)
    dados[hep] = dados[hep].astype('float64')
    dados['Ano'] = dados['Ano'].astype('int64') 
    return dados

        
def limpa_casos_regiao(dados_hep_A:pd.DataFrame, dados_hep_B:pd.DataFrame, dados_hep_C:pd.DataFrame, regiao:str):
    
    '''
    Função que recebe os DataFrames relacionados à cada virus de uma região especifíca e realiza algumas transformações:
        
        Chama a função 'limpa_casos_h' para cada tipo de vírus para realizar uma limpeza em cada DataFrame 
        Junta os dados de todas os vírus(A, B, C)
        Transforma as colunas relacionadas ao vírus em apenas uma coluna('virus') e atribui a 'regiao' como nome da coluna com os valore numéricos
    
    Parâmetros:
    
        dados_hep_A : DataFrame onde estão os dados mais recentes dos casos de hepatite A, tipo : pd.DataFrame
        dados_hep_B : DataFrame onde estão os dados mais recentes dos casos de hepatite B, tipo : pd.DataFrame
        dados_hep_C : DataFrame onde estão os dados mais recentes dos casos de hepatite C, tipo : pd.DataFrame
        regiao : Nome da região que o DataFrame se refere, tipo : pd.DataFrame
        
    Retorno :
        
        dados : retorna um Dataframe com os dados sobre casos de hepatite A, B e C de uma região específica, tipo : pd.DataFrame
    '''
    
    hep_A = limpa_casos_h(dados_hep_A, 'A')
    hep_B = limpa_casos_h(dados_hep_B, 'B')
    hep_C = limpa_casos_h(dados_hep_C, 'C')
    dados = pd.merge(hep_A, pd.merge(hep_B, hep_C))
    dados = pd.melt(dados,'Ano', var_name='virus', value_name=regiao)
    
    return dados

def limpa_obitos(dados, nome_valores):
    
    '''
    Função que recebe o DataFrame relacionado aos óbitos de cada virus e realiza algumas transformações:
        
        Retira as colunas que agrupam diversos anos, coluna 'Total' e coluna '2000-2006' 
        Retira a palavra 'Hepatite' antes do vírus(A,B,C)
        Renomeia a coluna Óbitos por virus
        Retira os dados relacionados à Hepatite D
        Transforma as colunas relacionadas aos Anos em apenas uma coluna('Ano') e atribui o 'nome_valores' como nome da coluna com os valores numéricos
        Trasnforma o tipo de dados da coluna 'Ano' em inteiro e a coluna com os dados numéricos para float(podem haver valores nulos) a fim de evitar problemas e facilitar a manipulação
    
    Parâmetros:
    
        dados : DataFrame onde estão os dados mais recentes dos óbitos de hepatite, tipo : pd.DataFrame
        hep : o nome que a coluna com os valores numéricos vai se referir, podendo ser a região do DataFrame ou a palavra 'Obitos' por exemplo, tipo : str
        
    Retorno :
        
        dados : retorna um Dataframe com os dados sobre os óbitos de hepatite A, B e C, tipo : pd.DataFrame
    '''
    
    dados = dados.drop(columns=['Total','2000-2006'])
    dados['Óbitos'] = dados.replace(r'Hepatite\s', '', regex=True)
    dados = dados.rename(columns={'Óbitos':'virus'})
    dados = dados.drop(index=3)
    dados = pd.melt(dados, 'virus', var_name='Ano', value_name=nome_valores)
    dados['Ano'] = dados['Ano'].astype('int64')
    dados[nome_valores] = dados[nome_valores].astype('float64')
    
    return dados

def limpa_vacinas_dados(dados:pd.DataFrame, nome_valores:str):
    
    '''
    Função que recebe o DataFrame relacionado às vacinas aplicadas de hepatite podendo ser sobre cobertura de vacinação ou doses aplicadas realiza algumas transformações:
        
        Retira as linhas que se referem aos dados totais e aos dados mais recentes de 2021 pois o ano ainda não acabou
        Retira a palavra 'Hepatite' antes do nome das colunas
        Renomeia a coluna Óbitos por virus
        Transforma as colunas relacionadas à virus em apenas uma coluna('virus') e atribui o 'nome_valores' como nome da coluna com os valores numéricos
    
    Parâmetros:
    
        dados : DataFrame onde estão os dados sobre vacinação da hepatite, tipo : pd.DataFrame
        nome_valores : o nome que a coluna com os valores numéricos vai se referir, podendo ser 'Cobertura' ou 'Doses_aplicadas' por exemplo, tipo : str
        
    Retorno :
        
        dados : retorna um Dataframe com os dados sobre vacinação da hepatite, tipo : pd.DataFrame
    '''
    
    dados = dados[(dados['Ano'] != 'Total') & (dados['Ano'] != '2021')]
    dados = dados.rename(columns=lambda x:re.sub(r'.*Hepatite A.*','A',x))
    dados = dados.rename(columns=lambda x:re.sub(r'.*Hepatite B.*','B',x))
    dados = pd.melt(dados, 'Ano', var_name='virus', value_name=nome_valores)
    return dados

def plota_grafico(dados: pd.DataFrame, x: str, y:str, hue=None, title='', subtitle=None, xlabel=None, ylabel=None, dict_hue_palette=None, palette_sns=None,formatter_x=None,
                  formatter_y=None,file_name=None, xlim=None, ylim=None, hue_legend=None,style='darkgrid', show=True, ax=None, color_xlabel='dimgray', color_ylabel='dimgray',
                 color_title='black', color_sub='dimgray', color_xticks='dimgray', color_yticks='dimgray', legend=False, legend_title='', title_loc='left', kind='line', intervalo_ano=None, **kwargs):
    '''
    
    Função que plota um gráfico entre duas variáveis, podendo ser um 'lineplot' do seaborn, 'scatterplot' ou um 'barplot' do seaborn
    
    Parâmetros:
    
            dados : DataFrame do pandas onde estão os dados, tipo=pd.DataFrame 
            x : coluna associada ao eixo x, tipo : str
            y : coluna associada ao eixo y, tipo : str
            hue : variável associada à tonalidade, tipo : str, padrão : None
            dict_hue_palette : dicionário com o nome da variável e a cor a ser plotada, tipo : dict, padrão : None
            palette_sns : palheta do seaborn com as cores a serem plotadas, tipo : sns.color_palette, padrão : None
            hue_legend : legenda do grupo que distingue a tonalidade no parâmetro hue, tipo: list, padrão : None
            legend : operador lógico para mostrar a legenda ou não, tipo : boolean(True or False), padrão : False
            legend_title : título da legenda, obs: apenas se legend = True, tipo : str, padrão : ''
            title : título do gráfico, tipo : str, padrão : ''
            title_loc : local do título, tipo : str, padrão : 'left'
            color_title : cor do título, tipo : str, padrão : 'black'
            subtitle : subtítulo do gráfico, tipo : str, padrão : None
            color_sub  : cor do subtítulo, tipo : str, padrão : 'dimgray'
            color_xticks : cor do eixo x, tipo : str, padrão : 'dimgray'
            color_yticks : cor do eixo y, tipo : str, padrão : 'dimgray'
            xlabel : legenda do eixo x, tipo : str, padrão : None 
            color_xlabel : cor da legenda do eixo x, tipo : str, padrão : 'dimgray'
            xlim : lista com dois valores numéricos indicando o limite do eixo x, tipo : list, padrão : None
            formatter_x : formatador dos números do eixo x, tipo : matplotlib.ticker, padrão : None
            ylabel : legenda do eixo y, tipo : str, padrão : None
            color_ylabel : cor da legenda do eixo y, tipo : str, padrão : 'dimgray'
            ylim : lista com dois valores numéricos indicando o limite do eixo y, tipo : list, padrão : None
            formatter_y : formatador dos números do eixo y, tipo : matplotlib.ticker, padrão : None
            file_name : nome do arquivo correspondente ao gráfico se quiser ser salvo, obs:por padrão não salva, tipo : str, padrão : None  
            style : stilo do grid do gráfico do seaborn, tipo:str, padrão : 'darkgrid' 
            show : operador lógico para mostrar o gráfico ou não, tipo : boolean(True or False), padrão : True
            ax : eixo se já existir, tipo : matplotlib.pyplot, padrão : Mone
            kind : tipo do gráfico se é um gráfico de linha ou um scatterplot, tipo : str('line' ,'scatter' ou 'bar'), padrão : 'line'
            intervalo_ano : intervalo dos anos mostrado no eixo, obs:a coluna relacionada ao ano precisa estar no eixo x e ser do tipo int, tipo : int, padrão : None 
            **kwargs : argumentos adicionais para incrementar a chamada do gráfico 'lineplot' ou 'scatterplot' do seaborn
    '''
    
    #Verificando se foi passado algum eixo 
    if ax == None:
        #Mudando o estilo de fundo
        sns.set_style(style)
        #Criando figura e eixos
        fig, ax = plt.subplots(figsize=(16,8)) 
    
    if palette_sns != None:
        palette = palette_sns
        
    elif dict_hue_palette != None:
        palette = dict_hue_palette
    
    else:
        palette=None
    
    #Verificando o tipo do gráfico e plotando
    if kind=='line':
        sns.lineplot(data=dados, x=x, y=y, hue=hue, palette=palette, ax=ax, **kwargs)
    elif kind=='scatter':
        sns.scatterplot(data=dados, x=x, y=y, hue=hue, palette=palette, ax=ax, **kwargs)
    elif kind == 'bar':
        sns.barplot(data=dados, x=x, y=y, hue=hue, palette=palette, ax=ax, **kwargs)

    #Plotando os títulos, mudando o tamanho e cores das fontes
    plt.sca(ax)
    plt.title(title + '\n', fontsize=25, loc=title_loc, color=color_title)
    plt.text(0,1.03, subtitle, color=color_sub, transform=ax.transAxes, fontsize=15)
    plt.xlabel(xlabel, color=color_xlabel, fontsize=15)
    plt.ylabel(ylabel, color=color_ylabel, fontsize=15)
    plt.yticks(fontsize=15, color=color_yticks)

        
    #Verificando se o eixo x se refere ao ano para mostrar todos os anos 
    if intervalo_ano != None and dados[x].dtypes == 'int64':
        plt.xticks(range(int(min(dados[x])),int(max(dados[x]+1)), intervalo_ano), range(int(min(dados[x])),int(max(dados[x]+1)), intervalo_ano), fontsize=15, color=color_xticks)
    else:
        plt.xticks(fontsize=12, color=color_xticks)
    
    #Verificando se a legenda foi passada como TRUE
    if legend == True:
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles=handles[1:], labels=hue_legend, title=legend_title, bbox_to_anchor=(1, 1), fontsize=12, title_fontsize=15)
    elif hue != None:
        plt.legend('')
    
    #Verificando os formatadores dos eixos
    if formatter_y != None:
        ax.yaxis.set_major_formatter(formatter_y)
    
    if formatter_x != None:
        ax.xaxis.set_major_formatter(formatter_x)
 
    #Criando a legenda no final da linha passada
    if hue != None and dict_hue_palette != None and kind=='line': 
        
        if hue_legend == None:
            hue_legend = dict_hue_palette.keys()

        for line, name in zip(ax.lines, hue_legend):
            y = line.get_ydata()[-1]
            plt.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(), 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=15, va="center")
    #Verificando se foi passado e o limite do eixo x
    if xlim != None:
        #Passando o limite do eixo x
        plt.xlim(xlim[0], xlim[1])
        
    #Verificando se foi passado e o limite do eixo y    
    if ylim != None: 
        #Passando o limite do eixo x
        plt.ylim(ylim[0], ylim[1])
    
    #Verificando se foi passado nome do arquivo
    if file_name != None:
        #Salvando o gráfico na pasta de imagens
        plt.savefig(f'../images/{file_name}')

    #Verificando se foi passado para mostrar o gráfico
    if show == True:
        #Mostrando o gráfico
        plt.show()


def thousand_formatter(x, pos):
    '''
    Função responsável por formatar um eixo do 'matplotlib' dividindo os valores por Mil, mostrando duas casas decimais depois da vírgula e colocando a palavra 'Mil' após os valores indicando a grandeza,
    precisa ser passada como parâmetro para a função FuncFormatter do matplotlib.ticker
    '''
   
    return "%.2f Mil" % (x/1E3)

def million_formatter(x, pos):
    '''
    Função responsável por formatar um eixo do 'matplotlib' dividindo os valores por Milhão, mostrando duas casas decimais depois da vírgula e colocando a palavra 'Mi' após os valores indicando a grandeza,
    precisa ser passada como parâmetro para a função FuncFormatter do matplotlib.ticker
    '''
    return "%.2f Mi" % (x/1E6)