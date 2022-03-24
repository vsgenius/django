from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=255)
    release_date = models.CharField(max_length=50)
    lte_exists = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

