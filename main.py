# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import arabic_reshaper
from PIL import Image, ImageFont, ImageDraw
from bidi.algorithm import get_display
from pyarabic.araby import tokenize

text = "قالَ اللَّهُ تبارَكَ وتعالى : (يا ابنَ آدمَ لو بلغت ذنوبُكَ عَنانَ السَّماءِ ثمَّ استغفرتَني غفرتُ لَكَ، ولا أبالي). صحيح الترمذي ٣٥٤٠"


def arabic_wrap_text_by_max_width(text, font, max_width):
    """return list of lines"""
    lines = []
    current_line = ""
    words = tokenize(text)
    for word in words:
        temp_line = current_line + word + " "
        if font.getbbox(temp_line)[2] >= max_width:
            lines.append(current_line.strip())
            current_line = word + " "
        else:
            current_line = temp_line

    lines.append(current_line)
    return lines

def main():
    image = Image.new("RGBA", (1080, 920), (255, 100, 200, 200))
    font = ImageFont.truetype("Amiri-Regular.ttf", 70)
    ascender, descender = font.getmetrics()
    print(ascender)
    print(descender)

    draw = ImageDraw.Draw(image)
    display = get_display(arabic_reshaper.reshape(text))
    lines = arabic_wrap_text_by_max_width(text, font, image.width * 0.8)
    y = 100
    height = sum([font.getbbox(line)[3] for line in lines]) / len(lines)

    for line in lines:
        draw.text((image.width / 2,  y), get_display(arabic_reshaper.reshape(line)), font=font, anchor="ma")
        # atau kita ambil box nya saja
        box = draw.textbbox((image.width / 2,  y), get_display(arabic_reshaper.reshape(line)), font=font, anchor="mt")
        # draw.rectangle(box)
        box_line = font.getbbox(line)

        y += ascender + descender
    image.show()
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
