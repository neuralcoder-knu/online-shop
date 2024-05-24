from django.contrib import admin

from shop.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('status', 'created')
    list_editable = ('price', 'status')
    raw_id_fields = ('category',)
    actions = ('change_status',)

    @admin.action(description='змінити статус продукта')
    def change_status(self, request, queryset):
        rows_count = queryset.update(status=True)
        self.message_user(request, f'{rows_count} статус змінено')
