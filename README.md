# TODO APP FLASK API

## Backgound

Creating a Python Flask application with Docker Compose is a great way to containerize and manage your web application's development environment. Docker Compose allows you to define and run multi-container Docker applications in a straightforward manner. Here's a description of a project that combines Python Flask with Docker Compose:

**Project Title**: Dockerized Python Flask Web Application with Docker Compose

**Description**:
In this project, we will develop a simple web application using Python and the Flask framework. Flask is a lightweight and easy-to-extend web framework that's ideal for building web applications, APIs, or microservices. We will containerize this application using Docker and manage the development environment and dependencies with Docker Compose.

**Key Components**:

1. **Python Flask Application**: We will create a basic Flask application that can serve web pages or APIs. This application can be customized based on your project's requirements.

2. **Docker**: Docker will be used to containerize our Flask application. Containers provide a consistent and isolated environment for running applications, making it easy to deploy across different platforms.

3. **Docker Compose**: Docker Compose will allow us to define, configure, and run multiple containers as a single application. We'll use it to manage our Flask application and any necessary services, such as databases or cache servers.

4. **Requirements.txt**: We will maintain a `requirements.txt` file that lists all Python dependencies required for our Flask application. Docker will use this file to install the necessary packages inside the container.

5. **Dockerfile**: We'll create a Dockerfile that defines how the Flask application container should be built. This file will include instructions for copying code, installing dependencies, and setting up the environment.

6. **docker-compose.yml**: This YAML file will define our multi-container application, including the Flask container, any service containers (e.g., a database), network configurations, and environment variables.

**Project Workflow**:

1. **Development**: Write and test your Flask application on your local machine. Make sure it runs correctly and handles all dependencies.

2. **Dockerize**: Create a Dockerfile for your Flask application. This file should include instructions for installing Python, copying your application code, and installing the required Python packages from `requirements.txt`.

3. **Docker Compose**: Create a `docker-compose.yml` file. Define the services and their configurations. You can specify volumes, networks, and environment variables here.

4. **Build and Run**: Use the `docker-compose` command to build and run your application. This will create Docker containers for your Flask app and any other services you defined.

5. **Testing**: Ensure that your application works as expected inside the Docker containers. You can access it through a web browser or use tools like `curl` to make API requests.

6. **Deployment**: Once your application works locally, you can deploy it to a server or cloud platform of your choice, such as AWS, Azure, Google Cloud, or a self-hosted server.

**Benefits**:

- **Isolation**: Docker containers provide a consistent and isolated environment for your application, reducing conflicts between dependencies and ensuring portability.

- **Scalability**: Docker Compose makes it easy to scale your application by adding more containers or services as needed.

- **Version Control**: Docker Compose allows you to version control your application's configuration, making it easy to reproduce the same environment across different development and deployment stages.

- **Ease of Deployment**: Docker containers are easier to deploy compared to traditional server setups, as they encapsulate the entire application and its dependencies.

By following this project's structure, you can develop, containerize, and manage your Python Flask web application efficiently using Docker Compose. This approach simplifies both the development and deployment processes, ensuring a consistent and reliable environment for your application.

## Folder Structure

```
.
├── app
│   ├── auth.py
│   ├── config.py
│   ├── __init__.py
│   ├── projects.py
    ├── config.py
    ├── extension.py
    models
│   │   └── models
│   │       ├── user.py
│   │       ├── task.py
│   │       ├── token.js
│   │       └── user.js
│   ├── static
│   │   └── js
│   │       ├── script-index.js
│   │       ├── script-login.js
│   │       ├── script-project.js
│   │       └── script-register.js
│   ├── tasks.py
│   ├── templates
│   │   ├── auth
│   │   │   ├── base.html
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── base.html
│   │   ├── index.html
│   │   └── project.html
│   └── views.py
├── docker-compose.yml
├── Dockerfile

├── README.md (documentation file for github)
├── requirements.txt (list third party packages used by flask app)
├── run.py (python file for running flask app)

```

## Features

#### Registration Page

![Registration Page](images/register.png?raw=true "Registration Page")

#### Login Page

![Login Page](images/login.png?raw=true "Login Page")

#### Project Page

- projects
  ![List of project](images/addproject.png?raw=true "List of project")
- Added new project
  ![Added new project](images/modalAddproject.png.png?raw=true "Added new project")
- Edit project
  ![Edit Project](images/editaddproject.png.png?raw=true "Edit Project")

#### Todo Page (Home)

- List of tasks
  ![List of tasks](images/task.png?raw=true "List of tasks")

- Added new task
  ![Added new task](images/addnewtask.png?raw=true "Added new task")
- Edit task
  ![Edit task](images/editTask.png?raw=true "Edit task")
- Delete task
  ![Delete task](images/deletTask.png?raw=true "Delete task")
