import easyocr

reader = easyocr.Reader(['en', 'ru'],
                        model_storage_directory='final_model',
                        user_network_directory='user_network',
                        recog_network='EasyOCR_finetuned')
print(reader)
result = reader.readtext('all_data/ru_val/800.jpg')
print(result)