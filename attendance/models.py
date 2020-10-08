from django.db import models
from entities.models import Entity
from users.models import User
from people.models import Person
# Create your models here.


class Attendance(models.Model):
    assisted_person = models.ForeignKey(Person, on_delete=models.SET_NULL,
                                        related_name="atendimento", blank=True, null=True)

    how_knew_about_drs = models.CharField(max_length=100, blank=True, null=True)
    current_occupation = models.CharField(max_length=100, blank=True, null=True)
    had_other_occupations = models.CharField(max_length=100, blank=True, null=True)
    relevant_information = models.CharField(max_length=100, blank=True, null=True)
    entities = models.ManyToManyField(Entity, related_name="entity")
    last_attendance_date = models.DateField()

    how_knew_about_transpasse = models.CharField(max_length=100, blank=True, null=True)
    psychology_intern = models.ForeignKey(User, verbose_name="Estagiária de psicologia", blank=True, null=True,
                                          on_delete=models.SET_NULL)
    lives_with = models.CharField(max_length=100, blank=True, null=True)
    cities_lived = models.CharField(max_length=100, blank=True, null=True)
    ist_exams_up_to_date = models.BooleanField(default=False)
    last_time_been_health_center = models.CharField(max_length=100, blank=True, null=True)
    is_drug_user = models.BooleanField(default=False, blank=True, null=True)
    which_drugs = models.CharField(max_length=100, blank=True, null=True)
    consider_drugs_bad = models.BooleanField(default=False, blank=True, null=True)
    uses_hormones = models.BooleanField(default=False, blank=True, null=True)
    use_accompanied_by_doctor = models.BooleanField(default=False, blank=True, null=True)
    which_hormones = models.CharField(max_length=100, blank=True, null=True)
    works = models.BooleanField(default=False, blank=True, null=True)
    where_works = models.CharField(max_length=100, blank=True, null=True)
    already_worked = models.BooleanField(default=False, blank=True, null=True)
    where_worked = models.CharField(max_length=100, blank=True, null=True)
    interests = models.CharField(max_length=100, blank=True, null=True)
    makes_track = models.BooleanField(default=False, blank=True, null=True)
    track_type = models.CharField(max_length=100, blank=True, null=True)
    where_makes_track = models.CharField(max_length=100, blank=True, null=True)
    documents_owned = models.CharField(max_length=100, blank=True, null=True)
    rectified_name_and_gender = models.BooleanField(default=False, blank=True, null=True)
    willing_to_rectify = models.BooleanField(default=False, blank=True, null=True)
    been_arrested = models.BooleanField(default=False, blank=True, null=True)
    city_arrested = models.CharField(max_length=100, blank=True, null=True)
    year_arrested = models.CharField(max_length=20, blank=True, null=True)
    was_processed = models.BooleanField(default=False, blank=True, null=True)