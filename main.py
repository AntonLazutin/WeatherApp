from decimal import Decimal
from tkinter import *
import requests
import timeit

api_key = 'ba3416e49fa704ff6ab7a96621ff9430'

def on_click():
    start = timeit.default_timer()
    try:
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={entry.get()}&appid={api_key}')
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        temp_label.config(text = 'Invalid input: ' + err.response.text[24:38])
        stop = timeit.default_timer()
        print('Time: ', stop - start)  
        return
    weather = "%.2f" % (response.json().get('main').get('temp') - 273.15)
    temp_label.config(text = f'{weather}°C')
    stop = timeit.default_timer()
    print('Time: ', stop - start)  

if __name__ == "__main__":

    window = Tk()
    window.title('Weather app')
    window.iconbitmap('images/cloudy.ico')

    entry = Entry (width=50)
    entry.pack()
    
    temp_label = Label(width=50, text='Temp will be there!')
    temp_label.pack()

    button_frame = Frame(window, highlightbackground = "black", 
                         highlightthickness = 1, bd=0)
    button = Button(button_frame, width=50, text='get weather', command=on_click)
    button.pack()
    button_frame.pack()
   
    window.mainloop()

