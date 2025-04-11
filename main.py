import json
import requests
import logging
from connectors.core.connector import Connector, ConnectorError
from connectors.core.constants import ACTION_STATUS

logger = logging.getLogger("huntress_http_collector")

class HuntressHECConnector(Connector):
    def __init__(self, *args, **kwargs):
        super(HuntressHECConnector, self).__init__(*args, **kwargs)
        self.base_url = "https://hec.huntress.io/services/collector"
        self.token = self.config.get('token')
        self.verify_ssl = self.config.get('verify_ssl', True)

    def build_headers(self):
        return {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

    def push_data(self, data):
        try:
            headers = self.build_headers()
            payload = {
                'event': data,
                'sourcetype': '_json',
                'source': 'netskope-cloud-exchange',
                'host': 'netskope-ce'
            }
            response = requests.post(self.base_url, headers=headers, json=payload, verify=self.verify_ssl)
            if response.status_code not in [200, 201, 202]:
                raise ConnectorError(f'Failed to send data. Status: {response.status_code}, Response: {response.text}')
            return {'status': 'success', 'response': response.text}
        except Exception as err:
            logger.exception("Error in push_data")
            raise ConnectorError(str(err))

    def execute(self, config, operation, params, **kwargs):
        self.config = config
        if operation == 'push_event':
            return self.push_data(params.get('event'))
        else:
            raise ConnectorError(f'Unsupported operation: {operation}')

    def check_health(self, config):
        try:
            self.config = config
            return self.push_data({'health_check': True})
        except Exception as err:
            logger.exception("Health check failed")
            raise ConnectorError(str(err))