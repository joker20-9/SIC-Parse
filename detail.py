import re
import json
with open('./aophong.txt', 'r') as file:
    lines = file.readlines()
    title_line = None
    mileStoneStartLine='CHI TIẾT SẢN PHẨM'
    mileStonePauseLine = 'MÔ TẢ SẢN PHẨM'
    result = {
       "breadcumb": [],
       "detail":{}
    }
    keyDetail=[]
    valueDetail=[]
    for line in lines:
        if re.findall(mileStoneStartLine, line):
         title_line = line
         break
    gettingBreadcumb = True
    for index, line in enumerate(lines[lines.index(title_line) +2:]):
        if line.rstrip() == mileStonePauseLine:
           break
        if gettingBreadcumb:
          if line.rstrip() != 'icon arrow right':
            if index % 2 == 1:
               keyDetail.append(line.rstrip())
               gettingBreadcumb = False
            else:
             result['breadcumb'].append(line.rstrip()) 

        else:
            if len(keyDetail) == len(valueDetail):
                keyDetail.append(line.rstrip())
            else:
                valueDetail.append(line.rstrip())
    result['detail'] = dict(zip(keyDetail, valueDetail))
    # File path to export the JSON data
    file_path = "./detailResult.json"

    # Export data to JSON file
    with open(file_path, 'w', encoding='utf-8') as f:
     json.dump(result, f, ensure_ascii=False, indent=4)

    print("Data exported to", file_path)
       
                 
           