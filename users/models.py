from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models.deletion import CASCADE, SET_NULL
from django.utils.translation import ugettext_lazy as _
from axis.models import Axis
from address.models import Address


class MyUserManager(UserManager):
    def create_user(self, name, email, date_joined, rg, cpf, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=email,
            name=name,
            email=self.normalize_email(email),
            date_joined=date_joined,
            rg=rg,
            cpf=cpf
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, date_joined, rg, cpf, password=None, **kwargs):
        user = self.create_user(
            username=email,
            name=name,
            email=self.normalize_email(email),
            date_joined=date_joined,
            rg=rg,
            cpf=cpf,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    SCHOLARSHIP_CHOICES = (('1', 'Bolsista'), ('2', 'Voluntário'))
    BOND_TYPE_CHOICES =(('1', 'Coordenador'), ('2', 'Orientador'), ('3', 'Estagiário'), ('4', 'Colaborador Eventual'))
    username = models.CharField(blank=True, null=True, default=None, max_length=50, unique=True)
    first_name = models.CharField(blank=True, null=True, default=None, max_length=50)
    last_name = models.CharField(blank=True, null=True, default=None, max_length=50)
    name = models.CharField(_("Nome"), max_length=100, blank=True, null=True)
    email = models.EmailField(_('Email'), unique=True)
    rg = models.CharField(_("RG"), max_length=20, blank=True, null=True)
    cpf = models.CharField(_("CPF"), max_length=50, blank=True, null=True)
    cnh = models.CharField(_("CNH"), max_length=50, blank=True, null=True)
    date_joined = models.DateField(_("Data de entrada na CDH"), auto_now=False, blank=True, null=True)
    axis = models.ForeignKey(Axis, verbose_name=_("Eixo"), on_delete=models.SET_NULL, blank=True, null=True)
    bond_type = models.CharField(_("Tipo de vínculo"), max_length=50, blank=True, null=True, choices=BOND_TYPE_CHOICES)
    phone = models.CharField(_("Telefone"), max_length=15, blank=True, null=True)
    registration = models.CharField(_("Nº de matrícula"), max_length=50, blank=True, null=True)

    course = models.CharField(_("Curso"), max_length=50, blank=True, null=True)
    university = models.CharField(_("Universidade"), max_length=50, blank=True, null=True)
    department = models.CharField(_("Departamento"), max_length=50, blank=True, null=True)

    date_fired = models.DateField(_("Data de desligamento"), default=None, blank=True, null=True)
    is_active = models.BooleanField(_("Ativo"), default=True)
    is_staff = models.BooleanField(_('Staff'), default=False)
    is_superuser = models.BooleanField(_('Admin'), default=False)

    scholarship = models.CharField(_("Bolsista"), max_length=50, blank=True, null=True, choices=SCHOLARSHIP_CHOICES)
    scholarship_type = models.CharField(_("Tipo de bolsa"), max_length=50, blank=True, null=True)

    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['bond_type', 'phone', 'registration', 'course', 'university', 'department',
    #                    'address', 'is_active', 'scholarship', 'scholarship_type']
    REQUIRED_FIELDS = ['name', 'bond_type', 'phone', 'registration', 'course', 'university', 'department',
                       'rg', 'cpf', 'cnh', 'address', 'date_joined', 'is_active', 'scholarship', 'scholarship_type']

    def __str__(self):
        return self.name
