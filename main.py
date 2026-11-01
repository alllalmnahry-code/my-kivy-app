# -*- coding: utf-8 -*-
"""
Kivy Mobile Application with Arabic Support.
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from arabic_helper import ar, get_arabic_font


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        btn = Button(
            text=ar("اضغط هنا"),
            font_name=get_arabic_font(),
            font_size="22sp",
            size_hint=(1, 0.4),
            background_normal="",
            background_color=(0.14, 0.48, 0.88, 1)
        )
        btn.bind(on_press=self.on_button_click)

        layout.add_widget(btn)
        return layout

    def on_button_click(self, instance):
        instance.text = ar("تم الضغط بنجاح!")


if __name__ == '__main__':
    MyApp().run()
