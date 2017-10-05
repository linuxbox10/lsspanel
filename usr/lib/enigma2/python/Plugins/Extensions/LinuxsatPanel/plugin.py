from Components.MenuList import MenuList
from Components.Label import Label
from Components.Button import Button
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Components.ActionMap import NumberActionMap
from Components.Input import Input
from Components.Pixmap import Pixmap
from Components.FileList import FileList
from Screens.ChoiceBox import ChoiceBox
from Plugins.Plugin import PluginDescriptor
from Components.ActionMap import ActionMap 
from Screens.PluginBrowser import PluginBrowser
from Components.config import config
from Components.Pixmap import Pixmap, MovingPixmap
from Components.FileList import FileList
from Components.ActionMap import ActionMap, NumberActionMap
from Components.Sources.StaticText import StaticText
from Components.FileList import FileList
from Components.AVSwitch import AVSwitch
from Components.Sources.List import List
import os, re
from twisted.web.client import getPage
from Screens.Standby import TryQuitMainloop
#################
from Screens.Screen import Screen
from Plugins.Plugin import PluginDescriptor
from Components.ActionMap import ActionMap
from Components.MenuList import MenuList
from Components.Pixmap import Pixmap
from xml.dom import Node
from xml.dom import minidom
import os
from Components.Button import Button
from Components.ScrollLabel import ScrollLabel
from enigma import *
from Screens.MessageBox import MessageBox
from Screens.Console import Console
from twisted.web.client import downloadPage
from twisted.web.client import getPage
import urllib2
from Components.Label import Label
from Components.ScrollLabel import ScrollLabel
from Tools.Directories import fileExists
##################
import gettext
from Components.MultiContent import MultiContentEntryText, MultiContentEntryPixmapAlphaTest
from enigma import getDesktop
DESKHEIGHT = getDesktop(0).size().height()

def _(txt):
	t = gettext.dgettext("LinuxsatPanel", txt)
	if t == txt:
		print "[LinuxsatPanel] fallback to default translation for", txt
		t = gettext.gettext(txt)
	return t

#####################################
#                                   #
#   Coded by masterG - oktus - pcd  #
#                                   #
#####################################

class RSList(MenuList):
	def __init__(self, list):
		MenuList.__init__(self, list, True, eListboxPythonMultiContent)
		if DESKHEIGHT > 1000: 
		       self.l.setItemHeight(50)
		       textfont = int(30)
		else:
		       self.l.setItemHeight(40)
		       textfont = int(20)
                self.l.setFont(0, gFont("Regular", textfont))
                

def RSListEntry(download):
	res = [(download)]

        white = 0xffffff 
        grey = 0xb3b3b9
        green = 0x389416
        black = 0x000000
        yellow = 0xe5b243
        blue = 0x002d39
        red = 0xf07655
        col = 0xffffff
#        colsel = 0xf07655
#        backsel = 0x000000
        colsel = 0xffffff
        backsel = 0x252727        
#          <widget name="list" position="80,140" size="720,500" zPosition="4" font="Regular;25" foregroundColor="#ffffff" foregroundColorSelected="#ffffff" backgroundColor="#3f4040" transparent="1"  backgroundColorSelected="#252727" scrollbarMode="showNever" alphatest="blend" />
        
#        res.append(MultiContentEntryText(pos=(0, 0), size=(650, 40), text=download, color=col, color_sel = colsel, backcolor_sel = backsel))
        res.append(MultiContentEntryText(pos=(0, 0), size=(1000, 40), text=download, color=col, color_sel = colsel, backcolor_sel = backsel))

        return res

def showlist(data, list):                   
                       icount = 0
                       plist = []
                       for line in data:
#                               print "In showlist line =", line
                               name = data[icount]                               
                               plist.append(RSListEntry(name))                               
                               icount = icount+1

		       list.setList(plist)


#################                
class LinuxsatPanelFHD(Screen):
        skin = """
        <screen name="LinuxsatPanelFHD" position="0,0" size="1920,1080" title="Linuxsat Addons Setup" >
		<ePixmap position="0,0" zPosition="0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/icons2/panel4.png" backgroundColor="#25062748" alphatest="on" />
		<eLabel position="0,0" zPosition="-10" size="1920,1080" backgroundColor="black" />
                <widget source="session.VideoPicture" render="Pig" position="1218,535" size="606,339" zPosition="1" backgroundColor="#ff000000" />

                <widget name="frame" position="135,150" size="180,195" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/pic_frame2B.png" zPosition="3" alphatest="on" />   
                <widget source="label1" render="Label" position="50,370" size="210,60" font="Regular;30" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap1" position="80,200" size="150,150" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label2" render="Label" position="280,370" size="210,60" font="Regular;30" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap2" position="310,200" size="150,150" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label3" render="Label" position="490,370" size="210,60" font="Regular;30" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap3" position="520,200" size="150,150" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label4" render="Label" position="700,370" size="210,60" font="Regular;30" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap4" position="730,200" size="150,150" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label5" render="Label" position="910,370" size="210,60" font="Regular;30" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap5" position="940,200" size="150,150" zPosition="2" transparent="1" alphatest="on" />

                <widget source="label6" render="Label" position="50,585" size="210,60" font="Regular;30" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap6" position="80,425" size="150,150" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label7" render="Label" position="280,585" size="210,60" font="Regular;30" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap7" position="310,425" size="150,150" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label8" render="Label" position="490,585" size="210,60" font="Regular;30" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap8" position="520,425" size="150,150" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label9" render="Label" position="700,585" size="210,60" font="Regular;30" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap9" position="730,425" size="150,150" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label10" render="Label" position="910,585" size="210,60" font="Regular;30" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap10" position="940,425" size="150,150" zPosition="2" transparent="1" alphatest="on" />

                <widget source="label11" render="Label" position="50,795" size="210,60" font="Regular;30" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap11" position="80,635" size="150,150" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label12" render="Label" position="280,795" size="210,60" font="Regular;30" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap12" position="310,635" size="150,150" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label13" render="Label" position="490,795" size="210,60" font="Regular;30" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap13" position="520,635" size="150,150" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label14" render="Label" position="700,795" size="210,60" font="Regular;30" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap14" position="730,635" size="150,150" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label15" render="Label" position="910,795" size="210,60" font="Regular;30" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap15" position="940,635" size="150,150" zPosition="2" transparent="1" alphatest="on" />

                <widget source="label16" render="Label" position="50,1005" size="210,60" font="Regular;30" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap16" position="80,845" size="150,150" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label17" render="Label" position="280,1005" size="210,60" font="Regular;30" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap17" position="310,845" size="150,150" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label18" render="Label" position="490,1005" size="210,60" font="Regular;30" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap18" position="520,845" size="150,150" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label19" render="Label" position="700,1005" size="210,60" font="Regular;30" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap19" position="730,845" size="150,150" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label20" render="Label" position="910,1005" size="210,60" font="Regular;30" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap20" position="940,845" size="150,150" zPosition="2" transparent="1" alphatest="on" />

                </screen>"""
        

