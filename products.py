from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import datetime


class GenericProductsPrinter(widgets.Output):
    def __init__(self):
        super(GenericProductsPrinter, self).__init__()
        self.slider_out = widgets.Output()
        self.pretty_print_out = widgets.Output()
        self.timestamp_out = widgets.Output()
        self.slider = None
        self.prods = []
        self.index = 0
        
        with self:
            display(self.pretty_print_out)
            display(self.slider_out)
            display(self.timestamp_out)

    def append(self, prod):
        self.prods.append((prod, str(datetime.datetime.now())))
        if self.index == len(self.prods) - 2:
            self.index += 1
        self.update_display()

    def update_index(self, change):
        self.index = change['new']
        self.update_pretty_print_display()

    def update_pretty_print_display(self):
        self.pretty_print_out.clear_output(True)
        self.timestamp_out.clear_output(True)
        if self.prods:
            prod, time = self.prods[self.index]
            with self.pretty_print_out:
                prod.pretty_print()
            with self.timestamp_out:
                print("timestamp - ", time)

    def update_slider(self):
        if not self.slider:
            with self.slider_out:
                self.slider = widgets.IntSlider(min=0, max=len(self.prods) - 1, step=1, value=self.index)
                display(self.slider)
                self.slider.observe(self.update_index, names='value')
        else:
            self.slider.max = len(self.prods) - 1
            self.slider.value = self.index

    def update_display(self):
        self.update_pretty_print_display()
        self.update_slider()
