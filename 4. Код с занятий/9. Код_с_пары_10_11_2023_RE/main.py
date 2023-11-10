# ПРОЧИТАТЬ -> Подробно о регулярных выражениях: https://clck.ru/H3xmB
# Отладка https://regex101.com/

# Основы:
# . - любой одиночный символ
# [] - любой из них, диапазоны
# $ - конец строки
# ^ - начало строки
# \ - экранирование
# \d - любую цифру [0-9]
# \D - все что угодно, кроме цифр
# \s - пробелы
# \S - все кроме пробелов
# \w - буква
# \W - все кроме букв
# \b - граница слова
# \B - не граница
#
# Квантификация
# n{4} - искать n подряд 4 раза
# n{4,6} - искать n от 4 до 6
# * от нуля и выше {0,}
# + от 1 и выше {1,}
# ? - нуль или 1 раз {0,1}

import re # Модуль re используется для работы с регулярными выражениями. Он позволяет производить поиск и сопоставление
            # шаблона в строке.

import csv # Модуль csv предоставляет функционал для работы с CSV-файлами.
           # Он позволяет читать и записывать данные в формате CSV.

import ssl # Модуль ssl используется для работы с SSL-сертификатами. Он позволяет создавать безопасные соединения
            # с серверами, проверять подлинность сертификатов и обрабатывать ошибки SSL.

import urllib.request # Модуль urllib.request предоставляет функциональность для открытия URL-адресов и обработки
                     # HTTP-запросов. Он позволяет получать содержимое веб-страниц, отправлять данные на серверы и
                     # выполнять другие действия, связанные с HTTP.

ssl._create_default_https_context = ssl._create_unverified_context # используется для отключения проверки
                                                                    # SSL-сертификатов. Это может быть полезно в случае,
                                                                    #  если сервер использует самоподписанный сертификат
                                                                    #  или сертификат с недействительным именем (МИИГАиК HotFix).

# 1. Парсинг email-адресов

f = open("adr.txt", encoding="UTF8").read()

email_pattern = r"[\w\-.]+@[\w-]+\.+[\w.-]+\b"
match = re.findall(email_pattern, f)

print(f'Список email-адресов: {match}')

# 2. Парсинг имен, адресов и номеров телефона с html-странички
adres_request = urllib.request.urlopen("https://www.summet.com/dmsi/html/codesamples/addresses.html").read().decode() # Данная строка кода выполняет следующие действия:

# 1. Использует модуль `urllib.request`, который позволяет отправлять HTTP-запросы к указанному URL-адресу и получать ответы от сервера.

# 2. С помощью функции `urlopen(<URL>)` создается объект запроса, который открывает соединение с указанным URL-адресом "https://www.summet.com/dmsi/html/codesamples/addresses.html".

# 3. Метод `.read()` вызывается на объекте запроса, чтобы получить данные ответа от сервера. Этот метод считывает содержимое ответа в виде последовательности байтов.

# 4. Метод `.decode()` вызывается в конце строки, чтобы преобразовать последовательность байтов в строку с использованием стандартной кодировки UTF-8.

# Наконец, результат выполнения данной строки кода присваивается переменной `adres_request`, которая будет содержать содержимое HTML-страницы по указанному URL-адресу в виде строки.

# Таким образом, данная строка кода запрашивает HTML-страницу по указанному URL-адресу и сохраняет ее содержимое в переменной `adres_request`.
# print(adres_request) # Вывод html-странички


pattern = r"(?:<li>)(?P<names>[^<]+)(?:<[^>]+>)(?P<street>[^<]+)(?:<[^>]+>)(?P<state>[^<]+)(?:<[^>]+>)(?P<numbers>[^<]+)(?:<[^>]+>)"

# Данное выражение представляет собой регулярное выражение (regular expression) на языке программирования Python. Оно используется для поиска и извлечения информации из HTML-кода по заданному шаблону.
#
# Подробное описание выражения:
#
# - r"(?:<li>) - это незахватывающая группа, которая ищет подстроку "<li>". В данном случае она используется для поиска начала информации о человеке (имени, улице, штате и номерах).
# - (?P<names>[^<]+) - это захватывающая группа, которая называется "names" и ищет последовательность символов, не включающих "<". Эта группа предполагается для захвата имен.
# - (?:<[^>]+>) - это еще одна незахватывающая группа, которая ищет произвольный тег HTML, заключенный в "<>".
# - (?P<street>[^<]+) - это захватывающая группа, которая называется "street" и ищет последовательность символов, не включающих "<". Эта группа предполагается для захвата названия улицы.
# - (?:<[^>]+>) - еще одна незахватывающая группа для поиска тега HTML.
# - (?P<state>[^<]+) - захватывающая группа "state", ищет последовательность символов, не включающих "<". Предполагается, что эта группа захватывает информацию о штате.
# - (?:<[^>]+>) - незахватывающая группа для поиска тега HTML.
# - (?P<numbers>[^<]+) - захватывающая группа "numbers", ищет последовательность символов, не включающих "<". Предполагается, что эта группа захватывает информацию о номерах.
# - (?:<[^>]+>) - финальная незахватывающая группа для поиска закрывающего тега HTML.

match = re.findall(pattern, adres_request)
print(match)


# Запись полученных данных в csv-файл
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'City', 'State', 'Phone'])

    for i in match:
        writer.writerow(i)

