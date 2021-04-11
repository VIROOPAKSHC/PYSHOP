from django.contrib import admin
from .models import Product,Offer,Home

class ProductAdmin(admin.ModelAdmin):
    list_display=("name","price","stock")


class OfferAdmin(admin.ModelAdmin):
    list_display=("code","discount")


class HomeAdmin(admin.ModelAdmin):
    list_displayed=("name")


admin.site.register(Product,ProductAdmin)
admin.site.register(Offer,OfferAdmin)
admin.site.register(Home,HomeAdmin)
