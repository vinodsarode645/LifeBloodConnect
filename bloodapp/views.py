from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from bloodapp.models import DonorRegistration, BloodRequest, BloodDonationCenter

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def login_view(request):
    # Handle user login
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to a dashboard page after login
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def signup(request):
    # Handle user signup
    if request.method == 'POST':
        # Process the signup form
        form = UserCreationForm(request.POST)
        #validate and save the new user
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required(login_url='signup')
def dashboard(request):
    # Protected dashboard view with dynamic data
    stats = {
        'total_donations': DonorRegistration.objects.filter(status='approved').count(),
        'blood_requests': BloodRequest.objects.filter(status='pending').count(),
    }
    centers = BloodDonationCenter.objects.all()
    return render(request, 'dashboard.html', {'stats': stats, 'centers': centers})


@csrf_exempt
@require_http_methods(["POST"])
def register_donor(request):
    """
    API endpoint to handle donor registration form submission
    """
    try:
        # Parse the incoming JSON data
        data = json.loads(request.body)
        
        # Check if donor with same Aadhar already exists
        if DonorRegistration.objects.filter(aadhar=data.get('aadhar')).exists():
            return JsonResponse({
                'success': False,
                'message': 'A donor with this Aadhar number is already registered.'
            }, status=400)
        
        # Create new donor registration
        donor = DonorRegistration(
            aadhar=data.get('aadhar'),
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            gender=data.get('gender'),
            dob=data.get('dob'),
            blood_group=data.get('bloodGroup'),
            weight=int(data.get('weight', 0)),
            height=int(data.get('height', 0)) if data.get('height') else None,
            last_donation=data.get('lastDonation') if data.get('lastDonation') else None,
            no_disease=data.get('noDisease', False) == 'on' or data.get('noDisease') == True,
            no_medication=data.get('noMedication', False) == 'on' or data.get('noMedication') == True,
            address=data.get('address'),
            city=data.get('city'),
            state=data.get('state'),
            pincode=data.get('pincode'),
            country=data.get('country', 'India'),
            additional_info=data.get('additionalInfo', ''),
            status='pending'
        )
        
        # Save the donor to the database
        donor.save()
        
        return JsonResponse({
            'success': True,
            'message': 'Registration submitted successfully! We will contact you shortly with appointment details.',
            'donor_id': donor.id
        }, status=201)
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error processing registration: {str(e)}'
        }, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def request_blood(request):
    """
    API endpoint to handle blood request form submission
    """
    try:
        # Parse the incoming JSON data
        data = json.loads(request.body)
        
        # Create new blood request
        blood_req = BloodRequest(
            name=data.get('name'),
            contact_no=data.get('contactNo'),
            address=data.get('address'),
            blood_group=data.get('bloodGroup'),
            units_required=int(data.get('unitsRequired', 0)),
            status='pending'
        )
        
        # Save to the database
        blood_req.save()
        
        return JsonResponse({
            'success': True,
            'message': 'Blood request submitted successfully! We will find donors and contact you shortly.',
            'request_id': blood_req.id
        }, status=201)
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error processing request: {str(e)}'
        }, status=500)