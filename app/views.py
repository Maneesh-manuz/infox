from django.http import request
from django.shortcuts import render



# Create your views here.
# def DEVindex(request):
#     return render(request,'DEVindex.html')
# def DEVprojects(request):
#     return render(request,'DEVprojects.html')
# def DEVtable(request):
#     return render(request,'DEVtable.html')
# def DEVtaskmain(request):
#     return render(request,'DEVtaskmain.html')   
# def DEVtaskform(request):
#     return render(request,'DEVtaskform.html')
# def DEVtask(request):
#     return render(request,'DEVtask.html')
# def DEVsuccess(request):
#     return render(request,'DEVsuccess.html')

def manager_index(request):
    return render(request,'manager_index.html')
def manager_upprojects(request):
    return render(request,'manager_upprojects.html')
def manager_newproject(request):
    return render(request,'manager_newproject.html')
def manager_description(request):
    return render(request,'manager_description.html')
def manager_table(request):
    return render(request,'manager_table.html')

