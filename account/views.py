from django.shortcuts import render


def login(request):
    return render(
        request,
        'account/login.html',
        {}
    )


def profile(request):
    return render(
        request,
        '',
        {}
    )


