from structureBreakDown import *
import json

path = './aophong.txt'

file = open(path, 'r')

def lines_that_contain(string, fp):
    return [line for line in fp if string in line]

results = findHeadingPosition(file.readlines(), {
    'Product Information Section': 0,
    'CHI TIẾT SẢN PHẨM': 0,
    'MÔ TẢ SẢN PHẨM': 0,
    'ĐÁNH GIÁ SẢN PHẨM': 0,
    'CÁC SẢN PHẨM KHÁC CỦA SHOP': 0
})

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)
