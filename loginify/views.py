from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import UserDetails
from django.contrib import messages
from .serializers import UserSerializer
import json



from django.views.decorators.csrf import csrf_exempt

def hello_world(request):
    return HttpResponse("Hello, World!")

def print_hello_template(request):
    return render(request, 'loginify/home.html')


# Signup View
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the email already exists
        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('signup')

        # Save the user
        user = UserDetails(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Signup successful! Please log in.")
        return redirect('login')

    return render(request, 'loginify/signup.html')

# Login View
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user
        user = UserDetails.objects.filter(email=email, password=password).first()
        if user:
            messages.success(request, f"Welcome, {user.username}!")
            return render(request, 'loginify/success.html', {'username': user.username})
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login')

    return render(request, 'loginify/login.html')




@csrf_exempt
def all_data(request):
    if request.method =="GET" :
        try:
            
            all_data = UserDetails.objects.all()
            serializer_data=UserSerializer(all_data, many=True)
            return JsonResponse(serializer_data.data,safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)},status=500)
        
    if request.method == "POST":
        try:
            input_data=json.loads(request.body) #from frontend side / client side
            serializer_data=UserSerializer(data=input_data) #converted data
            if serializer_data.is_valid(): #validation
                serializer_data.save()
                return JsonResponse({"message":"Data saved successfully"},status=201)
            else:
                return JsonResponse(serializer_data.errors,status=400)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
@csrf_exempt
def single_user_data(request,pk):
    if request.method == "GET":
        try:
            user_data=UserDetails.objects.get(pk=pk) #get single object
            serializer_data=UserSerializer(user_data) #serialized data
            return JsonResponse({
                "data":serializer_data.data
            },status=200)
        except UserDetails.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
    
    if request.method == "PUT":
        try:
            input_data=json.loads(request.body)
            user=UserDetails.objects.get(pk=pk)

            serializer_data=UserSerializer(user,data=input_data)
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({"message":"Data updated successfully"},status=200)
            else:
                return JsonResponse(serializer_data.errors,status=400)
        except UserDetails.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
        
    if request.method == "DELETE":
        try:
            user=UserDetails.objects.get(pk=pk)
            user.delete()
            return JsonResponse({"message":"Data deleted successfully"},status=204)
        except UserDetails.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
        
    if request.method == "PATCH":
        try:
            input_data=json.loads(request.body)
            user=UserDetails.objects.get(pk=pk)

            serializer_data=UserSerializer(user,data=input_data,partial=True) #partial update
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({"message":"Data updated successfully"},status=200)
            else:
                return JsonResponse(serializer_data.errors,status=400)
        except UserDetails.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
        
          