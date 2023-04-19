from View.base_screen import BaseScreenView

class LoginScreenView(BaseScreenView):
    
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
    
    def on_kv_post(self, base_widget):
        self.ids.button_login.bind( on_release = self.controller.open_login )
        self.ids.button_register.bind( on_release = self.controller.open_register )
        return super().on_kv_post(base_widget)
