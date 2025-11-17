from django.shortcuts import render
from django.http import JsonResponse

def display_landing(request):
    return render(request,"index.html") 

tiger={
    'name':'bengal tiger',
    'image': 'https://upload.wikimedia.org/wikipedia/commons/5/56/Tiger.50.jpg',

    'age':20, 
    'food':'pizza', 
    'donate':'abc',
    'caretaker':'RT'

}
lion={
    'name':'lion',
    'image': 'https://upload.wikimedia.org/wikipedia/commons/5/56/Tiger.50.jpg',

    'age':27, 
    'food':'meate', 
    'caretaker':'RL'  ,  'donate':'abc2'


}
swan={
    'name':'swan',
    'image': 'https://upload.wikimedia.org/wikipedia/commons/5/56/Tiger.50.jpg',

    'age':30, 
    'food':'leaf', 
    'caretaker':'RS'   , 'donate':'abc2'


}
gorilla={
    'name':'lion',
    'image': 'https://upload.wikimedia.org/wikipedia/commons/5/56/Tiger.50.jpg',

    'age':55, 
    'food':'banana', 
    'caretaker':'RG'    , 'donate':'abc3'


}
jaguar={
    'name':'jaguar',
    'image': 'https://upload.wikimedia.org/wikipedia/commons/5/56/Tiger.50.jpg',
    'donate':'abc5',

    'age':20, 
    'food':'rabbit', 
    'caretaker':'RJ'

}
def tiger_display(request):
    return render(request,"animal.html",context=tiger)

def lion_display(request):
    return render(request,"animal.html",context=lion)

def jaguar_display(request):
    return render(request,"animal.html",context=jaguar)

def swan_display(request):
    return render(request,"animal.html",context=swan)

def gorilla_display(request):
    return render(request,"animal.html",context=gorilla)

 
def animal_data(request):
    animals=[{
    'name':'jaguar',
    'image': 'https://upload.wikimedia.org/wikipedia/commons/5/56/Tiger.50.jpg',
    'donate':'abc5',

    'age':20, 
    'food':'rabbit', 
    'caretaker':'RJ'

},{
    'name':'lion',
    'image': 'https://upload.wikimedia.org/wikipedia/commons/5/56/Tiger.50.jpg',

    'age':55, 
    'food':'banana', 
    'caretaker':'RG'    , 'donate':'abc3'


},{
    'name':'swan',
    'image': 'https://upload.wikimedia.org/wikipedia/commons/5/56/Tiger.50.jpg',

    'age':30, 
    'food':'leaf', 
    'caretaker':'RS'   , 'donate':'abc2'


},{
    'name':'lion',
    'image': 'https://upload.wikimedia.org/wikipedia/commons/5/56/Tiger.50.jpg',

    'age':27, 
    'food':'meate', 
    'caretaker':'RL'  ,  'donate':'abc2'


},{
    'name':'bengal tiger',
    'image': 'https://upload.wikimedia.org/wikipedia/commons/5/56/Tiger.50.jpg',

    'age':20, 
    'food':'pizza', 
    'donate':'abc',
    'caretaker':'RT'

}

    ]
    return JsonResponse({'status':200,'data':animals})

def login(request):
    email_value=request.GET.get('email')
    password_value=request.GET.get('password')
    print(email_value)
    print(password_value)

    return JsonResponse({'email':email_value, 
                         'password':password_value})


def admin_login(request):
    email_value=request.GET.get('email')
    password_value=request.GET.get('password')
    if email_value=='admin@gmail.com'  and password_value=='admin1234' :
        return JsonResponse({
            'login':'login success'
        })
    else:
        return JsonResponse({
        'login':'login success'})
def book_ticket(request):
    email_value=request.GET.get('email')
    name_value=request.GET.get('name')  
    number_of_people=request.GET.get('number')

    return JsonResponse({
        'email':email_value,
        'name':name_value,
        'number':number_of_people
    })