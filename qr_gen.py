import qrcode
from qrcode.constants import ERROR_CORRECT_Q

url = "https://raw.githubusercontent.com/gonzaloop1494/gonzalo-pacheco-agredano/main/English_C1_Certificate.pdf"

qr = qrcode.QRCode(
    version=None,  # tamaño automático
    error_correction=ERROR_CORRECT_Q,  # alta tolerancia (ideal para imprimir)
    box_size=12,  # tamaño de cada cuadrado (calidad)
    border=4,  # margen obligatorio estándar
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("QR_English_Certificate.png")

print("QR generado correctamente")
