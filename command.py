import os
import downloader

class Interpreter:
	def __init__ (self):
		self.commands = {}
	def call (self, raw_command):
		if type (raw_command) != type (""): raise TypeError ("Input has to be a string")#Only string inputs
		self.raw = delSpaces (raw_command)#Interiorize the command
		self.getArgs ()
		self.callCommand ()
			
	def getArgs (self):
		self.args = []
		self.raw += " fakeArg"#Add fake arg
		while True:
			#When there is only 1 arg left, an error will occur and fake arg wont be added
			try:
				self.arg, self.raw = getArg (self.raw)#Take next arg
				self.args.append (self.arg)#Append new arg to the list
				self.raw = delSpaces (self.raw)#Clean remanents
			except:
				break
	
	def callCommand (self):
		self.command = None
		#try:
		if True:
			self.command = self.commands [self.args [0]]#Asign the command
			#try:
			if True:
				self.returned = self.command (*self.args[1:])#Call the command and pass the arguments
				if type (self.returned) == type (None):
					pass
				elif type (self.returned) == type ([]):
					for i in self.returned: print (i)
				else:
					print (self.returned)
			"""except Exception as inst:
				print (inst)"""
		"""except Exception as inst:
			print (inst)
			print ("Usually this is caused because you didnt import that command")"""

	def addCommand (self, name, function):
		self.commands [name] = function#Add comand to the list


def getArg (string):
	if string [0] == '"':#If the next arg is between "
		arg = string [1:string [1:].index ('"') + 1]
		return arg, string [len (arg) + 2:]
	else:#If the next arg isn't between "
		arg = string [:string [:].index (' ')]
		return arg, string [len (arg):]

def delSpaces (string):#Delete spaces on both sides of a string
	string = delStart (string)#Clean beggining
	string = delStart (string [::-1])#Cleaning the beggining fo the reverse, aka: the end
	return string[::-1]#Return and reverse again

def delStart (string):#Deletes spaces on the beggining of a string
	for i in range (len (string)):#Iterate the input
		if not string [i] == " ":#If its not a space,
			return string [i:]#return whats left
	
class SWFStarter:
	def __init__ (self, flashPath, SWFPath):
		self.flashPath = flashPath
		self.SWFPath = SWFPath
		self.aviable = self.getAviable ()

	def getAviable (self):
		self.all = os.listdir (self.SWFPath)
		self.files = [i for i in self.all if os.path.isfile (os.path.join (self.SWFPath, i))]
		self.swf = [i for i in self.files if os.path.splitext (i)[1] == ".swf"]
		self.swfNames = [i.split (".")[0] for i in self.swf]
		return self.swfNames

	def start (self, name):
		self.getAviable ()
		downloader.startSWF(self.flashPath, os.path.join (self.SWFPath, self.swf [self.swfNames.index (name)]))


def main ():
	interpreter = Interpreter ()
	starter = SWFStarter (os.path.join (downloader.relativePath (), "flashplayer.exe"), os.path.join (downloader.relativePath (), "SWF"))
	interpreter.addCommand ("start", starter.start)
	interpreter.addCommand ("getNames", starter.getAviable)
	while True:
		command = interpreter.call (input ("---"))

if __name__ == "__main__":
	main ()