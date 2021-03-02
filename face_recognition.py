from aip import AipFace
import photo


def face_recognize(config):
    client = AipFace(config[0], config[1], config[2])
    while(1):
        photo.capture_photo()
        image = photo.image_read('photo.png')
        image = str(image, 'utf-8')
        detect_result = client.detect(image, "BASE64")
        if detect_result['result']['face_list'][0]['face_probability'] > 0.6:
            search_result = client.search(image, "BASE64", config[3])
            if search_result['result']['user_list'][0]['score'] > 70:
                print("Recognize successfully!")
                print("Recognize score:", search_result['result']['user_list'][0]['score'])
                print("Clint_name:", search_result['result']['user_list'][0]['user_id'])
                break
            else:
                continue
        else:
            continue