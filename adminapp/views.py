from django.shortcuts import render, redirect
from adminapp.models import *
from userapp.models import *

# Create your views here.


def register(request):

    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        phone=request.POST['phone']
        pro_img = request.FILES.get('pro_img')

        if admin_register.objects.filter(email=email).exists():
            return render(request, 'admin_register.html', {'error': 'Email already registered. Please use a different email.'})
        
        data=admin_register(
            username=username,
            email=email,
            password=password,
            phone=phone,
            pro_img=pro_img
       
        )
        data.save()
        return redirect('/adminapp/admin_login')

    return render(request, 'admin_register.html')

def admin_login(request):

    if 'user_id' in request.session:
        return redirect('/adminapp/dashboard')
       
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = admin_register.objects.filter(email=email, password=password)
        if user.count()==0:
            return render(request, 'admin_login.html', {"error": "Invalid Email or Password"})
        else:
            row= user.first()
            request.session['user_id'] = row.id  
            return redirect('/adminapp/dashboard')

    return render(request, 'admin_login.html')

def admin_logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('/adminapp/admin_login')


def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id= request.session['user_id']) 

    all_bio = profile_bio.objects.all()



    return render(request, 'dashboard.html' , {'user': user, 'all_bio': all_bio})

def add_data(request):

    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=user_id)
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        pro_img = request.FILES.get('pro_img')
   
        data = admin_register(

            username=username,
            email=email,
            password=password,
            phone=phone,
            pro_img=pro_img
            
        )
        data.save()
        return redirect('/adminapp/view_data')

    return render(request, 'add_data.html', {'user':user})

def view_data(request):

    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
  
    user = admin_register.objects.get(id=request.session.get('user_id'))
    data = admin_register.objects.all()

    return render(request, 'view_data.html', {'data':data, 'user': user} )

def edit_data(request, id):

    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))
    data = admin_register.objects.get(id=id)

    if request.method == 'POST':
        data.username = request.POST['username']
        data.email = request.POST['email']
        data.password = request.POST['password']
        data.phone = request.POST['phone']
        pro_img = request.FILES.get('pro_img')
        
        if pro_img:
            data.pro_img = pro_img
        data.save()
        return redirect('/adminapp/view_data')

    return render(request, 'edit_data.html', {'data':data, 'user': user})

def delete_data(request, id):

    data = admin_register.objects.get(id=id)
    data.delete()
    return redirect('/adminapp/view_data')


def add_bio(request):

    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))

    if request.method == 'POST':
        name = request.POST['name']
        designation = request.POST['designation']
        about = request.POST['about']
        dob = request.POST['dob']
        age = request.POST['age']
        website = request.POST['website']
        degree = request.POST['degree']
        phone = request.POST['phone']
        email = request.POST['email']
        city = request.POST['city']
        religion = request.POST['religion']
        description = request.POST['description']
        pro_pic = request.FILES.get('pro_pic')

        bio_data = profile_bio(
            name=name,
            designation=designation,
            about=about,
            dob=dob,
            age=age,
            website=website,
            degree=degree,
            phone=phone,
            email=email,
            city=city,
            religion=religion,
            description=description,
            pro_pic=pro_pic
        )
        bio_data.save()
        return redirect('/adminapp/view_bio')

    return render(request, 'add_bio.html', {'user': user})

def view_bio(request):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))
    bio_data = profile_bio.objects.all()

    return render(request, 'view_bio.html', {'bio_data': bio_data, 'user': user})

def edit_bio(request, id):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))
    bio_data = profile_bio.objects.get(id=id)

    if request.method == 'POST':
        bio_data.name = request.POST['name']
        bio_data.designation = request.POST['designation']
        bio_data.about = request.POST['about']
        bio_data.dob = request.POST['dob']
        bio_data.age = request.POST['age']
        bio_data.website = request.POST['website']
        bio_data.degree = request.POST['degree']
        bio_data.phone = request.POST['phone']
        bio_data.email = request.POST['email']
        bio_data.city = request.POST['city']
        bio_data.religion = request.POST['religion']
        bio_data.description = request.POST['description']
        pro_pic = request.FILES.get('pro_pic')
        
        if pro_pic:
            bio_data.pro_pic = pro_pic
        bio_data.save()
        return redirect('/adminapp/view_bio')

    return render(request, 'edit_bio.html', {'bio_data':bio_data, 'user': user})