class LinuxsatPanel(Screen):
        skin = """
        
        <screen name="LinuxsatPanel" position="0,0" size="1280,720" title="Linuxsat Addons Setup" >
		<ePixmap position="0,0" zPosition="0" size="1280,720" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/icons/panel3.png" backgroundColor="#25062748" alphatest="on" />
		<eLabel position="0,0" zPosition="-10" size="1280,720" backgroundColor="black" />
                <widget source="session.VideoPicture" render="Pig" position="802,292" size="411,238" zPosition="1" backgroundColor="#ff000000" />

                <widget name="frame" position="90,50" size="120,130" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/pic_frame2.png" zPosition="3" alphatest="on" />   
                <widget source="label1" render="Label" position="35,225" size="140,40" font="Regular;20" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap1" position="55,120" size="100,100" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label2" render="Label" position="175,225" size="140,40" font="Regular;20" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap2" position="195,120" size="100,100" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label3" render="Label" position="315,225" size="140,40" font="Regular;20" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap3" position="335,120" size="100,100" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label4" render="Label" position="455,225" size="140,40" font="Regular;20" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap4" position="475,120" size="100,100" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label5" render="Label" position="595,225" size="140,40" font="Regular;20" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap5" position="615,120" size="100,100" zPosition="2" transparent="1" alphatest="on" />

                <widget source="label6" render="Label" position="35,365" size="140,40" font="Regular;20" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap6" position="55,260" size="100,100" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label7" render="Label" position="175,365" size="140,40" font="Regular;20" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap7" position="195,260" size="100,100" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label8" render="Label" position="315,365" size="140,40" font="Regular;20" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap8" position="335,260" size="100,100" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label9" render="Label" position="455,365" size="140,40" font="Regular;20" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap9" position="475,260" size="100,100" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label10" render="Label" position="595,365" size="140,40" font="Regular;20" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap10" position="615,260" size="100,100" zPosition="2" transparent="1" alphatest="on" />

                <widget source="label11" render="Label" position="35,500" size="140,40" font="Regular;20" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap11" position="55,395" size="100,100" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label12" render="Label" position="175,500" size="140,40" font="Regular;20" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap12" position="195,395" size="100,100" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label13" render="Label" position="315,500" size="140,40" font="Regular;20" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap13" position="335,395" size="100,100" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label14" render="Label" position="455,500" size="140,40" font="Regular;20" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap14" position="475,395" size="100,100" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label15" render="Label" position="595,500" size="140,40" font="Regular;20" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap15" position="615,395" size="100,100" zPosition="2" transparent="1" alphatest="on" />

                <widget source="label16" render="Label" position="35,635" size="140,40" font="Regular;20" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap16" position="55,530" size="100,100" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label17" render="Label" position="175,635" size="140,40" font="Regular;20" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap17" position="195,530" size="100,100" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label18" render="Label" position="315,635" size="140,40" font="Regular;20" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap18" position="335,530" size="100,100" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label19" render="Label" position="455,635" size="140,40" font="Regular;20" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap19" position="475,530" size="100,100" zPosition="2" transparent="1" alphatest="on" />
                <widget source="label20" render="Label" position="595,635" size="140,40" font="Regular;20" halign="center" zPosition="2" transparent="1" noWrap="1" foregroundColor="white" />
                <widget name="pixmap20" position="615,530" size="100,100" zPosition="2" transparent="1" alphatest="on" />

                </screen>  """

       

	def __init__(self, session, data):
	        if DESKHEIGHT > 1000:
		       self.skin = LinuxsatPanelFHD.skin
		else:       
		       self.skin = LinuxsatPanel.skin
		Screen.__init__(self, session)
		self.data = data
		title = "Linuxsat Support Addons Manager"
		self["title"] = Button(title)
#		self["text"] = Input("1234", maxSize=True, type=Input.NUMBER)
                if DESKHEIGHT > 1000:
		       self.pos = []		
                       self.pos.append([80,200])
                       self.pos.append([310,200])
                       self.pos.append([520,200])
                       self.pos.append([730,200])
                       self.pos.append([940,200])
                
                       self.pos.append([80,425])
                       self.pos.append([310,425])
                       self.pos.append([520,425])
                       self.pos.append([730,425])
                       self.pos.append([940,425])
                
                       self.pos.append([80,635])
                       self.pos.append([310,635])
                       self.pos.append([520,635])
                       self.pos.append([730,635])
                       self.pos.append([940,635])
                
                       self.pos.append([80,845])
                       self.pos.append([310,845])
                       self.pos.append([520,845])
                       self.pos.append([730,845])
                       self.pos.append([940,845])

                else:
		       self.pos = []		
                       self.pos.append([50,115])
                       self.pos.append([190,115])
                       self.pos.append([330,115])
                       self.pos.append([470,115])
                       self.pos.append([610,115])
                
                       self.pos.append([50,255])
                       self.pos.append([190,255])
                       self.pos.append([330,255])
                       self.pos.append([470,255])
                       self.pos.append([610,255])
                
                       self.pos.append([50,390])
                       self.pos.append([190,390])
                       self.pos.append([330,390])
                       self.pos.append([470,390])
                       self.pos.append([610,390])
                
                       self.pos.append([50,525])
                       self.pos.append([190,525])
                       self.pos.append([330,525])
                       self.pos.append([470,525])
                       self.pos.append([610,525])

