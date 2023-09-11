data = []

def get_id(data: list) -> int:
    if len(data) == 0:
        return 1
    else:
        max_id = max([i['id'] for i in data])
        return max_id + 1


def get_category() -> str:
    while get_category != str:
        category = input(
            "Название категорий:\n\tВеб-разработка\n\tРазработка мобильных приложений\n\tРазработка игр\nЧто выберите: "
            ).capitalize()
        
        if category in "Веб-разработка Разработка мобильных приложений Разработка игр":
            return category
        else:
            print("У нас нет других категорий!")
            continue
    

def get_subcategory() -> str:
    while get_subcategory != str:
        subcategory = input(
            "Название подкатегорий:\n\tPython\n\tJavaScript\n\tJava\nЧто выберите: "
            ).title()
        
        if subcategory in "Python Javascript Java":
            return subcategory
        else:
            print("У нас нет других подкатегорий!")
            continue
    

def get_header() -> str:
    while get_header != str:
        header = input("Заголовок курса (максимум 60 символов): ")

        if len(header) < 60:
            return header
        else:
            print("Максимум 60 символов в заголовке!")
            continue


def get_description() -> str:
    while get_description != str:
        description = input("Описание к курсу (минимум 10 слов): ")

        if description.count(" ") > 8:
            return description
        else:
            print("Нужно написать минимум 10 предложений!")
            continue
    

def get_level() -> str:
    while get_level != str:
        level = input(
            "Уровни подготовки:\n\tНачальный\n\tСредний\n\tПрофессиональный\nЧто выберите: "
        ).title()

        if level in "Начальный Средний Профессиональный":
            return level
        else:
            print("Других уровней подготовки у нас нет!")
            continue
    

def get_currency() -> str:
    while get_currency != str:
        currency = input("Валюты курса:\n\tUSD\n\tKGS\n\tEUR\nЧто выберите: ").upper()

        if currency in "USD KGS EUR":
            return currency
        else:
            print("Другую валюту не принимаем!")
            continue


def get_sum(currency: str) -> int:
    while get_sum != True:
        summ = 0
        try:
            summ = int(input("Сумма курса: "))
            if currency == "USD":
                return summ * 88
            elif currency == "EUR":
                return summ * 95
            elif currency == "KGS":
                return summ
            else:
                continue
        except (ValueError, ZeroDivisionError):
            print("Пишите только цифры и ноль писать нельзя!")


def post_product():
    new_data = {'id': get_id(data)}
    new_data['category'] = get_category()
    new_data["subcategory"] = get_subcategory()
    new_data["header"] = get_header()
    new_data["description"] = get_description()
    new_data["level"] = get_level()
    currenc = get_currency()
    samm = get_sum(currenc)
    new_data["price"] = {
        'currency': currenc,
        "summ": samm
    }
    data.append(new_data)
    return "201 CREATED", new_data


def patch_product(id):
    product = [i for i in data if i['id'] == id]
    index = data.index(product[0])
    
    if product:
        data.remove(product[0])
        product[0]['id'] = get_id(data)
        product[0]['category'] = get_category()
        product[0]["subcategory"] = get_subcategory()
        product[0]["header"] = get_header()
        product[0]["description"] = get_description()
        product[0]["level"] = get_level()
        currenc = get_currency()
        samm = get_sum(currenc)
        product[0]["price"] = {
            'currency': currenc,
            "summ": samm
        }
        data.insert(index, product[0])
        return 'Успешно изменен', product[0]
    else:
        return 'Вы ввели неправильные данные'    
    

def get_all():
    print(data)


def get_one(id):
    product = [i for i in data if i["id"] == id]
    if product:
        return product
    return "Нет такой записи"


def del_product(id):
    product = [i for i in data if i['id'] == id]
    if product:
        index = data.index(product[0])
        data.pop(index)
        return 'Удален'
    else:
        return 'Вы ввели неправильные данные'
    

def main():
    print("Дарова, тебе доступны следущие функции:\n\tGET\n\tPOST\n\tDETAIL\n\tPUT\n\tDELETE")
    method = input("Выберите одну из функций: ").upper()
    if method == 'GET':
        get_all()

    elif method == 'DETAIL':
        id = int(input("Введите ID: "))
        print(get_one(id))

    elif method == 'POST':
        print(post_product())

    elif method == 'PUT':
        id = int(input("Введите ID: "))
        print(patch_product(id))
    
    elif method == 'DELETE':
        id = int(input("Введите ID: "))
        print(del_product(id))

    else:
        print("Других функций нет!")

while True:
    try:
        main()
        check = input("Хотите продолжить? Y/N: ").upper()

        if check in "Y":
            continue
        else:
            break
    except IndexError:
        print("Записи с такой ID нету!")