from django.db import models



class Helper(models.Model):
    name = models.CharField(max_length=300, verbose_name="Nomi")
    title = models.TextField()
    number = models.PositiveBigIntegerField(verbose_name="Nomer")



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Manzil"
        verbose_name_plural = "Manzillar"
        ordering = ['id']




class Change(models.Model):
    name = models.CharField(max_length=4000, verbose_name="url name")
    simple_price = models.CharField(max_length=40, verbose_name="oddiy tarif")
    premium = models.CharField(max_length=40, verbose_name="premium tarif")
    platinum  = models.CharField(max_length=40, verbose_name="yuqori  tarif")



    def __str__(self):
        return self.name



    class Meta:
        verbose_name = "Url va Narxlar discord"
        ordering = ['id']




class ChangePrice(models.Model):
    name = models.CharField(max_length=4000, verbose_name="url name")
    simple_price = models.CharField(max_length=40, verbose_name="oddiy tarif")
    premium = models.CharField(max_length=40, verbose_name="premium tarif")
    platinum  = models.CharField(max_length=40, verbose_name="yuqori  tarif")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Url va Narxlar online_dars"
        ordering = ['id']



class ChangePrices(models.Model):
    name = models.CharField(max_length=4000, verbose_name="url name")
    simple_price = models.CharField(max_length=40, verbose_name="oddiy tarif")
    premium = models.CharField(max_length=40, verbose_name="premium tarif")
    platinum  = models.CharField(max_length=40, verbose_name="yuqori  tarif")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Narxlar savdo-robot"
        ordering = ['id']




class Result(models.Model):
    number  = models.PositiveBigIntegerField()
    name = models.CharField(max_length=4000, verbose_name="Natija nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Natija"
        verbose_name_plural = "Natijalar"
        ordering = ['id']



class Discord(models.Model):
    number = models.CharField(max_length=400, verbose_name="Azolar soni")
    title = models.TextField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
        ordering = ['id']



class Users(models.Model):
    name=models.CharField(max_length=200, verbose_name="Nomi")
    phone=models.PositiveIntegerField()
    subject = models.CharField(max_length=3000,  verbose_name="Bo'lim")
    message = models.TextField()
    #created  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"
        ordering = ['-id']



class Photos(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='photos/', verbose_name='rasm')
    img = models.ImageField(upload_to='photos/', verbose_name='rasm')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/" + str(self.id) + "/"
