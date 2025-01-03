import binascii
import math
import os
import random
import string


class Utils(object):

    def __init__(self):
        from RunExecutionScripts.common.common_lib import CommonPaths
        self.__auto_suite = CommonPaths.src_main

    @property
    def dataset(self):
        try:
            return self.__dataset
        except AttributeError:
            from .Dataset import Dataset
            self.__dataset = Dataset
            return self.__dataset

    @property
    def date(self):
        try:
            return self.__date
        except AttributeError:
            from AutomationSuite._Wrapper.Shared.Util import DateUtil
            self.__date = DateUtil
            return self.__date

    def unique_string(self, strlen=32):
        trunc = -1 if strlen % 2 != 0 else None
        return binascii.hexlify(os.urandom(int(math.ceil(float(strlen) / 2)))).decode('utf-8')[:trunc]

    def long_string(self, length=150):
        return self.unique_string(strlen=length)

    def unique_phone(self, length=10, str_format='(+91) {2}{3}{4}{5}{6}-{7}{8}{9}{0}{1}', formatted=False):
        start_range = end_range = 0
        for i in range(length):
            if i == 0:
                start_range += 2
            else:
                start_range *= 10
            end_range = end_range * 10 + 9

        if not formatted:
            return str(random.randrange(start_range, end_range))

        try:
            return str_format.format(*list(str(random.randrange(start_range, end_range))))
        except IndexError:
            raise ValueError(
                'The length requested ({0}) does not match the string format: {1}'.format(length, str_format))

    def abs_path(self, relative_path):
        return os.path.abspath(os.path.join(self.__auto_suite, relative_path))

    def unique_email(self, domain='cognine.com'):
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        return f"{username}@{domain}"

    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for i in range(length))
