import pandas as pd
import glob
import os

caminho_arquivos = r'C:\Users\YOUR USER\Desktop\ArquivosParajuntar\\'

arquivos = glob.glob(caminho_arquivos + "*.xlsx")

print(f"Arquivos encontrados: {arquivos}")

dataframes = []

diretorio_saida = r'C:\Users\YOUR USER\Desktop\resultadoUnificado'

if not os.path.exists(diretorio_saida):
    os.makedirs(diretorio_saida)

if arquivos:
    for arquivo in arquivos:
        df = pd.read_excel(arquivo)
        dataframes.append(df)

    df_unificado = pd.concat(dataframes, ignore_index=True)

    caminho_arquivo_unificado = os.path.join(diretorio_saida, 'arquivo_unificado.xlsx')
    df_unificado.to_excel(caminho_arquivo_unificado, index=False)

    print(f"Arquivo unificado salvo com sucesso em: {caminho_arquivo_unificado}")
else:
    print("Nenhum arquivo .xlsx encontrado no diretório.")
