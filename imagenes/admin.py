from django.contrib import admin


from .models import EEG, MRI, mRNA

admin.site.register(EEG)
admin.site.register(MRI)
admin.site.register(mRNA)
