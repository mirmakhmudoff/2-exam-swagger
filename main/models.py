import uuid
from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class About(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Contact from {self.name} <{self.email}>"


class News(BaseModel):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = models.TextField()
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    view_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    sphere_of_activity = models.TextField()
    education = models.TextField()
    scientific_degree = models.TextField()
    legal_practice = models.TextField()
    license = models.CharField(max_length=100)
    membership = models.CharField(max_length=100)
    languages = models.TextField()
    image = models.ImageField(upload_to='team_images/', null=True, blank=True)
    slug = models.SlugField(max_length=400, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Publication(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    team_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name='publications')
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Review(BaseModel):
    service_id = models.IntegerField()
    full_name = models.CharField(max_length=50)
    description = models.TextField()
    file = models.FileField(upload_to='review_files/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"Review by {self.full_name} for Service ID {self.service_id}"


class Search(models.Model):
    content_type = models.CharField(max_length=20)
    content_id = models.IntegerField()

    def __str__(self):
        return f"Search for {self.content_type} with ID {self.content_id}"


class Service(BaseModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='service_images/', null=True, blank=True)
    view_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
