from jinja2 import Template
#from jinja2.filters import escape
from markupsafe import escape


data = '''{% raw %}Модуль jinja вместо
определения {{ name }}
подставляет соответствующее значение{% endraw %}'''



tm = Template(data)
msg = tm.render(name='Федор')
print(msg)
print()


link = '''В HTML-документе ссылка определяются так:
<a href="#">Ссылка</a>'''

msg = escape(link)


print(msg)

