from ._anvil_designer import Strategy_dashTemplate
from anvil import *
import anvil.server
import datetime

class Strategy_dash(Strategy_dashTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.drop_down_1.items=['S1','S2']
    self.drop_down_2.items=['EURUSD','XAUUSD']
    self.outlined_card_3.visible=False
    self.date_picker_1.date=datetime.datetime.now().date() - datetime.timedelta(days=int(365))
    self.date_picker_2.date = datetime.datetime.now().date() #initialize to date
   
    #= date_to.date() - datetime.timedelta(days=int(ndays))
    

  def button_1_click(self, **event_args):
    start=self.date_picker_1.date
    end=self.date_picker_2.date
    symbol=self.drop_down_2.selected_value
    strategy=self.drop_down_1.selected_value
    bar,line,exp,num=anvil.server.call('stratFadeExposure',symbol,start,end)#Write this method 
    self.plot_1.figure=bar
    self.label_3.text=exp
    self.label_5.text=num
    self.outlined_card_3.visible=True
    
    
    

    

     
    
  
    
   





    
  


   
  
