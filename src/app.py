from PIL import Image, ImageDraw, ImageFont
import face_recognition
import os
import requests
import json

webhook_url = '' # redacted
# Load the jpg file into a numpy array
image = face_recognition.load_image_file(
    "/Users/lcao02/Dropbox/pygmathon19/src/anna.jpg")

# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# See also: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(image)
num_face = len(face_locations)
name = 'Anna'

if num_face >= 1:
    for face_location in face_locations:
        # Print the location of each face in this image
        top, right, bottom, left = face_location
        # You can access the actual face itself like this:
        # Create new face image
        # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
        face_image = image[top:bottom, left:right]
        # pil_image = Image.fromarray(face_image)
        pil_image = Image.fromarray(image)
        # Create a Pillow ImageDraw Draw instance to draw with
        draw = ImageDraw.Draw(pil_image)
        font = ImageFont.truetype("../fonts/Arial.ttf", 20)

        # Loop through each face found in the unknown image
        # Draw a box around the face using the Pillow module
        draw.rectangle(((left, top), (right, bottom)),
                       outline=(255, 255, 255),
                       width=1)

        # Draw a label with a name below the face
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 5), (right, bottom)),
                       fill=(255, 255, 255),
                       outline=(255, 255, 255),
                       width=1)
        draw.text((left + 6, bottom - text_height - 10),
                  name,
                  width=1,
                  font=font,
                  fill=(255, 0, 0, 255))
        # Remove the drawing library from memory as per the Pillow docs
        del draw
        # Display the resulting image
        # pil_image.show()
        pil_image.save('/Users/lcao02/Dropbox/Public/face.jpg')
        notif = f'WARNING: Your child is left in the car -- http'
        slack_data = {'text': notif}
        response = requests.post(webhook_url,
                                 data=json.dumps(slack_data),
                                 headers={'Content-Type': 'application/json'})

'''
References:
1. Face Recognition
https://github.com/ageitgey/face_recognition
2. Kids And Cars
https://www.kidsandcars.org/
Some secret URL and tokens have been redacted
'''
