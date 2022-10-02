from django.utils.text import slugify

def translite(text):
    '''
        Функция для транслита с русского на английский.
    '''
    symbol = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
              'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
              'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shc', 'ы': 'i', 'э': 'e',
              'ю': 'yu', 'я': 'ya', ' ': '_'}
    return slugify(''.join(symbol.get(w, w) for w in text.lower()))