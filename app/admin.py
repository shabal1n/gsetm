from django.contrib import admin
from .models import *

admin.site.site_header = 'Genset Machinery'


class HideModel(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class GeneratorImageAdmin(admin.StackedInline):
    model = GeneratorImage


class GeneratorEngineAdmin(admin.StackedInline):
    model = Engine


class GeneratorAlternatorAdmin(admin.StackedInline):
    model = Alternator


class GeneratorParametersAdmin(admin.StackedInline):
    model = GeneratorParameters


class GeneratorAdmin(admin.ModelAdmin):
    inlines = [GeneratorEngineAdmin, GeneratorAlternatorAdmin, GeneratorParametersAdmin, GeneratorImageAdmin]

    class Meta:
        model = Generator


admin.site.register(Generator, GeneratorAdmin)
admin.site.register(Engine, HideModel)
admin.site.register(Alternator, HideModel)
admin.site.register(GeneratorParameters, HideModel)
admin.site.register(GeneratorImage, HideModel)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(GeneratorCategory)
admin.site.register(GeneratorsRent)
admin.site.register(AboutUsNumbers)
admin.site.register(Fuel, HideModel)
admin.site.register(AvailableStock, HideModel)
admin.site.register(Execution, HideModel)
admin.site.register(StartSystem, HideModel)
admin.site.register(ReserveAutomat, HideModel)
admin.site.register(EngineManufacturer, HideModel)
admin.site.register(CylindersPositioning, HideModel)
admin.site.register(TurboEngine, HideModel)
admin.site.register(CoolingSystem, HideModel)
admin.site.register(RegulatorType, HideModel)
admin.site.register(AlternatorManufacturer, HideModel)