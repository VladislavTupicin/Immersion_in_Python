
# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

def most_frequent(text: str) -> list[str]:
    dict_counts = {}
    SHOW_LIMIT = 10
    new_sorted_dictionary = {}
    new_text = text.replace(',', ''). \
        replace('.', ''). \
        replace('!', ''). \
        replace('?', ''). \
        replace('"', ''). \
        lower(). \
        strip()
    words_list = new_text.split()
    for word in words_list:
        counter = words_list.count(word)
        dict_counts[word] = counter
    sorted_values = sorted(dict_counts.values())[::-1]
    for i in sorted_values:
        for k in dict_counts.keys():
            if dict_counts[k] == i:
                new_sorted_dictionary[k] = dict_counts[k]
    return list(new_sorted_dictionary.items())[0: SHOW_LIMIT]


text = 'Десятки бездомных семей выселят из лондонского отеля Travelodge из-за наплыва зрителей на концерт певицы Бейонсе, сообщает The Guardian. \
"Я страдаю от беспокойства, поэтому у меня была паническая атака, и я буквально просто плакала", – отреагировала одна из оставшихся без жилья женщин. \
По данным источника, с выселением столкнулись примерно 30 семей. Сейчас им ищут альтернативное жилье. ' \
       'Общественные деятели пообещали решить ситуацию с проживанием своих подопечных в ближайшее время. \
       В издании отмечают, что в отеле забронировано около 100 номеров местным городским советом для бездомных, некоторые из которых живут по шесть человек в одной комнате. \
       Бейонсе даст несколько концертов в Лондоне в рамках тура Renaissance. Она запланировала выступить в период с 29 мая по четвертое июня на стадионе Tottenham Hotspur.'

print(most_frequent(text))
