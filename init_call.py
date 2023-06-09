class CustomStrip:

    def __init__(self, characters):
        self.__characters = characters

    def __call__(self, str):
        return str.strip(self.__characters)


cs = CustomStrip('!$#@%')

string_to_clear = '@Hello, world!$'

result = cs(string_to_clear)

print(result)