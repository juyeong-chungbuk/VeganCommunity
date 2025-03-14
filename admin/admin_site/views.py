from django.db.models import Q
from django.shortcuts import render, redirect
from .models import User, Vegan_Store, Store_Review, User_Custom_Store, \
                    Food, Food_Review, Market_Goods,Goods_Comment
from .forms import UserForm, ReviewForm, VeganStoreForm, CustomStoreForm, \
                    FoodReviewForm, FoodForm, CommentForm, GoodForm

def main(request):
    return render(request, 'admin_site/main.html')

def user_list(request):
    list = User.objects.all()
    search_type = request.GET.get('search_type')
    search_key = request.GET.get('search_key')
    
    if search_key:
        if search_type == 'authority':
            list = list.filter(authority__icontains=search_key)
        elif search_type == 'id':
            list = list.filter(user_id__icontains=search_key)
        elif search_type == 'name':
            list = list.filter(name__icontains=search_key)
        elif search_type == 'vegan_step':
            list = list.filter(vegan_step__icontains=search_key)

    context = {
        'list': list,
    }

    return render(request, 'admin_site/user_list.html', context)

def user_detail(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user,
    }
    return render(request, 'admin_site/user_detail.html', context)

def user_delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('user_list')

def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
        return redirect('user_detail', user.id)
    else:
        form = UserForm()
    
    return render(request, 'admin_site/user_new.html', {'form': form})

def user_update(request, id):
    user = User.objects.get(id=id)

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', user.id)
    else:
        form = UserForm(instance=user)

    return render(request, 'admin_site/user_update.html', {'user':user, 'form':form})

def vegan_store_list(request):
    list = Vegan_Store.objects.all()
    search_type = request.GET.get('search_type')
    search_key = request.GET.get('search_key')

    if search_key:
        if search_type == 'name':
            list = list.filter(name__icontains=search_key)
        elif search_type == 'vegan_step':
            list = list.filter(vegan_step__icontains=search_key)
        elif search_type == 'address':
            list = list.filter(address__icontains=search_key)
        elif search_type == 'field':
            list = list.filter(field__icontains=search_key)
    context = {
        'list': list,
    }
    return render(request, 'admin_site/vegan_store_list.html', context)

def vegan_store_detail(request, id):
    store = Vegan_Store.objects.get(id=id)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            reviews = review_form.save()
    
    review_form = ReviewForm()
    reviews = store.reviews.all()

    return render(request, 'admin_site/vegan_store_detail.html', {
        'store': store, 'review_form': review_form, 'reviews': reviews,
    })

