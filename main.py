import json
from pprint import pprint

def Load_JSON_File_In_List(json_file, type_file):
    list_news = []
    if type_file == 1:
        with open(json_file) as news_file:
            new_file_data = json.load(news_file)
            for item_list in new_file_data['rss']['channel']['items']:
                temp_list_news = item_list['description'].split()
                # list_news += temp_list_news
                # pprint(item_list['description'])

                return temp_list_news

    else:
        pass



word_count = {}

list_news = Load_JSON_File_In_List('newsfr.json', 1)

for word_item in list_news:
    if len(word_item) >= 6:
        if word_item in word_count.keys():
            word_count[word_item] += 1
        else:
            word_count[word_item] = 1

temp_list = sorted(word_count, key=word_count.get, reverse=True)
for i in range(10):
    print(temp_list[i], word_count[temp_list[i]])


