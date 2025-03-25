import sys
import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivymd.uix.card import MDCard
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.list import MDList, MDListItem, MDListItemHeadlineText, MDListItemTrailingCheckbox
from kivymd.uix.fitimage import FitImage
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import MDDialog, MDDialogButtonContainer, MDDialogContentContainer, MDDialogHeadlineText, MDDialogIcon, MDDialogSupportingText
from kivymd.uix.widget import Widget
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText
from kivymd.uix.button import MDIconButton
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.videoplayer import VideoPlayer
module_directory = os.path.abspath("database")
sys.path.append(module_directory)
import itrendbase # type: ignore

UI = """
MDNavigationLayout:
    MDScreenManager:
        id: sm
        MDScreen:
            name: "home"
            FitImage:
                source: "home_back.jpg"
                size: self.parent.size
                pos_hint: {"center_x":.5, "center_y":.5}
            MDBoxLayout:
                orientation: "vertical"
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(40)
                    padding: dp(10)
                    MDIconButton:
                        icon: "menu"
                        size_hint_x: .1
                        on_release: nav_drawer.set_state("toggle")
                    Widget:
                        size_hint_x: .8
                    MDIconButton: 
                        id: account_info
                        icon: "account-circle-outline"
                        size_hint_x: .1
                        on_release: app.account_info()
                MDScrollView:
                    MDGridLayout:
                        cols: 1
                        padding: dp(10)
                        id: content_container
        MDScreen:
            name: "topic_screen"
            FitImage:
                source: "home_back.jpg"
                size: self.parent.size
                pos_hint: {"center_x":.5, "center_y":.5}
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(5)
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(30)
                    padding: dp(5)
                    MDIconButton:
                        icon: "arrow-left"
                        size_hint_x: .1
                        on_release: sm.current = "home"
                    Widget:
                MDScrollView:
                    MDGridLayout:
                        cols: 1
                        spacing: dp(28)
                        padding: dp(10)
                        id: topic_content
        MDScreen:
            name: "account_screen"
            id: account_screen
            FitImage:
                source: "home_back.jpg"
                size: self.parent.size
                pos_hint: {"center_x":.5, "center_y":.5}
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(5)
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(30)
                    padding: dp(5)
                    MDIconButton:
                        icon: "arrow-left"
                        size_hint_x: .1
                        on_release: sm.current = "home"
                    Widget:
                Widget:
                    size_hint_y: None
                    height: dp(20)
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(60)
                    spacing: dp(2.5)
                    padding: dp(10)
                    orientation: "vertical"
                    MDLabel:
                        id: account_name
                        text: " "
                        size_hint_y: None
                        adaptive_height: True
                        halign: "center"
                        valign: "top"
                        theme_font_size: "Custom"
                        font_size: sp(32)
                        theme_text_color: "Custom"
                        text_color: "yellow"
                        theme_font_name: "Custom"
                        font_name: "heading_font.ttf"
                    MDLabel:
                        id: account_email
                        text: " "
                        size_hint_y: None
                        adaptive_height: True
                        halign: "center"
                        valign: "top"
                        theme_font_size: "Custom"
                        font_size: sp(18)
                        theme_text_color: "Custom"
                        text_color: "yellow"
                        theme_font_name: "Custom"
                        font_name: "Montserrat-Bold.ttf"
                Widget:
                    size_hint_y: None
                    height: dp(20)
                MDBoxLayout:
                    orientation: "vertical"
                    spacing: dp(20)
                    padding: dp(10)
                    id: account_features
                    MDButton:
                        pos_hint: {"center_x":.5}
                        size_hint_x: .8
                        on_release: app.go_to_favorites()
                        MDButtonText:
                            text: "Modify Interests"
                        MDButtonIcon:
                            icon: "heart-outline"
                    MDButton:
                        on_release: app.show_favorites()
                        pos_hint: {"center_x":.5}
                        size_hint_x: .8
                        MDButtonText:
                            text: "My Favorites"
                        MDButtonIcon:
                            icon: "star-outline"
                    MDButton:
                        on_release: app.logout()
                        pos_hint: {"center_x":.5}
                        size_hint_x: .8
                        MDButtonText:
                            text: "Sign Out"
                        MDButtonIcon:
                            icon: "logout"
                Widget:
                
        MDScreen:
            name: "favorites_screen"
            FitImage:
                source: "home_back.jpg"
                size: self.parent.size
                pos_hint: {"center_x":.5, "center_y":.5}
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(5)
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(30)
                    padding: dp(5)
                    MDIconButton:
                        icon: "arrow-left"
                        size_hint_x: .1
                        on_release: sm.current = "account_screen"
                    Widget:
                MDScrollView:
                    MDGridLayout:
                        id: favorites_container
                        cols: 1
                        padding: dp(10)
                        spacing: dp(10)

        MDScreen:
            name: "fav_topic_screen"
            FitImage:
                source: "home_back.jpg"
                size: self.parent.size
                pos_hint: {"center_x":.5, "center_y":.5}
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(5)
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(30)
                    padding: dp(5)
                    MDIconButton:
                        icon: "arrow-left"
                        size_hint_x: .1
                        on_release: sm.current = "favorites_screen"
                    Widget:
                MDScrollView:
                    MDGridLayout:
                        cols: 1
                        spacing: dp(28)
                        padding: dp(10)
                        id: fav_topic_content
        MDScreen:
            name: "interests_screen"
            FitImage:
                source: "home_back.jpg"
                size: self.parent.size
                pos_hint: {"center_x":.5, "center_y":.5}
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(5)
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(30)
                    padding: dp(5)
                    MDIconButton:
                        icon: "arrow-left"
                        size_hint_x: .1
                        on_release: sm.current = "account_screen"
                    Widget:
                Widget:
                    size_hint_y: None
                    height: dp(20)
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(60)
                    spacing: dp(2.5)
                    padding: dp(10)
                    orientation: "vertical"
                    MDLabel:
                        id: interest_uname
                        text: " "
                        size_hint_y: None
                        adaptive_height: True
                        halign: "center"
                        valign: "top"
                        theme_font_size: "Custom"
                        font_size: sp(32)
                        theme_text_color: "Custom"
                        text_color: "yellow"
                        theme_font_name: "Custom"
                        font_name: "heading_font.ttf"
                    MDLabel:
                        text: "Modify Interests"
                        size_hint_y: None
                        adaptive_height: True
                        halign: "center"
                        valign: "top"
                        theme_font_size: "Custom"
                        font_size: sp(18)
                        theme_text_color: "Custom"
                        text_color: "yellow"
                        theme_font_name: "Custom"
                        font_name: "Montserrat-Bold.ttf"
                MDCard:
                    size_hint_y: None
                    height: dp(450)
                    padding: dp(25)
                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: dp(20)
                        MDLabel:
                            text: "Select from below: "
                            halign: "center"
                            size_hint_y: None
                            height: dp(35)
                        MDScrollView:
                            MDGridLayout:
                                id: interests_container
                                cols: 1
                Widget:
            
    MDNavigationDrawer:
        id: nav_drawer
        radius: 0, dp(16), dp(16), 0
        theme_bg_color: "Custom"
        md_bg_color: 0.796, 0.765, 0.89, 1
        MDBoxLayout:
            orientation: "vertical"
            spacing: dp(15)
            FitImage:
                source: "itrend.png"
                radius: [16, 16, 16, 16]
            MDLabel:
                text: "iTREND dashboard"
                size_hint_y: None
                height: dp(30)
                bold: True
                theme_font_name: "Custom"
                font_name: "Montserrat-Bold.ttf"
                theme_text_color: "Custom"
                text_color: "blue"
            MDScrollView:
                MDList:
                    MDListItem:
                        theme_bg_color: "Custom"
                        md_bg_color: 0.796, 0.765, 0.89, 1
                        on_release: app.account_screen()
                        MDListItemLeadingIcon:
                            icon: "account"
                            theme_icon_color: "Custom"
                            icon_color: "magenta"
                        MDListItemHeadlineText:
                            text: "Account"
                            theme_font_name: "Custom"
                            font_name: "Montserrat-Bold.ttf"
                            theme_text_color: "Custom"
                            text_color: "blue"
                    MDListItem:
                        theme_bg_color: "Custom"
                        md_bg_color: 0.796, 0.765, 0.89, 1
                        on_release: app.favorites_screen()
                        MDListItemLeadingIcon:
                            icon: "star-outline"
                            theme_icon_color: "Custom"
                            icon_color: "magenta"
                        MDListItemHeadlineText:
                            text: "Favorites"
                            theme_font_name: "Custom"
                            font_name: "Montserrat-Bold.ttf"
                            theme_text_color: "Custom"
                            text_color: "blue"
                    MDListItem:
                        theme_bg_color: "Custom"
                        md_bg_color: 0.796, 0.765, 0.89, 1
                        on_release: app.explore_content()
                        MDListItemLeadingIcon:
                            icon: "compass-outline"
                            theme_icon_color: "Custom"
                            icon_color: "magenta"
                        MDListItemHeadlineText:
                            text: "Explore"
                            theme_font_name: "Custom"
                            font_name: "Montserrat-Bold.ttf"
                            theme_text_color: "Custom"
                            text_color: "blue"
                    MDListItem:
                        theme_bg_color: "Custom"
                        md_bg_color: 0.796, 0.765, 0.89, 1
                        MDListItemLeadingIcon:
                            icon: "magnify"
                            theme_icon_color: "Custom"
                            icon_color: "magenta"
                        MDListItemHeadlineText:
                            text: "Quick Search"
                            theme_font_name: "Custom"
                            font_name: "Montserrat-Bold.ttf"
                            theme_text_color: "Custom"
                            text_color: "blue"
            MDList:
                MDListItem:
                    theme_bg_color: "Custom"
                    md_bg_color: 0.796, 0.765, 0.89, 1
                    MDListItemLeadingIcon:
                        icon: "heart"
                        theme_icon_color: "Custom"
                        icon_color: "magenta"
                    MDListItemHeadlineText:
                        text: "Donate"
                        theme_font_name: "Custom"
                        font_name: "Montserrat-Bold.ttf"
                        theme_text_color: "Custom"
                        text_color: "blue"
                MDListItem:
                    theme_bg_color: "Custom"
                    md_bg_color: 0.796, 0.765, 0.89, 1
                    MDListItemLeadingIcon:
                        icon: "information-outline"
                        theme_icon_color: "Custom"
                        icon_color: "magenta"
                    MDListItemHeadlineText:
                        text: "About iTREND"
                        theme_font_name: "Custom"
                        font_name: "Montserrat-Bold.ttf"
                        theme_text_color: "Custom"
                        text_color: "blue"
        
            
"""

