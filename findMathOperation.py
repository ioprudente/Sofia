import re

regex = r"(soma|some|subtraia|divida)(?:.)(\d+)(?:.+)(\d+)"
        

def find_math_operation(transcription):
    result = re.findall(regex, transcription)
    return result
