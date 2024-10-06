# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Ban(models.Model):
    tg_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ban'


class BarAccess(models.Model):
    tg_id = models.BigIntegerField()
    ban = models.BooleanField(blank=True, null=True)
    registration_completed = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bar_access'


class BarGoods(models.Model):
    img = models.CharField(max_length=100, blank=True, null=True)
    discription = models.CharField(max_length=350, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bar_goods'


class Booze(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booze'


class CoffeeGoods(models.Model):
    img = models.CharField(max_length=100, blank=True, null=True)
    discription = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coffee_goods'


class CoffeeTeam(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    discription = models.CharField(max_length=500, blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coffee_team'


class DiscussionChats(models.Model):
    chat_id = models.CharField(max_length=100, blank=True, null=True)
    branch = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discussion_chats'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigIntegerField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Hairdressers(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    img_src = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hairdressers'


class HairdressersWorks(models.Model):
    barber_id = models.IntegerField(blank=True, null=True)
    img_src = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hairdressers_works'


class MenuMedia(models.Model):
    role = models.CharField(max_length=15, blank=True, null=True)
    src = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_media'


class MessagesText(models.Model):
    role = models.CharField(max_length=30, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages_text'


class NailsMasters(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    img_src = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nails_masters'


class NailsMastersWorks(models.Model):
    master_id = models.IntegerField(blank=True, null=True)
    img_src = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nails_masters_works'


class Subscriptions(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    level = models.ForeignKey('TypesOfSubscriptions', models.DO_NOTHING, db_column='level', blank=True, null=True)
    paid_for = models.FloatField(blank=True, null=True)
    bonuses = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscriptions'


class Tincture(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tincture'


class TypesOfSubscriptions(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=650, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    cashback = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'types_of_subscriptions'


class Users(models.Model):
    tg_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsersInfo(models.Model):
    id = models.ForeignKey(Users, models.DO_NOTHING, db_column='id', primary_key=True)
    tg_nick = models.CharField(max_length=30, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    birthday = models.FloatField(blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    booze = models.CharField(max_length=30, blank=True, null=True)
    tincture = models.CharField(max_length=30, blank=True, null=True)
    allergy = models.CharField(max_length=100, blank=True, null=True)
    reg_step = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_info'