#                print " self.pos =", self.pos
		
		list = []
		tlist = []
		self.pics = []
		self.titles = []
		
	
		       			   
	            
		list.append("Arm Softcams")  
		list.append("Backup")
		list.append("Black Hole")
		list.append("Bouquets")
                list.append("Channel List")
		list.append("Dependencies")
		list.append("dreamelite")
		list.append("DVB USB")
		list.append("EPG")
		list.append("IPTV")
		list.append("ItalySat")
		list.append("Key Updater")
		list.append("Kodi")
		list.append("KodiLite")
                list.append("Merlin")
                list.append("MultiBoot")
		list.append("Multimedia")
		list.append("newnigma2")
		list.append("OE2.2 Plugins")
		list.append("OE2.2 Skins")
		list.append("OE2.2Softcams")
		list.append("OoZooN")
		list.append("OpenATV")
                list.append("OpenBlackHole")
                list.append("OpenDroid")
                list.append("OpenESI")
                list.append("OpenLD")
                list.append("OpenNFR")
                list.append("OpenPLI")
                list.append("OpenPLUS")
		list.append("OpenSPA")
                list.append("OSCam Configs")
		list.append("OSCam CCcam")
		list.append("Other")
                list.append("Panels")
                list.append("PBnigma2")
                list.append("Hyperion")
		list.append("Picon")
                list.append("PowerSat")
		list.append("Radio")
                list.append("RuDream")
                list.append("SatDreamGR")
                list.append("SH4")
		list.append("Skins BH")
                list.append("Skins OBH")
                list.append("Skins ViX")
		list.append("Skins VTi")	
                list.append("Softcam Tools")
                list.append("Sport")
                list.append("VTi")
                list.append("Weather")
                list.append("WeTeK")
		list.append("Information")
		list.append("About")
		
                self.titles.append("Arm Softcams")  
		self.titles.append("Backup")
		self.titles.append("Black Hole")
		self.titles.append("Bouquet plugin")
		self.titles.append("Channel List")
		self.titles.append(" Dependencies ")
		self.titles.append("DreamElite")
		self.titles.append("USB DVB Drivers ")
		self.titles.append(" EPG ")
		self.titles.append("IPTV-Streaming")
		self.titles.append("ItalySat")
		self.titles.append(" Key Updater ")
		self.titles.append("kodi")
		self.titles.append("KodiLite")
		self.titles.append("Merlin")
                self.titles.append(" MultiBoot ") 
		self.titles.append("MultiMedia")
		self.titles.append("Newnigma2")
		self.titles.append(" oe22-plugins ")
		self.titles.append(" OE2.2-Skins ")
		self.titles.append(" oe22-softcams ")
		self.titles.append("OoZoon")
		self.titles.append("OpenATV | OpenDroid | OpenESI | OpenNFR | OpenPlus")
		self.titles.append("Black Hole")
		self.titles.append("OpenATV | OpenDroid | OpenESI | OpenNFR | OpenPlus")
		self.titles.append("OpenATV | OpenDroid | OpenESI | OpenNFR | OpenPlus")
		self.titles.append(" OpenLD ")
		self.titles.append("OpenPLI")
                self.titles.append("OpenATV | OpenDroid | OpenESI | OpenNFR | OpenPlus")
                self.titles.append("OpenATV | OpenDroid | OpenESI | OpenNFR | OpenPlus")
		self.titles.append("OpenSPA")
		self.titles.append("Oscam Configs For All")
		self.titles.append("Oscam with CCcam Configs For All Packages")
		self.titles.append("other")
                self.titles.append("Panels")
                self.titles.append("PBnigma PowerBoard")
                self.titles.append("PKT Hyperion")
 		self.titles.append("Picon")       
		self.titles.append("Power Sat")
                self.titles.append("Radio")
		self.titles.append("ruDREAM")
		self.titles.append("OpenPLI")
		self.titles.append("sh4-softcams")
 		self.titles.append("Skins - Black Hole ")
                self.titles.append("Skins - Open Black Hole | OpenPLI")
 		self.titles.append("Skins - OpenViX ")
		self.titles.append("Skins - VTi")
 		self.titles.append("SoftCam Tools")
 		self.titles.append("Sports plugin")
                self.titles.append("VTI")
                self.titles.append(" Weather ")
		self.titles.append("WeTek")
				
                
                if DESKHEIGHT > 1000:
                       picfold = "/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/LSicons2/"
                else:       
                       picfold = "/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/LSicons/"
		self.pics.append(picfold + "Solo4k.png")
		self.pics.append(picfold + "Backup.png")
		self.pics.append(picfold + "blackhole.png")
		self.pics.append(picfold + "Bouquets.png")
		self.pics.append(picfold + "Channel-list.png")
		self.pics.append(picfold + "Dependencies.png")
		self.pics.append(picfold + "dreamelite.png")
		self.pics.append(picfold + "usb-tuner-drivers.png")
		self.pics.append(picfold + "plugin-epg.png")
		self.pics.append(picfold + "plugin-iptv-streaming.png")
		self.pics.append(picfold + "ItalySAT.png")
		self.pics.append(picfold + "key-updater.png")
		self.pics.append(picfold + "Kodi.png")
		self.pics.append(picfold + "KodiLite.png")
		self.pics.append(picfold + "Merlin.png")
		self.pics.append(picfold + "multiboot.png")
		self.pics.append(picfold + "Multimedia.png")
		self.pics.append(picfold + "Newnigma.png")
		self.pics.append(picfold + "OE2.2-Plugins.png")
		self.pics.append(picfold + "OE2.2-Skins.png")
		self.pics.append(picfold + "OE2.png")
		self.pics.append(picfold + "OoZooN.png")
		self.pics.append(picfold + "openatv.png")
                self.pics.append(picfold + "openblackhole.png")
                self.pics.append(picfold + "opendroid.png")
                self.pics.append(picfold + "openesi.png")
                self.pics.append(picfold + "openld.png")
                self.pics.append(picfold + "opennfr.png")
                self.pics.append(picfold + "openpli.png")
                self.pics.append(picfold + "openplus.png")
                self.pics.append(picfold + "openspa.png")
                self.pics.append(picfold + "OSCam.png")
                self.pics.append(picfold + "oscamcccam.png")
                self.pics.append(picfold + "Other.png")
                self.pics.append(picfold + "Panels.png")
                self.pics.append(picfold + "PBnigma.png")
                self.pics.append(picfold + "PKThiperion.png")
		self.pics.append(picfold + "plugin-picon.png")
		self.pics.append(picfold + "PowerSat.png")
                self.pics.append(picfold + "Radio.png")
                self.pics.append(picfold + "rudream.png")
                self.pics.append(picfold + "satdreamgr.png")
	        self.pics.append(picfold + "SH4-SoftCams.png")
		self.pics.append(picfold + "skins-blackhole.png")
                self.pics.append(picfold + "skins-openblackhole-openpli.png")
                self.pics.append(picfold + "skins-openvix-openatv.png")
                self.pics.append(picfold + "skins-vti.png")
		self.pics.append(picfold + "SoftCam-Tools.png")
                self.pics.append(picfold + "sport.png")
                self.pics.append(picfold + "vti.png")
                self.pics.append(picfold + "weather.png")
                self.pics.append(picfold + "wetek.png")
                self.pics.append(picfold + "Information.png")
                self.pics.append(picfold + "about.png")
                
                
                
                self.names= list
		print "self.names =", self.names
                
