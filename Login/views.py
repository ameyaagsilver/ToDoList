from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from pyasn1.type.univ import Null
import pyrebase
from django.contrib import auth
from django.templatetags.static import static

from ToDoList.settings import STATIC_ROOT


class toDoData:
    id: str
    Description : str
    Task : str
    isDone : bool


firebaseConfig = {
    "apiKey": "AIzaSyCW1vFED_-zRJWoY8GHj8ycYsuH01Spnpw",
    "authDomain": "to-do-list-3546a.firebaseapp.com",
    "databaseURL": "https://to-do-list-3546a.firebaseio.com",
    "projectId": "to-do-list-3546a",
    "storageBucket": "to-do-list-3546a.appspot.com",
    "messagingSenderId": "447584694516",
    "appId": "1:447584694516:web:f56d8c08b7c51d576e6ea1",
    "measurementId": "G-2XKMK8G1DT"
  };
cred = credentials.Certificate(STATIC_ROOT +'serviceAccountKey.json')
fapp = firebase_admin.initialize_app(cred)
db = firestore.client()

firebase = pyrebase.initialize_app(firebaseConfig)
# db = firebase.database()
authe = firebase.auth()


def login(request):
    return render(request, 'login/login.html')

def testSignUp(request):
    return render(request, "login/testSignUp.html")

def postSignUp(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    # try:
    #     user = authe.create_user_with_email_and_password(email, password)
    # except:
    #     message="Try again!!!Unable to sign you up"
    #     return render(request, "login/testSignUp.html", {"message" : message})
    user = authe.create_user_with_email_and_password(email, password)
    user_id = user['localId']
    databaseRef = db.collection('ToDo').document(user_id).collection('toDoList').document('initDoc')
    print(databaseRef.set({'init':"Reject this specific document from your To Do List"}))
    return render(request, "login/testLogin.html")

def testLogin(request):
    return render(request, 'login/testLogin.html')

def postLogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        user = authe.sign_in_with_email_and_password(email, password)
    except:
        message = "Invalid credentials"
        return render(request, 'login/testLogin.html', {"message":message})
    # print(user)
    # session_id = user['idToken']
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, 'login/welcome.html', {"email":email})

def logout(request):
    auth.logout(request)
    try:
        del request.session['uid']
    except:
        pass
    return render(request, "login/testLogin.html")

# def testingSessionId(request):
#     # print("This is testingSessionId page")
#     # print("Session local Id is", request.session['uid'])
#     user_id = request.session['uid']
#     print("***********")
#     # print(user_id, " == user ID")
#     # user = auth.get_user(user_id)
#     user=authe.get_account_info(user_id)
#     print(user['users'][0]['localId'])
#     # addTestData(user['users'][0]['localId'])
#     return render(request, "login/testingSessionId.html")

def testData(request):
    docs = db.collection('ToDo').document('cdGEBsrZ5rErR27rqjUN').collection('toDoList').stream()
    d = []
    # print(docs)
    for doc in docs:
        tempObject = toDoData()
        tempObject.Description = doc.to_dict()['Description']
        tempObject.isDone = doc.to_dict()['isDone']
        tempObject.Task = doc.to_dict()['Task']
        d.append(tempObject)
    # print("**********************************1")
    # print(d)
    # print("**********************************2")
    return render(request, 'login/testData.html', {'d':d})
    # return render(request, 'login/testData.html')

def toDoList(request):
    user_id = request.session['uid']
    user=authe.get_account_info(user_id)
    docs = db.collection('ToDo').document(user['users'][0]['localId']).collection('toDoList').stream()
    d = []
    print(docs)
    for doc in docs:
        tempObject = toDoData()
        if doc.id == "initDoc":
            continue
        tempObject.id = doc.id
        tempObject.Description = doc.to_dict()['Description']
        tempObject.isDone = doc.to_dict()['isDone']
        tempObject.Task = doc.to_dict()['Task']
        d.append(tempObject)
    return render(request, 'login/toDoList.html', {'d':d})

def addTestData(user_id):
    databaseRef = db.collection('ToDo').document(user_id).collection('toDoList')
    databaseRef.add({"Description":"Wash all clothes by 530pm...","Task":"Washing Clothes", "isDone":False})
    databaseRef.add({"Description":"Write physics journal","Task":"Wrtie journal", "isDone":False})
    databaseRef.add({"Description":"Sweep the floor by 455pm..","Task":"Sweeping", "isDone":False})

def addData(request):
    task = request.POST.get('Task')
    description = request.POST.get('Description')
    isDone = False
    user = authe.get_account_info(request.session['uid'])
    user_id = user['users'][0]['localId']
    databaseRef = db.collection('ToDo').document(user_id).collection('toDoList')
    databaseRef.add({"Description":description, "Task":task, "isDone":isDone})
    renderPage = toDoList(request)
    return renderPage

def deleteData(request):
    user = authe.get_account_info(request.session['uid'])
    user_id = user['users'][0]['localId']

    docId = request.POST.get('docId')
    databaseRef = db.collection('ToDo').document(user_id).collection('toDoList').document(docId)
    databaseRef.delete()

    renderPage = toDoList(request)
    return renderPage