def delete_bio(request, id):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    bio_data = profile_bio.objects.get(id=id)
    bio_data.delete()
    return redirect('/adminapp/view_bio')


def add_banner(request):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))

    if request.method == 'POST':
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        banner_img = request.FILES.get('banner_img')

        banner_data = banner(
            title=title,
            subtitle=subtitle,
            banner_img=banner_img
        )
        banner_data.save()
        return redirect('/adminapp/view_banner')

    return render(request, 'add_banner.html', {'user': user})

def view_banner(request):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))
    banner_data = banner.objects.all()

    return render(request, 'view_banner.html', {'banner_data': banner_data, 'user': user})


def edit_banner(request, id):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))
    banner_data = banner.objects.get(id=id)

    if request.method == 'POST':
        banner_data.title = request.POST['title']
        banner_data.subtitle = request.POST['subtitle']
        banner_img = request.FILES.get('banner_img')
        
        if banner_img:
            banner_data.banner_img = banner_img
        banner_data.save()
        return redirect('/adminapp/view_banner')

    return render(request, 'edit_banner.html', {'banner_data':banner_data, 'user': user})

def delete_banner(request, id):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    banner_data = banner.objects.get(id=id)
    banner_data.delete()
    return redirect('/adminapp/view_banner')


def add_skill(request):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))

    if request.method == 'POST':
        skill_name = request.POST['skill_name']
        skill_percentage = request.POST['skill_percentage']

        skill_data = skills(
            skill_name=skill_name,
            skill_percentage=skill_percentage
        )
        skill_data.save()
        return redirect('/adminapp/view_skill')

    return render(request, 'add_skill.html', {'user': user})

def view_skill(request):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))
    skill_data = skills.objects.all()

    return render(request, 'view_skill.html', {'skill_data': skill_data, 'user': user})

def edit_skill(request, id):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))
    skill_data = skills.objects.get(id=id)

    if request.method == 'POST':
        skill_data.skill_name = request.POST['skill_name']
        skill_data.skill_percentage = request.POST['skill_percentage']
        skill_data.save()
        return redirect('/adminapp/view_skill')

    return render(request, 'edit_skill.html', {'skill_data':skill_data, 'user': user})

def delete_skill(request, id):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    skill_data = skills.objects.get(id=id)
    skill_data.delete()
    return redirect('/adminapp/view_skill')
    

def add_education(request):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))

    if request.method == 'POST':
        degree = request.POST['degree']
        university = request.POST['university']
        start_year = request.POST['start_year']
        end_year = request.POST['end_year']
        description = request.POST['description']

        education_data = Education(
            degree=degree,
            university=university,
            start_year=start_year,
            end_year=end_year,
            description=description
        )
        education_data.save()
        return redirect('/adminapp/view_education')

    return render(request, 'add_education.html', {'user': user})

def view_education(request):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))
    education_data = Education.objects.all()

    return render(request, 'view_education.html', {'education_data': education_data, 'user': user})

def edit_education(request, id):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))
    education_data = Education.objects.get(id=id)

    if request.method == 'POST':
        education_data.degree = request.POST['degree']
        education_data.university = request.POST['university']
        education_data.start_year = request.POST['start_year']
        education_data.end_year = request.POST['end_year']
        education_data.description = request.POST['description']
        education_data.save()
        return redirect('/adminapp/view_education')

    return render(request, 'edit_education.html', {'education_data':education_data, 'user': user})


def delete_education(request, id):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    education_data = Education.objects.get(id=id)
    education_data.delete()
    return redirect('/adminapp/view_education')


def add_experience(request):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))

    if request.method == 'POST':
        job_title = request.POST['job_title']
        company_name = request.POST['company_name']
        start_year = request.POST['start_year']
        end_year = request.POST['end_year']
        desc_1 = request.POST['desc_1']
        desc_2 = request.POST['desc_2']
        desc_3 = request.POST['desc_3']
        desc_4 = request.POST['desc_4']


        experience_data = Experience(
            job_title=job_title,
            company_name=company_name,
            start_year=start_year,
            end_year=end_year,
            desc_1=desc_1,
            desc_2=desc_2,
            desc_3=desc_3,
            desc_4=desc_4
        )
        experience_data.save()
        return redirect('/adminapp/view_ex')

    return render(request, 'add_experience.html', {'user': user})

