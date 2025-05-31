import cv2
from PIL import Image

# Paths
image_path = 'ima\\man.png'
hat_path = 'ima\\tophatnew.png'
horn_path = 'ima\\horn.png'
cascade_path = 'haarcascade_frontalface_default (1).xml'

# Load face detector
face_cascade = cv2.CascadeClassifier(cascade_path)

# Load image and grayscale version
image_cv = cv2.imread(image_path)
gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

# Detect face(s)
faces = face_cascade.detectMultiScale(gray)

# Open images with transparency
image = Image.open(image_path).convert('RGBA')
hat = Image.open(hat_path).convert('RGBA')
horn = Image.open(horn_path).convert('RGBA')

if len(faces) > 0:
    (x, y, w, h) = faces[0]

    # --- Hat Placement (evenly centered on top of head) ---
    hat_width = int(1.2 * w)  # Slightly wider than the face
    hat_height = int(hat_width * hat.height / hat.width)
    resized_hat = hat.resize((hat_width, hat_height))

    hat_x = x + w // 2 - hat_width // 2  # Center horizontally
    hat_y = y - hat_height + int(h * 0.1)  # On top of head
    image.paste(resized_hat, (hat_x, hat_y), resized_hat)

    # --- Horn Placement (unchanged) ---
    horn_width = int(w * 0.55)
    horn_height = int(horn_width * horn.height / horn.width)
    resized_horn = horn.resize((horn_width, horn_height))

    horn_x = x + int(w * 0.25) - int(horn_width / 2)  # Previously left-shifted
    horn_y = y + int(h * 0.65) - int(horn_height / 2)
    image.paste(resized_horn, (horn_x, horn_y), resized_horn)

# Save and show result
output_path = 'img\\final_result.png'
image.save(output_path)

image_cv_result = cv2.imread(output_path)
cv2.imshow('Final', image_cv_result)
cv2.waitKey(0)
cv2.destroyAllWindows()