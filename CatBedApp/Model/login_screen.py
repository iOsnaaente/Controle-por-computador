from Model.base_model import BaseScreenModel

import os 
PATH = os.path.dirname( __file__ ).removesuffix('\\Model')

class LoginScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.login_screen.LoginScreen.LoginScreenView` class.
    """

    logo = PATH + '/assets/images/logo-gbn.png'