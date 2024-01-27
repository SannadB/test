from django.contrib import admin
from .models import Member, Product, Category, Review, Item, Rating

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "active")

class ProductAdmin(admin.ModelAdmin):
  list_display = ("name", "description", "price", "category")

class CategoryAdmin(admin.ModelAdmin):
  list_display = ("name", "description")

class ReviewAdmin(admin.ModelAdmin):
  list_display = ("product", "rating", "comment", "created_at")

class ItemAdmin(admin.ModelAdmin):
  list_display = ("name", "description", "price", "category")

admin.site.register(Member, MemberAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Rating)
