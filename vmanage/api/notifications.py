"""Cisco vManage Notifications API Methods.
"""

from vmanage.api.http_methods import HttpMethods
from vmanage.data.parse_methods import ParseMethods


class Notifications(object):
    """Access to Notificaton rules.

    vManage can generate notificatons. This class allows you to
    read these notifications.

    """
    def __init__(self, session, host, port=443):
        """Initialize Notifications object with session parameters.

        Args:
            session (obj): Requests Session object
            host (str): hostname or IP address of vManage
            port (int): default HTTPS 443

        """

        self.session = session
        self.host = host
        self.port = port
        self.base_url = f'https://{self.host}:{self.port}/dataservice/'

    def get_notification_rules(self):
        """Provides notification rules

        Returns:
            result (dict): All data associated with a response.
        """

        api = "notifications/rules"
        url = self.base_url + api
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result
