from Model.base_model import BaseScreenModel

import os 
PATH = os.path.dirname( __file__ ).removesuffix('\\Model')

class HomeScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.home_screen.HomeScreen.HomeScreenView` class.
    """

    logo = PATH + '/assets/images/logo-gbn.png'