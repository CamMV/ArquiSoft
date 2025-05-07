import requests
from social_core.backends.oauth import BaseOAuth2

class Auth0(BaseOAuth2):
    name = 'auth0'
    SCOPE_SEPARATOR = ' '
    ACCESS_TOKEN_METHOD = 'POST'
    EXTRA_DATA = [
        ('picture', 'picture'),
    ]
    
    def authorization_url(self):
        return "https://" + self.setting('DOMAIN') + "/authorize"
    
    def access_token_url(self):
        return "https://"+ self.setting('DOMAIN') + "/oauth/token"
    
    def get_user_id(self, details, response):
        return details['user_id']
    
    def get_user_details(self, response):
        url = "https://" + self.setting('DOMAIN') + "/userinfo"
        headers = {'authorization':'Bearer ' + response['access_token']}
        resp = requests.get(url, headers=headers)
        user_info = resp.json()
        return {
            'username': user_info['nickname'],
            'first_name': user_info['name'],
            'picture': user_info['picture'],
            'user_id': user_info['sub']
        }

def getRole(request):
    user = request.user
    auth0user = user.social_auth.filter(provider='auth0')[0]
    accesToken = auth0user.extra_data['access_token']
    url = "https://dev-urytz4eeb6bslk42.us.auth0.com/userinfo" 
    headers = {'authorization':'Bearer ' + accesToken}
    resp = requests.get(url, headers=headers)
    user_info = resp.json()
    role = user_info['dev-urytz4eeb6bslk42.us.auth0.com/role']
    return (role)