def view_experience(request):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))
    ex_data = Experience.objects.all()

    return render(request, 'view_experience.html', {'ex_data': ex_data, 'user': user})


def edit_experience(request, id):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))
    ex_data = Experience.objects.get(id=id)

    if request.method == 'POST':
        ex_data.job_title = request.POST['job_title']
        ex_data.company_name = request.POST['company_name']
        ex_data.start_year = request.POST['start_year']
        ex_data.end_year = request.POST['end_year']
        ex_data.desc_1 = request.POST['desc_1']
        ex_data.desc_2 = request.POST['desc_2']
        ex_data.desc_3 = request.POST['desc_3']
        ex_data.desc_4 = request.POST['desc_4']
        ex_data.save()
        return redirect('/adminapp/view_ex')

    return render(request, 'edit_experience.html', {'ex_data':ex_data, 'user': user})


def delete_experience(request, id):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    ex_data = Experience.objects.get(id=id)
    ex_data.delete()
    return redirect('/adminapp/view_ex')


def add_portfolio(request):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))

    if request.method == 'POST':
        project_name = request.POST['project_name']
        project_link = request.POST.get('project_link')
        desc_1 = request.POST['desc_1']
        desc_2 = request.POST['desc_2']
        desc_3 = request.POST['desc_3']
        desc_4 = request.POST['desc_4']
        

        portfolio_data = Portfolio(
            project_name=project_name,
            project_link=project_link,
            desc_1=desc_1,
            desc_2=desc_2,
            desc_3=desc_3,
            desc_4=desc_4,
        )
        portfolio_data.save()
        return redirect('/adminapp/view_portfolio')

    return render(request, 'add_portfolio.html', {'user': user})


def view_portfolio(request):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))
    portfolio_data = Portfolio.objects.all()

    return render(request, 'view_portfolio.html', {'portfolio_data': portfolio_data, 'user': user})


def edit_portfolio(request, id):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))
    portfolio_data = Portfolio.objects.get(id=id)

    if request.method == 'POST':
        portfolio_data.project_name = request.POST['project_name']
        portfolio_data.project_link = request.POST.get('project_link')
        portfolio_data.desc_1 = request.POST['desc_1']
        portfolio_data.desc_2 = request.POST['desc_2']
        portfolio_data.desc_3 = request.POST['desc_3']
        portfolio_data.desc_4 = request.POST['desc_4']
        portfolio_data.save()
        return redirect('/adminapp/view_portfolio')

    return render(request, 'edit_portfolio.html', {'portfolio_data':portfolio_data, 'user': user})

def delete_portfolio(request, id):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    portfolio_data = Portfolio.objects.get(id=id)
    portfolio_data.delete()
    return redirect('/adminapp/view_portfolio')


def add_service(request):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))

    if request.method == 'POST':
        service_title = request.POST['service_title']
        service_desc = request.POST['service_desc']
        service_icon = request.POST['service_icon']

        service_data = Services(
            service_title=service_title,
            service_desc=service_desc,
            service_icon=service_icon
        )
        service_data.save()
        return redirect('/adminapp/view_service')
    
    return render(request, "add_service.html", {'user': user})


def view_service(request):
    if 'user_id' not in request.session:    
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))
    service_data = Services.objects.all()

    return render(request, 'view_service.html', {'service_data': service_data, 'user': user})


def edit_service(request, id):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user = admin_register.objects.get(id=request.session.get('user_id'))
    service_data = Services.objects.get(id=id)

    if request.method == 'POST':
        service_data.service_title = request.POST['service_title']
        service_data.service_desc = request.POST['service_desc']
        service_data.service_icon = request.POST['service_icon']
        service_data.save()
        return redirect('/adminapp/view_service')
    
    return render(request, 'edit_service.html', {'service_data':service_data, 'user': user})

def delete_service(request, id):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    service_data = Services.objects.get(id=id)
    service_data.delete()
    return redirect('/adminapp/view_service')
    

def view_user_contact(request):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user_contact_data = user_contact.objects.all()
    user = admin_register.objects.get(id=request.session.get('user_id'))

    return render(request, 'view_user_contact.html', {'user_contact_data': user_contact_data, 'user': user})

def delete_user_contact(request,id):
    if 'user_id' not in request.session:
        return redirect('/adminapp/admin_login')
    
    user_contact_data = user_contact.objects.get(id=id)
    user_contact_data.delete()
    return redirect('/adminapp/view_user_contact')
    

    
    