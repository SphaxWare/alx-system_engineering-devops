## General
- What is a server
	- A server is a computer or system that provides services or resources to other computers, known as clients, over a network. Servers are designed to handle specific tasks or applications, such as serving web pages, processing database queries, managing emails, etc.
- Where servers usually live
	- Servers can physically reside in data centers or server rooms. They can also be hosted in the cloud, providing remote access and scalability. The location can vary, but servers are typically maintained in controlled environments with adequate power, cooling, and security measures.
- What is SSH
	- SSH (Secure Shell) is a cryptographic network protocol that provides a secure way to access and manage network devices and servers over an unsecured network. It encrypts the data transmitted between the client and server, preventing unauthorized access and protecting the integrity of the communication.
- How to create an SSH RSA key pair
	- You can create an SSH RSA key pair using the ssh-keygen command. Open a terminal and run:
```
ssh-keygen -t rsa -b 2048
```
Follow the prompts to specify the file location and, if needed, set a passphrase.
- How to connect to a remote host using an SSH RSA key pair
	- After generating the key pair, you need to copy the public key to the remote server's ~/.ssh/authorized_keys file. Use the following command:
```
ssh-copy-id -i ~/.ssh/id_rsa.pub user@remote_host
```
- The advantage of using #!/usr/bin/env bash instead of /bin/bash
	- '#!/usr/bin/env bash is more flexible than specifying the absolute path like /bin/bash. It allows the system to search for the bash interpreter in the user's PATH environment variable. This can be useful in cases where the location of the bash executable may vary across different systems or environments. Using env is considered a more portable and adaptable approach.
