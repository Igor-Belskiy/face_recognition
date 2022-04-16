import face_recognition
from PIL import Image, ImageDraw

def face_rec():
    gal_face_img = face_recognition.load_image_file('img/mnogo-devushek-belye.jpg')
    gal_face_location = face_recognition.face_locations(gal_face_img)

    print(gal_face_location)
    print(f'Found {len(gal_face_location)} face(s) in this image')

    pil_img = Image.fromarray(gal_face_img)
    draw1 = ImageDraw.Draw(pil_img)

    for (top, right, bottom, left) in gal_face_location:
        draw1.rectangle(((left, top),(right, bottom)), outline=(255, 255, 0), width=4)

    del draw1
    pil_img.save('img/mnogo-devushek-marked-faces.jpg')

def main():
    face_rec()

if __name__ == '__main__':
    main()
