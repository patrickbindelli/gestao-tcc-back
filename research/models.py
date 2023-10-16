import os
from django.db import models
from users.models import Student, Teacher, UserAccount
from django.core.exceptions import ValidationError
from hashid_field import HashidAutoField


class Course(models.Model):
    name = models.CharField(max_length=255)
    acronym = models.CharField(max_length=4)

    class Meta:
        verbose_name = "Curso"


class ThesisProject(models.Model):
    TCC1 = 1
    TCC2 = 2

    RESEARCH_CHOICES = (
        (TCC1, "TCC I"),
        (TCC2, "TCC II"),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        Student, related_name="research_author", on_delete=models.CASCADE
    )
    advisor = models.ForeignKey(
        Teacher,
        related_name="research_advisor",
        on_delete=models.CASCADE,
    )
    approved = models.BooleanField(default=False)
    approved_at = models.DateField(null=True, blank=True)

    type = models.PositiveSmallIntegerField(choices=RESEARCH_CHOICES, default=TCC1)

    committee = models.CharField(max_length=100, blank=True, null=True)
    defense_date = models.DateField(blank=True, null=True)

    invite = models.ForeignKey("Invite", on_delete=models.CASCADE)

    file = models.FileField(null=True, blank=True)

    responsible = models.ForeignKey(
        Teacher, verbose_name=("Professor Responsável"), on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Projeto de TCC"
        verbose_name_plural = "Projetos de TCC"


def validate_pdf_extension(value):
    if not value.name.endswith(".pdf"):
        raise ValidationError("Only PDF files are allowed.")


def file_upload_path(instance, filename):
    project_id = instance.project.id
    project_type = instance.project.get_type_display().replace(" ", "_")
    return os.path.join(f"{project_type}", str(project_id), "versions", filename)


class FileVersion(models.Model):
    hash_id = HashidAutoField(primary_key=True)
    version_number = models.PositiveIntegerField(null=True, blank=True, editable=False)

    comments = models.TextField(blank=True, null=True)
    file = models.FileField(
        null=True,
        blank=True,
        upload_to=file_upload_path,
        validators=[validate_pdf_extension],
    )

    project = models.ForeignKey(
        ThesisProject, on_delete=models.CASCADE, related_name="file_versions"
    )

    def save(self, *args, **kwargs):
        if not self.version_number:
            max_version = FileVersion.objects.filter(project=self.project).aggregate(
                models.Max("version_number")
            )["version_number__max"]
            self.version_number = max_version + 1 if max_version else 1

        if self.file and not os.path.basename(self.file.name).startswith(
            self.project.title
        ):
            split_file_name = os.path.splitext(self.file.name)

            new_filename = f"{split_file_name[0]}_Version_{self.version_number}{split_file_name[1]}"
            self.file.name = new_filename

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Version {self.version_number} of {self.project.title}"


Teacher
from datetime import timedelta, datetime


def get_deadline():
    return datetime.today() + timedelta(days=20)


class Invite(models.Model):
    type = models.PositiveSmallIntegerField(
        choices=ThesisProject.RESEARCH_CHOICES,
        default=ThesisProject.TCC1,
    )

    sender = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name="sent_invites"
    )

    receiver = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="received_invites"
    )

    advisor = models.ForeignKey(
        Teacher,
        related_name="research_advisor_invite",
        on_delete=models.CASCADE,
    )

    responsible = models.ForeignKey(
        Teacher,
        verbose_name=("Professor Responsável"),
        related_name="research_responsible_invite",
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    limit_date = models.DateTimeField(blank=False, null=False, default=get_deadline)

    def __str__(self):
        invite_type = dict(ThesisProject.RESEARCH_CHOICES).get(
            self.type, "Tipo Desconhecido"
        )
        status = "Aceito" if self.accepted else "Pendente"
        return f"Convite de {self.sender.first_name} {self.sender.last_name} para {self.receiver.user.first_name} {self.receiver.user.last_name} - Tipo: {invite_type} - Status: {status}"

    class Meta:
        verbose_name = "Convite"
