from django.shortcuts import render
from django.http import HttpResponse
from ginthusiasm.models import Review, Gin
from ginthusiasm.models import UserProfile
from django.contrib.auth.models import User
from ginthusiasm.forms import ReviewForm

def add_review(request, gin_name_slug):

    gin = Gin.objects.get(slug=gin_name_slug)
    #check = User.objects.get(username=user_name).userprofile
    check = request.user.userprofile


    print(gin)

    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            if gin:
                if check:
                    review = form.save(commit=False)
                    review.gin = gin
                    review.user = check
                    review.review_type = check.user_type
                    review.save()

    else:
        print(form.errors)



    return render(request, 'ginthusiasm/add_review_widget.html', {'form':form, 'gin':gin })
