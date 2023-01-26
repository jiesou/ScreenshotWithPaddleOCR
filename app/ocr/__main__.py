from paddleocr import PaddleOCR
import re

def main():
    ocr = PaddleOCR(use_angle_cls = True, use_gpu= False, show_log = False)
    result = ocr.ocr("temp.png", cls=True)
    text = "\n".join([line[1][0] for line in result[0]])

    # filter consecutive whitespace
    text = re.sub(r"(\S)\s\s*", r"\1\n", text)

    # replace line break with space after engilsh words
    text = re.sub(r"([a-zA-Z0-9,.?!;])\n", r"\1 ", text)
    # delete line break after other characters
    text = re.sub(r"(\S)\n", r"\1", text)

    # add spaces around english words and others characters
    text = re.sub(r"([^a-zA-Z0-9,\.\?!;:'\"()，。？！；：、“”（）\s])([a-zA-Z0-9,\.\?!;])",
                r"\1 \2", text)
    text = re.sub(r"([a-zA-Z0-9,\.?!;])([^a-zA-Z0-9,\.\?!;:'\"()，。？！；：、“”（）\s])",
                r"\1 \2", text)
    print(text)


if __name__ == "__main__":
    main()