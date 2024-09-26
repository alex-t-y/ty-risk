from ._anvil_designer import HOMETemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
#import anvil.users
from ..Overview_dash import Overview_dash
from ..Clients_dash import Clients_dash
from ..Newsfeed_dash import Newsfeed_dash
from ..Strategy_dash import Strategy_dash
from ..Settings import Settings
from ..Execution_dash import Execution_dash

class HOME(HOMETemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.Overview_dash=None # PERSISTENSE 
    self.Clients_dash=None
    self.Strategy_dash=None
    #self.content_panel.add_component(Main_dash(),full_width_row=True)
    # Any code you write here will run before the form opens.
  
  def link_1_click(self, **event_args):
    self.Overview_dash=self.Overview_dash or Overview_dash() # PERSISTENSE
    self.content_panel.clear()
    self.link_2.role=' '
    self.link_3.role=' '
    self.link_4.role=' '
    self.link_5.role=' '
    self.link_6.role=' '
    # Add Page1 to the content panel
    self.content_panel.add_component(self.Overview_dash, full_width_row=True)
    self.link_1.role='selected'
    
  def link_2_click(self, **event_args):
    self.Clients_dash=self.Clients_dash or Clients_dash() # PERSISTENSE
    self.content_panel.clear()
    self.link_1.role=' '
    self.link_3.role=' '
    self.link_4.role=' '
    self.link_5.role=' '
    self.link_6.role=' '
    self.content_panel.add_component(self.Clients_dash,full_width_row=True)
    self.link_2.role='selected'
    
  def link_3_click(self, **event_args):
    self.content_panel.clear()
    self.link_1.role=' '
    self.link_2.role=' '
    self.link_4.role=' '
    self.link_5.role=' '
    self.link_6.role=' '
    self.content_panel.add_component(Settings(),full_width_row=True)
    self.link_3.role='selected'

  def link_4_click(self, **event_args):
    self.content_panel.clear()
    self.link_1.role=' '
    self.link_2.role=' '
    self.link_3.role=' '
    self.link_5.role=' '
    self.link_6.role=' '
    self.content_panel.add_component(Newsfeed_dash(),full_width_row=True)
    self.link_4.role='selected'

  def link_5_click(self, **event_args):
    self.Strategy_dash=self.Strategy_dash or Strategy_dash() # PERSISTENSE
    self.content_panel.clear()
    self.link_1.role=' '
    self.link_2.role=' '
    self.link_3.role=' '
    self.link_4.role=' '
    self.link_6.role=' '
    self.content_panel.add_component(self.Strategy_dash,full_width_row=True)
    self.link_5.role='selected'

  def link_6_click(self, **event_args):
    self.content_panel.clear()
    self.link_1.role=' '
    self.link_2.role=' '
    self.link_3.role=' '
    self.link_4.role=' '
    self.link_5.role=' '
    self.content_panel.add_component(Execution_dash(),full_width_row=True)
    self.link_6.role='selected'
    
   
  

  def button_1_click(self, **event_args):
    #self.timer_1.interval = 0 
    #self.timer_2.interval = 0 
    #anvil.users.logout()
    #anvil.server.call('MT5ManagerDisconnect')
    open_form('Login')


    
    


  
