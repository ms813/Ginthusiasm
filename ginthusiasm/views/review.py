from django.shortcuts import render
from ginthusiasm.models import Gin
from ginthusiasm.forms import ReviewForm

"""
This view file handles creation of new Reviews by a User about a Gin
"""
def add_review(request, gin_name_slug):

    gin = Gin.objects.get(slug=gin_name_slug)
    check = request.user.userprofile

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
            # bad form data
            print(form.errors)

    return render(request, 'ginthusiasm/add_review_widget.html', {'form':form, 'gin':gin })
