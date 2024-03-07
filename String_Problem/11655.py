import sys
def ROT13(string):
    for char in string:
        if not char.isalpha():
            print(char, end="")
        else:
            if char.isupper():
                if ord(char) >= 78:
                    char = chr(65 + ord(char) + 13 - 91)
                else:
                    char = chr(ord(char) + 13)
            else:
                if ord(char) >= 110:
                    char = chr(97 + ord(char) + 13 - 123)
                else:
                    char = chr(ord(char) + 13)
            print(char, end="")

string = sys.stdin.readline().rstrip()
ROT13(string)