import re
import json

def search_pattern(text):
    with open("/Users/watcharak/BAY/voiceAnalystic/Backend/core/API/Algolithm/dataset/pattern.json" , "r") as f:
        data = json.load(f)
    for key, value in data.items():
        for pattern in value['pattern']:
            result = re.findall(pattern, text)
            if(result):
                print(f"Match intent {key}: with value {result}")
            # else :
            #     print("not match")
    return result


text = "สวัสดีค่า ติดต่อจากบริษัทอยุธยาแคปปิตอลออโตลีส ขออนุญาตเรียนสายคุณสมชายค่ะ ใช่คุณสมชายใช่ไหมคะ ขอบคุณที่ใช้บริการธนาคารกรุงศรี สวัสดีค่ะ"


# print(search_pattern(text))