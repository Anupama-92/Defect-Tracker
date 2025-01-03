import os
import sys
import yaml


class COGConfig(object):
    __raw_dict = None

    def get_config(self):
        return self.__raw_dict

    @property
    def portal_login(self):
        return self.__raw_dict.get('portal_login').get('member_id')

    @property
    def login_credentials(self):
        email = self.__raw_dict.get('credentials').get('email')
        password = self.__raw_dict.get('credentials').get('password')
        return {'email': email, 'password': password}

    @property
    def run_params(self):
        return self.__raw_dict['machine_data']['run_params']

    @property
    def browser_type(self):
        return self.run_params.get('browser_type', 'chrome')

    @property
    def site_mode(self):
        return self.run_params.get('site_mode', 'default')

    @property
    def is_chorus(self):
        return 'chorus' in self.site_mode

    @property
    def chorus_web_ui_config(self):
        if self.is_chorus:
            return self.get_config().get('sites').get(self.site_mode).get('web_ui_configs')
        else:
            return self.get_config().get('chorus').get('web_ui_configs')

    @property
    def logging(self):
        return self.__raw_dict.get('logging', None)

    @property
    def log_level(self):
        return self.logging.get('log_level', 'INFO')

    @staticmethod
    def _config_update(source, override):
        from collections.abc import Mapping
        for k, v in override.items():
            if isinstance(v, Mapping):
                r = COGConfig._config_update(source.get(k, {}), v)
                source[k] = r
            else:
                source[k] = override[k]
        return source

    @staticmethod
    def load_from_file():
        config_path = os.path.join(os.path.dirname(__file__), "./cog_config.yml")
        override_path = os.path.join(os.path.dirname(__file__), "./cog_config_override.yml")
        config = yaml.load(open(config_path).read(), Loader=yaml.SafeLoader)

        # check for a local override yaml file
        if os.path.isfile(override_path):
            override = yaml.load(open(override_path).read(), Loader=yaml.SafeLoader)
            config = COGConfig._config_update(config, override)

        COGConfig.__raw_dict = config

        return config
