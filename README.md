<h1>This repo is for holding my TradingView custom WebHook URL build so I can get text messages to my phone when one of my alerts gets triggered.</h1>

Use openssl to create the CSR and KEY for setting up HTTPS in nginx config file for the site. 
Also, I like to store all of the SSL-related file for Nginx vhosts in /etc/nginx/certs to keep them all in one simple place for later reference. That being said, you'll need to make that directory first before running this command
```
openssl req -new -newkey rsa:2048 -keyout /etc/nginx/certs/webhook.lab.sanderson.com.key -out webhook.lab.sanderson.com.csr
```


To test the webhook.php page you can use the curl command to send data to it to make sure it's working properly.
```
curl -k -X POST https://webhook.lab.sanderson.com:8443/webhook.php -H "Content-Type: application/json" -d @payload
```
Alternatively, you can use the manual way to send the json data like this:
```
curl -k -X POST https://webhook.lab.sanderson.com:8443/webhook.php -H "Content-Type: application/json" -d '{"name": "John Doe", "role": "user"}'
```
