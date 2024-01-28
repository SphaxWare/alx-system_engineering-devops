![A](2-secured_and_monitored_web_infrastructure.jpeg)
# Additional elements
- Firewalls
  - We added firewalls to prevent unauthorized access and protect against cyber threats.
- SSL Certificate (for HTTPS)
  - Encrypts data transmitted between clients and servers.
- Monitoring clients
  - Monitoring is used to track the performance, availability, and security of the infrastructure.
# Specifics about this infrastructure
- What are firewalls for?
  - Firewall 1 (Before Load Balancer):
    - Acts as the first line of defense at the network perimeter.
    - Controls and filters incoming traffic from external sources before it reaches the load balancer.
    - Enforces security policies and prevents unauthorized access.
  - Firewalls 2 and 3 (After Load Balancer):
    - Provide an additional layer of security within the internal network.
    - Control and monitor traffic between the load balancer and the internal servers.
    - Protect against unauthorized access and potential threats within the network.
- Why is the traffic served over HTTPS?
  -  SSL Certificate (Installed on Load Balancer):
    - Enables HTTPS by encrypting the data transmitted between clients and the load balancer.
    - Ensures data confidentiality, integrity, and authenticity.
    - Protects sensitive information from eavesdropping and tampering.
- What monitoring is used for?
  - Gather data from various sources, such as logs, metrics, and performance indicators.
  - Provide insights into the behavior and status of the system.
# Issues
- Why terminating SSL at the load balancer level is an issue
  - Terminating SSL (SSL offloading) at the load balancer means that the communication between the load balancer and the internal servers is not encrypted.
- Why having only one MySQL server capable of accepting writes is an issue
  - Having a single MySQL server capable of accepting writes creates a single point of failure.
- Why having servers with all the same components (database, web server, and application server) might be a problem
  - If all servers share the same components, they are vulnerable to the same software vulnerabilities, exploits, and security threats.
  - A single vulnerability could potentially impact all servers simultaneously.
