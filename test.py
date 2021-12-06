import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("D:\Projects\ToDoList\Login\serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

ref = db.collection('ToDo').document('cdGEBsrZ5rErR27rqjUN').collection('toDoList')
# ref.set({
#     'name':'AMG',
#     'lName':'Gonal',
#     'age': 10
# })
docs = ref.stream()

# for doc in docs:
#     print('{} => {}'.format(doc.id, doc.to_dict()))

# TO ADD A DOC TO A COLLECTION
# user_id = 'user[]'
# databaseRef = db.collection('ToDo').document(user_id).collection('toDoList').document('intialDoc')
# databaseRef.add({'init':"This is false data"})


# TO DELETE A DOC FROM COLLECTION
# doc = 'onSUMHcP0mXjGWdjG2Vv'
# databaseRef = db.collection('ToDo').document(user_id).collection('toDoList').document(doc)
# databaseRef.delete()