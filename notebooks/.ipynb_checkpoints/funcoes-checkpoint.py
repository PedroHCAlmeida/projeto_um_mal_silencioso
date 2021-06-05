import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import ticker

def limpa_casos_h(dados, hep):
    
    dados = dados.drop(columns=['Total', '1999-2006'])
    dados = dados.drop(index=1)
    dados = pd.melt(dados, var_name='Ano', value_name=hep)
    dados = dados.drop(0)
    dados[hep] = dados[hep].astype('int64')
    dados['Ano'] = dados['Ano'].astype('int64') 
    return dados

@ticker.FuncFormatter
def thousand_formatter(x, pos):
    '''
    Formata os dados para cada Mil e mostra duas casas decimais depois da vírgula
    '''
    return "%.2f Mil" % (x/1E3)

@ticker.FuncFormatter
def million_formatter(x, pos):
    '''
    Formata os dados para cada Milhão e mostra duas casas decimais depois da vírgula
    '''
    return "%.2f Mi" % (x/1E6)


def plota_rel(dados: pd.DataFrame, x: str, y:str, hue=None, title='', subtitle=None, xlabel=None, ylabel=None, dict_hue_palette=None,formatter_x=None,
             formatter_y=None, file_name=None, xlim=None, ylim=None, hue_legend=None, style='darkgrid', show=True, ax=None, 
             color_title='black', color_sub='dimgray', color_ticks='dimgray', legend=False, legend_title='', title_loc='left', kind='line', **kwargs):
    '''
    
    Função que plota um gráfico de relacionamento entre duas variáveis, podendo ser um 'lineplot' do seaborn ou um 'scatterplot' do seaborn
    
    Parâmentros:
    
            dados : DataFrame do pandas onde estão os dados, tipo=pd.DataFrame 
            x : coluna associada ao eixo x, tipo : str
            y : coluna associada ao eixo y, tipo : str
            hue : variável associada à tonalidade, tipo : str, padrão : None
            dict_hue_palette : dicionário com o nome da variável e a cor a ser plotada, tipo : dict, padrão : None
            hue_legend : legenda do grupo que distingue a tonalidade no parâmetro hue, tipo: list, padrão : None
            legend : operador lógico para mostrar a legenda ou não, tipo : boolean(True or False), padrão : False
            legend_title : título da legenda, obs: apenas se legend = True, tipo : str, padrão : ''
            title : título do gráfico, tipo : str, padrão : ''
            title_loc : local do título, tipo : str, padrão : 'left'
            color_title : cor do título, tipo : str, padrão : 'black'
            subtitle : subtítulo do gráfico, tipo : str, padrão : None
            color_sub  : cor do subtítulo, tipo : str, padrão : 'dimgray'
            color_ticks : cor dos eixos, tipo : str, padrão : 'dimgray'
            xlabel : legenda do eixo x, tipo : str, padrão : None 
            xlim : lista com dois valores numéricos indicando o limite do eixo x, tipo : list, padrão : None
            formatter_x : formatador dos números do eixo x, tipo : matplotlib.ticker, padrão : None
            ylabel : legenda do eixo y, tipo : str, padrão : None
            ylim : lista com dois valores numéricos indicando o limite do eixo y, tipo : list, padrão : None
            formatter_y : formatador dos números do eixo y, tipo : matplotlib.ticker, padrão : None
            file_name : nome do arquivo correspondente ao gráfico se quiser ser salvo, obs:por padrão não salva, tipo : str, padrão : None  
            style : stilo do grid do gráfico do seaborn, tipo:str, padrão : 'darkgrid' 
            show : operador lógico para mostrar o gráfico ou não, tipo : boolean(True or False), padrão : True
            ax : eixo se já existir, tipo : matplotlib.pyplot, padrão : Mone
            kind : tipo do gráfico se é um gráfico de linha ou um scatterplot, tipo : str('line' ou 'scatter'), padrão : 'line'
            **kwargs : argumentos adicionais para incrementar a chamada do gráfico 'lineplot' ou 'scatterplot' do seaborn
    '''
    
    #Mudando o estilo de fundo
    sns.set_style(style)
    
    #Verificando se foi passado algum eixo 
    if ax == None:
        #Criando figura e eixos
        fig, ax = plt.subplots(figsize=(16,8)) 
    
    #Verificando o tipo do gráfico e plotando
    if kind=='line':
        sns.lineplot(data=dados, x=x, y=y, hue=hue, palette=dict_hue_palette, ax=ax, **kwargs)
    elif kind=='scatter':
        sns.scatterplot(data=dados, x=x, y=y, hue=hue, palette=dict_hue_palette, ax=ax, **kwargs)

    #Plotando os títulos, mudando o tamanho e cores das fontes
    plt.sca(ax)
    plt.title(title + '\n', fontsize=25, loc=title_loc, color=color_title)
    plt.text(0,1.03, subtitle, color=color_sub, transform=ax.transAxes, fontsize=15)
    plt.xlabel(xlabel, color=color_ticks, fontsize=15)
    plt.ylabel(ylabel, color=color_ticks, fontsize=15)
    plt.yticks(fontsize=15, color=color_ticks)

        
    #Verificando se o eixo x se refere ao ano para mostrar todos os anos 
    if dados[x].dtypes == 'int64':
        plt.xticks(range(int(min(dados[x])),int(max(dados[x]+1))), range(int(min(dados[x])),int(max(dados[x]+1))), fontsize=15, color=color_ticks)
    else:
        plt.xticks(fontsize=12, color=color_ticks)
    
    #Verificando se a legenda foi passada como TRUE
    if legend == True:
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles=handles[1:], labels=hue_legend, title=legend_title, bbox_to_anchor=(1, 1), fontsize=12, title_fontsize=15)
    else:
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
    if show:
        #Mostrando o gráfico
        plt.show()

def limpa_casos_regiao(dados_hep_A, dados_hep_B, dados_hep_C, regiao):
    
    hep_A = limpa_casos_h(dados_hep_A, 'A')
    hep_B = limpa_casos_h(dados_hep_B, 'B')
    hep_C = limpa_casos_h(dados_hep_C, 'C')
    dados = pd.merge(hep_A, pd.merge(hep_B, hep_C))
    dados = pd.melt(dados,'Ano', var_name='Classe_viral', value_name=regiao)
    
    return dados

def limpa_obitos_reg(dados, regiao):
    
    dados = dados.drop(columns=['Total','2000-2006'])
    dados['Óbitos'] = dados.replace(r'Hepatite\s', '', regex=True)
    dados = dados.rename(columns={'Óbitos':'Classe_viral'})
    dados = dados.drop(index=3)
    dados = pd.melt(dados, 'Classe_viral', var_name='Ano', value_name=regiao)
    
    return dados