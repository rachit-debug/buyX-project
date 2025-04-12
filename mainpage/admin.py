from django.contrib import admin
from mainpage.models import Contactdata
from mainpage.models import *
from import_export.admin import ImportExportModelAdmin 
from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from .models import Quote

# Create a Resource class for Quote model to enable import/export functionality
class QuoteResource(resources.ModelResource):
    class Meta:
        model = Quote
        # Specify the fields to export (if you want to limit to specific fields)
        fields = ('company_name', 'phone', 'email', 'country', 'scaffolding_type', 'quantity', 'product_finish')
        export_order = fields  # Specify the order in which the fields will be exported

# Define the ModelAdmin for Quote
class QuoteAdmin(ExportMixin, admin.ModelAdmin):
    # Tabular display of fields in the list view
    list_display = ('company_name', 'phone', 'email', 'country', 'scaffolding_type', 'quantity', 'product_finish')
    
    # Add search functionality for company_name, email, and phone fields
    search_fields = ['company_name', 'email', 'phone']
    
    # Add filtering options based on country and scaffolding type
    list_filter = ['country', 'scaffolding_type']
    
    # Allow the admin to import/export quotes
    resource_class = QuoteResource
    
    # You can add pagination, ordering, etc., here if needed
    list_per_page = 25  # Display 25 records per page

# Register the model and the admin class
admin.site.register(Quote, QuoteAdmin)

# Register your models here.
admin.site.register(Contactdata)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product) 
admin.site.register(Blog)
admin.site.register(ExtendedUser)  
class damAdmin(ImportExportModelAdmin):
    list_display=( 'customer_no','customer_name','customer_username','phone','email','address','Product_id','product_img','Product_quantity','product_price','product_name','status','add_on','total_cost')
    search_fields=('customer_no','customer_username','phone','email','address')
    list_filter=('add_on',)
    ordering=('-add_on',)
admin.site.register(order,damAdmin)
admin.site.register(Returns_Shipping_Policy)
admin.site.register(Privacy_Policy)
admin.site.register(Cancelation_Policy)
admin.site.register(about_compeny)

