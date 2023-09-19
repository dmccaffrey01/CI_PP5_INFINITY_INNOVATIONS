from .models import Brand, Category


def all_brands_categories(request):

    all_brands = Brand.objects.all()
    all_real_brands = all_brands.filter(universe='real')
    all_digital_brands = all_brands.filter(universe='digital')

    all_categories = Category.objects.all()
    all_real_categories = all_categories.filter(universe='real')
    all_digital_categories = all_categories.filter(universe='digital')

    context = {
        'all_brands': all_brands,
        'all_real_brands': all_real_brands,
        'all_digital_brands': all_digital_brands,
        'all_categories': all_categories,
        'all_real_categories': all_real_categories,
        'all_digital_categories': all_digital_categories,
    }

    return context