class LogMixin:
    @staticmethod
    def write(self, msg):
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        self.write(self, f'INFO: {msg}')

    def log_error(self, msg):
        self.write(self, f'ERROR: {msg}')
        pass
