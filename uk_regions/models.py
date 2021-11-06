from django.db import models


# Create your models here.


class ReDicKoatuuRegion(models.Model):
    """
    Все областя
    """
    this_id = models.IntegerField(verbose_name="Идентификатор", primary_key=True)
    level = models.PositiveIntegerField(verbose_name="Уровень")
    name = models.CharField(max_length=100, verbose_name="Область")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Областя'


class ReDistrict(models.Model):
    """
    Модель РАЙОНОВ!!!!!!!
    """
    region = models.ForeignKey(
        ReDicKoatuuRegion,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="region", verbose_name="Область"
    )
    this_id = models.IntegerField(verbose_name="Идентификатор", primary_key=True)
    level = models.PositiveIntegerField(verbose_name="Уровень")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class RegionCenter(models.Model):
    """
    Региональные центры и районы обл центров.
    """
    district = models.ForeignKey(
        ReDistrict,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="district",
        verbose_name="Район"
    )

    this_id = models.IntegerField(verbose_name="Идентификатор", primary_key=True)
    level = models.PositiveIntegerField(verbose_name="Уровень")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class CenterRegional(models.Model):
    """
    Обласные центры
    """
    region = models.ForeignKey(
        ReDicKoatuuRegion,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="regioncenter",
        verbose_name="Область"
    )
    level = models.PositiveIntegerField(verbose_name="Уровень")
    this_id = models.IntegerField(verbose_name="Идентификатор", primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обласной центр'
        verbose_name_plural = 'Обласные центры'
