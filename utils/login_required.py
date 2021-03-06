import jwt

from django.conf import settings
from django.http import JsonResponse

from users.models import User

SECRET_KEY = settings.SECRET_KEY
ALGORITHM  = settings.ALGORITHM


def login_required(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get("Authorization", None)
            payload      = jwt.decode(access_token, SECRET_KEY, algorithms=ALGORITHM)
            user         = User.objects.get(id=payload.get('id'))
            request.user = user

            return func(self, request, *args, **kwargs)

        except KeyError as e:
            return JsonResponse({'message':getattr(e,'message',str(e))}, status=401)
        except jwt.exceptions.DecodeError:
            return JsonResponse({'message':"InvalidToken"}, status=400)

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message':"WrongToken"}, status=400)

        except jwt.ExpiredSignatureError:
            return JsonResponse({'message':'TokenExpired'}, status=400)

        except User.DoesNotExist:
            return JsonResponse({'message':'UserDoesNotExist'}, status=400)

    return wrapper
