from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Robot
from django.core.exceptions import ValidationError
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class RobotView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            model = data.get('model')
            version = data.get('version')
            created = data.get('created')

            Robot(serial=model + '-' + version, model=model, version=version, created=created).full_clean()
            Robot(serial=model + '-' + version, model=model, version=version, created=created).save()

            return JsonResponse({'success': True}, status=201)

        except ValueError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        except ValidationError as e:
            return JsonResponse({'error': e.message_dict}, status=400)