#                print "self.pics = ", self.pics

		self["frame"] = MovingPixmap()

                self["label1"] = StaticText()
                self["label2"] = StaticText()
                self["label3"] = StaticText()
                self["label4"] = StaticText()
                self["label5"] = StaticText()
                self["label6"] = StaticText()
                self["label7"] = StaticText()
                self["label8"] = StaticText()
                self["label9"] = StaticText()
                self["label10"] = StaticText()
                self["label11"] = StaticText()
                self["label12"] = StaticText()
                self["label13"] = StaticText()
                self["label14"] = StaticText()
                self["label15"] = StaticText()
                self["label16"] = StaticText()
                self["label17"] = StaticText()
                self["label18"] = StaticText()
                self["label19"] = StaticText()
                self["label20"] = StaticText()


                self["pixmap1"] = Pixmap()
                self["pixmap2"] = Pixmap()
                self["pixmap3"] = Pixmap()
                self["pixmap4"] = Pixmap()
                self["pixmap5"] = Pixmap()
                self["pixmap6"] = Pixmap()
                self["pixmap7"] = Pixmap()
                self["pixmap8"] = Pixmap()
                self["pixmap9"] = Pixmap()
                self["pixmap10"] = Pixmap()
                self["pixmap11"] = Pixmap()
                self["pixmap12"] = Pixmap()
                self["pixmap13"] = Pixmap()
                self["pixmap14"] = Pixmap()
                self["pixmap15"] = Pixmap()
                self["pixmap16"] = Pixmap()
                self["pixmap17"] = Pixmap()
                self["pixmap18"] = Pixmap()
                self["pixmap19"] = Pixmap()
                self["pixmap20"] = Pixmap()
				
		self["actions"] = NumberActionMap(["OkCancelActions", "MenuActions", "DirectionActions", "NumberActions"],
			{
				"ok": self.okbuttonClick,
				"cancel": self.closeNonRecursive,
				"left": self.key_left,
			        "right": self.key_right,
			        "up": self.key_up,
			        "down": self.key_down,

				"menu": self.closeRecursive,
				"1": self.keyNumberGlobal,
				"2": self.keyNumberGlobal,
				"3": self.keyNumberGlobal,
				"4": self.keyNumberGlobal,
				"5": self.keyNumberGlobal,
				"6": self.keyNumberGlobal,
				"7": self.keyNumberGlobal,
				"8": self.keyNumberGlobal,
				"9": self.keyNumberGlobal
			})
                self.index = 0
                self.maxentry = len(list)-1
                self.index = 0
                ln = len(self.names)
                self.npage = int(float(ln/20)) + 1
#                print "self.npage =", self.npage
                self.ipage = 1
                self.icount = 0
                self.onShown.append(self.openTest)


        def paintFrame(self):
#		if self.maxentry < self.index or self.index < 0:
#			return
                ifr = self.index - (20*(self.ipage-1))
		ipos = self.pos[ifr]
		self["frame"].moveTo( ipos[0], ipos[1], 1)
		self["frame"].startMoving()


        def openTest(self):
#                coming in self.ipage=1, self.shortnms, self.pics
                 print "self.ipage, self.npage =", self.ipage, self.npage
		 if self.ipage < self.npage:
                        self.maxentry = (20*self.ipage)-1
                        self.minentry = (self.ipage-1)*20
                        #self.index 0-11

                 elif self.ipage == self.npage:
                        self.maxentry = len(self.pics) - 1
                        self.minentry = (self.ipage-1)*20
                        i1 = 0
                        blpic = "/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/LSicons/Blank.png"
                        while i1 < 20:
                              self["label" + str(i1+1)].setText(" ")
                              self["pixmap" + str(i1+1)].instance.setPixmapFromFile(blpic)
                              i1 = i1+1

                 i = 0
                 i1 = 0
                 self.picnum = 0
                 ln = self.maxentry - (self.minentry-1)
                 while i < ln:
                    idx = self.minentry + i 
                    self["label" + str(i+1)].setText(self.names[idx])
                    pic = self.pics[idx]
                    if not os.path.exists(self.pics[idx]):
                           pic = "/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/LSicons/Blank.png"
                    self["pixmap" + str(i+1)].instance.setPixmapFromFile(self.pics[idx])
                    i = i+1  
               
                 self.paintFrame()
                           



        def key_left(self):
		self.index -= 1
		if self.index < (self.minentry):
                    if self.ipage > 1:
                        self.ipage = self.ipage - 1
                        self.openTest()
                         
		    elif self.ipage == 1:	
                        self.close()
		if self.index < 0:
			self.index = self.maxentry
		self.paintFrame()

        def key_right(self):
		self.index += 1
		if self.index > self.maxentry:
			self.index = 0
			self.ipage= 1
			self.openTest()
                
		self.paintFrame()

        def key_up(self):
		self.index = self.index - 5
		if self.index < (self.minentry):
                    if self.ipage > 1:
                        self.ipage = self.ipage - 1
                        self.openTest()
                         
		    elif self.ipage == 1:
                    	self.index = self.index + 20
                    	self.paintFrame()
