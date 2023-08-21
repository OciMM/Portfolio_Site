from django.db import models


# section "CAREER AND EDUCATION"
class Experience(models.Model):
    """Model of record the experience"""
    name_organization = models.CharField("An organization", max_length=120)
    position = models.CharField("A position", max_length=120)
    description = models.TextField("Description of the job")
    start_at = models.DateTimeField("Date of start your experience")
    end_at = models.DateTimeField(
        "Date of end your experience",
        blank=True
    )

    def __str__(self):
        return self.name_organization


class Education(models.Model):
    """Model of record the education"""
    name_organization = models.CharField("An organization", max_length=120)
    major = models.CharField("A major", max_length=120)
    description = models.TextField("Description of the major")
    start_at = models.DateTimeField("Date of start your education")
    end_at = models.DateTimeField(
        "Date of end your education",
        blank=True
    )

    def __str__(self):
        return self.name_organization


# PORTFOLIO
# class Project(models.Model):
#     """Model of projects"""
#     name_job = models.CharField("Job", max_length=120)
#     name_project = models.CharField("Project", max_length=120)
#     description = models.CharField("Short description", max_length=160)
#     image = models.ImageField(verbose_name='image of project', upload_to='projects/')
#     name_image = models.CharField("alter name of image", max_length=80, blank=True)
#     url = models.URLField(verbose_name='URL', unique=True)
#
#     def __str__(self):
#         return self.name_job
