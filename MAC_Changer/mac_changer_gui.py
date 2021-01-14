import tkinter as tk
import mac_changer


window = tk.Tk()
window.title('MAC Address Changer')
window.iconbitmap('mac.ico')
window.geometry('300x200')



bt = tk.StringVar(window)
bt.set('NetWork Interface')


def clicked(*args):
	
	global insert_mac	

	insert_mac = tk.Entry(window, textvariable = bt.get(), width = 30)
	insert_mac.pack()
	
	enter_button = tk.Button(window, text = 'Enter', command = lambda: print(insert_mac.get()))
	enter_button.pack()


available_interfaces = ['eth0', 'eth1', 'wlan0', 'wlan1']

drop = tk.OptionMenu(window, bt, *available_interfaces, command = clicked)
drop.pack()

window.mainloop()

