import qrcode
import os
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, CircleModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask, SquareGradiantColorMask

script_dir = os.path.dirname(os.path.abspath(__file__))
LOGO_IMG = os.path.join(script_dir, 'face.png')
OUTPUT_PATH = os.path.join(script_dir, "styled_qr.png")

qr = qrcode.QRCode(
	version= 1,
	error_correction=qrcode.constants.ERROR_CORRECT_H,
	box_size= 50,
	border= 0,
)

qr.add_data("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
qr.make(fit=True)

img = qr.make_image(
	image_factory= StyledPilImage,
	module_drawer= RoundedModuleDrawer(radius_ratio=0.5),
	eye_drawer = RoundedModuleDrawer(radius_ratio=1),
	color_mask = RadialGradiantColorMask(
		back_color=(255, 255, 255, 0),
		center_color=(0, 0, 255, 255),    
		edge_color=(128, 0, 128, 255)
		)
).convert("RGBA")

logo = Image.open(LOGO_IMG)

width, height = img.size
logo_size = 700

logo = logo.resize((logo_size, logo_size))
pos = ((width - logo_size) // 2, (height - logo_size) // 2)

img.paste(logo, pos)

img.save(OUTPUT_PATH)
print("Saved")