# 4. Вывод информации по именованным группам:

matches = re.finditer(pattern, adres_request)

for match in matches:
    print("Name:", match.group('names'))
    print("Street:", match.group('street'))
    print("State:", match.group('state'))
    print("Numbers:", match.group('numbers'))
    print("\n")

if not re.search(pattern, adres_request):
    print("No match found.")

# В этой версии кода `re.finditer` используется для поиска итераций,
# затем цикл `for` выводит содержимое каждой группы для каждого вхождения.
# Если соответствие не найдено, выводится сообщение "No match found.".


# Подробный комментарий по коду в целом:
#
# 1. Парсинг email-адресов:
#    - Считывает содержимое файла "adr.txt" с помощью функции `open` и метода `read()`, используя кодировку UTF8.
#    - Создает шаблон для поиска email-адресов с помощью регулярного выражения `r"[\w\-.]+@[\w-]+\.+[\w.-]+\b"`.
#    - Ищет все совпадения шаблона в считанном тексте с помощью функции `findall` из модуля `re`.
#    - Выводит список найденных email-адресов.
#
# 2. Парсинг имен, адресов и номеров телефона с html-странички:
#    - Открывает и считывает содержимое html-страницы "https://www.summet.com/dmsi/html/codesamples/addresses.html" с помощью модуля `urllib.request`.
#    - Создает шаблон для поиска имен, адресов и номеров телефона с помощью регулярного выражения `r"(?:<li>)(?P<names>[^<]+)(?:<[^>]+>)(?P<street>[^<]+)(?:<[^>]+>)(?P<state>[^<]+)(?:<[^>]+>)(?P<numbers>[^<]+)(?:<[^>]+>)"`.
#    - Ищет все совпадения шаблона в считанном html-коде с помощью функции `findall` из модуля `re`.
#    - Выводит список найденных совпадений.
#
# 3. Запись полученных данных в csv-файл:
#    - Открывает файл "data.csv" с помощью функции `open` в режиме записи.
#    - Создает объект writer с помощью функции `csv.writer` для записи данных в csv-файл.
#    - Записывает заголовок таблицы (Name, City, State, Phone) с помощью метода `writerow`.
#    - Записывает каждое совпадение из предыдущего шага в csv-файл с помощью цикла и метода `writerow`.
#
# 4. Вывод информации по именованным группам:
#    - Используется тот же шаблон для поиска, что и в предыдущем пункте.
#    - Ищет все совпадения шаблона в считанном html-коде с помощью функции `finditer` из модуля `re`.
#    - Выводит каждое совпадение в консоль, печатая информацию из именованных групп (Name, Street, State, Numbers).
#
# 5. Проверка наличия совпадений:
#    - Используется тот же шаблон для поиска, что и в предыдущих пунктах.
#    - Проверяет наличие совпадений в считанном html-коде с помощью функции `search` из модуля `re`.
#    - Если совпадений не найдено, выводит сообщение "No match found".
#
# Общий результат работы кода заключается в нахождении и выводе email-адресов из текстового файла и информации об именах,
# адресах и номерах телефона с html-страницы. После этого результаты записываются в csv-файл, а информация о совпадениях
# выводится в консоль.
#
# Разбор начального регулярного выражения, предназначенного для поиска и проверки соответствия адресов электронной почты.
#
# Разберем подробно каждую часть выражения:
# 1. `email_pattern = r"[\w\-.]+@[\w-]+\.+[\w.-]+\b"`
#    1. `email_pattern` - это имя переменной, которая хранит регулярное выражение.
#    2. `r` перед строкой указывает, что это строка сырого текста (raw string), что означает, что экранирующие символы не будут интерпретироваться.
#    3. `"[\w\-.]+@[\w-]+\.+[\w.-]+\b"` - это само регулярное выражение.
#
# 2. `"[\w\-.]+@[\w-]+\.+[\w.-]+\b"`
#    1. `[\w\-.]+` - это набор символов, которые включают в себя любую алфавитно-цифровую букву, знак подчеркивания или
#                    дефис, повторяющийся один или более раз.
#    2. `@` - обозначает символ `@`, который должен быть присутствовать в адресе электронной почты.
#    3. `[\w-]+` - это алфавитно-цифровая буква или знак подчеркивания, повторяющиеся один или более раз.
#    4. `\.` - символ `\` экранирует символ `.`, чтобы он интерпретировался как точка, а не как специальный символ
#              регулярного выражения. Точка должна быть присутствует в адресе электронной почты.
#    5. `[\w.-]+` - это набор символов, который включает в себя любой алфавитно-цифровой символ, знак подчеркивания,
#                   дефис или точку, повторяющийся один или более раз.
#    6. `\b` - обозначает границу слова (word boundary), что означает, что после этой границы следует конец слова.
#
#   Таким образом, данное регулярное выражение будет находить адреса электронной почты, состоящие из набора
# алфавитно-цифровых символов, знака подчеркивания, дефиса или точки, за которыми следует символ `@`,
# после которого идет набор алфавитно-цифровых символов и знака подчеркивания, за которыми следует точка, и, наконец,
# после точки идет набор символов, который может включать в себя любой алфавитно-цифровой символ, знак подчеркивания,
# дефис или точку, завершающийся границей слова.
