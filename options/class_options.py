import configparser
import os


class AppOptions:
    def __init__(self):

        self.options = configparser.ConfigParser()
        self.Option1 = None
        self.Option2 = None
        self.Option3 = None
        self.__load_options()

    def __load_options(self):
        """ Load options from config file"""
        self.options.read(os.path.join(os.getcwd(),'config.ini'))
        self.option1 = self.options.get('OPTIONS', 'option 1')
        self.option2 = self.options.get('OPTIONS', 'option 2')
        self.option3 = self.options.get('OPTIONS', 'option 3')

    def __save_options(self):
        """ Save options to config file"""
        self.options.write(open(os.path.join(os.getcwd(), 'config.ini'), 'w'))

    @property
    def option1(self):
        return self.Option1

    @option1.setter
    def option1(self, v):
        self.Option1 = v
        self.options.set('OPTIONS','option 1', str(v))
        self.__save_options()

    @property
    def option2(self):
        return self.Option2

    @option2.setter
    def option2(self, v):
        self.Option2 = v
        self.options.set('OPTIONS', 'option 2', str(v))
        self.__save_options()

    @property
    def option3(self):
        return self.Option3

    @option3.setter
    def option3(self, v):
        self.Option3 = v
        self.options.set('OPTIONS', 'option 3', str(v))
        self.__save_options()
