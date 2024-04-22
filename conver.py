import re
import json
with open('./aophong.txt', 'r') as file:
    lines = file.readlines()
    title_line = None
    hashtags_line = None
    result = {}
    for line in lines:
        if re.findall('MÔ TẢ SẢN PHẨM', line):
         title_line = line
        if re.findall(r'#\w+', line):
         hashtags_line = line
         break
    result['content'] = []
    for line in lines[lines.index(title_line) +1:]:
        if line !='\n':
         if line == hashtags_line:
          break
         result['content'].append(line.rstrip() )

    if hashtags_line:   
        hashtags = re.findall(r'#\w+', hashtags_line)
        unique_hashtags = list(set(hashtags))
        result['hashtag'] = unique_hashtags

        result['key_words'] = []
        for line in lines[lines.index(hashtags_line) + 1:]:
            if line !='\n':
             if line.rstrip() != 'ĐÁNH GIÁ SẢN PHẨM':
                result['key_words'].extend(re.findall(r'[\w\s]+', line.rstrip()))              
             break

    print(result)

    # File path to export the JSON data
    file_path = "./resultDescribe.json"

    # Export data to JSON file
    with open(file_path, 'w', encoding='utf-8') as f:
     json.dump(result, f, ensure_ascii=False, indent=4)

    print("Data exported to", file_path)