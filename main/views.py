from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import ToDoList, Item
from main.form import CreateNewList 
# from main.form import CreateNewList , NewItem
from django.contrib import messages

# Create your views here.
# is it request or response that will come inside this view functions
# def index(response):
# def index(response ,id):
# # def index(request ,id):
# # def index(request ,name):
   
#     # return HttpResponse("This is Martian, trying to be more curious!")
#     # return HttpResponse("This is the id from url", id) -> it will not work because it is not a printstatement, it will return or render a string on the webpage.
#     # So we can only pass string into it.
    
#     #### integer example
#     # return HttpResponse(f"This is the id from url {id}")

#     ####### string example

#     # return HttpResponse(f"This is Martian trying to be more curious and wanna be like {name}")
#     # object = ToDoList.objects.all().get(id = id).item_set.all().values_list("text",flat = True)
#     # # you don't need docstring for storing this -> list = """ """
#     # list = ""
#     # for item_no, items in enumerate(object, start = 1):
#     #     list+=str(item_no) +": " + items + "\n"
        
#     # print(list)
        
#     """
#         This is the result for id = 4, which is getting stored in our list, but it is not showing in the
#         same way in our webpage, it is getting rendered in one line.
#         # result of print(list)
#             1: Click more portraits
#             2: Practice Light Painting
#             3: Go for photowalk
#     """

#     # return HttpResponse(list)
#     return render(response, 'main/base.html', {})

## dynamic index page for viewing the todolist items and creating the items in a todolist
def index(response ,id):
    
    ls = ToDoList.objects.all().get(id = id)
    print(ls)
    if ls in response.user.todolist.all():

        if response.method == "POST":
            # printing the dictionary 
            print(response.POST)
            # changes save, or update check button
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c"+str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()

            # if new item was created
            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                # validating it
                if len(txt)>2 and len(txt)<=300:
                    t = ls.item_set.create(text = txt, complete = False)
                    t.save()
                else:
                    print("invalid")

        return render(response,"main/list.html",{"ls":ls})
    else:
        return render(response,"main/view.html",{})


    
# thsi is the wrong way -> here we are trying to use the custom form, so the prebuild form will not work
# def index(response ,id):
#     # ls = ToDoList.objects.all().get(id = id)
#     # below is just for testing
#     # # ls = ToDoList.objects.all().get(id = id).item_set.all().values_list()
#     # print("ls is ", ls)
    
#     # return render(response, "main/list.html",{"ls":ls})

#     ## dynamic index page for viewing the todolist items and creating the items in a todolist
#     ls = ToDoList.objects.all().get(id = id)
#     print(ls)

#     if response.method == "POST":
#             form = NewItem(response.POST)
#             text = form.cleaned_data("text")
#             check = form.cleaned_data("check")
#             t = ls.item_set.create(text = text, complete = check)
#             t.save()
#             form = NewItem()
#             return render(response, "main/list.html", {"form":form})
#     else:
#         form = NewItem()
#         return render(response, "main/list.html", {"form":form})

def home(response):
    return render(response, 'main/home.html', {})


##   Made by Martian according to her understanding and had used message framework
# def create(response):
    
#     if response.method == "POST":

#         # form = Create(response.POST)
#         form = Create()
#         # all_message = messages.success(response, "Item successfully created.")
#         # return render(response, "main/create.html", messages.success(response, "Item successfully created."))
#         return render(response, "main/create.html", {"form":form} , messages.success(response, "Item successfully created."))
#         # return render(response, "main/create.html", {"form":form, "all_message":all_message})

#         # return render(response, "main/create.html", {"form": form})
#     else:
#         form = Create()
#         return render(response, "main/create.html", {"form":form})
    

def create(response):
    
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            t = ToDoList(name = name)
            t.save()
            response.user.todolist.add(t)
        # *** otherwise we can redirect the user to do created to do list
        return HttpResponseRedirect("/%i" % t.id)

        # # *** Below is the code where i want the user to see the same create to do list page with the messages successfully created.
            
        # # if will create a blank page and will show the message, saying to do list created successfully.
        # form = CreateNewList()

        # ## *** Note: Both of the below codes were working properly, it we don't pass messages tag or code inside the render,
        # #  then also it is working properly.

        # # *** We need to pass the message tag as it is, we can't put it under some variable and try to pass it like dictionary, it won't work otherwise. ***

        # # messages.success(response, "To do list successfully created.")
        # # return render(response, "main/create.html", {"form":form})
        # return render(response, "main/create.html", {"form":form} ,  messages.success(response, "To do list successfully created."))

    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})

def view(response):
    return render(response, "main/view.html",{})