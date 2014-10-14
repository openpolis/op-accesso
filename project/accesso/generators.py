from oauthlib.common import generate_client_id as oauthlib_generate_client_id
from oauth2_provider.generators import BaseHashGenerator, CLIENT_ID_CHARACTER_SET


class ClientSecretGenerator(BaseHashGenerator):
    def hash(self):
        return oauthlib_generate_client_id(length=100, chars=CLIENT_ID_CHARACTER_SET)