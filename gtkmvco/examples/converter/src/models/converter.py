#  Author: Roberto Cavada <cavada@irst.itc.it>
#
#  Copyright (c) 2006 by Roberto Cavada
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
#  License along with this library; if not, write to the Free Software
#  Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#  For more information on pygtkmvc see <http://pygtkmvc.sourceforge.net>
#  or email to the author <cavada@irst.itc.it>.
#  Please report bugs to <cavada@irst.itc.it>.


import utils._importer
import utils.globals

from amount import AmountModel
from gtkmvc import Model

class ConverterModel (Model):
    __properties__ = {
        'can_convert' : False,
        }
    def __init__(self, currencies_model):
        Model.__init__(self)

        self.source = AmountModel(currencies_model)
        self.target = AmountModel(currencies_model)

        self.source.register_observer(self)
        self.target.register_observer(self)

        return

    def convert(self):
        if not self.can_convert: return
        srate = self.source.get_currency().rate        
        crate = self.target.get_currency().rate
        self.target.amount = self.source.amount * (crate / srate)
        return
        
    
    # ----------------------------------------
    #          observable properties
    # ----------------------------------------
    def property_iter_value_change(self, model, old, new):
        assert model in (self.source, self.target)
        self.can_convert = (self.source.iter is not None and
                            self.target.iter is not None)
        return
        
    pass # end of class
