from django.http import  JsonResponse
from rest_framework.decorators import api_view
from .models import users,follow,blogs,private_blogs,groups

import bcrypt


@api_view(['POST'])
# Create your views here.
def users_info(request):
    if(request.method=="POST"):
        if request.headers.get("token"):
            id=request.POST['id']
            token=request.headers.get("token")
            user=users.objects.filter(id=id)
            if(len(user)==0):
                return JsonResponse({"status":False,"error":"Invalid user id"})
            else:
                if not token==user[0].token:
                    return JsonResponse({"status":False,"error":"Invalid Token"})
                response={}
                response['id']=user[0].id
                response['username']=user[0].username
                response['firstname']=user[0].firstname
                response['lastname']=user[0].lastname
                blogs_return=get_blogs(user[0])
                get_followers_id(user[0])
                userdetail={}
                userdetail['id']=user[0].id
                userdetail['description']=user[0].aboutme
                userdetail['url']=user[0].profileimageurl
                userdetail['house']=user[0].house
                response['blogs']=blogs_return
                response['user-detail']=userdetail
                # print(response)
                return JsonResponse({"status":True,"info":response})

        else:
            return JsonResponse({"status":False,"error":"Token not provided"})
    else:
        return JsonResponse({"status":False,"error":"This route accepts only Post requests"})



@api_view(['POST'])
def register(request):
    if request.method == "POST":
        user = users()
        # print(request.data)
        email = request.POST['email']
        user1 = users.objects.filter(email=email)
        if len(user1):
            return JsonResponse({"error": "user already exist", "status": False})
        user.firstname = request.POST['firstname']
        user.lastname = request.POST['lastname']
        user.email = request.POST['email']
        user.username = request.POST['username']
        user.house = request.POST['house']
        password = request.POST['password'].encode('utf-8')
        user.password = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')
        user.token = bcrypt.hashpw((user.password + password.decode('utf-8')).encode('utf-8'), bcrypt.gensalt()).decode(
            'utf-8')
        user.profileimageurl = request.POST['profileimageurl']
        user.aboutme = request.POST['aboutme']

        user.save()
        return JsonResponse({"status": True, "token": user.token,"user-id":user.id})
    else:
        return JsonResponse("This route accepts only post request")


@api_view(['POST'])
def signin(request):
    if request.method == "POST":
        print(request.headers.get('token'))
        email = request.POST['email']
        user = users.objects.filter(email=email)

        if len(user) == 0:
            return JsonResponse({"status": False, "error": "User not registered"})
        else:
            password = user[0].password
            ok = bcrypt.checkpw(request.POST['password'].encode('utf-8'), password.encode('utf-8'))
            print(ok)
            if ok:
                return JsonResponse({"status": ok, "token": user[0].token,'user-id':user[0].id})
            else:
                return JsonResponse({"status": ok, "error": "incorrect password"})
    else:
        return JsonResponse("This route accepts only post request")


@api_view(['POST'])
def add_blogs(request):
    if authenticate(request):
        blog=blogs()
        blog.content=request.POST['content']
        blog.blogimageurl=request.POST['blogimage']
        blog.title=request.POST['blogtitle']
        blog.category=request.POST['category']
        id = request.POST['id']
        user = users.objects.get(id=id)
        blog.writtenby=user
        if request.POST['public'].lower()=='false':
            #Note: This part need an group_id field in the request
            blog.public=False
            blog.save()
            # print(request.POST['group_id'])
            if(request.data.get('group_id')!=None):
                group_id = groups.objects.get(id=request.POST['group_id'])
                print(group_id)
                private_blog = private_blogs()
                private_blog.blogid = blog
                private_blog.groupid = group_id
                private_blog.save()
            else:
                return JsonResponse({"status":False,"error":"Blog is private but group id is not provided."})
        else:
            blog.public=True
            blog.save()

        # if blog.public==True:
        return JsonResponse({"status":True})
    else:
        return JsonResponse({"status": False})




#Helper Functions
def get_followers_id(user):
    followers=follow.objects.filter(following=user)
    followers=[x for x in followers]
    followers_return=[]
    for x in followers:
        temp={}
        temp['id']=x.id
        followers_return.append(temp)
    print(followers[0].username)

def get_blogs(user):
    blog=blogs.objects.filter(writtenby=user)
    blogs_return=[]
    for x in blog:
        temp={}
        temp['Blog-id']=x.id
        temp['Blog-url']=x.blogimageurl
        temp['title']=x.title
        temp['category']=x.category
        temp['date']=x.date
        author={}
        author['username']=user.username
        author['firstname']=user.firstname
        author['lastname']=user.lastname
        author['email']=user.email
        user_detail={}
        user_detail['id']=user.id
        user_detail['url']=user.profileimageurl
        author['user_detail']=user_detail
        temp['author']=author
        temp['status']=x.status
        blogs_return.append(temp)
    return blogs_return

def authenticate(request):
    request_token=request.headers.get('token')
    if request_token==None:
        return False
    else:
        
        id = request.data.get('id')
        if id==None:
            return False
            
        user = users.objects.filter(id=id)
        if len(user)==0:
            return False
        else:
            if not request_token == user[0].token:
                return False
            else:
                return True

