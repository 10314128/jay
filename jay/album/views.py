from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from album.models import Category, Page
from album.forms import CategoryForm, PageForm

def album(request):
    categories = Category.objects.order_by('-likes')
    context = {'categories':categories}
    return render(request, 'album/album.html',context)

def category(request, categoryName):
    context = {}
    try:
        category = Category.objects.get(name=categoryName)
        context['category'] = category
        context['pages'] = Page.objects.filter(category=category)
    except Category.DoesNotExist:
        pass
    return render(request, 'album/category.html', context)

def addCategory(request):
    template = 'album/addCategory.html'
    if request.method=='GET':
        return render(request, template, {'form':CategoryForm()})
    # request.method=='POST'
    form = CategoryForm(request.POST)
    if not form.is_valid():
        return render(request, template, {'form':form})
    form.save()
    return redirect(reverse('album:album'))
    # Or try this: return album(request)

def addPage(request, categoryName):
    template = 'album/addPage.html'
    try:
        pageCategory = Category.objects.get(name=categoryName)
    except Category.DoesNotExist:
        return category(request, categoryName)
    context = {'category':pageCategory}
    if request.method=='GET':
        context['form'] = PageForm()
        return render(request, template, context)
    # request.method=='POST'
    form = PageForm(request.POST)
    context['form'] = form
    if not form.is_valid():
        return render(request, template, context)
    page = form.save(commit=False)
    page.category = pageCategory
    page.save()
    return redirect(reverse('album:category', args=(categoryName, )))

def deleteCategory(request, categoryID):
    if request.method!='POST':
        return album(request)
    # request.method=='POST':
    categoryToDelete = Category.objects.get(id=categoryID)
    if categoryToDelete:
        categoryToDelete.delete()
    return redirect(reverse('album:album'))
    
