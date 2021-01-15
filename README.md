# SFIA2





Requirements
- An Asana board or equivalent Kanban board tech (Trello board)
- An application that is fully integrated using the Feature-Branch model into a Version Control System which will be built through a CI server (Jenkins) and deployed to a cloud-based virtual machine (GCP Virtual machines)
- If a change is made to a codebase, webhooks should be used so Jenkins recreates and redeploys the changed application
- Project must follow the service-oriented architecture that has been asked for (4 services)
- Project must be deployed using containerisation (Docker) and an orchestration tool (Docker Swarm)
- Create an Ansible Playbook that will provision the environment that your application needs to run
- Project must make use of a reverse proxy (NGINX) to make your application accessible to the user

Must be able to demonstrate the working CI pipeline that you have been able to build by rolling out updates to the system without interrupting the user experience

Produce reports of any designs and work created.

Trello board:
https://trello.com/b/goLwBUbZ/qa-sfia2 

My idea:
Service 1 is the User Interface
Service 2 generates a random footballer strength (Reflexes, Defending, Crossing, Speed, Shooting, Passing) 
Service 3 generates a random footballer weakness (Reflexes, Defending, Crossing, Speed, Shooting, Passing)
Service 4 generates a footballer's ideal position with their random strength and weakness (Goalkeeper, Defender, Full back, Midfielder, Winger, Striker)
