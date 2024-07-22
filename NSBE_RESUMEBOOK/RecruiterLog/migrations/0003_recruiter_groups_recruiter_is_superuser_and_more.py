# Generated by Django 4.2.2 on 2023-10-25 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("RecruiterLog", "0002_recruiter_is_recruiter"),
    ]

    operations = [
        migrations.AddField(
            model_name="recruiter",
            name="groups",
            field=models.ManyToManyField(
                blank=True, related_name="recruiters", to="auth.group"
            ),
        ),
        migrations.AddField(
            model_name="recruiter",
            name="is_superuser",
            field=models.BooleanField(
                default=False,
                help_text="Designates that this user has all permissions without explicitly assigning them.",
                verbose_name="superuser status",
            ),
        ),
        migrations.AddField(
            model_name="recruiter",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
        migrations.AddField(
            model_name="recruiter",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True, related_name="recruiters", to="auth.permission"
            ),
        ),
        migrations.DeleteModel(name="StudentInfoAccess",),
    ]
