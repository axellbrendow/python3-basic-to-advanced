import os
import fnmatch

# ../../__file__
# caminho_original = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
caminho_original = r'C:\Users\ADM-Leka\AppData\Local\Android\Sdk\emulator\resources\macroPreviews'
caminho_novo = r'C:\Users\ADM-Leka\Downloads\PB_Weapons\myvideos'

comando_ffmpeg = 'ffmpeg'  # Baixar ffmpeg caso não tenha
codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'

for caminho_diretorio, diretorios, arquivos in os.walk(caminho_original):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.mp4'):
            continue

        caminho_antigo_arquivo = os.path.join(caminho_diretorio, arquivo)
        caminho_novo_arquivo = os.path.join(caminho_novo, arquivo)
        caminho_arquivo_antigo_sem_ext, ext_arquivo = os.path.splitext(caminho_antigo_arquivo)
        caminho_legenda = caminho_arquivo_antigo_sem_ext + '.srt'  # Caso os vídeos tivessem legenda

        if os.path.isfile(caminho_legenda):
            input_legenda = f'-i "{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'  # c:s codec subtitle (legenda)

        else:
            input_legenda = ''
            map_legenda = ''

        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

        arquivo_saida = os.path.join(caminho_novo, f'{nome_arquivo}_NOVO{extensao_arquivo}')

        comando = f'{comando_ffmpeg} -i "{caminho_antigo_arquivo}" {input_legenda} ' \
            f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} ' \
            f'{debug} {map_legenda} "{arquivo_saida}"'

        os.system(comando)
