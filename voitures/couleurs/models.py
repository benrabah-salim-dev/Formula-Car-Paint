from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super().save(*args, **kwargs)


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    colors = models.ManyToManyField("Color", related_name="car_models")

    def __str__(self):
        return f"{self.brand} {self.name} {self.year}"


class Color(models.Model):
    car_model = models.ForeignKey(Model, on_delete=models.CASCADE, null=True, blank=True, related_name="car_colors")
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=10)
    color_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            existing_color = Color.objects.get(color_code=self.color_code)
            self.pk = existing_color.pk
        except Color.DoesNotExist:
            pass

        super().save(*args, **kwargs)


class BaseColor(models.Model):
    name = models.CharField(max_length=50)
    color_code = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class ColorFormula(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    color_code = models.CharField(max_length=7)

    def __str__(self):
        return str(self.color)


class BaseColorFormula(models.Model):
    formula = models.ForeignKey(ColorFormula, on_delete=models.CASCADE)
    base_color = models.ForeignKey(BaseColor, on_delete=models.CASCADE)
    amount_in_grams = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.base_color} {self.amount_in_grams}g"
