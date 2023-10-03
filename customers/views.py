from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer
from robots.models import Robot
from django.conf import settings
from django.http import HttpResponse


@receiver(post_save, sender=Customer)
def notify_customers(sender, instance, **kwargs):
    if instance.available:
        orders = Customer.objects.filter(robot=instance.robot, available=True)
        for order in orders:
            subject = 'Робот {} версии {} теперь в наличии'.format(instance.robot.model, instance.robot.version)
            message = f'Добрый день!\nНедавно вы интересовались нашим роботом модели {instance.robot.model}, версии {instance.robot.version}.\nЭтот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами.'
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [order.email])
            order.available = False
            order.save()


"""Нужно подключаться к SMTP среверу для отправки писем"""

"""Снизу пример для проверки работспособности сервиса отправки писем"""


def test_case_task3(request):
    robot = Robot.objects.get(id=1)
    customer = Customer(email='example@gmail.com', robot=robot, available=True)
    customer.save()
    return HttpResponse("Письмо отправлено")
