from django.shortcuts import redirect,render
from core.models import Category, SubCategory, Vendor, Product, ProductImages, ProductReview, CartOrder, CartOrderItems, wishlist, Add
from core.forms import ProductReviewForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages
# Create your views here.
def index(request):
    products = Product.objects.all().order_by("-id")
    
    context = {
        "products":products
    }
    return render(request,'core/index.html', context)

def product_list_view(request):
    products = Product.objects.filter(product_status="published")
    
    context = {
        "products":products
    }
    return render(request,'core/product.html', context)

def product_category_list_view(request,sid):
    subcategory = SubCategory.objects.get(sid=sid)
    products = Product.objects.filter(product_status="published", subcategory=subcategory)
    
    context = {
        "subcategory":subcategory,
        "products":products
    }
    return render(request,'core/subcategory-product-list.html', context)

def product_detail_view(request,pid):
    product = Product.objects.get(pid=pid)
    p_image = product.p_images.all()
    products = Product.objects.filter(subcategory=product.subcategory).exclude(pid=pid)
    
    review = ProductReview.objects.filter(product=product).order_by("-date")
    review_form = ProductReviewForm()
    context = {
        "product":product,
        "p_image":p_image,
        "review_form":review_form,
        "review":review,
        "products":products,
    }
    return render(request,'core/product-detail.html', context)

def ajax_add_review(request,pid):
    product = Product.objects.get(pid=pid)
    user = request.user
    
    review= ProductReview.objects.create(
        user=user,
        product=product,
        review=request.POST['review'],
        rating=request.POST['rating'],
        
    )
    
    context={
        'user':user.username,
        'review':request.POST['review'],
        'rating':request.POST['rating'],
    }
    return JsonResponse(
        {'bool':True,
        'context':context}
    )
    
def search_view(request):
    query = request.GET.get("q")
    
    products = Product.objects.filter(title__icontains=query).order_by("-date")
    
    context = {
        "products":products,
        "query":query,
    }
    return render(request,'core/search.html', context)

def filter_product(request):
    subcategories = request.GET.getlist("subcategory[]")
    min_price= request.GET['min_price']
    max_price= request.GET['max_price']
    
    products=Product.objects.filter(product_status="published").order_by("-id").distinct()
    products = products.filter(price__gte=min_price)
    products = products.filter(price__lte=max_price)
    
    
    if len(subcategories)>0:
        products = products.filter(subcategory__id__in = subcategories).distinct()
        
    context = render_to_string("core/async/product-list.html",{"products":products})
    return JsonResponse({"context":context})
    
def about(request):
    return render(request,'core/about.html')


def add_to_cart(request):
    cart_product ={}

    cart_product[str(request.GET['id'])]={
        'title':request.GET['title'],
        'qty':request.GET['qty'],
        'price':request.GET['price'],
        'image':request.GET['image'],
        'pid':request.GET['pid'],
    }

    if 'cart_data_obj' in request.session:
        if str(request.GET['id']) in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['qty'] = int(cart_product[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cart_data_obj']=cart_data
            
        else:
            cart_data = request.session['cart_data_obj']
            cart_data.update(cart_product)
            request.session['cart_data_obj'] = cart_data
    else:
        request.session['cart_data_obj'] = cart_product 
    return JsonResponse({"data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj'])})       


def cart_view(request):
    cart_total_amount=0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            print("874784",item['qty'])
            print("874784555",item['price'])
            cart_total_amount += int(item['qty']) * float(item['price'])
        print("ssssssssssssssss",request.session['cart_data_obj'].items())    
        return render(request, "core/cart.html",{"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount':cart_total_amount})
    else:
        messages.warning(request,"your cart is empty!..")
        return redirect("core:index") 
     
def delete_item_from_cart(request):
    product_id = str(request.GET['id'])
    if 'cart_data_obj' in request.session:
        if product_id in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            del request.session['cart_data_obj'][product_id]
            request.session['cart_data_obj'] = cart_data
        cart_total_amount=0
        if 'cart_data_obj' in request.session:
            for p_id, item in request.session['cart_data_obj'].items():
                cart_total_amount += int(item['qty']) * float(item['price'])    

        context = render_to_string("core/async/cart-list.html",{"cart_data":request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj']), 'cart_total_amount':cart_total_amount})
        return JsonResponse({"data":context, 'totalcartitems': len(request.session['cart_data_obj'])})
def checkout(request):
    return render(request,'core/checkout.html')
