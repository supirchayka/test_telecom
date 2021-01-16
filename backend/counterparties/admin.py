from django.contrib import admin

from counterparties.models import Counterparties, Manager, Cities, Channel, TypeOfService, TypeOfCP, KnowsFrom

admin.site.register(Counterparties)
admin.site.register(Manager)
admin.site.register(Cities)
admin.site.register(Channel)
admin.site.register(TypeOfService)
admin.site.register(TypeOfCP)
admin.site.register(KnowsFrom)