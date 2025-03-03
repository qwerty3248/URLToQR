import qrcode
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <url>")
    sys.exit(1)

url = sys.argv[1]

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr.png")