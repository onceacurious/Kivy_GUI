from kivy.uix.gridlayout import GridLayout
from kivy.uix import boxlayout, button, checkbox, gridlayout, label, textinput


class AuthLayout(GridLayout):
    def __init__(self, **kwargs):
        super(AuthLayout, self).__init__(**kwargs)

        self.cols = 1
        self.rows = 3

        self.singinLbl = label.Label(text="Sign In")
        self.singinLbl.font_size = 25
        self.singinLbl.bold = True
        self.singinLbl.color = "#3485fdff"

        self.inputLayout = gridlayout.GridLayout()
        
        self.inputLayout.cols = 2
        self.inputLayout.rows = 3
        self.inputLayout.padding = 5, 5, 5, 5
        self.inputLayout.spacing = 5

        self.usernameLbl = label.Label(text="Username:")
        self.usernameLbl.font_size = 16

        self.usernameInput = textinput.TextInput(text="Username")

        self.inputLayout.add_widget(self.usernameLbl)
        self.inputLayout.add_widget(self.usernameInput)
        
        self.passwordLbl = label.Label(text="Password:")
        self.passwordLbl.font_size = 16
        
        self.passwordInput = textinput.TextInput(text="Password")

        self.inputLayout.add_widget(self.passwordLbl)
        self.inputLayout.add_widget(self.passwordInput)

        self.submitBtn = button.Button(text="SUBMIT")
        self.cancelBtn = button.Button(text="CANCEL")

        self.inputLayout.add_widget(self.submitBtn)
        self.inputLayout.add_widget(self.cancelBtn)

        self.bottomLayout = gridlayout.GridLayout()
        self.bottomLayout.cols = 1
        self.bottomLayout.rows = 3

        self.rememberLayout = gridlayout.GridLayout()
        self.rememberLayout.cols = 2
        self.rememberLayout.rows = 1

        self.rememberCBox = checkbox.CheckBox()
        self.rememberLbl = label.Label(text="Remember Username")

        self.rememberLayout.add_widget(self.rememberCBox)
        self.rememberLayout.add_widget(self.rememberLbl)

        self.createAccountLbl = label.Label(text="Create Account")
        self.forgotPasswordLbl = label.Label(text="Forgot Password")

        self.bottomLayout.add_widget(self.rememberLayout)
        self.bottomLayout.add_widget(self.createAccountLbl)
        self.bottomLayout.add_widget(self.forgotPasswordLbl)

        self.add_widget(self.singinLbl)
        self.add_widget(self.inputLayout)
        self.add_widget(self.bottomLayout)


        