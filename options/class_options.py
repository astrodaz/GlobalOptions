import configparser
import os


class AppOptions:
    def __init__(self):

        self.options = configparser.ConfigParser()
        self.__load_options()

    def __load_options(self):
        """ Load options from config file"""
        self.options.read(os.path.join(os.getcwd(),'config.ini'))

    def __save_options(self):
        """ Save options to config file"""
        self.options.write(open(os.path.join(os.getcwd(), 'config.ini'), 'w'))

    @property
    def option1(self):
        v = self.options.get('OPTIONS', 'option 1')
        return v

    @option1.setter
    def option1(self, v):
        self.options.set('OPTIONS','option 1', str(v))
        self.__save_options()

    @property
    def option2(self):
        v = self.options.get('OPTIONS', 'option 2')
        return v

    @option2.setter
    def option2(self, v):
        self.options.set('OPTIONS', 'option 2', str(v))
        self.__save_options()

    @property
    def option3(self):
        v = self.options.get('OPTIONS', 'option 3')
        return v

    @option3.setter
    def option3(self, v):
        self.options.set('OPTIONS', 'option 3', str(v))
        self.__save_options()
