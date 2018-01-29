# Description: An app that allows user to share photos taken at events.
---

### Api breaks in to 2 main parts 
- account 
- events

---

### list of all api calls
- create-account

---


All infomation should be sent to URL using json style

**URL: https://site-name/v1/create-account**
- Description: Api call allows to create an account. The call takes a username, password and email. Received success tag information can either be "True" or "False." The Description tag will return information on the outcome of the request.if Success then will return "Account created". If failure will return why it failed. It will also return a "status code" which identifies what went wrong. "1" means username taken. "2" means email taken. password should be checked before request to api is made. 

```
Send data: 
{	
	"Username" : "String",
	"Password" : "String"
	"Email" : "string"
}
Receive data: 
{
	"Success" : "True" ,
	"Description" : "Info about request"
}
Receive data: 
{
	"Success" : "False" ,
	"Status code" : "1,2"
	"Description" : "Info about request"
}
```






