from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ApiSerializerClass
from home.utils import to_english, to_morse_code

# Create your views here.

@api_view(['GET'])
def api_translator(request):
    data = request.GET.dict()
    serializer = ApiSerializerClass(data=data)
    if serializer.is_valid(raise_exception=True):
        text = data["text"]
        if data["translate"] == "morse":
            result = to_morse_code(text)
        else:
            result = to_english(text)

        response_data = {"translate": data["translate"], "text":text, "translation":result}

        return Response(response_data)