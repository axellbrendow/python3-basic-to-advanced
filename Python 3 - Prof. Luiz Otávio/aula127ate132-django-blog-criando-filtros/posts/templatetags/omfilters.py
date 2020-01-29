from django import template

register = template.Library()


@register.filter(name='plural_comentarios')
def plural_comentarios(num_comentarios):
    try:
        num_comentarios = int(num_comentarios)

        if num_comentarios == 0:
            plural = 'Nenhum comentário'

        elif num_comentarios == 1:
            plural = '1 comentário'

        else:
            plural = f'{num_comentarios} comentários'

    except:
        plural = f'{num_comentarios} comentário(s)'

    return plural
