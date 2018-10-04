# week 4 cognito
using cognito, one can add sign-in and sign-out feature.


### ADD HTTPS
from week4, the lecture also covered how to set HTTPS.
-> make a note about how to set HTTPS


### RDS instance
Start the RDS database instance.
* open RDS dashboard
* Instances from left navigation pane
* choose instance and start


### Cloud9 preview URL
* top menu bar : Run -> Run Configurations -> Python3RunConfiguration
* Preview -> Preview Running Application
* Pop out the window
* note the URL

the URL will be used for Cognito user pool configuration


### set up Cognito user pool
* Amazon Cognito
* Manage your User Pools
* create a user pool
* pool name: phtos-pool
* step through settings
    * How do you want your end users to sign in
    * which standard attributes
    * Message customization : verification type
* App clients: Add an app client
    * name
    * create app client
* create pool and make a note of Pool ID

#### App client set up
* App integration: App client setting from left navigation menu
* Enabled Identity Providers: check Cognito User Pool
* set Callback URL: the Cloud9 Preview URL and add callback
* set Sign out URL: the Cloud9 Preview URL (end in trailing slash `/`)
* OAuth 2.0: check Authorization code grant, check openid
* Save changes

#### Domain name
* App integration: Domain name from left navigation menu
* save changes

#### App client info
* General setting: App client from left navigation menu
* Show details
* make a note of App client ID and App client secret


### Flask code
```python
@application.route("/login")
def login():
    """Login route"""
    # http://docs.aws.amazon.com/cognito/latest/developerguide/login-endpoint.html
    session['csrf_state'] = util.random_hex_bytes(8)
    cognito_login = ("https://%s/"
                     "login?response_type=code&client_id=%s"
                     "&state=%s"
                     "&redirect_uri=%s/callback" %
                     (config.COGNITO_DOMAIN, config.COGNITO_CLIENT_ID, session['csrf_state'],
                      config.BASE_URL))
    return redirect(cognito_login)

@application.route("/logout")
def logout():
    """Logout route"""
    # http://docs.aws.amazon.com/cognito/latest/developerguide/logout-endpoint.html
    flask_login.logout_user()
    cognito_logout = ("https://%s/"
                      "logout?response_type=code&client_id=%s"
                      "&logout_uri=%s/" %
                      (config.COGNITO_DOMAIN, config.COGNITO_CLIENT_ID, config.BASE_URL))
    return redirect(cognito_logout)

@application.route("/callback")
def callback():
    """Exchange the 'code' for Cognito tokens"""
    #http://docs.aws.amazon.com/cognito/latest/developerguide/token-endpoint.html
    csrf_state = request.args.get('state')
    code = request.args.get('code')
    request_parameters = {'grant_type': 'authorization_code',
                          'client_id': config.COGNITO_CLIENT_ID,
                          'code': code,
                          "redirect_uri" : config.BASE_URL + "/callback"}
    response = requests.post("https://%s/oauth2/token" % config.COGNITO_DOMAIN,
                             data=request_parameters,
                             auth=HTTPBasicAuth(config.COGNITO_CLIENT_ID,
                                                config.COGNITO_CLIENT_SECRET))

    # the response:
    # http://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-with-identity-providers.html
    if response.status_code == requests.codes.ok and csrf_state == session['csrf_state']:
        verify(response.json()["access_token"])
        id_token = verify(response.json()["id_token"], response.json()["access_token"])

        user = User()
        user.id = id_token["cognito:username"]
        session['nickname'] = id_token["nickname"]
        session['expires'] = id_token["exp"]
        session['refresh_token'] = response.json()["refresh_token"]
        flask_login.login_user(user, remember=True)
        return redirect(url_for("home"))

    return render_template_string("""
        {% extends "main.html" %}
        {% block content %}
            <p>Something went wrong</p>
        {% endblock %}""")
```


### run and test

### stop RDS instance



------ 
## notes
### HTTPS between user and load balance
To secure the connection between the users and my load balancer, one should create a listener to encrypt the connection (SSL offload).
[HTTPS Listeners for Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html)


### Encrypting Data in AWS
#### Encrypting Data in Transit:
* [Configure Apache Webserver on Amazon Linux to Use SSL/TLS from EC2 User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/SSL-on-an-instance.html#letsencrypt)
* [Using SSL to Encrypte a Connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html)

#### Encrypting Data at Rest
* EC2 Instance: use [EBS volume with Encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html)
* RDS database: [Encrypting RDS Resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html)
* S3 Contens: [S3 Default Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) and [S3 Encryptiong](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingEncryption.html)
* more about Encryptiong Key: [KMS](https://docs.aws.amazon.com/kms/latest/developerguide/service-integration.html)
* more on [Encryption](https://aws.amazon.com/blogs/security/category/encryption/)

#### Compliance programs
* [compliance programs](https://aws.amazon.com/compliance/pci-data-privacy-protection-hipaa-soc-fedramp-faqs/)
* [security whitepaper](https://d1.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf)
