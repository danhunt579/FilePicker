"""
File:	filedemo.py
Date:	03.28.19
Name: 	Dan

-	demonstrates use of file open dialog box in python
"""

from breezypythongui import EasyFrame
import tkinter.filedialog

class FileDialogDemo(EasyFrame):
	"""Demonstrates the use of a file dialog"""
	def __init__(self):
		"""Sets up the window and the widgets"""
		EasyFrame.__init__(self, title = "File Dialog Demo")
		self.outputArea = self.addTextArea("", row = 0, column = 0, width = 80, height = 15)
		
		# Command Button
		self.addButton(text = "open", row = 1, column = 0, command = self.openFile)
		
		
	def openFile(self):
		"""Pops up an open file dialog.  If a file is selected, it will display it's text in the text area and it's path name in the title bar."""
		
		fList = [("Python Files", "*.py"), ("Text Files", "*.txt")]
		fileName = tkinter.filedialog.askopenfilename(parent = self, filetypes = fList)
		
		if fileName != "":
			file = open(fileName, 'r')
			text = file.read()
			file.close()
			self.outputArea.setText(text)
			self.setTitle(fileName)
			
			
def main():
	FileDialogDemo().mainloop()
	
main()
		
		
	