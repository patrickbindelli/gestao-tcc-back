from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Usuários devem fornecer um email válido")

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(email=email, **kwargs)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(email, password=password, **kwargs)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Course:
    SISTEMAS_DE_INFORMACAO = 1
    ADMNISTRACAO = 2
    ENGENHARIA_DE_PRODUCAO = 3
    MATEMATICA = 4

    COURSE_CHOICES = (
        (SISTEMAS_DE_INFORMACAO, "Sistemas de Informação"),
        (ADMNISTRACAO, "Admnistração"),
        (ENGENHARIA_DE_PRODUCAO, "Engenharia de Produção"),
        (MATEMATICA, "Matemáticca"),
    )


class Role:
    STUDENT = 1
    TEACHER = 2

    ROLE_CHOICES = (
        (STUDENT, "Aluno"),
        (TEACHER, "Professsor"),
    )


class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255, verbose_name="Primeiro Nome")
    last_name = models.CharField(max_length=255, verbose_name="Sobrenome")

    email = models.EmailField(
        verbose_name="Endereço de Email",
        max_length=255,
        unique=True,
    )

    role = models.PositiveSmallIntegerField(
        choices=Role.ROLE_CHOICES, blank=True, null=True, verbose_name="Tipo de Usuário"
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == Role.STUDENT:
            Student.objects.get_or_create(user=self)
        elif self.role == Role.TEACHER:
            Teacher.objects.get_or_create(user=self)
        elif self.role is None:
            pass

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    course = models.PositiveSmallIntegerField(
        choices=Course.COURSE_CHOICES,
        blank=True,
        null=True,
        verbose_name="Curso",
    )

    user = models.OneToOneField(
        UserAccount, blank=False, null=False, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Teacher(models.Model):
    user = models.OneToOneField(
        UserAccount, blank=False, null=False, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
