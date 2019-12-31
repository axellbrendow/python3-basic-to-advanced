import PyPDF2
import os
import shutil

caminho = r'pdfs'
caminho_pdfs_separados = r'pdfs_separados'
caminho_pdf_mesclado = os.path.join(caminho, 'novo_arquivo.pdf')
novo_pdf = PyPDF2.PdfFileMerger()

print('Mesclando PDFs...')

for caminho_diretorio, diretorios, arquivos in os.walk(caminho):
    for arquivo in arquivos:
        caminho_completo = os.path.join(caminho_diretorio, arquivo)
        arquivo_pdf = open(caminho_completo, 'rb')
        novo_pdf.append(arquivo_pdf)
        arquivo_pdf.close()


os.remove(caminho_pdf_mesclado)

print('Escrevendo resultado...')

with open(caminho_pdf_mesclado, 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)

print('Separando as páginas...')

with open(caminho_pdf_mesclado, 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)
    num_pags = leitor.getNumPages()

    shutil.rmtree(caminho_pdfs_separados)
    os.mkdir(caminho_pdfs_separados)

    for num_pag in [0, 1]:  # num_pags:
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(num_pag)
        escritor.addPage(pagina_atual)

        with open(os.path.join(caminho_pdfs_separados, f'{num_pag}.pdf'), 'wb') as novo_pdf:
            escritor.write(novo_pdf)

print('Ok!')
