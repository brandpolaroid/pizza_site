from django.contrib import admin
from .models import Pizza, Order, Offered


admin.site.register(Pizza)
admin.site.register(Order)
admin.site.register(Offered)




























# class TablePerson(admin.ModelAdmin):
#     list_display = ('name', 'age')
#     exclude = ('cash',)
#     search_fields = ('name',)

#
# admin.site.register(Person, TablePerson)
# admin.site.register(Customer)
# admin.site.register(Messages)