# PythonAssignment3
TITLE
The work of Assignment3 was done in the pair of Farabi Samalyk and Daniyar Issenov

Installation 

Python packages which were used to implement the project:

pyjwt (https://pyjwt.readthedocs.io/en/stable/)
flask (https://flask.palletsprojects.com/en/2.0.x/)
flask_sqlalchemy (https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
<img width="864" alt="image" src="https://user-images.githubusercontent.com/79573421/139110062-1e59b538-bd8c-489a-a137-db0f26b0e39b.png">

Example and description 

Web server provideы 2 routes

 login
 
After successful login( if login and password matches with a record in User Table), as response route should return html text: token: <token value> and store that token in the User Table
If provided login and password does not exist in the User Table, as a response route should return html text: Could not found a user with login: <login>

  protected
  
This route receive as a parameter token value
Token value needs to be passed over URL, 
e.g. http://127.0.01:5000/protected?token=24230ifdsjfjdsklfj43943ut943
This route return html text: <h1>Hello, token which is provided is correct </h1>, if as a parameter RIGHT token value is passed
This route return html text: <h1>Hello, Could not verify the token </h1>, if as a parameter WRONG token value is passed
<img width="1126" alt="image" src="https://user-images.githubusercontent.com/79573421/139116624-93cc925c-0104-42ff-8f29-9dccb3cb2a72.png">
