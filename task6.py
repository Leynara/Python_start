# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с
# прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(text_example):

    return text_example.capitalize()

print(int_func('test'))