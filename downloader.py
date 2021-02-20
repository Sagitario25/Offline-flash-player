import swf_collector as SWF
import subprocess
import os

def relativePath (relative = ""):#Relative path
	return os.path.join (os.path.dirname (__file__), relative)

def main (url, gameName):
    swf = SWF.SWF ()

    for i in ['"', "'"]:
        swf.getPage (url)
        getresult = swf.get (i)
        while True:
            if getresult == -1:
                print ("None swf file in page")
                break
            elif getresult == "non valid":
                getresult = swf.getNext (i)
            else:
                print ("Swf file found!!")
                print ("Downloading...")
                while True:
                    try:
                        path = os.path.join (relativePath (), "SWF")
                        fileName = gameName + ".swf"
                        if not os.path.exists (path):
                            os.mkdir (path)
                        swf.download (os.path.join (path, fileName))
                        break
                    except Exception:
                        print ("Trying")
                        swf.getNext ()
                print ("Done")
                print ("Starting...")
                subprocess.call([os.path.join (relativePath (), "flashplayer.exe"), os.path.join (relativePath (), "SWF", gameName + ".swf")])
                exit ()
    
if __name__ == "__main__":
    main ("https://www.newgrounds.com/portal/view/604080", "Rogue soul")