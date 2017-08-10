from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# Create your models here.


class FileUp(models.Model):
    img = models.ImageField(upload_to='imagens')

    def save(self):
        # Opening the uploaded image
        im = Image.open(self.img)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((50, 50))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.img = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.img.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)

        super(FileUp, self).save()


