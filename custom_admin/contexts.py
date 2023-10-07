from products.models import Brand, Category, Product


def all_model_objects(request):

    all_products = Product.objects.all()

    all_brands = Brand.objects.all()
    all_real_brands = all_brands.filter(universe='real')
    all_digital_brands = all_brands.filter(universe='digital')

    all_categories = Category.objects.all()
    all_real_categories = all_categories.filter(universe='real')
    all_digital_categories = all_categories.filter(universe='digital')

    context = {
        'all_products': all_products,
        'all_brands': all_brands,
        'all_real_brands': all_real_brands,
        'all_digital_brands': all_digital_brands,
        'all_categories': all_categories,
        'all_real_categories': all_real_categories,
        'all_digital_categories': all_digital_categories,
    }

    return context