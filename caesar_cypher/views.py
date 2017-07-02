from django.shortcuts import render
from django.http import JsonResponse

from .lib.cipher.caesar_cipher import CaesarCipher

from . import config

def index(request):
    return render(request, "cesar_cypher/index.html")


def encrypt(request):
    original_text = request.GET.get('original_text', None)
    rotation = int(request.GET.get('rotation', 0))

    if original_text:
        caesar = CaesarCipher(config.allowed_alphabets)
        encrypted = caesar.encrypt(original_text, rotation)
        return JsonResponse({'encrypted': encrypted})


def decrypt(request):
    encrypted_text = request.GET.get('encrypted_text', None)
    rotation = int(request.GET.get('rotation', 0))

    if encrypted_text:
        caesar = CaesarCipher(config.allowed_alphabets)
        decrypted = caesar.decrypt(encrypted_text, rotation)
        return JsonResponse({'decrypted': decrypted})


def guess(request):
    pass