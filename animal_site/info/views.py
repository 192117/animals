from django.shortcuts import render
from .models import Answers, Questions, SocialMedia, PriceList, Info


def faq_page(request):
    info = Info.objects.get(pk=1)
    social = SocialMedia.objects.get(pk=1)
    price = PriceList.objects.get(pk=1)
    answers = Answers.objects.all()
    questions = Questions.objects.all()
    return render(request, 'info/faq.html', context={'answers': answers, 'questions': questions,
                                                     'info': info, 'social': social, 'price': price})
