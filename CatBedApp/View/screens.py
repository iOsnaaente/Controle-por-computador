# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


from Model.login_screen import LoginScreenModel
from Controller.login_screen import LoginScreenController
from Model.home_screen import HomeScreenModel
from Controller.home_screen import HomeScreenController
from Model.aux_screen import AuxScreenModel
from Controller.aux_screen import AuxScreenController

screens = {
    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController,
    },

    "home screen": {
        "model": HomeScreenModel,
        "controller": HomeScreenController,
    },

    "aux screen": {
        "model": AuxScreenModel,
        "controller": AuxScreenController,
    },
}