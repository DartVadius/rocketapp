from django.core.files.storage import FileSystemStorage
from galleryapp.models import Photo
import time
from PIL import Image


class Files:

    @staticmethod
    def images_to_gallery_upload(obj, files_list):
        for file in files_list:
            fs = FileSystemStorage()
            filename = fs.save(str(obj.id) + '/' + str(round(time.time())) + '_' + file.name, file)
            splited = filename.split('/')
            splited[-1] = 'thumb_' + splited[-1]
            thumb_path = '/'.join(splited)
            uploaded_file_url = fs.url(filename)
            img = Photo()
            img.gallery_id = obj.id
            img.path = uploaded_file_url
            img.save()
            img = Image.open('media/' + filename)
            size = (280, 280)
            img.thumbnail(size)
            img.save('media/' + thumb_path)
