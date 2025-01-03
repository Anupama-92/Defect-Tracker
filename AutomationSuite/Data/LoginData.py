class Login(object):
    email = None
    password = None

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


logins = {
    "Default": Login('QA', 'Automation', "chorus.automation@cognine.com",
                           "Welcome2Cognine")
}