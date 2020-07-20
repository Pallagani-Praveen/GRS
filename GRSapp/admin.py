from django.contrib import admin
from .models import ContactModel,UsersModal,itemslist,Mobiles,Laptops,HeadSet,Camera,Powerbank,Refrigerator,Kettle,Television,WashingMachine,AdminModel
from .models import mobilereview,laptopreview,kettlereview,camerareview,powerbankreview,headsetreview,washmanchinereview,fridgereview,televisionreview

admin.site.register(AdminModel)

admin.site.register(ContactModel)
admin.site.register(UsersModal)
admin.site.register(itemslist)
admin.site.register(Mobiles)
admin.site.register(Laptops)
admin.site.register(HeadSet)
admin.site.register(Camera)
admin.site.register(Powerbank)
admin.site.register(Refrigerator)
admin.site.register(Kettle)
admin.site.register(Television)
admin.site.register(WashingMachine)


admin.site.register(mobilereview)
admin.site.register(laptopreview)
admin.site.register(headsetreview)
admin.site.register(camerareview)
admin.site.register(powerbankreview)
admin.site.register(kettlereview)
admin.site.register(washmanchinereview)
admin.site.register(fridgereview)
admin.site.register(televisionreview)





