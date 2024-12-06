from django.contrib import admin
from .models import DanjoVarity, atomReviews,Store,AtomCertification


# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = atomReviews
    extra = 2
    
class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type, date_added')
    inlines = [ChaiReviewInline]
    
class StoreAdmin(admin.ModelAdmin):
    list_display=('name', 'location')
    filter_horizontal=('chai_varieties',)

class ChaiCetificateAdmin(admin.ModelAdmin):
    list_display=('chai', 'certificate_number')



admin.site.register(DanjoVarity,ChaiVarietyAdmin)
