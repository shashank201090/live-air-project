# Live Air

GTNexus LiveAir is a platform service and callable set of web services created to conveniently retrieve status updates, provide near real-time tracking and precise Estimated Times of Arrival (ETAs) of aircargo regardless of the number of flights or legs within a flight.

## Getting Started

Since we are using Serverless Architecture,we do not need to start any server.
We can just start by calling REST API's.

### Prerequisites


1. AWS account (For using AWS Services)
2. Python (installed on system)
3. Chalice Framework (installed as a python package)
4. Python Supporting Editor

```
Editor eg: PyDev on Eclipse
```

### Installing

The creation of functions,API Gateways and running environment is taken care by the Chalice Framework. 

For accesing chalice install chalice package:

```
pip install chalice
```

http://chalice.readthedocs.io/en/latest/quickstart.html

Also you need to install boto3 package to acces AWS services for python.
```
pip install boto3
```

https://boto3.readthedocs.io/en/latest/guide/quickstart.html

## Deployment

Open Command Prompt and goto the project directory and run following command:
1. Chalice Deploy
Note: Make sure the credentials details are present in the home/.aws directory.

## Built With

* [Chalice](http://chalice.readthedocs.io/en/latest/api.html)- The web framework used

## Running the App
1. The app can be run on a webserver or can be loaded form a browser.
Starting page is /Orders.html



## Versioning

We use git(https://git-scm.com/) for versioning. For the versions available, see the [tags on this repository](https://gitlab.corecompete.com/liveair/proto). 

## Authors
1.Shashank Kumar

## Acknowledgements

