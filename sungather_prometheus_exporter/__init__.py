import logging
from prometheus_client import start_http_server, Gauge


class Export():

    def __init__(self):
        False

    def configure(self, config, inverter):
        self.prefix = config.get('prefix', '')
        port = config.get('port', 5055)
        host = config.get('host', 'localhost')
        try:
            start_http_server(port, host)
            logging.info(f"Prometheus metric: Configured")
        except Exception as err:
            logging.error("Prometheus metric: Error: {}", err)
            return False
        return True

    def publish(self, inverter):
        for register, value in inverter.latest_scrape.items():
            unit = inverter.getRegisterUnit(register)
            metric = Gauge(f'{prefix}{register}', unit)
            metric.set(value)
