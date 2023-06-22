from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
import os
from samproject.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        a = regform(request.POST)
        if a.is_valid():
            cn = a.cleaned_data['companyname']
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            cp = a.cleaned_data['password2']
            mb = a.cleaned_data['mobile']
            ad = a.cleaned_data['address']
            if ps == cp:
                b = regmodel(companyname=cn, email=em, password=ps, mobile=mb, address=ad)
                b.save()
                return redirect(login)
            else:
                return HttpResponse("Incorrect password")
        else:
            return HttpResponse("Registration failed")
    return render(request, 'register.html')


# correct


def login(request):
    if request.method == 'POST':
        a = logform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = regmodel.objects.all()
            for i in b:
                cmp = i.companyname
                request.session[
                    'companyname'] = cmp  # request.session-this method is used to globally catch variable name
                id = i.id

                # print(id)
                if i.email == em and i.password == ps:
                    return render(request, 'profile.html', {'cmp': cmp, 'id': id})
            else:
                return HttpResponse("Login failed")
    else:
        return render(request, 'login.html')


def navbar(request):
    return render(request, 'navbar.html')


def footer(request):
    return render(request, 'footer.html')


def profile(request):
    return render(request, 'profile.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def about(request):
    return render(request, 'about.html')


def terms(request):
    return render(request, 'terms.html')


def samplenavbar(request):
    return render(request, 'samplenavbar.html')


def contact(request):
    return render(request, 'contact.html')


# def sendmessage(request):
#     return render(request,'sendmessage.html')


# correct

def vaccancyupload(request, id):
    b = regmodel.objects.get(id=id)
    cm = b.companyname
    em = b.email

    if request.method == 'POST':
        a = vaccancyuploadform(request.POST)
        if a.is_valid():
            cn = a.cleaned_data['companyname']
            em = a.cleaned_data['email']
            jt = a.cleaned_data['jobtitle']
            jp = a.cleaned_data['jobtype']
            wt = a.cleaned_data['worktype']
            er = a.cleaned_data['experiencerequired']
            qr = a.cleaned_data['qualificationrequired']
            b = vaccancyuploadmodel(companyname=cn, email=em, jobtitle=jt, jobtype=jp, worktype=wt,
                                    experiencerequired=er, qualificationrequired=qr)
            b.save()
            return redirect(vaccancysuccess)
            # return HttpResponse("Upload success")
        else:
            return HttpResponse("Upload failed")
    return render(request, 'vaccancyupload.html', {'cm': cm, 'em': em})


def vaccancysuccess(request):
    a = vaccancyuploadmodel.objects.all()
    b = request.session['companyname']
    return render(request, 'vaccancysuccess.html', {'a': a, 'b': b})


def vaccancyedit(request, id):
    a = vaccancyuploadmodel.objects.get(id=id)
    if request.method == 'POST':
        a.companyname = request.POST.get('companyname')
        a.email = request.POST.get('email')
        a.jobtitle = request.POST.get('jobtitle')
        a.jobtype = request.POST.get('jobtype')
        a.worktype = request.POST.get('worktype')
        a.experiencerequired = request.POST.get('experiencerequired')
        a.qualificationrequired = request.POST.get('qualificationrequired')
        a.save()
        return redirect(vaccancysuccess)
    return render(request, 'vaccancyedit.html', {'a': a})


def vaccancydelete(request, id):
    a = vaccancyuploadmodel.objects.get(id=id)
    a.delete()
    return redirect(vaccancysuccess)


def userregistration(request):
    if request.method == 'POST':
        a = userregistrationform(request.POST)

        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        un = request.POST.get('username')
        em = request.POST.get('email')
        ps = request.POST.get('password')
        cp = request.POST.get('confirmpassword')  # getting directly from html form
        if ps == cp:
            b = User(username=un, first_name=fn, last_name=ln, email=em, password=ps)
            b.save()
            return redirect(userlogin)
        else:
            return HttpResponse("Incorrect password")
    # else:
    # return HttpResponse("Registration failed")

    else:
        return render(request, 'userregistration.html')


# def userlogin(request):
#     if request.method == 'POST':
#         a = userloginform(request.POST)
#         if a.is_valid():
#             em = a.cleaned_data['email']
#             ps = a.cleaned_data['password']
#             b = User.objects.all()
#             for i in b:
#                 un = i.username
#
#                 if i.email == em and i.password == ps:
#                     # return redirect(userprofile)
#                     return render(request, 'userprofile.html', {'un': un})
#             else:
#                 return HttpResponse("Login failed")
#     else:
#         return render(request, 'userlogin.html')


def userlogin(request):
    if request.method == 'POST':
        a = userloginform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = User.objects.all()
            for i in b:
                un = i.username

                if i.email == em and i.password == ps:
                    request.session['id'] = i.id
                    # return redirect(userprofile)
                    return render(request, 'userprofile.html', {'un': un, 'id':request.session['id']})
            else:
                return HttpResponse("Login failed")
    else:
        return render(request, 'userlogin.html')






# def userdetails(request):
#
#     if request.method == 'POST':
#         a = userdetailsform(request.POST, request.FILES)
#         if a.is_valid():
#             fn = a.cleaned_data['fullname']
#             em = a.cleaned_data['email']
#             rs = a.cleaned_data['resume']
#             im = a.cleaned_data['image']
#             eq = a.cleaned_data['educationalqualification']
#             ex = a.cleaned_data['experience']
#             ad = a.cleaned_data['address']
#             mb = a.cleaned_data['mobile']
#             b = userdetailsmodel(fullname=fn, email=em, resume=rs, image=im, educationalqualification=eq, experience=ex,
#                                  address=ad, mobile=mb)
#             b.save()
#             # return HttpResponse("Details ulpoaded successfully !")
#             return render(request, 'userprofile.html', {'un': fn})
#             # return redirect(userprofile)
#         else:
#             return HttpResponse("Details uploading failed")
#     return render(request, 'userdetails.html')


def userdetails(request,id):
    b = User.objects.get(id=id)
    fn = b.first_name
    ln = b.last_name
    el = b.email
    if request.method == 'POST':
        a = userdetailsform(request.POST, request.FILES)
        if a.is_valid():
            fn = a.cleaned_data['fullname']
            em = a.cleaned_data['email']
            rs = a.cleaned_data['resume']
            im = a.cleaned_data['image']
            eq = a.cleaned_data['educationalqualification']
            ex = a.cleaned_data['experience']
            ad = a.cleaned_data['address']
            mb = a.cleaned_data['mobile']
            id = request.session['id']
            b = userdetailsmodel(uid=id,fullname=fn, email=em, resume=rs, image=im, educationalqualification=eq, experience=ex,
                                 address=ad, mobile=mb)
            b.save()
            # return HttpResponse("Details ulpoaded successfully !")
            return render(request, 'userprofile.html', {'un': fn})
            # return redirect(userprofile)
        else:
            return HttpResponse("Details uploading failed")
    return render(request, 'userdetails.html',{'fn':fn, 'ln':ln, 'el':el})


def userprofile(request):
    id=request.session['id']
    print(id)
    return render(request, 'userprofile.html',{'id':id})


def userviewvaccancy(request):
    a = vaccancyuploadmodel.objects.all()
    return render(request, 'userviewvaccancy.html', {'a': a})


# def userdisplay(request):
#     a = userdetailsmodel.objects.all()
#     fullname = []
#     email = []
#     resume = []
#     image = []
#     education = []
#     experience = []
#     address = []
#     mobile = []
#     id = []
#     for i in a:
#         img = i.image
#         image.append(str(img).split('/')[-1])
#         fn = i.fullname
#         fullname.append(fn)
#         em = i.email
#         email.append(em)
#         res = i.resume
#         resume.append(str(res).split('/')[-1])
#         eq = i.educationalqualification
#         education.append(eq)
#         ex = i.experience
#         experience.append(ex)
#         ad = i.address
#         address.append(ad)
#         mob = i.mobile
#         mobile.append(mob)
#         id1 = i.id
#         id.append(id1)
#     mylist = zip(image, fullname, email, resume, education, experience, address, mobile, id)
#     return render(request, 'userdisplay.html', {'mylist': mylist})


def userdisplay(request):
    a = userdetailsmodel.objects.all()
    fullname = []
    email = []
    resume = []
    image = []
    education = []
    experience = []
    address = []
    mobile = []
    id = []
    uid = []
    for i in a:
        ui = i.uid
        uid.append(ui)
        img = i.image
        image.append(str(img).split('/')[-1])
        fn = i.fullname
        fullname.append(fn)
        em = i.email
        email.append(em)
        res = i.resume
        resume.append(str(res).split('/')[-1])
        eq = i.educationalqualification
        education.append(eq)
        ex = i.experience
        experience.append(ex)
        ad = i.address
        address.append(ad)
        mob = i.mobile
        mobile.append(mob)
        id1 = i.id
        id.append(id1)
    kk = request.session['id']
    print(kk)
    print(uid)
    mylist = zip(image, fullname, email, resume, education, experience, address, mobile, id,uid)
    return render(request, 'userdisplay.html', {'mylist': mylist,'kk':kk})



def userdetailsedit(request, id):
    a = userdetailsmodel.objects.get(id=id)
    image = str(a.image).split('/')[-1]
    resume = str(a.resume).split('/')[-1]
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(a.image) > 0:
                os.remove(a.image.path)
            a.image = request.FILES['image']

            if len(a.resume) > 0:
                os.remove(a.resume.path)
            a.resume = request.FILES['resume']

        a.fullname = request.POST.get('fullname')
        a.email = request.POST.get('email')
        a.educationalqualification = request.POST.get('educationalqualification')
        a.experience = request.POST.get('experience')
        a.address = request.POST.get('address')
        a.mobile = request.POST.get('mobile')
        a.save()
        return redirect(userdisplay)
    return render(request, 'userdetailsedit.html', {'a': a, 'image': image, 'resume': resume})


def userdetailsdelete(request, id):
    a = userdetailsmodel.objects.get(id=id)
    if len(a.image) > 0:
        os.remove(a.image.path)
    if len(a.resume) > 0:
        os.remove(a.resume.path)
    a.delete()
    return redirect(userdisplay)


def editcompanyprofile(request, id):
    a = regmodel.objects.get(id=id)
    if request.method == 'POST':
        a.companyname = request.POST.get('companyname')
        a.email = request.POST.get('email')
        a.password = request.POST.get('password')
        a.confirmpassword = request.POST.get('confirmpassword')
        a.mobile = request.POST.get('mobile')
        a.address = request.POST.get('address')

        a.save()
        return render(request, 'profile.html', {'cmp': a.companyname})
    return render(request, 'editcompanyprofile.html', {'a': a})


def jobapply(request, id):
    a = vaccancyuploadmodel.objects.get(id=id)
    cmp = a.companyname
    job = a.jobtitle
    id = a.id
    if request.method == 'POST':
        a = jobapplyform(request.POST, request.FILES)
        if a.is_valid():
            cn = a.cleaned_data['companyname']
            jt = a.cleaned_data['jobtitle']
            fn = a.cleaned_data['fullname']
            em = a.cleaned_data['email']
            rs = a.cleaned_data['resume']
            b = jobapplymodel(companyname=cn, jobtitle=jt, fullname=fn, email=em, resume=rs)
            b.save()
            subject = f"New job applied to {cmp}"
            message = f'Hi {fn} \n Your application for  {jt}  is applied successfully'
            email_from = EMAIL_HOST_USER  # from
            send_mail(subject, message, email_from, [em])
            return redirect(applysuccess)
        else:
            return HttpResponse("Failed")
    return render(request, 'jobapply.html', {'cmp': cmp, 'jt': job, 'id': id})


def applysuccess(request):
    return render(request, 'applysuccess.html')


def wishlist(request, id):
    a = vaccancyuploadmodel.objects.get(id=id)
    id=request.session['id']
    print(id)
    b = wishlistmodel(uid=id,cid=id, companyname=a.companyname, email=a.email, jobtitle=a.jobtitle, jobtype=a.jobtype,
                      worktype=a.worktype, experiencerequired=a.experiencerequired,
                      qualificationrequired=a.qualificationrequired)
    b.save()
    return redirect(mywish)



def mywish(request):
    a = wishlistmodel.objects.all()
    id = request.session['id']
    return render(request, 'mywish.html', {'a': a,'id':id})


def removewish(request, id):
    a = wishlistmodel.objects.get(id=id)
    a.delete()
    return redirect(mywish)


def viewappliedusers(request):
    a = jobapplymodel.objects.all()
    b = request.session['companyname']
    resume = []
    companyname = []
    jobtitle = []
    fullname = []
    email = []
    id1 = []
    for i in a:
        res = i.resume
        resume.append(str(res).split('/')[-1])
        cn = i.companyname
        companyname.append(cn)
        jt = i.jobtitle
        jobtitle.append(jt)
        fn = i.fullname
        fullname.append(fn)
        em = i.email
        email.append(em)
        id = i.id
        id1.append(id)
    mylist = zip(jobtitle, companyname, fullname, email, resume, id1)
    return render(request, 'viewappliedusers.html', {'mylist': mylist, 'b': b})


def success(request):
    return render(request, 'success.html')


def email(request, id):
    a = jobapplymodel.objects.get(id=id)
    email = a.email
    companyname = a.companyname
    if request.method == 'POST':
        b = emailform(request.POST)
        if b.is_valid():
            em = b.cleaned_data['email']
            ms = b.cleaned_data['message']
            subject = companyname
            message = ms
            email_from = EMAIL_HOST_USER  # from
            send_mail(subject, message, email_from, [em])
            return redirect(success)
    return render(request, 'email.html', {'a': email})


def removeapply(request, id):
    a = jobapplymodel.objects.get(id=id)
    a.delete()
    return HttpResponse("Removed successfully")



def viecompanies(request):
    a = regmodel.objects.all()

    return render(request,'viewcompanies.html',{'a':a})
