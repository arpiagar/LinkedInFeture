


Tried accessing the FB data using the Graph API but the newer version of it,v2.0 does not provide additional info about one's friend keeping in mind the concerns raised for one's privacy.


So the next was the exploit my Professional Network i.e LinkedIn. Cleared it Oauth2 by creating a local server setup on my local machine and changing URL entry in the /etc/hosts file.

Dumped the LinkedIn Data in a json file.My script would parse this JSON file and analyse it at various data points.
LinkedIn API Used: https://api.linkedin.com/v1/people/~/connections
LinkedIN API Not Available:https://api.linkedin.com/v1/people/id=XYZ/connections - Be it available to me, could have dug the 1st Degree connections' connection and created analysis around Mutual Friends and FOF. 


Installed panda and its dependencies for Data Analysis(Github:https://github.com/pydata/pandas)
sudo pip install panda.

Installed matplotlib for pictorial represenation of the processed data.
sudo pip install matplotlib



Steps to run the script:

1. As of now, I have kept connections.json parallel to the python script. Ideal way would be fetch the JSON returned by the LinkedIn API.


Python Version: 3.X
Command: python3 DataAnalysis.py
Output: output.png by default.

