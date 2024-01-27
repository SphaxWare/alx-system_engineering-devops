# Additions
- We added another server to fix the SPOF probleme and prevent downtime when maintenance is needed and a load-balancer (HAProxy) to handle the incoming traffic better.
- Our load-balancer is configured with Round Robin algorithme which is a simple algorithme that distributes incoming requests among the available servers.
- <p>My load-balancer is enabling an Active-Active setup.In an Active-Active setup, both servers are actively handling incoming requests simultaneously providing better performance and scalability.In an Active-Passive setup, one server (the active server) actively handles incoming requests, while the other server (the passive server) remains in standby mode.The passive server becomes active only if the active server fails or is taken offline intentionally.</p>
- Primary-Replica (Master-Slave) cluster works by setting the Primary node (Master) responsible for read and write operations, while the Replica nodes (Slaves) replicate data from the Primary and handle read operations.
- Difference Between Primary and Replica Nodes:
  - Primary Node: Handles write operations and serves as the authoritative source for data.
  - Replica Node: Replicates data from the Primary and handles read operations.
