from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from .models import Profile,Escort,patient,Reminder

@receiver(pre_save, sender=patient)
def set_patient_username(sender, instance, **kwargs):
    if not instance.Handel:
        username = f'{instance.FirstName}_{instance.LasttName}'.lower()
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f'{instance.FirstName}_{instance.LastName}_{counter}'.lower()
            counter += 1
        instance.Handel = username


@receiver(pre_save, sender=Escort)
def set_escort_username(sender, instance, **kwargs):
    if not instance.yourHandel:
        username = f'{instance.FirstName}_{instance.LasttName}'.lower()
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f'{instance.FirstName}_{instance.LastName}_{counter}'.lower()
            counter += 1
        instance.yourHandel = username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(pre_save, sender=User)
def set_username(sender, instance, **kwargs):
    if not instance.username:
        username = f'{instance.first_name}_{instance.last_name}'.lower()
        counter = 1
        while User.objects.filter(username=username):
            username = f'{instance.first_name}_{instance.last_name}_{counter}'.lower()
            counter += 1
        instance.username = username




@receiver(post_save, sender=Reminder)
def update_pill_count_on_save(sender, instance, **kwargs):
    patient = instance.patientID
    if instance.Checked:
        patient.total_pills -= instance.PillCount
    else:
        patient.total_pills += instance.PillCount
    patient.save()

@receiver(post_delete, sender=Reminder)
def update_pill_count_on_delete(sender, instance, **kwargs):
    patient = instance.patientID
    if instance.Checked:
        patient.total_pills += instance.PillCount
    patient.save()
    
def update_pills_count(sender, instance, **kwargs):
    instance.decrease_pills_count()    