def review_create(request, id):
    store = Vegan_Store.objects.get(id=id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.store_id = id
            review.save()
            return redirect('vegan_store_detail', id)
    else:
        form = ReviewForm()
    context = {'form': form, 'id': id, 'store': store}
    return render(request, 'admin_site/review_create.html', context)

def review_list(request):
    list = Store_Review.objects.all()
    search_type = request.GET.get('search_type')
    search_key = request.GET.get('search_key')

    if search_key:
        if search_type == 'store':
            list = list.filter(store__icontains=search_key)
        elif search_type == 'star':
            list = list.filter(star__icontains=search_key)
    context = {
        'list': list,
    }
    return render(request, 'admin_site/review_list.html', context)

def vegan_store_delete(request, id):
    store = Vegan_Store.objects.get(id=id)
    store.delete()
    return redirect('vegan_store_list')

def vegan_store_new(request):
    if request.method == "POST":
        form = VeganStoreForm(request.POST)
        if form.is_valid():
            store = form.save()
        return redirect('vegan_store_detail', store.id)
    else:
        form = VeganStoreForm()
    
    return render(request, 'admin_site/vegan_store_new.html', {'form': form})

def vegan_store_update(request, id):
    store = Vegan_Store.objects.get(id=id)

    if request.method == "POST":
        form = VeganStoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('vegan_store_detail', store.id)
    else:
        form = VeganStoreForm(instance=store)

    return render(request, 'admin_site/vegan_store_update.html', {'store':store, 'form':form})

def custom_store_list(request):
    list = User_Custom_Store.objects.all()
    search_type = request.GET.get('search_type')
    search_key = request.GET.get('search_key')

    if search_key:
        if search_type == 'name':
            list = list.filter(name__icontains=search_key)
        elif search_type == 'vegan_step':
            list = list.filter(vegan_step__icontains=search_key)
        elif search_type == 'address':
            list = list.filter(address__icontains=search_key)
        elif search_type == 'field':
            list = list.filter(field__icontains=search_key)
    context = {
        'list': list,
    }
    return render(request, 'admin_site/custom_store_list.html', context)

def custom_store_detail(request, id):
    store = User_Custom_Store.objects.get(id=id)
    context = {
        'store': store,
    }
    return render(request, 'admin_site/custom_store_detail.html', context)

def custom_store_delete(request, id):
    store = User_Custom_Store.objects.get(id=id)
    store.delete()
    return redirect('custom_store_list')

def custom_store_new(request):
    if request.method == "POST":
        form = CustomStoreForm(request.POST)
        if form.is_valid():
            store = form.save()
        return redirect('custom_store_detail', store.id)
    else:
        form = CustomStoreForm()
    
    return render(request, 'admin_site/custom_store_new.html', {'form': form})

def custom_store_update(request, id):
    store = User_Custom_Store.objects.get(id=id)

    if request.method == "POST":
        form = CustomStoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('custom_store_detail', store.id)
    else:
        form = CustomStoreForm(instance=store)

    return render(request, 'admin_site/custom_store_update.html', {'store':store, 'form':form})

def food_list(request):
    list = Food.objects.all()
    search_type = request.GET.get('search_type')
    search_key = request.GET.get('search_key')

    if search_key:
        if search_type == 'name':
            list = list.filter(name__icontains=search_key)
        elif search_type == 'all_nutrition':
            list = list.filter(all_nutrition__icontains=search_key)
        elif search_type == 'allegy_nutrition':
            list = list.filter(allegy_nutrition__icontains=search_key)
        elif search_type == 'Feature':
            list = list.filter(Feature__icontains=search_key)
    context = {
        'list': list,
    }
    return render(request, 'admin_site/food_list.html', context)

def food_detail(request, id):
    food = Food.objects.get(id=id)
    if request.method == "POST":
        review_form = FoodReviewForm(request.POST)
        if review_form.is_valid():
            reviews = review_form.save()
    
    review_form = FoodReviewForm()
    reviews = food.review.all()

    return render(request, 'admin_site/food_detail.html', {
        'food': food, 'review_form': review_form, 'reviews': reviews,
    })

def food_review_create(request, id):
    food = Food.objects.get(id=id)
    if request.method == "POST":
        form = FoodReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.food_id = id
            review.save()
            return redirect('food_detail', id)
    else:
        form = FoodReviewForm()
    context = {'form': form, 'id': id, 'food': food}
    return render(request, 'admin_site/food_review_create.html', context)

def food_review_list(request):
    list = Food_Review.objects.all()
    search_type = request.GET.get('search_type')
    search_key = request.GET.get('search_key')

    if search_key:
        if search_type == 'food':
            list = list.filter(food__icontains=search_key)
        elif search_type == 'star':
            list = list.filter(star__icontains=search_key)
    context = {
        'list': list,
    }
    return render(request, 'admin_site/food_review_list.html', context)

def food_delete(request, id):
    food = Food.objects.get(id=id)
    food.delete()
    return redirect('food_list')

def food_new(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save()
        return redirect('food_detail', food.id)
    else:
        form = FoodForm()
    
    return render(request, 'admin_site/food_new.html', {'form': form})

def food_update(request, id):
    food = Food.objects.get(id=id)

    if request.method == "POST":
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_detail', food.id)
    else:
        form = FoodForm(instance=food)

    return render(request, 'admin_site/food_update.html', {'food':food, 'form':form})

def good_list(request):
    list = Market_Goods.objects.all()
    search_type = request.GET.get('search_type')
    search_key = request.GET.get('search_key')

    if search_key:
        if search_type == 'user_name':
            list = list.filter(user_name__icontains=search_key)
        elif search_type == 'food_name':
            list = list.filter(food_name__icontains=search_key)
        elif search_type == 'feature':
            list = list.filter(feature__icontains=search_key)
    context = {
        'list': list,
    }
    return render(request, 'admin_site/goods_list.html', context)

def good_detail(request, id):
    good = Market_Goods.objects.get(id=id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comments = comment_form.save()
    
    comment_form = CommentForm()
    comments = good.comment.all()

    return render(request, 'admin_site/goods_detail.html', {
        'good': good, 'comment_form': comment_form, 'comments': comments,
    })

def comment_create(request, id):
    good = Market_Goods.objects.get(id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.goods_id = id
            comment.save()
            return redirect('good_detail', id)
    else:
        form = CommentForm()
    context = {'form': form, 'id': id, 'good': good}
    return render(request, 'admin_site/comment_create.html', context)

def comment_list(request):
    list = Goods_Comment.objects.all()
    search_key = request.GET.get('search_key')

    if search_key:
        list = list.filter(goods__icontains=search_key)
    context = {
        'list': list,
    }
    return render(request, 'admin_site/comment_list.html', context)

def good_delete(request, id):
    good = Market_Goods.objects.get(id=id)
    good.delete()
    return redirect('good_list')

def good_new(request):
    if request.method == "GET":
        form = GoodForm()
    else:
        form = GoodForm(request.POST, request.FILES)
        if form.is_valid():
            good = form.save()
        return redirect('good_detail', good.id)
            
    return render(request, 'admin_site/goods_new.html', {'form': form})

def good_update(request, id):
    good = Market_Goods.objects.get(id=id)

    if request.method == "POST":
        form = GoodForm(request.POST, instance=good)
        if form.is_valid():
            form.save()
            return redirect('good_detail', good.id)
    else:
        form = GoodForm(instance=good)

    return render(request, 'admin_site/goods_update.html', {'good':good, 'form':form})