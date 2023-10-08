from django.shortcuts import render, redirect, reverse, get_object_or_404
import os
from django.contrib import messages
from .forms import ProductForm, CategoryForm, BrandForm
from django.contrib.auth.decorators import login_required
from products.models import Product, Category, Brand
from profiles.models import UserProfile



@login_required
def custom_admin(request):
    """A view to render the custom admin page"""
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can enter this page')
        return redirect(reverse('home'))


    return render(request, 'custom_admin/custom_admin.html')


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can add products')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
        
    else:
        form = ProductForm()

    template = 'products/add_product.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can edit products')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
        
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'

    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can delete products')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')

    return redirect(reverse('products'))


@login_required
def add_category(request):
    """ Add a category to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can add categories')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added category!')
            return redirect(reverse('custom_admin'))
        else:
            messages.error(request, 'Failed to add category. Please ensure the form is valid.')
        
    else:
        form = CategoryForm()

    template = 'categories/add_category.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_category(request, category_id):
    """ Edit a category in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can edit categories')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=category_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated category!')
            return redirect(reverse('custom_admin'))
        else:
            messages.error(request, 'Failed to update category. Please ensure the form is valid.')
        
    else:
        form = CategoryForm(instance=category)
        messages.info(request, f'You are editing {category.name}')

    template = 'categories/edit_category.html'

    context = {
        'form': form,
        'category': category,
    }

    return render(request, template, context)


@login_required
def delete_category(request, category_id):
    """ Delete a category from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can delete categories')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    messages.success(request, 'Category deleted!')

    return redirect(reverse('custom_admin'))


@login_required
def add_brand(request):
    """ Add a brand to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can add brands')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added brand!')
            return redirect(reverse('custom_admin'))
        else:
            messages.error(request, 'Failed to add brand. Please ensure the form is valid.')
        
    else:
        form = BrandForm()

    template = 'brands/add_brand.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_brand(request, brand_id):
    """ Edit a brand in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can edit brands')
        return redirect(reverse('home'))

    brand = get_object_or_404(Brand, pk=brand_id)

    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated brand!')
            return redirect(reverse('custom_admin'))
        else:
            messages.error(request, 'Failed to update brand. Please ensure the form is valid.')
        
    else:
        form = BrandForm(instance=brand)
        messages.info(request, f'You are editing {brand.name}')

    template = 'brands/edit_brand.html'

    context = {
        'form': form,
        'brand': brand,
    }

    return render(request, template, context)


@login_required
def delete_brand(request, brand_id):
    """ Delete a brand from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can delete categories')
        return redirect(reverse('home'))

    brand = get_object_or_404(Brand, pk=brand_id)
    brand.delete()
    messages.success(request, 'Brand deleted!')

    return redirect(reverse('custom_admin'))

