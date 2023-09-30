from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

  is_entrepreneur = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=True)

  def __str__(self):
      return self.username 
  class Meta:
        verbose_name_plural = "Users"


class Entrepreneur_Data(models.Model):
    id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    age = models.IntegerField()
    country = models.CharField(max_length=255)
    studyField = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.id}"

    class Meta:
        app_label = 'sel4c'
        verbose_name = "Entrepreneur's Data"
        verbose_name_plural = "Entrepreneurs' Data"
    
    @classmethod
    def create(cls, user_identifier, degree, institution, gender, age, country, studyField):
        # Try to find the user by either username or id
        try:
            user = User.objects.get(username=user_identifier)
        except User.DoesNotExist:
            try:
                user = User.objects.get(id=user_identifier)
            except User.DoesNotExist:
                raise Exception("User not found.")

        # Create or update Entrepreneur_Data instance
        entrepreneur_data, created = cls.objects.get_or_create(id=user)
        entrepreneur_data.degree = degree
        entrepreneur_data.institution = institution
        entrepreneur_data.gender = gender
        entrepreneur_data.age = age
        entrepreneur_data.country = country
        entrepreneur_data.studyField = studyField
        entrepreneur_data.save()

        return entrepreneur_data
    

class Activity(models.Model):
    id_activity = models.BigAutoField(primary_key=True)
    activity_num = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    description = models.TextField()
    deliveries = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.activity_num}"
    class Meta:
        app_label = 'sel4c'


class Question(models.Model):
    id_question = models.BigAutoField(primary_key=True)
    question_num = models.IntegerField(default=0)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.id}. ({self.description})"
    class Meta:
        app_label = 'sel4c'


class Answer(models.Model):
    id_answer = models.BigAutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.IntegerField(default=0)

    entrepreneur = models.ForeignKey(Entrepreneur_Data, on_delete=models.CASCADE, default=0)

    def __str__(self) -> str:
        return f"{self.question_id}.{self.id}"
    class Meta:
        app_label = 'sel4c'


class File(models.Model):
    id_file = models.BigAutoField(primary_key=True)
    file = models.FileField(upload_to='files/')
    filetype = models.CharField(max_length=255)

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    entrepreneur = models.ForeignKey(Entrepreneur_Data, on_delete=models.CASCADE, default=0)

    def __str__(self) -> str:
        return f"{self.id} ({self.activity_id})"
    class Meta:
        app_label = 'sel4c'
