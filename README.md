### Description: An app that allows user to share photos taken at events.
---

api breaks in to 2 main parts 
-account 
-events

---

# list of all api calls
API List:
-create-account

---


All infomation should be sent to URL using json style

**URL: https://site-name/v1/create-account**
- Description: Api call allows to create an account. The call takes a username, password and email. Received success tag information can either be "True" or "False." The Description tag will return information on the outcome of the request. If failure will return why it failed. if Success then will return "Account created".

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
```






