from jinja2 import Template, Environment, FileSystemLoader

from markupsafe import escape

persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}]

def loadTP



file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.htm')
msg = tm.render(users=persons)
print(msg)
















# data = '''{% raw %}Модуль jinja вместо
# определения {{ name }}
# подставляет соответствующее значение{% endraw %}'''
#
# tm = Template(data)
# msg = tm.render(name='Федор')
# print(msg)
# print()
#
#
# link = '''В HTML-документе ссылка определяются так:
# <a href="#">Ссылка</a>'''
#
# msg = escape(link)
#
#
# print(msg)

