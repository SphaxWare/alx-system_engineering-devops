![simple web stack](0-simple_web_stack.PNG)
# About this infrastructure
## What is a server
a server is a computer only accessible by a network,and it provides functionality for other devices called clients.
## What is the role of the domain name
the domain name serves as human-readable text that represent an IP adresse of a server or website on the internet.
## What type of DNS record www is in www.foobar.com
www is a CNAME record
## What is the role of the web server
The role of the web server is to listen for HTTP requests from the user and direct them to the appropriate resources like the application server.
## What is the role of the application server
The role of the application server is to execute the business logic of the application and communic1te with the database to retrieve or update data needed to respond for the user's request.
## What is the role of the database
The role of the database is storing and managing the web application's data
## What is the server using to communicate with the computer of the user requesting the website
the server is using the HTTP to communicate with the computer of the user requesting the website.
# Issues with this infrastructure
## SPOF
The whole system relies on a single server. If the server fails, the entire website is down.
## Downtime when maintenance needed (like deploying new code web server needs to be restarted
Deploying new code or performing maintenance may require restarting the web server, leading to downtime during the restart process.
## Cannot scale if too much incoming traffic
This infrastructure may struggle to handle a significant increase in incoming traffic as it lacks mechanisms for horizontal scalability.