#                        self.close()
                else:
                        self.paintFrame()



        def key_down(self):
                self.index = self.index + 5
		if self.index > (self.maxentry):
                    if self.ipage < self.npage:
                        self.ipage = self.ipage + 1
                        self.openTest()
                         
		    elif self.ipage == self.npage:	
                        self.index = 0
                        self.ipage = 1
                        self.openTest()

                else:
		        self.paintFrame()



	def keyNumberGlobal(self, number):
		# Calculate index
		number -= 1
                print "Here in Menu 4"
		if len(self["menu"].list) > number:
			self["menu"].setIndex(number)
			print "Here in Menu 8"
			self.okbuttonClick()

	def closeNonRecursive(self):
                self.close(False)

	def closeRecursive(self):
                self.close(True)

	def createSummary(self):
                return
 

	def createSummary(self):
#                return MenuSummary
                return

        def okbuttonClick(self):

          self.idx = idx = self.index
          if self.idx is None:
                return
          name = self.names[self.idx]   
          print "In okbuttonClick name =", name   
          if name == "Information":
                 self.session.open(LSinfo, name)
          elif name == "About":
                 self.session.open(LSinfo, name)       
                 
#                 url = 'http://linuxsat-support.com/addons2016/info.txt'
#                 getPage(url).addCallback(self.gotPage).addErrback(self.errorLoad)     
          else:      
                 title = self.titles[self.idx]          
 	
                 n1 = self.data.find(title, 0)
                 n2 = self.data.find("</plugins>", n1)	
                 fxml = self.data[n1:n2]
# 	  print "fxml =", fxml
                 self.session.open(ipkInstall, fxml) 
           
        def errorLoad(self,error):
              print "error =", str(error)

        def gotPage(self, data):
                print "data =", data
                self.session.open(LSinfo, data)

	def callbackView(self, val=0):
		self.index = val
		if self.old_index != self.index:
			self.paintFrame()
	def Exit(self):
		del self.picload
		self.close(self.index + self.dirlistcount)
		
 
###################################                
class ipkInstallFHD(Screen):
    skin = """
    <screen name="ipkInstall" position="0,0" size="1920,1080" title="Linuxsat Addons Setup" >
	  <ePixmap position="0,0" zPosition="0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/icons2/panel.png" backgroundColor="#25062748" alphatest="on" />
	  <eLabel position="0,0" zPosition="-10" size="1920,1080" backgroundColor="black" />
          <widget source="session.VideoPicture" render="Pig" position="1218,535" size="606,339" zPosition="1" backgroundColor="#ff000000" />
                                                                       
          <!--widget name="list" position="120,210" size="1080,720" zPosition="4" font="Regular;30" foregroundColor="#ffffff" foregroundColorSelected="#ffffff" backgroundColor="#3e403d" backgroundColorSelected="#012e3d" scrollbarMode="showOnDemand" /-->

          <widget name="frame" position="120,195" size="960,45" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/icons2/select1.png" zPosition="2" alphatest="on" />   


          <widget source="label1" render="Label" position="120,195" size="960,45" font="Regular;30" halign="center" valign="center" zPosition="3" transparent="1" noWrap="1" foregroundColor="white" />
          <widget source="label2" render="Label" position="120,270" size="960,45" font="Regular;30" halign="center" valign="center" zPosition="3" transparent="1" noWrap="1" foregroundColor="white" />
          <widget source="label3" render="Label" position="120,345" size="960,45" font="Regular;30" halign="center" valign="center" zPosition="3" transparent="1" noWrap="1" foregroundColor="white" />
          <widget source="label4" render="Label" position="120,420" size="960,45" font="Regular;30" halign="center" valign="center" zPosition="3" transparent="1" noWrap="1" foregroundColor="white" />
          <widget source="label5" render="Label" position="120,495" size="960,45" font="Regular;30" halign="center" valign="center" zPosition="3" transparent="1" noWrap="1" foregroundColor="white" />
          <widget source="label6" render="Label" position="120,570" size="960,45" font="Regular;30" halign="center" valign="center" zPosition="3" transparent="1" noWrap="1" foregroundColor="white" />
          <widget source="label7" render="Label" position="120,645" size="960,45" font="Regular;30" halign="center" valign="center" zPosition="3" transparent="1" noWrap="1" foregroundColor="white" />
          <widget source="label8" render="Label" position="120,720" size="960,45" font="Regular;30" halign="center" valign="center" zPosition="3" transparent="1" noWrap="1" foregroundColor="white" />
          <widget source="label9" render="Label" position="120,795" size="960,45" font="Regular;30" halign="center" valign="center" zPosition="3" transparent="1" noWrap="1" foregroundColor="white" />
          <widget source="label10" render="Label" position="120,870" size="960,45" font="Regular;30" halign="center" valign="center" zPosition="3" transparent="1" noWrap="1" foregroundColor="white" />


          <widget name="info" position="150,900" zPosition="4" size="1500,60" font="Regular;33" foregroundColor="#7bd7f7" backgroundColor="#40000000" transparent="1" halign="left" valign="center" />

          <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/icons/red.png" position="90,990" size="45,45" alphatest="on" />
          <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/icons/green.png" position="465,990" size="45,45" alphatest="on" />
          <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/icons/yellow.png" position="840,990" size="45,45" alphatest="on" />
          <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/icons/blue.png" position="1215,990" size="45,45" alphatest="on" />

          <widget name="key_red" position="150,990" size="300,45" valign="center" halign="left" zPosition="4"  foregroundColor="#ffffff" font="Regular;27" transparent="1" shadowColor="#25062748" shadowOffset="-2,-2" /> 
          <widget name="key_green" position="525,990" size="300,45" valign="center" halign="left" zPosition="4"  foregroundColor="#ffffff" font="Regular;27" transparent="1" shadowColor="#25062748" shadowOffset="-2,-2" /> 
          <widget name="key_yellow" position="900,990" size="300,45" valign="center" halign="left" zPosition="4"  foregroundColor="#ffffff" font="Regular;27" transparent="1" shadowColor="#25062748" shadowOffset="-2,-2" />
          <widget name="key_blue" position="1275,990" size="300,45" valign="center" halign="left" zPosition="4"  foregroundColor="#ffffff" font="Regular;27" transparent="1" shadowColor="#25062748" shadowOffset="-2,-2" />
        
          </screen>"""
          
