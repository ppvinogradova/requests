import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text_file, result_file, from_lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """
    with open(text_file, 'r') as f:
        params = {
        'key': API_KEY,
        'text': f.read(),
        'lang': '{}-{}'.format(from_lang, to_lang),
        }
    
    response = requests.get(URL, params=params)
    json_ = response.json()
    result = ''.join(json_['text'])

    with open(result_file, 'w') as f:
        f.write(result)

if __name__ == '__main__':
    translate_it('FR.txt', 'resFR.txt', 'fr')
    translate_it('DE.txt', 'resDE.txt', 'de')
    translate_it('ES.txt', 'resES.txt', 'es')