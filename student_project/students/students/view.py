from django.shortcuts import render
from django.http import JsonResponse
import requests

api_key = "AIzaSyDVrhFbMMT-gJGFiqIPv9pOq6VZKhU8CcA"

def chatbot(request):
    query = request.GET.get('query', '')

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": (
                            "I want you to act as an interviewer for Django and HTML. "
                            "Keep it engaging, ask interactive questions, and focus on the most asked questions in 2024. "
                            + query
                        )
                    }
                ]
            }
        ]
    }

    params = {"key": api_key}
    print("RAW RESPONSE:", data)


    try:
        result = requests.post(
            "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent",
            params=params,
            json=payload
        )

        data = result.json()
        print("RAW RESPONSE:", data)  # 🔥 IMPORTANT DEBUGGING LINE

        # ------- SAFE EXTRACTION -------
        candidates = data.get("candidates")
        if not candidates:
            return JsonResponse({'result': "Error: No candidates returned."})

        content = candidates[0].get("content", {})
        parts = content.get("parts")

        if not parts or not isinstance(parts, list):
            return JsonResponse({'result': "Error: No text content returned."})

        text = parts[0].get("text", "Error: No text in response.")

        # --------------------------------

        return JsonResponse({'result': text})

    except Exception as e:
        print("ERROR:", str(e))
        return render(request,'chatbot.html')
       # return JsonResponse({'result': "Error: " + str(e)})
  
def display_landing(request):
    return render(request,"index.html") 

student=[]
proffesor=[]
facility=[]

def render_chatbot(request):
   return render(request,'chatbot.html')

def add_student(request):
   name=request.GET.get('name')
   
   if name is None:
    return JsonResponse({

    })
   else:
      student.append(name)
      return JsonResponse({'message':'student added'})


def view_student(request):
    return JsonResponse(student,safe=False)

def add_proff(request):
   name=request.GET.get('name')
   proffesor.append(name)
   return JsonResponse({
        'name':name,
    })


def view_proff(request):
    return JsonResponse(proffesor,safe=False)

def add_facility(request):
   name=request.GET.get('name')
   facility.append(name)
   return JsonResponse({
        'name':name,
    })


def view_facility(request):
    return JsonResponse(facility,safe=False)



