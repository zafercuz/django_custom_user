from django.db import models


class Career(models.Model):
    career_name = models.CharField(max_length=100, verbose_name='Career')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.career_name

    class Meta:
        verbose_name = "Career"
        verbose_name_plural = "Careers"
