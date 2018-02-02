# Description: An app that allows user to share photos taken at events.
---

### Api breaks in to 2 main parts 
- account 
- events

---

### list of all api calls
- create-account
- send-access-code
- activate-account

---
### Corrent order of api call to make 
- create-account ->
 send-access-code - > activate-account
---

All information should be sent to URL using json style

**URL: https://site-name/v1/create-account**
- Description: Api call allows to create an account. The call takes a username, password and email. Received success tag information can either be "True" or "False." The Description tag will return information on the outcome of the request.if Success then will return "Account created". If failure will return why it failed. It will also return a "status code" which identifies what went wrong. "1" means email taken. "-1" means that something else is wrong and to look at discription, mainly used for testing. Password should be checked before request to api is made. 

```
Send data: 
{	
	"Username" : "String",
	"Password" : "String",
	"Email" : "String"
}
Receive data: 
{
	"Success" : true (boolean),
	"Description" : "Info about request"
}
Receive data: 
{
	"Success" : false (boolean),
	"Status code" : -1,1,(int),
	"Description" : "Info about request"
}
```

**URL: https://site-name/v1/send-access-code**
- Description: Send a verification number to a phone number.Some failures can occur if email sent is not in database, or database was updated while trying to add the verification number to the account. Lastly, an error will occur if the account is already activated. This API call should only be called before an account is activated 
```
Send data: 
{	
	"Phone_number" : "String",
	"Email" : "String"
}
Receive data: 
{
	"Success" : true (boolean),
	"Description" : "Info about request"
}
Receive data: 
{
	"Success" : false (boolean),
	"Status code" : -1,(int),
	"Description" : "Info about request"
}
```

**URL: https://site-name/v1/activate-account**
- Description: will return 1 if issues with access code.
```
Send data: 
{	
	"Phone_number" : "String",
	"Email" : "String",
	"Access_code" : "String"
}
Receive data: 
{
	"Success" : true (boolean),
	"Description" : "Info about request"
	"Id":"Id number of user(Stirng)"
}
Receive data: 
{
	"Success" : false (boolean),
	"Status code" : -1,1,(int)
	"Description" : "Info about request"
}
```

**URL: https://site-name/v1/login**
- Description: Added phone number to account. 
```
Send data: 
{	
	"Password" : "String",
	"Email" : "String"
}

Receive data: 
{
	"Success" : true (boolean),
	"Description" : "Info about request"
	"Id":"Id number of user(Stirng)"
}
Receive data: 
{
	"Success" : false (boolean),
	"Status code" : -1,1,2(int)
	"Description" : "Info about request"
}
```



