In the uwsgi.ini file, you define the following options: [read more](https://uwsgi-docs.readthedocs.io/en/latest/Options.html)
• socket: The UNIX/TCP socket to bind the server.
• chdir: The path to your project directory, so that uWSGI changes to that directory before loading the Python application.
• module: The WSGI module to use. You set this to the application callable contained in the wsgi module of your project.
• master: Enable the master process.
• chmod-socket: The file permissions to apply to the socket file. In this case, you use 666 so that NGINX can read write the socket.
• uid: The user ID of the process once it’s started.
• gid: The group ID of the process once it’s started.
• vacuum: Using true instructs uWSGI to clean up any temporary files or UNIX sockets it creates.

