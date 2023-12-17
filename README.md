# ChitChat - A real time chat application...
This is my final project for CS50W. With this project two or more users can send and receive messages in real time.  
The project was built using Django as a backend framework and JavaScript as a frontend programming language. All generated information are saved in database (SQLite by default). 
[Demo Video](https://youtu.be/eGhKah4_PFU)  
Contents of this readme:-  
[Distinctiveness and complexity](#distinctiveness-and-complexity)  
[Installation and how to run](#installation-and-how-to-run)  
[File Structure](#file-structure)  
[Features](#features)  



### Distinctiveness and complexity
My project is complex, why?
- This Project utilizes django channels. Channels is a project that takes Django and extends its abilities beyond HTTP - to handle WebSockets, chat protocols, IoT protocols, and more.
- My project uses the websocket handshaking protocol to send and receive messages
```
Diagram for websocket handshake:-
Client                                                     Server
   |                                                          |
   |     WebSocket Handshake                                  |
   |     (HTTP GET with Upgrade header)                       |
   |--------------------------------------------------------->|
   |                                                          |
   |     WebSocket Handshake                                  |
   |     (HTTP 101 Switching Protocols)                       |
   |<---------------------------------------------------------|
   |                                                          |
   |                                                          |
   |           WebSocket Open                                 |
   |<---------------------------------------------------------|
   |                                                          |
   |                                                          |
   |           WebSocket Data                                 |
   |<---------------------------------------------------------|
   |                                                          |
```
- I created consumers and asynchronously connected them to send and receive messages in real time.
- I have made passwords to enter rooms to avoid wrong people joining in.
- There are also validations to create uniquely named rooms.
- And a voice typing feature
- With all the messages being stored in the database, so even if application closes the messages are saved until the database is deleted.

How is it different from other cs50w projects?  
- In this project I am not selling pizzas and there is not a shopping cart/watchlist or any tangible product, so it is different than the old CS50w pizza project and commerce project 2 in new cs50w.
- This project is significantly different than the network project of cs50w as it uses django channels and websockets to send and receive messages in real time with a voice type feature whereas the network project aims to create a social media application for uploading posts and liking them, and it does not have any features that I have implemented in my Final Project.  

In conclusion, my project is not based on any prior cs50w project and uses technologies that are not implemented in any prior cs50w project.

Scalability: The current configuration utilizes SQLite as the database, but it's flexible and can be switched to another option like PostgreSQL or MySQL by incorporating an additional Docker container. The Django Channels feature employs an In-Memory layer, which can be substituted with a different option like Redis, but this would necessitate the installation of an additional library.

### Installation and how to run
Prerequisite: You may want to run a virtual environment before installing dependencies. And also have a working microphone to access voice type feature.
 - Install project dependencies by running `pip install -r requirements.txt`.  
 Dependencies include Django and Channels(3.0.4) module that allows Django to work with channels.
  - Make and apply migrations by running `python manage.py makemigrations` and `python manage.py migrate`.
  - Create superuser with `python manage.py createsuperuser`. This step is optional.
  - Go to website address and register an account.

### File Structure
What Each File Contains:-  
 ``chatapp`` (Main Application Directory)   
   - ``__init__.py``(Packages Data)  
   -  ``__pycache__`` (Cached data after running)  
   -  ``asgi.py`` (ProtocolTypeRouter to forward http, websocket urls asynchronously)           
   -  ``settings.py`` (All Directories, Apps, & settings config. info.)  
   - ``urls.py`` (Root directory urls.py)  
   - ``wsgi.py`` (Rules of Application for deploying)   

``manage.py``

 ``chat``   (Application Directory for Web App Layout and User Auth.)  
   - ``__init__.py``   (Packages Data)  
   - ``__pycache__`` (cached Data)  
   - ``admin.py`` (No models in this Django App, so nothing to register)  
   - ``apps.py`` (Application config. method)  
   - ``forms.py``(Signup Form Declaration for user authentication)  
   - ``migrations`` (Cached Data After Migration)  
   - ``models.py`` (No models used in this Django App)  
   - ``static`` (Contains CSS File for this App)  
      &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; └── ``styles.css`` (CSS written for html templates)  
   -  ``templates/chat`` (Layout, Landing Page, Login, & SingUp
        templates)  
          &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;├── ``index.html`` (Landing Page HTML and css written in style tags and inline styles)  
           &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;├── ``layout.html`` (Base HTML Template)  
          &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;├── ``login.html``(Login Page HTML and css written in style tags and inline styles)  
          &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;└── ``signup.html``(Sign Up Page HTML and css written in style tags and inline styles)  
   - ``tests.py``(No tests written, it's empty)  
  - ``urls.py``(Routing Urls for this application, & also using inbuilt login and logout functions)  
   - ``views.py``(View for user Sign Up Logic with inbuilt login function and view for landing page)  

 ``room``(Application Directory for the Main Functionality of the chat app i.e. rooms for chatting)  
   - ``__init__.py``(Packages Data)  
   - ``__pycache__``(Cached data)  
   - ``admin.py``(2 models Registered Room and Message)  
   - ``apps.py``(Application config. method)  
   - ``consumers.py``(Python script to send and receive messages from channels)  
   - ``migrations``(Cached Data After Migration)  
   - ``models.py``(2 models made Room and Message details in Features Section)  
   - ``routing.py``(url pattern of the consumers.py file)  
   - ``templates/room``(Templates for the All rooms page and each room)  
          &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;├── ``room.html``(HTML for each room css written in style tags, inline style, and also scripts written for speech recognition, auto scrolling and websockets in javascript)  
          &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;└── ``rooms.html``(HTML for all rooms page and to create, delete, & join rooms and css written in style tags and inline styles)  
   - ``tests.py``(No tests written its empty)  
   - ``urls.py``(Urls for routing the rooms, create, join, delete, and each room page)  
   - ``views.py``(Views for rooms, creating rooms, deleting rooms, joining rooms, and each room storing messages in the database)  


### Features
Models Used:-  
Models are made in the room App in models.py folder:  
1. Room Model - Create each room for sending and receiving messages
```python
class Room(models.Model): 
    name=models.CharField(max_length=64)
    slug=models.SlugField(unique=True)
    passwords=models.CharField(max_length=64)
```
2. Message Model - Storing Messages in the database ordered by date added.
```python
class Message(models.Model):
    room=models.ForeignKey(Room, related_name='messages',on_delete=models.CASCADE)
    user=models.ForeignKey(User, related_name='messages',on_delete=models.CASCADE)
    content=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('date_added',)
```

Features Implemented:-
1. User Authentication
2. All Rooms Page and join using password
3. Create a Room 
4. Delete a Room
5. Quick Join a room directly with name and password
6. Send and Receive Messages in Real Time
7. Voice Typing Feature
8. Storing Messages 
9. Mobile Responsiveness
10. Auto scrolling to bottom in messages