class iTREND(MDApp):
    def build(self):
        return Builder.load_string(UI)
    
    def on_start(self):
        self.signedin = False
        self.add_content()
    
    
    def add_content(self):
        topics = itrendbase.session.query(itrendbase.Topic).all()
        self.grid = self.root.ids.content_container
        self.grid.size_hint_y = None
        self.grid.bind(minimum_height = self.grid.setter("height"))
        for topic in topics:
            self.heading = topic.topic_title
            self.illustration = topic.topic_description
            self.media = topic.topic_media_url
            self.likes = topic.like_count
            self.dislikes = topic.dislike_count
            self.shares = topic.share_count
            self.favorites = topic.favorite_count
            self.reports = topic.reported_count
            self.comment_count = topic.comment_count
            content = f"\n{self.heading}\n{self.illustration}\n\t\t{self.media}\t\t\n\t\t{self.likes} Likes  {self.dislikes} Dislikes  {self.shares} Shares  {self.favorites} Favorites {self.reports} Reports"
            heading_title = MDLabel(
                        text = self.heading,
                        size_hint_y = None,
                        height = dp(40),
                        pos_hint = {"y":.9},
                        theme_font_size = "Custom",
                        font_size = sp(22),
                        bold = True,
                        theme_text_color = "Custom",
                        text_color = [0, 0, .6, 1]
                        
                    )
            paragraph = MDLabel(
                    text = f"{self.illustration[:109]} ...",
                    max_lines = 1,
                    ellipsis_options = {"mode": "end"},
                    halign = "left",
                    pos_hint = {"y":.69},
                    size_hint_y = None,
                    height = dp(20)
                )
            image_card = MDCard(
                        FitImage(
                            source = self.media,
                            pos_hint = {"center_x":.5, "center_y":.5},
                            radius = [16, 16, 16, 16]
                        ),
                        size_hint_y = None,
                        height = dp(150),
                        size_hint_x = 0.95,
                        pos_hint = {"center_y":.3, "center_x":.5}
                    )
            video_card = MDCard(
                        VideoPlayer(
                            source = self.media,
                            state = "stop",
                            options = {"eos": "loop"}
                        ),
                        size_hint_y = None,
                        height = dp(150),
                        size_hint_x = 0.95,
                        pos_hint = {"center_y":.3, "center_x":.5}
                    )
            cont_layout = MDRelativeLayout()
            cont_layout.add_widget(heading_title)
            cont_layout.add_widget(paragraph)
            if not ".mp4" in self.media:
                cont_layout.add_widget(image_card)
            else:
                cont_layout.add_widget(video_card)
            content_card = MDCard(
                cont_layout,
                size_hint_y = None,
                height = dp(300),
                padding = dp(20),
                radius = [18, 18, 0, 0],
                style = "outlined",
                theme_bg_color = "Custom",
                md_bg_color = [0, 1, 1, .2],
                on_release = lambda instance, topic_title = self.heading, topic_desc = self.illustration, topic_media = self.media: self.view_content(topic_title, topic_desc, topic_media)
            )
            feedback_card = MDCard(
                MDRelativeLayout(
                    MDIconButton(
                        icon = "thumb-up",
                        pos_hint = {"center_y":.5, "center_x":.059},
                        size_hint_x = 0.2,
                        padding = dp(5),
                        on_release = lambda btn, title = self.heading: self.like_topic(title)
                    ),
                    MDLabel(
                        text = str(f"  {self.likes}"),
                        size_hint = (None, None),
                        height = dp(5),
                        width = dp(20),
                        pos_hint = {"center_y":.5, "center_x":.125},
                        theme_text_color = "Custom",
                        text_color = [0, 0, .6, 1]
                    ),
                    MDIconButton(
                        icon = "thumb-down",
                        pos_hint = {"center_y":.5, "center_x":.225},
                        size_hint_x = 0.2,
                        on_release = lambda btn, title = self.heading: self.dislike_topic(title)
                    ),
                    MDLabel(
                        text = str(f"  {self.dislikes}"),
                        size_hint = (None, None),
                        height = dp(5),
                        width = dp(20),
                        pos_hint = {"center_y":.5, "center_x":.291},
                        theme_text_color = "Custom",
                        text_color = [0, 0, .6, 1]
                    ),
                    MDIconButton(
                        icon = "message",
                        pos_hint = {"center_y":.5, "center_x":.391},
                        size_hint_x = 0.2,
                        on_release = lambda btn, title = self.heading: self.open_comments_card(title)
                    ),
                    MDLabel(
                        text = str(f"  {self.comment_count}"),
                        size_hint = (None, None),
                        height = dp(5),
                        width = dp(20),
                        pos_hint = {"center_y":.5, "center_x":.457},
                        theme_text_color = "Custom",
                        text_color = [0, 0, .6, 1]
                    ),
                    MDIconButton(
                        icon = "share",
                        pos_hint = {"center_y":.5, "center_x":.557},
                        size_hint_x = 0.2,
                    ),
                    MDLabel(
                        text = str(f"  {self.shares}"),
                        size_hint = (None, None),
                        height = dp(5),
                        width = dp(20),
                        pos_hint = {"center_y":.5, "center_x":.623},
                        theme_text_color = "Custom",
                        text_color = [0, 0, .6, 1]
                    ),
                    MDIconButton(
                        icon = "star-outline",
                        pos_hint = {"center_y":.5, "center_x":.723},
                        size_hint_x = 0.2,
                        on_release = lambda btn, title = self.heading: self.favorite_topic(title)
                    ),
                    MDLabel(
                        text = str(f"  {self.favorites}"),
                        size_hint = (None, None),
                        height = dp(5),
                        width = dp(20),
                        pos_hint = {"center_y":.5, "center_x":.789},
                        theme_text_color = "Custom",
                        text_color = [0, 0, .6, 1]
                    ),
                    MDIconButton(
                        icon = "cancel",
                        pos_hint = {"center_y":.5, "center_x": .889},
                        size_hint_x = 0.2,
                        on_release = lambda btn, title = self.heading: self.report_topic(title)
                    ),
                    MDLabel(
                        text = str(f"  {self.reports}"),
                        size_hint = (None, None),
                        height = dp(5),
                        width = dp(20),
                        pos_hint = {"center_y":.5, "center_x":.965}, 
                        theme_text_color = "Custom",
                        text_color = [0, 0, .6, 1]
                    ),
                ),
                size_hint_y = None,
                height = dp(40),
                radius = [0, 0, 18, 18],
                style = "outlined",
                theme_bg_color = "Custom",
                md_bg_color = [0, 1, 1, .4]
            )
            space = Widget(
                size_hint_y = None,
                height = dp(20)
                
            )
            self.grid.add_widget(content_card)
            self.grid.add_widget(feedback_card)
            self.grid.add_widget(space)
    def account_info(self):
        if not hasattr(self, 'account_menu') or not self.account_menu:
            account_items = [
                {
                    "text": "Sign In",
                    "theme_text_color": "Custom",
                    "text_color": [0, 0, .6, 1],
                    "leading_icon": "account",
                    "theme_leading_icon_color": "Custom",
                    "leading_icon_color": [0, 0, .6, 1],
                    "on_release": self.go_to_login
                },
                {
                    "text": "Register",
                    "leading_icon": "account-plus",
                    "theme_text_color": "Custom",
                    "text_color": [0, 0, .6, 1],
                    "theme_leading_icon_color": "Custom",
                    "leading_icon_color": [0, 0, .6, 1],
                    "on_release": self.open_signup_dialog
                }
            ]
            self.signin_signup_menu =  MDDropdownMenu(
                caller = self.root.ids.account_info,
                items = account_items
            )
            self.account_menu = self.signin_signup_menu
        self.account_menu.open()
    
    def close_account_menu(self, *args):
        if self.account_menu:
            self.account_menu.dismiss()  # Dismiss the dialog
            self.account_menu = None 
    
    def go_to_login(self):
        self.close_account_menu()
        self.open_login_dialog()
    
    def open_login_dialog(self):
        if not hasattr(self, 'login_dialog') or not self.login_dialog:
            self.signin_username = MDTextField(
                MDTextFieldHintText(text="Username")
            )
            self.signin_password = MDTextField(
                MDTextFieldHintText(text="Password"),
                password = True
            )
            
            self.signin_validator = MDLabel(
                text = " ",
                theme_text_color = "Custom",
                text_color = "red"
            )

            content = MDDialogContentContainer(orientation="vertical", spacing=dp(20))
            content.add_widget(self.signin_username)
            content.add_widget(self.signin_password)
            content.add_widget(self.signin_validator)

            self.login_dialog = MDDialog(
                MDDialogIcon(icon="account"),
                MDDialogHeadlineText(text="Login to your account"),
                MDDialogSupportingText(text="Enter the username and password below"),
                content,
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(text="Sign In"),
                        on_release=lambda x: self.signin()
                    ),
                    MDButton(
                        MDButtonText(text="Cancel"),
                        on_release=lambda x: self.close_login_dialog()
                    ),
                    spacing=dp(15)
                )
            )

        self.login_dialog.open()

    def close_login_dialog(self):
        if self.login_dialog:
            self.login_dialog.dismiss()  # Dismiss the dialog
            self.login_dialog = None    # Clear the reference to allow re-creation

    def open_signup_dialog(self):
        self.close_account_menu()
        if not hasattr(self, 'signup_dialog') or not self.signup_dialog:
            self.register_username = MDTextField(
                MDTextFieldHintText(text = "Set username")
            )
            self.register_email = MDTextField(
                MDTextFieldHintText(text = "Email")
            )
            self.register_password = MDTextField(
                MDTextFieldHintText(text = "Set password"),
                password = True
            )
            self.register_password_confirm = MDTextField(
                MDTextFieldHintText(text = "Confirm password"),
                password = True
            )
            self.register_gender = MDTextField(
                MDTextFieldHintText(text = "Gender")
            )
            self.signup_validator = MDLabel(
                text = " ",
                theme_text_color = "Custom",
                text_color = "red"
            )
            content = MDDialogContentContainer(orientation = "vertical", spacing = dp(20))
            content.add_widget(self.register_username)
            content.add_widget(self.register_email)
            content.add_widget(self.register_password)
            content.add_widget(self.register_password_confirm)
            content.add_widget(self.register_gender)
            content.add_widget(self.signup_validator)
            self.signup_dialog = MDDialog(
                MDDialogIcon(icon = "account-plus"),
                MDDialogHeadlineText(text = "Create an iTREND account"),
                MDDialogSupportingText(text = "Enter your credentials as below"),
                content,
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(text = "Register"),
                        on_release = self.register
                    ),
                    MDButton(
                        MDButtonText(text = "Cancel"),
                        on_release = self.close_signup_dialog
                    ),
                    spacing = dp(15)
                )
            )
        self.signup_dialog.open()
    
    def close_signup_dialog(self, *args):
        if self.signup_dialog:
            self.signup_dialog.dismiss()  
            self.signup_dialog = None 

    def signin(self, *args):
        self.username = self.signin_username.text
        self.password = self.signin_password.text
        stored_user = itrendbase.session.query(itrendbase.Viewer).filter_by(viewer_name = self.username).first()
        if stored_user:
            if self.password == stored_user.viewer_password:
                self.open_welcome_dialog()
                self.signedin = True
                self.root.ids.account_info.on_release = self.show_signed_in_account
                return
            else:
                self.signin_validator.text = "Incorrect Password. Try again."
        else:
            self.signin_validator.text = f"<{self.username}> does not exist. Try different username"
    def show_signed_in_account(self, *kwargs):
        self.account_menu.dismiss()
        if not hasattr(self, 'signin_menu') or not self.signin_menu:
            sigin_menu = [
                        {"text": self.username,
                        "theme_text_color": "Custom",
                        "text_color": [0, 0, .6, 1],
                        "leading_icon": "account",
                        "theme_leading_icon_color": "Custom",
                        "leading_icon_color": [0, 0, .6, 1],
                        "on_release": self.initialize_account
                        }
                    ]
            self.signin_menu =  MDDropdownMenu(
                    caller = self.root.ids.account_info,
                    items = sigin_menu
                )
        self.new_menu = self.signin_menu
        self.new_menu.open()
    def close_new_account_menu(self, *args):
        if self.signin_menu:
            self.signin_menu.dismiss()
            self.signin_menu = None 
    def initialize_account(self):
        self.close_new_account_menu()
        self.go_to_account()
    def go_to_account(self, *args):
        stored_user = itrendbase.session.query(itrendbase.Viewer).filter_by(viewer_name = self.username).first()
        self.root.ids.sm.current = "account_screen"
        self.root.ids.account_name.text = self.username
        self.root.ids.account_email.text = stored_user.viewer_email
        self.root.ids.account_name.bind(width = lambda inst, val: setattr(inst, "text_size", (val, None)))
        self.root.ids.account_email.bind(width = lambda inst, val: setattr(inst, "text_size", (val, None)))
    def register(self, *args):
        username = self.register_username.text
        email = self.register_email.text
        password = self.register_password.text
        pass_confirm = self.register_password_confirm.text
        gender = self.register_gender.text
        
        stored_user = itrendbase.session.query(itrendbase.Viewer).filter_by(viewer_name = username).first()

        if password != pass_confirm:
            self.signup_validator.text = "Passwords do not match! Try re-entering them."
        elif stored_user:
            self.signup_validator.text = "Username already exists. Try something else."
            return
        else:
            itrendbase.session.add(itrendbase.Viewer(viewer_name = username, viewer_email = email, viewer_password = password, viewer_sex = gender, viewer_interests = "Anything..."))
            itrendbase.session.commit()
            self.finish_signup()

    def finish_signup(self):
        self.close_signup_dialog()
        self.finish_signup_dialog = MDDialog(
            MDDialogIcon(
                icon = "star-outline"
            ),
            MDDialogHeadlineText(
                text = "Signup Success!"
            ),
            MDDialogSupportingText(
                text = "You can now sign in to your account to access all features"
            ),
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(
                        text = "Sign In"
                    ),
                    on_release = self.request_login
                ),
                Widget()
            )
        )
        self.finish_signup_dialog.open()
    def request_login(self, *args):
        self.finish_signup_dialog.dismiss()
        self.open_login_dialog()
        
    def like_topic(self, title, *args):
        if self.signedin:
            viewer_username = self.username
            topic_title = title
            viewer_object = itrendbase.get_viewer_by_uname(viewer_username)
            topic_object = itrendbase.get_topic_by_title(topic_title)
            if viewer_object:
                itrendbase.session.add(itrendbase.Like(viewer_id = viewer_object.viewer_id, topic_id = topic_object.topic_id))
                topic = itrendbase.session.query(itrendbase.Topic).filter_by(topic_id = topic_object.topic_id).first()
                topic.like_count += 1
                itrendbase.session.commit()
                print("Liked successfully...")
        else:
            self.open_login_dialog()
    
    def dislike_topic(self, title, *args):
        if self.signedin:
            viewer_username = self.username
            topic_title = title
            viewer_object = itrendbase.get_viewer_by_uname(viewer_username)
            topic_object = itrendbase.get_topic_by_title(topic_title)
        
            if viewer_object:
                itrendbase.session.add(itrendbase.Dislike(viewer_id = viewer_object.viewer_id, topic_id = topic_object.topic_id))
                topic = itrendbase.session.query(itrendbase.Topic).filter_by(topic_id = topic_object.topic_id).first()
                topic.dislike_count += 1
                topic.like_count -= 1
                itrendbase.session.commit()
                print("Disliked successfully...")
        else:
            self.open_login_dialog()
    
    def favorite_topic(self, title, *args):
        if self.signedin:
            viewer_username = self.username
            topic_title = title
            viewer_object = itrendbase.get_viewer_by_uname(viewer_username)
            topic_object = itrendbase.get_topic_by_title(topic_title)
        
            if viewer_object:
                itrendbase.session.add(itrendbase.Favorite(viewer_id = viewer_object.viewer_id, topic_id = topic_object.topic_id))
                topic = itrendbase.session.query(itrendbase.Topic).filter_by(topic_id = topic_object.topic_id).first()
                topic.favorite_count += 1
                itrendbase.session.commit()
                print("Added to favorites successfully...")
        else:
            self.open_login_dialog()
            
    def report_topic(self, title, *args):
        if self.signedin:
            viewer_username = self.username
            topic_title = title
            viewer_object = itrendbase.get_viewer_by_uname(viewer_username)
            topic_object = itrendbase.get_topic_by_title(topic_title)
        
            if viewer_object:
                itrendbase.session.add(itrendbase.Reported(viewer_id = viewer_object.viewer_id, topic_id = topic_object.topic_id))
                topic = itrendbase.session.query(itrendbase.Topic).filter_by(topic_id = topic_object.topic_id).first()
                topic.reported_count += 1
                itrendbase.session.commit()
                print("Reported successfully...")
        else:
            self.open_login_dialog()
    
    def view_content(self, topic_title, topic_desc, topic_media, *args):
        self.root.ids.sm.current = "topic_screen"
        grid = self.root.ids.topic_content
        grid.size_hint_y = None
        grid.bind(minimum_height = grid.setter("height"))
        grid.clear_widgets()
        title = topic_title.upper()
        article_text = topic_desc
        media = topic_media
        
        topic_header = MDLabel(
            text = title,
            halign = "left",
            size_hint_y = None, 
            valign = "top",
            adaptive_height = True,
            bold = True,
            theme_font_size = "Custom",
            font_size = sp(18),
            theme_font_name = "Custom",
            font_name = "heading_font.ttf",
            theme_text_color = "Custom",
            text_color = "yellow"
        )
        topic_header.bind(width = lambda inst, val: setattr(inst, "text_size", (val, None)))
        article = MDLabel(
            text = article_text,
            size_hint_y = None, 
            valign = "top",
            halign = "left",
            theme_text_color = "Custom",
            text_color = [1, 1, 1, 1],
            theme_font_name = "Custom",
            font_name = "desc_font.ttf",
            adaptive_height = True
        )
        article.bind(width = lambda inst, val: setattr(inst, "text_size", (val, None)))
        image_card = MDCard(
            FitImage(
                source = topic_media
            ),
            size_hint_y = None,
            height = dp(300),
        )
        video_card = MDCard(
            VideoPlayer(
                source = topic_media,
            ),
            size_hint_y = None,
            height = dp(300),
        )
        grid.add_widget(topic_header)
        grid.add_widget(article)
        if not ".mp4" in media:
            grid.add_widget(image_card)
            return
        grid.add_widget(video_card)    
    def open_welcome_dialog(self):
        self.close_login_dialog()
        if not hasattr(self, 'welcome_dialog') or not self.welcome_dialog:
            self.welcome_dialog = MDDialog(
                MDDialogIcon(
                    icon = "star",
                ),
                MDDialogHeadlineText(
                    text = f"Hello, {self.username}!"
                ),
                MDDialogSupportingText(
                    text = "Sign In Success. Access all the content features now."
                ),
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(text = "Okay"),
                        on_release = self.close_welcome_dialog
                    ),
                    Widget()
                )
            )
        self.welcome_dialog.open()
    def close_welcome_dialog(self, *args):
        if self.welcome_dialog:
            self.welcome_dialog.dismiss()  # Dismiss the dialog
            self.welcome_dialog = None
    def open_comments_card(self, title, *args):
        if self.signedin:
            self.comment_text = MDTextField(MDTextFieldHintText(text = "Add comment..."))
            topic_object = itrendbase.get_topic_by_title(title)
            content = MDDialogContentContainer(orientation = "vertical", spacing = dp(20))
            main_scroll = MDScrollView(size_hint_y = None)
            main_grid = MDGridLayout(cols = 1, spacing = dp(10))
            main_grid.size_hint_y = None
            main_grid.bind(minimum_height = main_grid.setter("height"))
            main_scroll.add_widget(main_grid)
            content.add_widget(main_scroll)
            content.add_widget(
                Widget()
            )
            content.add_widget(self.comment_text)
            
            comment_objects = itrendbase.session.query(itrendbase.Comment).filter_by(topic_id = topic_object.topic_id).all()
            for comment_object in comment_objects:
                commenter = comment_object.viewer_commenting.viewer_name
                comment = comment_object.comment
                viewer_info = MDLabel(
                    text = f"{commenter}\n      {comment}",
                    size_hint_y = None,
                    halign = "left",
                    valign = "top",
                    adaptive_height = True,
                    )
                viewer_info.bind(width = lambda inst, val: setattr(inst, "text_size", (val, None)))
                main_grid.add_widget(viewer_info)
            self.comments_card = MDDialog(
                MDDialogIcon(
                    icon = "message"
                ),
                MDDialogHeadlineText(
                    text = f"Comment on {title}"
                ),
                MDDialogSupportingText(
                    text = "Your comment will be visible to other viewers."
                ),
                content,
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(
                            text = "Submit"
                        ),
                        on_release = lambda btn, topic_obj = topic_object: self.add_comment(topic_obj)
                    ),
                    MDButton(
                        MDButtonText(
                            text = "Cancel"
                        )
                    ),
                    spacing = dp(10)
                )
            )
            self.comments_card.open() 
        else:
            self.open_login_dialog()
    def add_comment(self, topic_obj, *args):
        topic_object = topic_obj
        viewer_username = self.username
        viewer_object = itrendbase.get_viewer_by_uname(viewer_username)
        if viewer_object:
            itrendbase.session.add(itrendbase.Comment(viewer_id = viewer_object.viewer_id, topic_id = topic_object.topic_id, comment = self.comment_text.text))
            topic = itrendbase.session.query(itrendbase.Topic).filter_by(topic_id = topic_object.topic_id).first()
            topic.comment_count += 1
            itrendbase.session.commit()
            print("Commented successfully...")
    def show_favorites(self, *args):
        self.root.ids.sm.current = "favorites_screen"
        user = itrendbase.get_viewer_by_uname(self.username)
        fav_topics = itrendbase.session.query(itrendbase.Favorite).filter_by(viewer_id = user.viewer_id).all()
        self.fav_grid = self.root.ids.favorites_container
        self.fav_grid.size_hint_y = None
        self.fav_grid.bind(minimum_height = self.fav_grid.setter("height"))
        self.fav_grid.clear_widgets()
        for topic in fav_topics:
            self.fav_heading = topic.topic_favorited.topic_title
            self.fav_illustration = topic.topic_favorited.topic_description
            self.fav_media = topic.topic_favorited.topic_media_url
            heading_title = MDLabel(
                        text = self.fav_heading,
                        size_hint_y = None,
                        height = dp(40),
                        pos_hint = {"y":.9},
                        theme_font_size = "Custom",
                        font_size = sp(22),
                        bold = True,
                        theme_text_color = "Custom",
                        text_color = [0, 0, .6, 1]
                        
                    )
            paragraph = MDLabel(
                    text = f"{self.fav_illustration[:109]} ...",
                    max_lines = 1,
                    ellipsis_options = {"mode": "end"},
                    halign = "left",
                    pos_hint = {"y":.69},
                    size_hint_y = None,
                    height = dp(20)
                )
            image_card = MDCard(
                        FitImage(
                            source = self.fav_media,
                            pos_hint = {"center_x":.5, "center_y":.5},
                            radius = [16, 16, 16, 16]
                        ),
                        size_hint_y = None,
                        height = dp(150),
                        size_hint_x = 0.95,
                        pos_hint = {"center_y":.3, "center_x":.5}
                    )
            video_card = MDCard(
                        VideoPlayer(
                            source = self.fav_media,
                            state = "stop",
                            options = {"eos": "loop"}
                        ),
                        size_hint_y = None,
                        height = dp(150),
                        size_hint_x = 0.95,
                        pos_hint = {"center_y":.3, "center_x":.5}
                    )
            cont_layout = MDRelativeLayout()
            cont_layout.add_widget(heading_title)
            cont_layout.add_widget(paragraph)
            if not ".mp4" in self.media:
                cont_layout.add_widget(image_card)
            else:
                cont_layout.add_widget(video_card)
            content_card = MDCard(
                cont_layout,
                size_hint_y = None,
                height = dp(300),
                padding = dp(20),
                radius = [18, 18, 18, 18],
                style = "outlined",
                theme_bg_color = "Custom",
                md_bg_color = [0, 1, 1, .2],
                on_release = lambda instance, topic_title = self.fav_heading, topic_desc = self.fav_illustration, topic_media = self.fav_media: self.view_fav_content(topic_title, topic_desc, topic_media)
            )
            space = Widget(
                size_hint_y = None,
                height = dp(20)
            )
            self.fav_grid.add_widget(content_card)
            self.grid.add_widget(space)
    def view_fav_content(self, topic_title, topic_desc, topic_media, *args):
        self.root.ids.sm.current = "fav_topic_screen"
        grid = self.root.ids.fav_topic_content
        grid.size_hint_y = None
        grid.bind(minimum_height = grid.setter("height"))
        grid.clear_widgets()
        title = topic_title.upper()
        article_text = topic_desc
        media = topic_media
        
        topic_header = MDLabel(
            text = title,
            halign = "left",
            size_hint_y = None, 
            valign = "top",
            adaptive_height = True,
            bold = True,
            theme_font_size = "Custom",
            font_size = sp(18),
            theme_font_name = "Custom",
            font_name = "heading_font.ttf",
            theme_text_color = "Custom",
            text_color = "yellow"
        )
        topic_header.bind(width = lambda inst, val: setattr(inst, "text_size", (val, None)))
        article = MDLabel(
            text = article_text,
            size_hint_y = None, 
            valign = "top",
            halign = "left",
            theme_text_color = "Custom",
            text_color = [1, 1, 1, 1],
            theme_font_name = "Custom",
            font_name = "desc_font.ttf",
            adaptive_height = True
        )
        article.bind(width = lambda inst, val: setattr(inst, "text_size", (val, None)))
        image_card = MDCard(
            FitImage(
                source = topic_media
            ),
            size_hint_y = None,
            height = dp(300),
        )
        video_card = MDCard(
            VideoPlayer(
                source = topic_media,
            ),
            size_hint_y = None,
            height = dp(300),
        )
        grid.add_widget(topic_header)
        grid.add_widget(article)
        if not ".mp4" in media:
            grid.add_widget(image_card)
            return
        grid.add_widget(video_card)
    def favorites_screen(self):
        if self.signedin:
            self.show_favorites()
        else:
            self.open_login_dialog()
    def account_screen(self):
        if self.signedin:
            self.go_to_account()
        else:
            self.open_login_dialog()
    def explore_content(self):
        self.root.ids.sm.current = "home"
    
    def go_to_favorites(self):
        self.root.ids.interest_uname.text = self.username
        self.root.ids.sm.current = "interests_screen" 
        interests = ["Politics", "Programming", "Art and Craft", "Music and Songs", 
                    "Movies and Films", "Lifestyle", "Gossip", "Health and Hygiene",
                    "Space Exploration", "Nature and Wildlife", "Sports"]
        grid = self.root.ids.interests_container
        grid.size_hint_y = None
        grid.bind(minimum_height = grid.setter("height"))
        grid.clear_widgets()
        for interest in interests:
            list_box = MDBoxLayout(
                MDCheckbox(
                    size_hint = (None, None),
                    size = (dp(48), dp(48))
                ),
                MDLabel(
                    text = f"\n{interest}",
                    size_hint_y = None,
                    height = dp(40),
                    valign =  "center"
                ),
                size_hint_y = None,
                height = dp(40),
                spacing = dp(10)
            )
            grid.add_widget(list_box)
        
        
    
    def logout(self):
        MDApp.get_running_app().stop()
    


if __name__ == "__main__":
    app = iTREND()
    app.run()