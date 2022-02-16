
from django.contrib import admin
from Common.util import getMandal, is_member, messageIcons

from django.utils.translation import gettext as _
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from FolloWUp.models import FollowUp, FollowupStatus
from Mandal.models import Karyakram, MandalProfile
from SamparkKarykar.models import KaryakarProfile
from Yuvak.models import YuvakProfile

# Register your models here.

class KaryakramAdmin(admin.ModelAdmin):
    change_form_template = "admin/karyakram_change_form.html"
    list_display = ("__str__", "Karyakram_date", "Start_date","End_date","Start_Folloup","Start_Attandance","IsDone")
    list_per_page = 20
    
    def get_fieldsets(self, request, obj) :
        if not request.user.is_superuser:
            if is_member(request.user,"Sampark Karykar"):
                return ((None, {"fields": ("Title","Karyakram_date","Start_date","End_date","Mandal")}),)
            elif is_member(request.user,"Yuvak"):
                return ((None, {"fields": ("Title","Karyakram_date","Mandal")}),)
        else: return ((None, {"fields": ("Title","Karyakram_date","Start_date","End_date","Mandal")}),)
    

    def get_queryset(self, request):
        qs = super(KaryakramAdmin, self).get_queryset(request).filter(Mandal=getMandal(request.user)).order_by('-Karyakram_date')
        if not request.user.is_superuser:
            return qs.filter(Start_Folloup=True)
        return qs

    def get_list_display(self,request):
        if not request.user.is_superuser:
            if is_member(request.user,"Sampark Karykar"):
                return ["__str__", "Karyakram_date","Start_date","End_date","Start_Folloup"]
            elif is_member(request.user,"Yuvak"):
                return ["__str__", "Karyakram_date"]
        return super().get_list_display(request)
   
    def save_model(self, request, obj, form, change):
        if "_followup_record_create" in request.POST or "_attandance_record_create" in request.POST or "_done_karykram" in request.POST:
            if obj.pk:
                if "_followup_record_create" in request.POST:
                    for karyakar_vrund in obj.Mandal.karyakarprofile_set.all():
                        for yuvak in karyakar_vrund.Yuvaks.all():
                            FollowUp.objects.get_or_create(Karyakram=obj,
                                            KaryKarVrund=karyakar_vrund,
                                            Yuvak=yuvak)
                    Karyakram.objects.filter(pk=obj.pk).update(Start_Folloup=True)
                    Mandal=getMandal(request.user)
                    Yuvaks = YuvakProfile.objects.filter(karyakarprofile__isnull=True,mandal=Mandal)
                    karyakar_vrund = KaryakarProfile.objects.filter(mandal=Mandal,karykar1profile__FirstName="Admin",karykar1profile__MiddleName=Mandal.Name,karykar1profile__SurName="Mandal").first()
                    if karyakar_vrund:
                        for yuvak in Yuvaks.all():
                            FollowUp.objects.get_or_create(Karyakram=obj,
                                        KaryKarVrund=karyakar_vrund,
                                        Yuvak=yuvak)
                        
                elif "_attandance_record_create" in request.POST:
                    if obj.Start_Folloup == True:
                        Mandal=getMandal(request.user)
                        Yuvaks = YuvakProfile.objects.filter(karyakarprofile__isnull=True,mandal=Mandal)
                        karyakar_vrund = KaryakarProfile.objects.filter(mandal=Mandal,karykar1profile__FirstName="Admin",karykar1profile__MiddleName=Mandal.Name,karykar1profile__SurName="Mandal").first()
                        if karyakar_vrund:
                            for yuvak in Yuvaks.all():
                                FollowUp.objects.get_or_create(Karyakram=obj,
                                            KaryKarVrund=karyakar_vrund,
                                            Yuvak=yuvak)
                            Karyakram.objects.filter(pk=obj.pk).update(Start_Attandance=True)
                        else:
                            msg = format_html(_('Please Create Admin User first Initiate FollowUp first.'))
                            self.message_user(request, msg, messages.WARNING)
                            return HttpResponseRedirect("/admin/Mandal/karyakram")
                    else:
                        msg = format_html(_('Please Initiate FollowUp first.'))
                        self.message_user(request, msg, messages.WARNING)
                        return HttpResponseRedirect("/admin/Mandal/karyakram")
                elif "_done_karykram" in request.POST:
                    FollowUp.objects.filter(Karyakram=obj,Status=FollowupStatus.Pending).update(Status=FollowupStatus.No)
                    FollowUp.objects.filter(Karyakram=obj,Present__isnull=True).update(Present=False)
                    Karyakram.objects.filter(pk=obj.pk).update(IsDone=True)   
            
            else:
                msg = format_html(_('Please save karykram first.'))
                self.message_user(request, msg, messages.WARNING)
                return HttpResponseRedirect("/admin/Mandal/karyakram")
        else:
            return super().save_model(request, obj, form, change)

class MandalProfileAdmin(admin.ModelAdmin):
    # change_list_template = 'admin/mandal_change_list.html'
    list_display = ("__str__", "Nirikshak_details", "Sanchalak_details",)
    list_per_page = 20

    def Nirikshak_details(self,obj):
        if obj.Nirikshak : 
            return format_html(obj.Nirikshak.FirstName + " " +obj.Nirikshak.SurName +" <br> "+ messageIcons(obj.Nirikshak.WhatsappNo,20))
        return ''
    def Sanchalak_details(self,obj):
        if obj.Sanchalak:
            return format_html(obj.Sanchalak.FirstName + " " +obj.Sanchalak.SurName +" <br> " + messageIcons(obj.Nirikshak.WhatsappNo,20))
        return ''
        
admin.site.register(MandalProfile,MandalProfileAdmin)
admin.site.register(Karyakram,KaryakramAdmin)