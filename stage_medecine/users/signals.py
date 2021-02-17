from django.db.models import Sum
from users.models import Student


def stage_added_to_student(sender, **kwargs):
    if kwargs['action'] == 'post_add':
        kwargs['instance'].stage_points = kwargs['instance'].stages_done.all().aggregate(total=Sum('value')).get('total') or 0.0
        kwargs['instance'].save()


def create_user_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)


def save_user_student(sender, instance, **kwargs):
    instance.student.save()

