from django.shortcuts import render


def start(request):
    user_id = request.GET.get('user_id')
    print(user_id)
    return render(
        request,
        'profile.html',
        context={'user_id': user_id}
    )
