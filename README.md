# Google Search App

## Short description: 
- This app returns the first 10 Google results based on a variable keyword (app_google_results.py)
- Incoming requests (**GET** / **POST**) are processed via an endpoint (endpoint.py)

## Function: 
- First, via a login page (http://127.0.0.1:5000/login), a user name and the password "password" must be entered as a GET-Request according this scheme:  {'user': auth.username, 'password' : 'password'}
- The issued token must then be sent back as a POST request with the variable keyword to the route  http://127.0.0.1:5000/
  - The token is passed as a parameter according this scheme: {'Token': issued token}  
  (e.g. http://127.0.0.1:5000/?Token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiTWVsYW5pZSJ9.2Qzbbyco8YiBn3tWejoodcIw0la44xzHqTOX1F_sD7U)
  - The variable keyword as a form-data in the request body according this scheme: {'keyword' : 'keyword'}
- After sending the POST request the token will be decoded with a secret key
- If all ordered data are present and valid, the token is valid for exactly 2 minutes 
  - For this purpose, after automatic control, the app will output the first 10 Google results as **JSON** string for the corresponding keyword  
  - This **JSON** string will be returned as a list of result objects with its position, url and top domain level

### Testing: 
- Start endpoint.py and call http://127.0.0.1:5000/login
- Enter any username and the password "password"
- Then create a POST request with the result token as a parameter and your desired keyword as a form-data to http://127.0.0.1:5000/  
 

### JSON scheme and example:
  - Keyword: **Botnet**

<img src="JSON.PNG" height="973" width="699" >
