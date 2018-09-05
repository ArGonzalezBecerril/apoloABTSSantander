import operator


class OracleJDBC(object):

    def __init__(self, user, driver, password, url):
        print "*******Class OracleJDBC *****"
        self.user = user
        self.driver = driver
        self.password = password
        self.url = url

    user = property(operator.attrgetter('_user'))

    @user.setter
    def user(self, u):
        if not u:
            raise Exception("El Campo usuario no debe estar vacio")
        self._user = u

    driver = property(operator.attrgetter('_driver'))

    @driver.setter
    def driver(self, d):
        if not d:
            raise Exception("El Campo driver no debe estar vacio")
        self._driver = d

    password = property(operator.attrgetter('_password'))

    @password.setter
    def password(self, p):
        if not p:
            raise Exception("El campo 'password' no debe estar vacio")
        self._password = p

    url = property(operator.attrgetter('_url'))

    @url.setter
    def url(self, u):
        if not u:
            raise Exception("El campo 'url_jdbc' no debe estar vacio")
        self._url = u
