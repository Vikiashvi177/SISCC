from django.shortcuts import render
from .models import crudst
from django.contrib import messages
from .forms import stform
from django.http import JsonResponse

def home(request):
    return render(request,"home.html")

def location(request):
    return render(request,"location.html")

def usertable(request):
    results = crudst.objects.all()
    return render(request,"usertable.html",{"crudst":results})

def locationtable(request):
    results = crudst.objects.all()
    return render(request,"locationtable.html",{"crudst":results})

def stinsert(request):
    if request.method == "POST":
        if request.POST.get('stname') and request.POST.get('stemail') and request.POST.get('staddress') and request.POST.get('stmobile') and request.POST.get('stgender'):
            savest = crudst()
            savest.stname = request.POST.get('stname')
            savest.stemail = request.POST.get('stemail')
            savest.staddress = request.POST.get('staddress')
            savest.stmobile = request.POST.get('stmobile')
            savest.stgender = request.POST.get('stgender')
            savest.ststart = request.POST.get('ststart')
            savest.stend = request.POST.get('stend')
            savest.stbank = request.POST.get('stbank')
            savest.staadhar = request.POST.get('staadhar')
            savest.strfid = request.POST.get('strfid')
            savest.save()
            messages.success(request,"The Record "+savest.stname+" Is Saved Successfully..!")
            return render(request,"Create.html")
    else:
        return render(request,"Create.html")
    
def stedit(request,id):
    getuserdetails = crudst.objects.get(id=id)
    return render(request,'edit.html',{"crudst":getuserdetails})

def stupdate(request,id):
    stupdate = crudst.objects.get(id=id)
    form = stform(request.POST,instance=stupdate)
    if form.is_valid():
        form.save()
        messages.success(request,"The User Record is Updated Successfully..!")
        return render(request,"edit.html",{"crudst":stupdate})
    
def stdel(request,id):
    delstudent = crudst.objects.get(id=id)
    delstudent.delete()
    results = crudst.objects.all()
    return render(request,"home.html",{"crudst":results})

from django.shortcuts import render
from .models import crudst, RFIDInfo
from django.contrib import messages
from .forms import stform, RFIDInfoForm
from django.http import JsonResponse


def check_rfid(request):
    rfid = request.GET.get('rfid')
    nearest_stop = request.GET.get('nearestStop', None)  # Get the nearest stop from the request

    # Query the database to check if the RFID exists
    try:
        user = crudst.objects.get(strfid=rfid)

        if user.ststart == 'N/A' and user.stend == 'N/A':
            if nearest_stop:
                user.ststart = nearest_stop
            user.stend = 'N/A'
            user.save()
        elif user.ststart != 'N/A' and user.stend == 'N/A':
            if nearest_stop:
                user.stend = nearest_stop
                user.save()

                # Create a new RFIDInfo entry when the end location changes from 'N/A' to a detected location
                rfid_info = RFIDInfo(rfid=rfid, start_location=user.ststart, end_location=nearest_stop, price=calculate_price(user.ststart, nearest_stop), route=102, time=None)
                rfid_info.save()

                # Change the start and end locations to 'N/A'
                user.ststart = 'N/A'
                user.stend = 'N/A'
                user.save()

        return JsonResponse({'message': 'RFID found and locations updated'})
    except crudst.DoesNotExist:
        return JsonResponse({'message': 'RFID not found in the database'})

def calculate_price(start_location, end_location):
    route = {
        "102": ['Broadway', 'R.B.I. Parrys', 'Secretariat', 'Island Ground', 'Anna Square', 'Marina Beach', 'Kannagi Statue', 'Queen Marys College', 'Light House (All India Radio)', 'Employment Office (Santhome)', 'Foreshore Estate', 'M.R.C. Nagar', 'Iyappan Koil', 'Music College', 'Andhra Mahila Sabha Hospital (Sathya Studios)', 'Adyar Signal', 'Adyar O.T.', 'Adyar Depot', 'Indira Nagar Water Tank', 'Jayanthi Theatre', 'S.R.P. Tools', 'I.G.P.', 'Kandanchavadi', 'Perungudi', 'Seevaram', 'Jain College', 'Rattha Tech Tower', 'Okkiyampet', 'T.C.S.', 'Karapakkam', 'Accenture', 'Sholinganallur', 'Satyabhama Dental College and Hospital', 'Semmancheri', 'Navallur', 'Siruseri (Muttukadu)', 'S.I.P.C.O.T. (Muttukadu)', 'Vaniyanchavadi Padma Adarsh School', 'Kazhipattur', 'Hindustan College', 'Chettinad Hospital', 'Padur', 'Vandalur Road Junction', 'Kelambakkam'],
    }
    
    # Get the index values of start and end locations
    start_index = route["102"].index(start_location)
    end_index = route["102"].index(end_location)
    
    # Calculate the price based on the index difference
    price = abs(end_index - start_index) * 10  # You can adjust the price calculation as needed
    
    return price

    

def view_rfid_info(request):
    rfid_info_list = RFIDInfo.objects.all()
    return render(request, 'rfidinfo.html', {'rfid_info_list': rfid_info_list})


from django.shortcuts import render
from django.http import JsonResponse
from .models import RFIDInfo

def get_data(request):
    rfid_info = None
    rfid = None  # Initialize rfid as None
    total_amount = 0  # Initialize total_amount as 0

    if request.method == "POST":
        rfid = request.POST.get('rfid')
        rfid_info = RFIDInfo.objects.filter(rfid=rfid).order_by('time')
        
        # Calculate the total amount
        total_amount = sum(info.price for info in rfid_info)

    return render(request, 'getdata.html', {'rfid_info': rfid_info, 'searched_rfid': rfid, 'total_amount': total_amount})