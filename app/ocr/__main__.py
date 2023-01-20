from paddleocr import PaddleOCR

def main():
    ocr = PaddleOCR(use_angle_cls = True, use_gpu= False, show_log = False)
    result = ocr.ocr("temp.png", cls=True)
    for line in result[0]:
       print(line[1][0])

if __name__ == "__main__":
    main()