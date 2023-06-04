import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import openai

openai.api_key = "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"

messages = []

@csrf_exempt
def chat_service(request):
    if request.method == 'POST':
        input1 = request.POST['input1']
        messages.append({"role": "user", "content": input1})

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        response = completion['choices'][0]['message']['content'].strip()

        messages.append({"role": "user", "content": response})

        output = {
            "response": response
        }
        return HttpResponse(json.dumps(output), status=200)
    else:
        return render(request, 'addresses/chat_test.html')