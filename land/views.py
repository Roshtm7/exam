from django.shortcuts import render,redirect,get_object_or_404

from django.views.generic import View

from land.forms import RealEstateForm,RealEstateUpdateForm

from land.models import RealEstate

from django.db.models import Q

class RealEstateCreateView(View):
    template_name="real_estate_add.html"
    form_class=RealEstateForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance= self.form_class(form_data,files=request.FILES)

        
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
            RealEstate.objects.create(**data)
            return redirect("realestate-list")
           

        return render(request,self.template_name,{"form":form_instance})

class RealEstateListView(View):
    template_name="real_estate_list.html"
    def get(self,request,*args,**kwargs):
        
        search_text=request.GET.get("filter")
        qs=RealEstate.objects.all()
        all_address=RealEstate.objects.values_list("address",flat=True).distinct()
        all_price=RealEstate.objects.values_list("price",flat=True).distinct()
        all_location=RealEstate.objects.values_list("location",flat=True).distinct()
        all_contact_details=RealEstate.objects.values_list("contact_details",flat=True).distinct()
        all_records=[]
        all_records.extend(all_address)
        all_records.extend(all_price)
        all_records.extend(all_location)
        all_records.extend(all_contact_details)
        print(all_records)


        if search_text:
            qs=qs.filter(
                Q(address__contains=search_text)|Q(price__contains=search_text)|
                Q(location__contains=search_text)|Q(contact_details__contains=search_text)
            )
        return render(request,self.template_name,{"data":qs,"records":all_records})

class RealEstateDetailsView(View):
    template_name="real_estate_details.html"
    def get(self,request,*args,**kwargs):
        print(kwargs)
        id=kwargs.get("pk")
        qs=RealEstate.objects.get(id=id)
        return render(request,self.template_name,{"data":qs})

class RealEstateDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        RealEstate.objects.get(id=id).delete()
        return redirect("realestate-list") 

class RealEstateUpdateView(View):
    template_name="real_estate_update.html"
    form_class=RealEstateUpdateForm
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        RealEstate_object=get_object_or_404(RealEstate,id=id)
        form_instance=self.form_class(instance=RealEstate_object)
        return render(request,self.template_name,{"form":form_instance})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        RealEstate_object=get_object_or_404(RealEstate,id=id)
        form_data=request.POST
        form_instance=self.form_class(form_data,files=request.FILES,instance=RealEstate_object)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("realestate-list")
        return render(request,self.template_name,{"form":{form_instance}}) 
