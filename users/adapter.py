from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
User = settings.AUTH_USER_MODEL



class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.phone_number = data.get('phone_number')
        user.school = data.get('school')
        user.department = data.get('department')
        user.level = data.get('level')
        user.school_id = data.get('school_id')
        user.course = data.get('course')
        user.is_landlord =data.get('is_landlord')

        #LANDLORDS DETAILS
        user.ID_card =data.get('ID_card')
        user.location =data.get('location')

        if user.is_landlord == True:
           
            user.is_active = False
        
        user.save()
        return user