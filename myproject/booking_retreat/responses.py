from rest_framework import status
from django.http import JsonResponse


def send_200(data):
    return JsonResponse(data, status=status.HTTP_200_OK)


def send_201(data):
    return JsonResponse(data, status=status.HTTP_201_CREATED)


def send_400(data):
    return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)


def send_404(data):
    return JsonResponse(data, status=status.HTTP_404_NOT_FOUND)
