# IpNote

This app makes a request to an external server every 5 minutes (default value, configurable), which then notes the IP to be accessible by other clients.
Here a more detailed description:

![Diagram](https://user-images.githubusercontent.com/95703244/169898909-bb27b070-7ae3-4b32-82f4-241ce7d973b3.png)

# Requirements
Project made for Ubuntu 20.04 Focal Fossa.

## Setup
### Info Server
1. Clone the InfoServer folder to your /home directory.
2. Set up the flask server utilizing uWSGI and nginx. (Have a look at [this](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04) good tutorial.)
### Target Server
1. Clone the TargetServer folder to your machine.
2. If you do not wish to manually run the script every time at startup and you are using Ubuntu you should consider looking into [converting it into a service](https://websofttechs.com/tutorials/how-to-setup-python-script-autorun-in-ubuntu-18-04/).
### Client
I've uploaded a demo inside the Client folder. You can build this function into your code easily and without any external modules.
