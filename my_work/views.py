from django.shortcuts import render


def start_page(request):
    context = {
        'title': 'Стартовая',
    }
    return render(request, 'index.html', context=context)


def work_page(requests):
    return render(requests, 'work_page.html')
