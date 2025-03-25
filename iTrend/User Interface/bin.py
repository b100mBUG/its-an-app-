from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor
    MDIcon:
        icon: "gmail"
        pos_hint: {'center_x': .5, 'center_y': .5}
        MDBadge:
            text: "12"
'''
class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)
Example().run()