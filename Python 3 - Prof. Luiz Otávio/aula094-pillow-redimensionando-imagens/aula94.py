import os
from PIL import Image


def main(images_folder: str, new_width=300):
    if not os.path.isdir(images_folder):
        raise NotADirectoryError(f'O caminho {images_folder} precisa ser um diretório')

    else:
        converted_tag = '_converted'

        for caminho, diretorios, arquivos in os.walk(images_folder):
            for arquivo in arquivos:
                if converted_tag in arquivo:
                    os.remove(os.path.join(caminho, arquivo))

                elif arquivo.endswith('.png'):
                    caminho_completo = os.path.join(caminho, arquivo)
                    nome_novo_arquivo, extensao = os.path.splitext(arquivo)
                    novo_arquivo = f'{nome_novo_arquivo}{converted_tag}{extensao}'
                    caminho_novo_arquivo = os.path.join(caminho, novo_arquivo)

                    img_pillow = Image.open(caminho_completo)

                    # image_extra_info = img_pillow._getexif()  # Estas linhas só funcionam com .jpg
                    # print(image_extra_info.get(36867))  # O número 36867 é uma tag para obter a data da imagem

                    width, height = img_pillow.size
                    new_height = round(new_width * height / width)

                    print(f'Redimensionando a imagem {caminho_novo_arquivo}')
                    nova_imagem = img_pillow.resize((new_width, new_height), Image.LANCZOS)
                    nova_imagem.save(
                        caminho_novo_arquivo,
                        optimize=True,
                        quality=70,
                        # exif=img_pillow.info['exif']  # Só funciona com .jpg
                    )

                    nova_imagem.close()
                    img_pillow.close()


if __name__ == '__main__':
    images_folder = r'C:\Users\ADM-Leka\Downloads\PB_Weapons\StarWarsApp\src\assets'
    main(images_folder)
