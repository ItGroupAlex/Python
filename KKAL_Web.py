from collections import namedtuple
from jinja2 import Template, Environment, FileSystemLoader
from flask import Flask, render_template, redirect, url_for, request, session, app
import json, requests



app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)


# функция определения наличия в заданном элементе str символа из списка
def is_part_in_list(str_, words):
    for word in words:
        if word in str_:
            return True
    return False


Message = namedtuple('Message', 'text massa kkal')
messages = []
summa_l = []
s={"--выбирите продукт--":0}
l0 = {
'Молоко':60,
'Кефир':53,
'Творог':145,
'Яйцо куриное':157,
'Макароны':333,
'Йогурт':68,
'Мороженое пломбир':232,
'Сметана':206,
'Сыр твердый':344,
'Скумбрия':191,
'Щука':84,
'Кальмар':100,
'Икра красная':249,
'Батон':262,
'Крупа рисовая':333,
'Мука':329,
'Печенье':417,
'Хлеб':201,
'Сушки':339,
'Сухари':399,
'Фасоль':298,
'Арахис':552,
'Миндаль':609,
'Фундук':653,
'Кабачки':24,
'Капуста белокочанная':28,
'Капуста брокколи':34,
'Капуста пекинская':16,
'Картофель':77,
'Морковь':35,
'Огурец':14,
'Помидор':24,
'Редис':20,
'Свекла':42,
'Спаржа':21,
'Тыква':22,
'Чеснок':149,
'Шпинат':23,
'Абрикос':44,
'Авокадо':160,
'Ананас':52,
'Апельсин':43,
'Банан':96,
'Виноград':72,
'Гранат':72,
'Грейпфрут':35,
'Груша':47,
'Ежевика':34,
'Лимон':34,
'Киви':47,
'Мандарин':38,
'Персик':45,
'Яблоки':47,
'Курага':32,
'Чернослив':256,
'Финики':292,
'Грибы белые':34,
'Грибы шампиньоны':27,
'Сок апельсиновый':45,
'Сок виноградный':70,
'Сок морковный':56,
'Масло подсолнечное':899,
'Масло оливковое':898,
'Майонез':629,
'Колбаса сервелат':461,
'Колбаски охотничьи':463
}

l=s|l0

l_keys = []
for x in l:
    l_keys.append(x)


@app.route('/', methods=['GET'])
def dropdown():
    return render_template('main.html', products=l_keys)


@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html', messages=messages, summa = str(round(sum(summa_l), 2)), products=l_keys, mes_massa=mes_massa)


@app.route('/add_message', methods=['POST'])
def add_message():
    global mes_massa
    text = request.form['text']
    if text == "--выбирите продукт--":
        mes_massa = "вы не выбрали тип продукта"
        redirect(url_for('main'))
    else:
        massa = request.form['massa']
        while massa or massa == "":
            if massa == "":
                mes_massa = "вы не выбрали вес продукта"
            elif massa == "":
                mes_massa = "вы не выбрали вес"
            elif bool(massa.count("-")):
                mes_massa = "вы ввели вес меньше 0"
            elif massa == "0":
                mes_massa = "вы ввели вес равный 0"
            elif is_part_in_list(massa, [",","."]):
                mes_massa = "вы ввели не целое количество грамм"
            elif massa.isdigit() and int(massa) > 10000:
                mes_massa = "ведрами есть нельзя) повторите ввод"
            elif massa.isdigit() and int(massa) <= 10000:
                kkal = round(int(massa) / 100 * l0.get(text), 2)
                messages.append(Message(text, massa, kkal))
                summa_l.append(kkal)
                mes_massa = ""
            else:
                mes_massa = "вы ввели не число"
            break

    return redirect(url_for('main'))


@app.route('/del_messages', methods=['POST'])
def del_messages():
    global messages
    messages = []
    global summa_l
    summa_l = []
    return redirect(url_for('main'))

# JSON - Postman

@app.route('/list', methods=['GET'])
def list():
    dict_food = ['Справочник каллорийности продуктов доступных для подбора:', l0]
    return  dict_food


# перевод JSON в lowercase в отдельный JSON
lowercase_l = {key.lower(): val for key, val in l0.items()}
# обьединение json для отсутствия значимости регистра
l_full=l0|lowercase_l
# получение всех ключей l_full
l_full_keys = []
for x in l_full:
    l_full_keys.append(x)

@app.route('/search', methods=['GET'])
def search():
    food = request.args.get('food')
    # проверяем, передается ли параметр 'food' в URL-адресе
    if food and food != '':
        if food.replace(" ","").isalpha() == False:
            return 'Введите буквенное значение на русском языке!'
        elif l_full_keys.count(food) == False:
            return 'Данный тип продукта не найден в списке доступных к рассчету!'
        else:
            food_dict = {}
            food_kkal = l_full.get(food)
            food_dict[food] = food_kkal
            return food_dict
    elif food == '':
        return 'Не выбран тип продукта в параметре "food", введите значение на русском языке!'
    else:
        return 'Вы не ввели в запросе GET параметр типа продукта "food"!'

