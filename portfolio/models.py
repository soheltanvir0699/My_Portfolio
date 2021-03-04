from django.db import models


# Create your models here.

class Product(models.Model):
    DEVELOP_CHOICES = (
        ('Android', 'Android'),
        ('Ios', 'Ios'),
        ('Web Development', 'Web Development'),
        ('Web Design', 'Web Design'),
    )
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=800, null=False, blank=False)
    image = models.ImageField()
    category = models.CharField(max_length=100, choices=DEVELOP_CHOICES, null=False, blank=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            this = Product.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()
        except:
            pass
        super(Product, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # first, delete the file
        self.image.delete(save=False)

        # now, delete the object
        super(Product, self).delete(*args, **kwargs)


class Blog(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    descriptions = models.CharField(max_length=800, null=False, blank=False)
    descriptions_details = models.CharField(max_length=1000, null=False, blank=False)
    admin = models.CharField(max_length=50, null=False, blank=False)
    comment = models.IntegerField(null=False, blank=False)
    image = models.ImageField()
    like = models.IntegerField(null=False, blank=False)
    tag = models.IntegerField(null=False, blank=False)
    productLink = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            this = Blog.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()
        except:
            pass
        super(Blog, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # first, delete the file
        self.image.delete(save=False)

        # now, delete the object
        super(Blog, self).delete(*args, **kwargs)