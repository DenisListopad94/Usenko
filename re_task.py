import re

# 1
strings = ["dog", "cat", "mouse", "cat and dog", "elephant", "catfish"]

for string in strings:
    if re.search(r'\bcat\b', string):
        print(string)
# 2
strings = ["az123z", "bzABCz", "cz#z", "dzyzZ", "ez   z"]
for string in strings:
    if re.search(r'z.{3}z',string):
        print(string)
# 3
numbers = ["1234567890", "2345678901", "3456789012", "4567890123", "5678901234", "6789012345", "7890123456",
          "8901234567", "9012345678", "0123456789", "1357924680", "2468135790", "8642097531", "7531598624",
          "1597534862", "9513578642", "8642019753", "7531869240", "1597486532", "9513268740", "8642951736",
          "7531846925", "1597468253", "9513286475", "8642975136", "7531864925", "1597486253", "9513268475",
          "8642917536", "7531896425", "1597462538", "9513284675", "8642971536", "7531869254", "1597482635"
          ]
for number in numbers:
    if re.search(r'[8|9]\d{9}',number):
        print(number)
# 4
text = '''Python is a high-level, interpreted programming language that has gained popularity due to its clear syntax and readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
Python was created by Guido van Rossum and first released in 1991. It's designed to be easy to understand and write. The language is very flexible and versatile, making it suitable for a wide range of tasks, from simple scripting to complex machine learning algorithms.
One of the key features of Python is its extensive library of modules and packages, which provides pre-written code for various tasks. This includes modules for web development, mathematics, data analysis, machine learning, and more.
Python also has a large and active community of developers who contribute to its development and create third-party packages. This makes Python a great choice for both beginners and experienced developers.
In summary, Python is a powerful, versatile language with a strong community and a wide range of applications.
'''
print(re.findall(r'''\b[^ qwrtplkjhgfdszxcvbnm1234567890;,.:_-]\w*''',text.lower()))
# 5
text="В один прекрасный день, температура поднялась до +30 градусов. Это было на 20 градусов выше, чем вчера. Однако, к вечеру температура упала до -5 градусов. Это было на 35 градусов ниже, чем днем. Несмотря на это, люди были счастливы, потому что разница в температуре составила всего 10 градусов по сравнению с прошлым годом."
print(re.findall(r'''[-+]?\d+''',text.lower()))
# 6
pattern = r'human'
repl = r'computer'
string = r"Human - это уникальное существо с невероятной способностью к обучению и адаптации. Human может создавать, исследовать и менять мир вокруг себя. Но что делает human настолько особенным? Это его способность к эмпатии, способность понимать и делиться чувствами другого human. Это то, что отличает human от многих других видов на нашей планете."
print(re.sub(pattern, repl, string.lower(), count=0))
# 7
text = r"Сегодня 28-10-2023 года, и это особенный день. Ровно год назад, 28.10.2022, мы запустили наш новый проект. Это было важное событие, которое мы отмечали всю неделю до 04/11/2022. Но самым важным днем для нас был 2022-11-05, когда мы получили первые положительные отзывы от наших пользователей. С тех пор мы работаем над улучшением нашего продукта каждый день."
print(re.findall(r'\d\d-\d\d-\d{4}', text))
# 8
text = r"Barbara, a bright and bold biologist, lives in a beautiful brick building by the beach. She has a big backyard with blooming bluebells and butterflies. Every morning, Barbara enjoys her breakfast of blueberries and bran bread on her balcony, while observing the breathtaking beauty of the beach. She believes in the brilliance of balance in life and always brings her best to her work in biology."
print(re.findall(r'\b\w*b\w*\b',text.lower()))
# 9
text = "Sadfdsf jkjjkkkjds. fsdsfsda djffffaaaa fksdDl kkkkds fsdf jjjjfd."
print(re.sub(r"(\w)\1+", r"\1", text, count=0))
