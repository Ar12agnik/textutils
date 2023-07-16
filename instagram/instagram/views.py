from django.http import HttpResponse
from django.shortcuts import render
import sql_data
def index(request,params=None):
    return render(request,'index.html',params)
def signup(request,params=None):
    return render(request,'signup.html',params)
def create_user(request):
    user_name=request.GET.get('username')
    password1=request.GET.get('password1')
    password2=request.GET.get('password2')

    if password1==password2:
        sql_data.write_data({'username':user_name,'password':password2})
        return render(request,'create_user.html')
    else:
        params={'problem':'Passwords do not match'}
        return signup(request,params)
def user_login(request):
    user_name=request.GET.get('username')
    password=request.GET.get('password')
    database_data=sql_data.read_data()
    found=False
    for data in database_data:
        if (data[0]==user_name) and (data[1]==password):
            found=True
            break
    if found:
        params={"name":user_name}
        return render(request,'user_login.html',params)
    else:
        params={"problem":"invalid credencials"}
        return index(request,params)

