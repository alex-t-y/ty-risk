from ._anvil_designer import Overview_dashTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import datetime

class Overview_dash(Overview_dashTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.server.call('MT5ManagerConnect3')
    global days
    days=1
    anvil.server.call('requestDeals',days-1)
    anvil.server.call('requestOpenPositions')
    
    print(anvil.server.call('lenDeals'))
    self.plot_4.figure=anvil.server.call('plot_closed_pl_allgroups')
    exp_symbol,exp_login=anvil.server.call('plot_expectations_closed')

    self.repeating_panel_2.items=anvil.server.call('display_metrics')
    self.repeating_panel_1.items=anvil.server.call('floatingPL_table')
    self.plot_7.figure=exp_symbol
    self.plot_8.figure=exp_login
    

    open_pl=anvil.server.call('plot_floating')
    self.plot_1.figure=open_pl

    exp_symbol,exp_login=anvil.server.call('plot_expectations_floating')
    #self.plot_7.figure=exp_symbol
    #self.plot_8.figure=exp_login
    
    
    '''
    p1,p2,p3=anvil.server.call('plot_open_positions_groups')
    self.plot_1.figure=p1
    self.plot_2.figure=p2
    self.plot_3.figure=p3
    exp_symbol,exp_login=anvil.server.call('plot_rolling_expectations',days,30,0.5)
    self.plot_5.figure=exp_symbol
    self.plot_6.figure=exp_login
    '''

  def timer_1_tick(self, **event_args):
    self.timer_1.interval = 15
    now = datetime.datetime.now()
    print(now)
    anvil.server.call_s('requestDeals',days-1)
    self.repeating_panel_2.items=anvil.server.call_s('display_metrics')
    self.label_1.text='Last update: '+str(now)
    
    


  
    



   