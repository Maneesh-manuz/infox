from django.shortcuts import redirect


def manager_index(request):
    return redirect('/app/')