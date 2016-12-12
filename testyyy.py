from tkinter import *

import tkinter
import tkinter.simpledialog
import webbrowser, time
import os

root = tkinter.Tk()
root.resizable(width=False, height=False)  #prevent changing window size by user
root.geometry('{}x{}'.format(300, 120))  # window size (width, height)
root.wm_title("Open da UrLyyy")

google_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
firefox_path = "C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s"
# iexplorer_path = "C:/Program Files/Internet Explorer/iexplore.exe %s"
iexplorer_path = webbrowser.iexplore

# open entered URL
def open_url_chrome():
	if (e1.get() != ''):
		webbrowser.get(google_path).open_new(e1.get())
	if (e2.get() != ''):
		webbrowser.get(google_path).open_new_tab(e2.get())
	if (e3.get() != ''):
		webbrowser.get(google_path).open_new_tab(e3.get())
	else:
		print("nein!")

def open_url_firefox():

	urls = []
	urls.append(e1.get()) if (e1.get() != '') else ""
	urls.append(e2.get()) if (e2.get() != '') else ""
	urls.append(e3.get()) if (e3.get() != '') else ""

	webbrowser.get(firefox_path).open(urls[0])
	time.sleep(5)
	for url in urls[1:]:
		webbrowser.get(firefox_path).open_new_tab(url)
	# if (e1.get() != ''):
	# 	webbrowser.get(firefox_path).open(e1.get())
	# if (e2.get() != ''):
	# 	webbrowser.get(firefox_path).open_new_tab(e2.get())
	# if (e3.get() != ''):
	# 	webbrowser.get(firefox_path).open_new_tab(e3.get())
	# else:
	# 	print("nein!")

def open_url_ie():
	if (e1.get() != ''):
		webbrowser.get(iexplorer_path).open_new(e1.get())
	if (e2.get() != ''):
		webbrowser.get(iexplorer_path).open_new_tab(e2.get())
	if (e3.get() != ''):
		webbrowser.get(iexplorer_path).open_new_tab(e3.get())
	else:
		print("nein!")

# labels
Label(root, text="URL").grid(row=0)
Label(root, text="URL2").grid(row=1)
Label(root, text="URL3").grid(row=2)

# entries
e1 = Entry(root, width=40)
e2 = Entry(root, width=40)
e3 = Entry(root, width=40)

e1.grid(row=0, column=1, padx=5, pady=5)
e2.grid(row=1, column=1, padx=5, pady=5)
e3.grid(row=2, column=1, padx=5, pady=5)

########## condition to check if the text field is empty ###############
def inputCheck():
	if len(e1.get() or e2.get() or e3.get()) == 0:
		print("No input detected")
	else:
		# open_url_ie()
		# open_url_chrome()
		open_url_firefox()		
########################################################################

ok_button = Button(root, text='OK', command=inputCheck).grid(row=3, column=0, sticky=W, padx=5)
quit_button = Button(root, text='Quit', command=root.quit).grid(row=3, column=1, sticky=E)

mainloop()