from django.db import models
from django.core.exceptions import ValidationError

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='projects')
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='images'
    )
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f"Image for {self.project.title}"

class Resume(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField()
    about = models.TextField()
    skills = models.ManyToManyField(Tag, related_name='skill')
    links = models.URLField(max_length=200, blank=True)

    def clean(self):
        """Проверка, что существует только одно резюме"""
        if not self.pk and Resume.objects.exists():
            raise ValidationError("Может существовать только одно резюме")

    def save(self, *args, **kwargs):
        """Сохраняем как Singleton"""
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_solo(cls):
        """Получаем единственное резюме"""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def delete(self, *args, **kwargs):
        """Запрещаем удаление"""
        pass

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resume"

class ResumeImage(models.Model):
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name='images', default=Resume.get_solo
    )
    image = models.ImageField(upload_to='resume_images/')

    def __str__(self):
        return f"Image for {self.resume.name} {self.resume.surname}"

class ResumeLink(models.Model):
    resume = models.ForeignKey(
        Resume, 
        on_delete=models.CASCADE, 
        related_name='resume_links', 
        default=Resume.get_solo
    )
    name = models.CharField(max_length=100, verbose_name="Название ссылки")  # Новое поле
    url = models.URLField(max_length=200, verbose_name="URL ссылки")  # Переименовано из link в url

    def __str__(self):
        return f"{self.name} - {self.url}"