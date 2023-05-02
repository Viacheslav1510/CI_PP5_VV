from django.db import models
from profiles.models import UserProfile
from products.models import Album


class Wishlist(models.Model):
    """
    Model for users to save their favoutite
    products to a wishlist
    """
    product = models.ForeignKey(
        Album,
        related_name='wishlist',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        UserProfile,
        related_name='wishlist',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.product.name

    def whishlist_count(self):
        return self.whishlist_set.filter(user=UserProfile).count()