class ipkInstall(Screen):
    skin = """
    <screen name="ipkInstall" position="0,0" size="1280,720" title="Linuxsat Addons Setup" >
	  <ePixmap position="0,0" zPosition="0" size="1280,720" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/icons/panel.png" backgroundColor="#25062748" alphatest="on" />
	  <eLabel position="0,0" zPosition="-10" size="1280,720" backgroundColor="black" />
          <widget source="session.VideoPicture" render="Pig" position="802,292" size="411,238" zPosition="1" backgroundColor="#ff000000" />
                                                                       
          <!--widget name="list" position="80,140" size="720,480" zPosition="4" font="Regular;20" foregroundColor="#ffffff" foregroundColorSelected="#ffffff" backgroundColor="#3e403d" backgroundColorSelected="#012e3d" scrollbarMode="showOnDemand" /-->

          <widget name="frame" position="70,130" size="640,36" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/icons/select.png" zPosition="2" alphatest="on" />   


          <widget source="label1" render="Label" position="80,130" size="640,30" font="Regular;20" halign="center" valign="center" zPosition="3" transparent="1" noWrap="1" foregroundColor="white" />
          <widget source="label2" render="Label" position="80,180" size="640,30" font="Regular;20" halign="center" valign="center" zPosition="3" transparent="1" noWrap="1" foregroundColor="white" />
          <widget source="label3" render="Label" position="80,230" size="640,30" font="Regular;20" halign="center" valign="center" zPosition="3" transparent="1" noWrap="1" foregroundColor="white" />
          <widget source="label4" render="Label" position="80,280" size="640,30" font="Regular;20" halign="center" valign="center" zPosition="3" transparent="1" noWrap="1" foregroundColor="white" />
          <widget source="label5" render="Label" position="80,330" size="640,30" font="Regular;20" halign="center" valign="center" zPosition="3" transparent="1" noWrap="1" foregroundColor="white" />
          <widget source="label6" render="Label" position="80,380" size="640,30" font="Regular;20" halign="center" valign="center" zPosition="3" transparent="1" noWrap="1" foregroundColor="white" />
          <widget source="label7" render="Label" position="80,430" size="640,30" font="Regular;20" halign="center" valign="center" zPosition="3" transparent="1" noWrap="1" foregroundColor="white" />
          <widget source="label8" render="Label" position="80,480" size="640,30" font="Regular;20" halign="center" valign="center" zPosition="3" transparent="1" noWrap="1" foregroundColor="white" />
          <widget source="label9" render="Label" position="80,530" size="640,30" font="Regular;20" halign="center" valign="center" zPosition="3" transparent="1" noWrap="1" foregroundColor="white" />
          <widget source="label10" render="Label" position="80,580" size="640,30" font="Regular;20" halign="center" valign="center" zPosition="3" transparent="1" noWrap="1" foregroundColor="white" />


          <widget name="info" position="100,600" zPosition="4" size="1000,40" font="Regular;22" foregroundColor="#7bd7f7" backgroundColor="#40000000" transparent="1" halign="left" valign="center" />

          <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/icons/red.png" position="60,660" size="30,30" alphatest="on" />
          <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/icons/green.png" position="310,660" size="30,30" alphatest="on" />
          <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/icons/yellow.png" position="560,660" size="30,30" alphatest="on" />
          <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/icons/blue.png" position="810,660" size="30,30" alphatest="on" />

          <widget name="key_red" position="100,660" size="200,30" valign="center" halign="left" zPosition="4"  foregroundColor="#ffffff" font="Regular;18" transparent="1" shadowColor="#25062748" shadowOffset="-2,-2" /> 
          <widget name="key_green" position="350,660" size="200,30" valign="center" halign="left" zPosition="4"  foregroundColor="#ffffff" font="Regular;18" transparent="1" shadowColor="#25062748" shadowOffset="-2,-2" /> 
          <widget name="key_yellow" position="600,660" size="200,30" valign="center" halign="left" zPosition="4"  foregroundColor="#ffffff" font="Regular;18" transparent="1" shadowColor="#25062748" shadowOffset="-2,-2" />
          <widget name="key_blue" position="850,660" size="200,30" valign="center" halign="left" zPosition="4"  foregroundColor="#ffffff" font="Regular;18" transparent="1" shadowColor="#25062748" shadowOffset="-2,-2" />
        
          </screen>"""


                

    def __init__(self, session, fxml):
	if DESKHEIGHT > 1000:
		 self.skin = ipkInstallFHD.skin
	else:       
		 self.skin = ipkInstall.skin
    
       
        Screen.__init__(self, session)
        self.fxml = fxml
	title = "Linuxsat Support Addons Manager"
	self["title"] = Button(title)
        self['key_red'] = Button(_('Exit'))
        self['key_green'] = Button(_('Install/Update'))
        self['key_yellow'] = Button(_('Remove ipk'))
        self['key_blue'] = Button(_('Restart enigma'))
        self.list = []
