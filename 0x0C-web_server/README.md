# Web Servers

## Main Role of a Web Server
A web server acts as the intermediary between web clients (browsers) and web resources (websites, applications) on the internet. It receives HTTP requests from clients, interprets them, retrieves the requested resources, and delivers the response back.

## Child Processes

### What is a Child Process?
In web servers, a child process is a new process created by the parent (web server) to handle individual client requests.

### Why are Child Processes Used?
- **Efficiency:** Avoids overhead of creating new processes for each request.
- **Scalability:** Handles high traffic volumes by distributing requests among multiple processes.
- **Isolation:** Errors or crashes in a child process do not affect the parent or other children.

## HTTP Requests

### Main HTTP Requests:
- **GET:** Retrieves a resource.
- **POST:** Submits data (e.g., form submissions).
- **PUT:** Updates an existing resource.
- **PATCH:** Makes partial modifications.
- **DELETE:** Removes a resource.
- **HEAD:** Requests header information only.
- **OPTIONS:** Lists supported methods and options for the resource.

## DNS (Domain Name System)

### What is DNS?
DNS translates human-readable domain names into machine-readable IP addresses.

### Main Role of DNS
DNS acts like the internet's phone book, allowing browsers and applications to find the correct web servers.

## DNS Record Types

- **A (Address):** Maps a domain name to an IPv4 address.
- **CNAME (Canonical Name):** Creates an alias for a domain name, pointing it to another existing domain name.
- **TXT (Text):** Stores arbitrary text data associated with a domain name (e.g., email verification).
- **MX (Mail Exchange):** Specifies the mail servers responsible for handling email for a domain name.

## Additional Notes
- Web servers can handle other protocols besides HTTP (e.g., FTP, SMTP).
- DNS is a distributed system, ensuring resilience against individual server failures.
