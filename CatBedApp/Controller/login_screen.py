import importlib

import View.LoginScreen.login_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.LoginScreen.login_screen)


from kivymd.uix.card import MDCard
class LoginCard( MDCard ):
    ''' MDCard que abre a tela de login '''
class RegisterCard( MDCard ):
    ''' MDCard que abre a tela de registro de novo usuário '''


from kivy.animation import Animation

class LoginScreenController:
    """
    The `LoginScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """
    register_card: RegisterCard 
    login_card : LoginCard  
    register_opened : bool 
    login_opened : bool 

    def __init__(self, model):
        self.model = model  # Model.login_screen.LoginScreenModel
        self.view = View.LoginScreen.login_screen.LoginScreenView(controller = self, model = self.model)
        self.register_opened = False 
        self.login_opened = False 

    def get_view(self) -> View.LoginScreen.login_screen:
        return self.view
    
    def open_login(self, some_event = None):
        # Verifica se o registro não esta aberto 
        if self.register_opened: 
            self.close_register() 

        # Inicia a tela de login 
        self.login_card = LoginCard()
        self.get_view().add_widget( self.login_card )
        self.get_view().ids.button_login.unbind( on_release = self.open_login )
        # Animação do bottão e da tela
        button = Animation( pos_hint = { 'top': 0.6 }, size_hint = [ 1.5, 0.15 ], duration = 0.25 )
        screen = Animation( pos_hint = { 'center_x': 0.5, 'top': 0.75 }, size_hint = [ 0.75, 0.3 ], duration = 0.25 )
        screen.start( self.login_card )
        button.start( self.get_view().ids.button_login ) 
        # Troca a função do botão 
        self.get_view().ids.button_login.bind( on_release = self.close_login )
        self.login_opened = True 


    def close_login(self, some_event = None):
        # remove o Widget 
        self.get_view().remove_widget( self.login_card )
        self.get_view().ids.button_login.unbind( on_release = self.close_login )
        # Animation back 
        animation = Animation( pos_hint = {'center_x': 0.50,'top': 1}, size_hint = [ 1, 0.15], duration = 0.25 )
        animation.start(self.get_view().ids.button_login)  
        # Troca a função do botõa 
        self.get_view().ids.button_login.bind( on_release = self.open_login )
        self.login_opened = False 


    def open_register( self, some_event = None ): 
        # Verifica se o login não esta aberto 
        if self.login_opened: 
            self.close_login()
        # Inicia a tela de registro 
        self.register_card = RegisterCard()
        self.get_view().add_widget( self.register_card )
        self.get_view().ids.button_register.unbind( on_release = self.open_register )
        
        # Animação do bottão e da tela
        button = Animation( pos_hint = { 'top': 0.5 }, duration = 0.25 )
        button.start( self.get_view().ids.button_register )

        screen = Animation( pos_hint = { 'center_x': 0.5, 'center_y': 0.375 }, size_hint = [ 0.75, 0.5 ], duration = 0.25 )
        screen.start( self.register_card )
        
        # Troca a função do botão 
        self.get_view().ids.button_register.bind( on_release = self.close_register )
        self.register_opened = True  
    
    def close_register( self, some_event = None ): 
        # remove o Widget 
        self.get_view().remove_widget( self.register_card )
        self.get_view().ids.button_register.unbind( on_release = self.close_register )
        # Animation back 
        button = Animation( pos_hint = {'center_x': 0.50, 'top': 1}, size_hint = [ 1, 0.6], duration = 0.25 )
        button.start(self.get_view().ids.button_register)  
        # Troca a função do botõa 
        self.get_view().ids.button_register.bind( on_release = self.open_register )
        self.login_opened = False 