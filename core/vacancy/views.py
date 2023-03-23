from django.shortcuts import render


def main(request):
    return render(request, 'vacancy/main.html')


def vacancies(request):
    return render(request, 'vacancy/vacancies.html')
