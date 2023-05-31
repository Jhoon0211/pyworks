# 이미지 처리 - flow
from PIL import Image
from pytesseract import pytesseract

# 엔진
pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

img = Image.open("source/size.PNG")
# img.show()
text = pytesseract.image_to_string(img, lang="kor+eng")
print(text)

# 변환된 텍스트 파일에 쓰기
# encoding = 'utf-8' 꼭 명시해야 함
with open("./output/new.text", 'w', encoding='utf-8') as f:
    f.write(text)
    f.write(text.replace(" ", ""))