#        self['list'] = MenuList([])
#        self["list"] = RSList([])
        self["label1"] = StaticText()
        self["label2"] = StaticText()
        self["label3"] = StaticText()
        self["label4"] = StaticText()
        self["label5"] = StaticText()
        self["label6"] = StaticText()
        self["label7"] = StaticText()
        self["label8"] = StaticText()
        self["label9"] = StaticText()
        self["label10"] = StaticText()
        
        self["frame"] = MovingPixmap()
        
        if DESKHEIGHT > 1000:
                       self.pos = []		
                       self.pos.append([120,195])
                       self.pos.append([120,270])
                       self.pos.append([120,345])
                       self.pos.append([120,420])
                       self.pos.append([120,495])
                
                       self.pos.append([120,570])
                       self.pos.append([120,645])
                       self.pos.append([120,720])
                       self.pos.append([120,795])
                       self.pos.append([120,870])        

        else:
                       self.pos = []		
                       self.pos.append([80,130])
                       self.pos.append([80,180])
                       self.pos.append([80,230])
                       self.pos.append([80,280])
                       self.pos.append([80,330])
                
                       self.pos.append([80,380])
                       self.pos.append([80,430])
                       self.pos.append([80,480])
                       self.pos.append([80,530])
                       self.pos.append([80,580])        

        self['info'] = Label()
        self['fspace'] = Label()
        self.icount = 0
        self.downloading = False
        self['info'].setText(' ')
        self['actions'] = ActionMap(["OkCancelActions", "MenuActions", "DirectionActions", "NumberActions", 'ColorActions'], 
        {'ok': self.okClicked,
         "left": self.key_left,
	 "right": self.key_right,
	 "up": self.key_up,
	 "down": self.key_down,
 
         'green': self.okClicked,
         'cancel': self.close,
         'red': self.close,
         'blue': self.restart,
         'yellow': self.remove}, -2)
         
        self.names, self.urls = self.openTest1() 
        list = self.names 
        self.index = 0
        self.maxentry = len(list)-1
        self.index = 0
        ln = len(self.names)
        self.npage = int(float(ln/10)) + 1
#       print "self.npage =", self.npage
        self.ipage = 1
        self.icount = 0
        self.onShown.append(self.openTest) 
#        self.onLayoutFinish.append(self.openTest) 


    def openTest1(self):	
                regex = '<plugin name = "(.*?)">.*?url>(.*?)</url'
	        match = re.compile(regex,re.DOTALL).findall(self.fxml)
	        self.names = []
	        self.urls = []
                for name, url in match:	
 		       self.names.append(name)
 		       self.urls.append(url)
 		return self.names, self.urls       
 		       
    def paintFrame(self):
                print "In paintFrame self.index =", self.index
                ifr = self.index - (10*(self.ipage-1))
		ipos = self.pos[ifr]
		print "In paintFrame ipos =", ipos
		self["frame"].moveTo( ipos[0], ipos[1], 1)
		self["frame"].startMoving()


    def openTest(self):
		 if self.ipage < self.npage:
                        self.maxentry = (10*self.ipage)-1
                        self.minentry = (self.ipage-1)*10
                        #self.index 0-11

                 elif self.ipage == self.npage:
                        self.maxentry = len(self.names) - 1
                        self.minentry = (self.ipage-1)*10
                        i1 = 0
#                        blpic = "/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/LSicons/Blank.png"
                        while i1 < 10:
                              self["label" + str(i1+1)].setText(" ")
#                              self["pixmap" + str(i1+1)].instance.setPixmapFromFile(blpic)
                              i1 = i1+1

                 i = 0
                 i1 = 0
                 ln = self.maxentry - (self.minentry-1)
                 while i < ln:
                    idx = self.minentry + i 
                    self["label" + str(i+1)].setText(self.names[idx])
#                    pic = self.pics[idx]
#                    if not os.path.exists(self.pics[idx]):
#                           pic = "/usr/lib/enigma2/python/Plugins/Extensions/LinuxsatPanel/LSicons/Blank.png"
#                    self["pixmap" + str(i+1)].instance.setPixmapFromFile(self.pics[idx])
                    i = i+1  
               
                 self.paintFrame()
                           



    def key_left(self):
		self.index -= 1
		if self.index < (self.minentry):
                    if self.ipage > 1:
                        self.ipage = self.ipage - 1
                        self.openTest()
                         
		    elif self.ipage == 1:	
                        self.close()
		if self.index < 0:
			self.index = self.maxentry
		self.paintFrame()

    def key_right(self):
		self.index += 1
		if self.index > self.maxentry:
			self.index = 0
			self.ipage= 1
			self.openTest()
                
		self.paintFrame()

    def key_up(self):
		self.index = self.index - 1
		if self.index < (self.minentry):
                    if self.ipage > 1:
                        self.ipage = self.ipage - 1
                        self.openTest()
                         
		    elif self.ipage == 1:
                    	self.index = self.index + 10
                    	self.paintFrame()
#                        self.close()
                else:
                        self.paintFrame()



    def key_down(self):
                self.index = self.index + 1
		if self.index > (self.maxentry):
                    if self.ipage < self.npage:
                        self.ipage = self.ipage + 1
                        self.openTest()
                         
		    elif self.ipage == self.npage:	
                        self.index = 0
                        self.ipage = 1
                        self.openTest()

                else:
		        self.paintFrame()
                
    def okClicked(self):
                idx = self.index
                if idx is None:
                       return
    	        url = self.urls[idx]
    	        n1 = url.rfind("/")
    	        plug = url[(n1+1):]
    	        if ".ipk" in plug:
    	               n2 = plug.find("_", 0)
    	               iname = plug[:n2]
    	        elif ".zip" in plug:
                       iname = plug
    	        task = "Downloading " + plug
                self['info'].setText(task)
                self.plug = plug
                xdest = "/tmp/" + self.plug
                xurl = url 
	        downloadPage(xurl, xdest).addCallback(self.gotplug).addErrback(self.showError)

    def showError(self, error):
                print "ERROR :", error
                self['info'].setText(error)

    def gotplug(self, fplug):  
                self['info'].setText(' ')
                plug = self.plug
                if ".ipk" in plug:
                       cmd2 = "opkg install --force-overwrite '/tmp/" + plug + "'"
                elif ".zip" in plug:        
                        cmd2 = "unzip -o -q '/tmp/" + plug + "' -d /"       
                cmd3 = "rm '/tmp/" + plug + "'"
                cmd = cmd2 + " && " + cmd3
                print "cmd =", cmd
                title = _("Installing %s" %(plug))
                self.session.open(Console,_(title),[cmd])

    def remove(self):
    	        idx = self.index
    	        url = self.urls[idx]
    	        n1 = url.rfind("/")
    	        ipk = url[(n1+1):]
    	        if ".zip" in ipk:
    	               return
    	        n2 = ipk.find("_", 0)
    	        iname = ipk[:n2]
    	        
    	        
                cmd = "opkg remove '" + iname + "'"
