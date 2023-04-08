from runlengthencoding import run_length_encoder2 as e
from runlengthdecoding import run_length_decoder as d

string = "Hello World"
print(e(string))
print(d(e(string)))
