import arabic_reshaper
from PIL import Image, ImageDraw, ImageFont
from bidi.algorithm import get_display
from pyarabic import araby

text = "العربية لغة سهلة"
text = "قالَ اللَّهُ تبارَكَ وتعالى : (يا ابنَ آدمَ لو بلغت ذنوبُكَ عَنانَ السَّماءِ ثمَّ استغفرتَني غفرتُ لَكَ، ولا أبالي). صحيح الترمذي ٣٥٤٠"


def wrap_text(text, font, max_width):
    # simpan list
    lines = []
    # simpan current_line
    current_line = ""
    # split text mejadi words
    words = araby.tokenize(text) # pip install pyarabic
    # untuk setiap word:
    for word in words:
    # temp_line = current + word + " " // temp_line = " ".join(current, word)
        temp_line = " ".join([current_line, word])
    # hitung >= max_width -> menambahkan ke list + current line == word ?: current line = temp line
        width = font.getbbox(temp_line)[2]  # x,y,x,y
        if width >= max_width:
            lines.append(current_line)
            current_line = ""
        else:
            current_line = temp_line

    # keluar dari loop -> jangan lupa tambahkan current line
    lines.append(current_line)

    # lines
    return lines

# text = arabic_reshaper.reshape(text)
# text = get_display(text)

image = Image.new("RGB", (1080, 920), (100, 100, 100))
canvas = ImageDraw.Draw(image)
font = ImageFont.truetype("Amiri-Regular.ttf", size=70)


# canvas.text((image.width - 100, 100), text, font=font, anchor="ra")

lines = wrap_text(text, font, image.width * 0.8)

y = 100
x = image.width - (image.width * 0.1)

ascender, descender = font.getmetrics()

for line in lines:
    line = arabic_reshaper.reshape(line)
    line = get_display(line)
    canvas.text((x, y), line, font=font, fill="black", anchor="ra")
    y += ascender + descender

image.show()

