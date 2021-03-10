from django.shortcuts import redirect, render
from .models import Courses, Subjects
from account.models import Schools, Genie_Users

# Create your views here.
def register(request):
    if request.method == 'POST':
        
        img = request.FILES.get("profimage")
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        gender = request.POST['gender']
        email = request.POST['email']
        phone = request.POST['telephone']
        cpassword = request.POST['cpassword']
        subjects = request.POST.getlist('subjects')
        school = request.POST['schools']
        course = request.POST['courses']
        cutoff = request.POST['cutoff']
        jambscore = request.POST['jambscore']
        aspire = request.POST['wantscore']

        if password == cpassword:
            
            print("Correct Passwords\n")
            # if User_info.objects.filter(username=username).exists() or User.objects.filter(username=username).exists():
            #     print("User Name Taken\n")

            if Genie_Users.objects.filter(email=email).exists():
                print("Email Taken")
                # messages.info(request, "Email Taken")
                
            else:

                #print(subjects)
                #print(type(subjects))

              
                pschool = Schools.objects.get(short_name=school)
                pcourse = Courses.objects.get(short_name=course)
                Guser = Genie_Users.objects.create(
                    profileimg=img,
                    first_name=first_name, 
                    last_name=last_name,
                    username=username, 
                    password=password, 
                    email=email,
                    gender=gender, 
                    phone_number=phone, 
                    institution=pschool,
                    course=pcourse,
                    cutoff=cutoff,
                    jamb_score=jambscore,
                    asp_score=aspire)
                Guser.save()

                for e in subjects:
                    # print(e)
                    sub = Subjects.objects.get(code=e)
                    # print(sub)
                    Guser.subjects.add(sub)
                

               
                print("User created: Information Saved")
                # messages.info(request, "User created")
                return redirect('login')
        else:
            print("Incorrect\n")
        
        #print(locals())
        # return redirect('register')


    all_subjects = Subjects.objects.all()
    all_schools = Schools.objects.all()
    all_courses = Courses.objects.all()
    try:
        del request.session['GenieUser']
    except:
        pass
    return render(request, 'account/regr.html', {'subjects':all_subjects, 'schools':all_schools, 'courses':all_courses})


def registerr(request):
   
    return render(request, 'account/register.html', {})


def login(request):
    if request.method == 'POST':
        # print(request.POST.keys())
        email = request.POST['email']
        password = request.POST['password']

        # print(locals())

        if Genie_Users.objects.filter(email=email, password=password).exists():
            User = Genie_Users.objects.get(email=email)
            request.session['GenieUser'] = User.id
            return redirect('dashboard')
    
    try:
        del request.session['GenieUser']
        
    except: pass
    

    response = render(request, 'account/login.html', {})
    response.delete_cookie('subjects') # clear cookie

    return response