#                print "cmd =", cmd
                title = _("Removing %s" %(iname))
                self.session.open(Console,_(title),[cmd])

    def restart(self):
                self.session.open(TryQuitMainloop, 3)  
                
        	


##################################
class LSinfoFHD(Screen):
	skin = """
                <screen name="LSinfo"   position="center,center" size="790,580" backgroundColor="#00060606" title="Information"   >
                
		<widget name="list" backgroundColor="#00060606" foregroundColor="#76addc" position="30,50" size="760,480" font="Regular;22"   zPosition="2" scrollbarMode="showNever" />
                </screen>  """
class LSinfo(Screen):
	skin = """
                <screen name="LSinfo"   position="center,center" size="790,580" backgroundColor="#00060606" title="Information"   >
                
		<widget name="list" backgroundColor="#00060606" foregroundColor="#76addc" position="30,50" size="760,480" font="Regular;22"   zPosition="2" scrollbarMode="showNever" />
                </screen>  """
		
	def __init__(self, session, icon):
		Screen.__init__(self, session)
	        if DESKHEIGHT > 1000:
		        self.skin = LSinfoFHD.skin
	        else:       
		        self.skin = LSinfo.skin
                self.color="#00060606"
                self.icon = icon
                if self.icon == "Information": 
                       title = "Information"
                else:       
                       title = "About"
		self['list'] = MenuList([])
		self["actions"] = ActionMap(["WizardActions", "DirectionActions", "ColorActions"], 
		{       
			"ok": self.cancel,
			"back": self.cancel,
		        			
			"up": self["list"].pageUp,
			"down": self["list"].pageDown
		}, -1)
		
		self.setTitle(title)
		self.onLayoutFinish.append(self.startRun) # dont start before gui is finished
           
	def startRun(self):
	        data=''   
                if self.icon == "Information": 
                       url = 'http://linuxsat-support.com/addons2016/info.txt'      
                else:
                       url = 'http://linuxsat-support.com/addons2016/about.txt'
                f = urllib2.urlopen(url)
                lines=f.readlines()
                self["list"].setList(lines)

	def cancel(self):       
		self.close()
##################################		
_session = ""
date = ""
newstext = ""
NewUpdate = ""
def main(session,**kwargs):
        global _session
        _session = session
########################################
        xurl = "https://linuxsat-support.com/addons2016/update.txt"
        xdest = "/tmp/update.txt"
        print "going in downloadPage"
	downloadPage(xurl, xdest).addCallback(gotNews).addErrback(showNewsError)

def showNewsError(error):
               print "error =", error
               menustart()

def gotNews(txt=" "):
                       session = _session
                       indic = 0
                       global date
                       date = ""
                       olddate = ""
                       if not os.path.exists("/tmp/update.txt"):
                               indic = 0
                       else:
                               myfile = file(r"/tmp/update.txt")
                               icount = 0
                               for line in myfile.readlines():
                                   if icount == 0:
                                           date = line
                                           break
                                   icount = icount+1
                               myfile.close()
                               myfile = file(r"/tmp/update.txt") 
                               global newstext   
                               newstext = myfile.read()
                               print "In gotNews newstext =", newstext
                               myfile.close()
                               news = newstext
                               n1 = news.find("update2", 0)
                               if n1 > -1:
                                      upd = news[n1:(n1+14)]
		               else:
		                      upd = "None"
		               global NewUpdate
                               NewUpdate = upd       
		               if fileExists("/etc/lsupd"): 
		                      myfile = file(r"/etc/lsupd")
                                      icount = 0
                                      for line in myfile.readlines():
                                             if icount == 0:
                                                    upd1 = line
                                                    break
                                             icount = icount+1
                                      myfile.close()
                               else:   
                                      upd1 = "None"
                                     
                               n2 = upd1.find(".", 0)
                               if n2 > -1:   
                                      upd1 = upd1[:n2]
                               print "upd =", upd
                               print "upd1 =", upd1
                               if upd != "None":
                                   if upd1 != upd:
                                      txt = _("New ") + upd + _(" is available. \nAfter update - gui will restart.\nUpdate Now ?")
                                      session.openWithCallback(do_upd, MessageBox, txt, type = 0)
                                   else:
                                      menustart()
                               else:
                                      menustart()
                               
plug = " "

def do_upd(answer):
        session = _session
        if answer is None:
                menustart()
        else:
            if answer is False:
                menustart()
            else:  
                global plug      
                plug = NewUpdate + ".zip"
                if "update" in plug:
                        f=open("/etc/lsupd", 'w')
                        txt = plug + "\n"
                        f.write(txt)
                xdest = "/tmp/" + plug
#                cmd1 = "wget -O '" + dest + "' 'http://linuxsat-support.com/addons2016/" + plug + "'"
                xurl = "https://linuxsat-support.com/addons2016/" + plug 
	        downloadPage(xurl, xdest).addCallback(gotupd).addErrback(showError)

def showError(error):
                print "ERROR :", error
                menustart()

def gotupd(fplug):  
                session = _session        
                cmd = "unzip -o -q '/tmp/" + plug + "' -d /"
                title = _("Installing software %s" %(plug))
                session.openWithCallback(done_upd,Console,_(title),[cmd])
                
def done_upd():
                session = _session                
                session.open(TryQuitMainloop, 3)


def menustart():
########################################
	url = 'http://linuxsat-support.com/addons2016/addons2016.xml'
        getPage(url).addCallback(_gotPageLoad).addErrback(errorLoad)

def errorLoad(error):
        print "error =", str(error)

def _gotPageLoad(data):
                print "data =", data
                session = _session 
                session.open(LinuxsatPanel, data)

def menu(menuid):
	if menuid == "mainmenu":
		return [(_("Linuxsat Panel"), main, "extra_setup", 40)]
	return []
        
        

def Plugins(**kwargs):
        return [
               PluginDescriptor(name="Linuxsat Panel", description="Linuxsat Addons Setup Panel", icon="LinuxsatPanel.png", where = PluginDescriptor.WHERE_PLUGINMENU, fnc=main),
               PluginDescriptor(name="Linuxsat Panel", description="Linuxsat Addons Setup Panel", where = PluginDescriptor.WHERE_MENU, fnc=menu),
               ]











