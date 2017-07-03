from collections import Counter

from django.shortcuts import render
from django.http import JsonResponse

from .lib.cipher.caesar_cipher import CaesarCipher
from .lib.cipher.alphabet import Alphabet

from . import config


def index(request):
    return render(request, "caesar_cypher/index.html")


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


def break_cipher(request):
    text = request.GET['text']
    alphabet = Alphabet('a', 'z')
    caesar = CaesarCipher(config.allowed_alphabets)
    freqs = config.ENG_FREQS

    keys = {}

    # brut force with frequency letter frequency analysis
    for i in range(alphabet.length):
        shifted = caesar.encrypt(text.lower(), i)
        freq_sum = 0

        for letter in shifted:

            position = alphabet.get_character_position(letter)

            if position:
                freq_sum += freqs[position]

        key = (alphabet.length - i) % alphabet.length
        keys[key] = freq_sum

    possible_key = max(keys, key=keys.get)
    decrypted = caesar.decrypt(text, possible_key)

    return JsonResponse({
        "keys": keys,
        "key": possible_key,
        "decrypted": decrypted
    })