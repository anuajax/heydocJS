# SERVERLESS BACK-END 

We used AWS Lambda and AWS API-Gateway to implement server-less.
We followed microservice architecture for efficiency in development and data consistency. 

## Installation

1. Open AWS developer console.
2. Go to Lambda and create new lambda functions using Python 3.8 .
3. Upload additional packages by uploading as zip, wherever applicable.
4. Go to API-Gateway and create new REST-API, set lambda integration, use lambda proxy.
5. Set API routes as mentioned later in the doc.


## Usage

### /login
Redirects requests to login.py lambda function.

#### ->POST
Takes 3 arguments in request.
```python
{
  "flag" : "doc"/ "pat",
  "username" : "username",
  "password" : "password"
}
```
If username-password pair is valid it returns,
```python
{
  "success" : True,
}
```
Else
```python
{
  "success" : False,
}
```
### /search
Redirects requests to search.py lambda function.

#### ->POST
Takes 3 arguments in request.
```python
{
  "city" : "",
  "name" : "",
  "specialist" : ""
}
```
Scans the entire list of doctors and returns the list of doctors satisfying all the above criteria
```python
{
  "result" : ["doctors","..."]
}
```
### /app
Redirects requests to appointment.py lambda function.

#### ->POST
Takes 2 arguments in request.
```python
{
  "doc" : "",
  "pat" : "",
}
```
Adds new appointment in pending lists of both doctor and patient and returns a message according to flow and doctor and patient objects.
```python
{
  "result" : "message"
  "doc" : {},
  "pat" : {}
}
```
#### ->GET
Takes 2 arguments in request.
```python
{
  "doc" : "",
  "pat" : "",
}
```
Removes appointment from pending lists adds to approved lists for both doctor and patient and returns a message according to flow and doctor and patient objects.
```python
{
  "result" : "message"
  "doc" : {},
  "pat" : {}
}
```
#### ->DELETE
Takes 2 arguments in request.
```python
{
  "doc" : "",
  "pat" : "",
}
```
removes appointment from Approved lists adds to previous lists for both doctor and patient and returns a message according to flow and doctor and patient objects.
```python
{
  "result" : "message"
  "doc" : {},
  "pat" : {}
}
```
### /sign
Redirects requests to signInSignUp.py lambda function.

#### ->POST
Takes user data with additional flag attribute in request.
```python
{
  "flag" : "doc/pat",
  "..."
}
```
Saves user data to appropriate DynamoDB table pointed by flag if not already there and returns success Boolean.
```python
{
  "success" : True/False
}
```
#### ->GET
Takes 2 arguments in request.
```python
{
  "flag" : "doc"/"pat",
  "username" : "username",
}
```
Returns user data with success Boolean.
```python
{
  "success" : True/False,
  "..."
}
```
## License
[MIT](https://choosealicense.com/licenses/mit/)