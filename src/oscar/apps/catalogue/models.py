"""
Vanilla product models
"""
from oscar.apps.catalogue.abstract_models import *  # noqa
from oscar.core.loading import is_model_registered
from django.utils.functional import cached_property
__all__ = ['ProductAttributesContainer']


if not is_model_registered('catalogue', 'ProductClass'):
    @cached_property
    class ProductClass(AbstractProductClass):
        pass

    __all__.append('ProductClass')


if not is_model_registered('catalogue', 'Category'):
    @cached_property
    class Category(AbstractCategory):
        pass

    __all__.append('Category')


if not is_model_registered('catalogue', 'ProductCategory'):
    @cached_property
    class ProductCategory(AbstractProductCategory):
        pass

    __all__.append('ProductCategory')


if not is_model_registered('catalogue', 'Product'):
    @cached_property
    class Product(AbstractProduct):
        pass

    __all__.append('Product')


if not is_model_registered('catalogue', 'ProductRecommendation'):
    class ProductRecommendation(AbstractProductRecommendation):
        pass

    __all__.append('ProductRecommendation')


if not is_model_registered('catalogue', 'ProductAttribute'):
    @cached_property
    class ProductAttribute(AbstractProductAttribute):
        pass

    __all__.append('ProductAttribute')


if not is_model_registered('catalogue', 'ProductAttributeValue'):
    @cached_property
    class ProductAttributeValue(AbstractProductAttributeValue):
        pass

    __all__.append('ProductAttributeValue')


if not is_model_registered('catalogue', 'AttributeOptionGroup'):
    @cached_property
    class AttributeOptionGroup(AbstractAttributeOptionGroup):
        pass

    __all__.append('AttributeOptionGroup')


if not is_model_registered('catalogue', 'AttributeOption'):
    @cached_property
    class AttributeOption(AbstractAttributeOption):
        pass

    __all__.append('AttributeOption')


if not is_model_registered('catalogue', 'Option'):
    @cached_property
    class Option(AbstractOption):
        pass

    __all__.append('Option')


if not is_model_registered('catalogue', 'ProductImage'):
    @cached_property
    class ProductImage(AbstractProductImage):
        pass

    __all__.append('ProductImage')
