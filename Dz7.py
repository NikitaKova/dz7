def add_surname(d):

    with open ('telefon_book.bd', 'a') as file:
        file.write('surname: {}\n'
        
    .format (d))

def add_name(d):

    with open ('telefon_book.bd', 'a') as file:
        file.write('name: {}\n'
 .format (d))

def add_number (d):

from tabulate import tabulate1

prinr = ["Surname", "Name", "Phone_number", "Discription"]


def add_data(d):
    with open ('telefon_book.bd', 'a') as file:
        file.write('phone_number: {}\n'
 .format (d))
def add_description(d):
    
        file.write (tabulate(d, headers ='head', tablefmt="grid"·))


    with open ('telefon_book.bd', 'a') as file:
        file.write('discripion: {}\n'.format (d))

from cgitb import html
from user_dirictor import surname_view
from user_dirictor import name_view
from user_dirictor import phone_number_view
from user_dirictor import discription_view


def create():
    style= 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '·='.format(style, surname_view())
    html += '·='.format(style,name_view())
    html += '+='.format(style, phone_number_view())
    html += '+='.format(style, discription_view())
    html += ' </body>\n<html>'
    with open('index.html','w') as page:
        page.write(html)

<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Телефонный справочник</title>
</head>
<body>
<h1>Справочник</h1>
<p>Surname:Сидоров</p>
<p>name:Максим</p>
<p>Phone_Number:89536391245</p>
<p>Discription:Сослуживец</p>
<p>Data:(['Маринин', 'Сергей', '89638953612', 'Шиномонтаж'], ['Герасимов', 'Никита', '89454568973', 'личный'], ['Макарова', 'Марина', '89617539512', 'личный'], ['Сидоров', 'Александр', '89452364589', 'рабочий'], ['Иванова', 'Любовь', '88453564592', 'рабочий'])</p>
 
</body>
</html>

import re
from tokenize import Number


def get_surname():
    surname = input('фамилия:')
    return surname

def get_data():
    surname = input('Surname:')
    name = input('Name:')
    number = input('Number_telefon:')
    description = input('Description:') == [surname, name, number, description] 
    return list

def get_name():
    name = input('Имя:')
    return name

def get_number():
    number = input('№ телефона:')
    return number

def get_description():
    description = input('Описвние')
    return description

def data_coliection():
    return (get_surname(),get_data(), get_name(), get_number(),get_description())    

