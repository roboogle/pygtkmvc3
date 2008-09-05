#  Author: Roberto Cavada <cavada@fbk.eu>
#
#  Copyright (c) 2008 by Roberto Cavada
#
#  pygtkmvc is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
#
#  pygtkmvc is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, write to the Free
#  Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110, USA.
#  02111-1307 USA.
#
#  For more information on pygtkmvc see
#  <http://pygtkmvc.sourceforge.net> or email to the author Roberto
#  Cavada <cavada@fbk.eu>.  Please report bugs to
#  <cavada@fbk.eu>.


import _importer
from gtkmvc import Model, Controller, View
from gtkmvc.adapters.basic import Adapter

import gtk

# Here a set of widgets is connected to a set of data in the model.
# Changing one value in the model has the effect of changing all
# widgets which observe that value in the model.
#
# The resulting example is a little weird, but looking at the
# simplicity of the code it should be easy to understand the powerful
# of adapters.


class MyView (View):
    def __init__(self, ctrl):
        View.__init__(self, ctrl, "adapters.glade", "window9")
        return
    pass

import datetime
class MyModel (Model):
    __properties__ = {
        'expan' : True,
        'toggle' : True,
        'color' : gtk.gdk.color_parse("black"),
        'url' : "http://pygtkmvc.sourceforge.net/",
        'spin' : 5.0,
        }

    def __init__(self):
        Model.__init__(self)
        return
    pass


class MyCtrl (Controller):
    def __init__(self, m):
        Controller.__init__(self, m)
        return

    def register_adapters(self):        
        # labels
        self.adapt("expan", "label10")
        
        ad = Adapter(self.model, "toggle")
        ad.connect_widget(self.view["label_t1"], setter=lambda w,v: \
                            w.set_markup("<big><b>%i</b></big>" % v))
        self.adapt(ad)
        self.adapt("toggle", "label_t2")
        self.adapt("color", "label_t3")
        self.adapt("url", "label_t4")
        self.adapt("spin", "label_t5")

        # controls
        self.adapt("expan", "expander1")        
        self.adapt("toggle", "togglebutton1")
        self.adapt("toggle", "checkbutton1")
        self.adapt("color", "colorbutton1")
        #self.adapt("url", "linkbutton1") ##This needs glade-3
        self.adapt("spin", "spinbutton1")
        return

    def on_window9_delete_event(self, w, e):
        gtk.main_quit()
        return True

    pass # end of class

# ----------------------------------------------------------------------

m = MyModel()
c = MyCtrl(m)
v = MyView(c)

gtk.main()
