# import io
# from google.cloud import vision
#
# # vision_client = vision.Client()
# # file_name = 'images/test_receipt.jpeg'
# #
# # with io.open(file_name, 'rb') as image_file:
# #     content = image_file.read()
# #     image = vision_client.image(content=content)
# #
# # labels = image.detect_labels()
# #
# # for label in labels:
# #     print(label.description)
#
#
# client = vision.ImageAnnotatorClient()
# with open('images/test_receipt.jpeg', 'rb') as image_file:
#     content = image_file.read()
#     response = client.logo_detection({
#     'content': content,
#     })
#
# labels = image.detect_labels()
#
# for label in labels:
#     print(label.description)

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    # Client will talk to Vision API
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

detect_text("../images/test_receipt.jpeg")
