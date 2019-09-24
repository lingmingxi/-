######################################################################
# ͬ����ѡ���λ��
#
# by ��؈(lingmao88733478@gmail.com)
# ע�����ߵ����������ת�غ��޸�
#
######################################################################
##ͬ����ѡ���λ��

doc = MQSystem.getDocument()


dlg=MQWidget.Dialog(MQWidget.getMainWindow())
dlg.title="ͬ��ѡ���"
dlg.windowFrame=True
dlg.titleBar=True
dlg.canResize=True
dlg.closeButton=True
dlg.maximizeButton=False
dlg.minimizeButton=False
dlg.maximized=False
dlg.minimized=False


##Frame
labelframe=dlg.createHorizontalFrame(dlg)
labelframe.uniformSize = True




##Frame
inputframe=dlg.createHorizontalFrame(dlg)
inputframe.uniformSize = True


##Frame
buttonframe=dlg.createHorizontalFrame(dlg)
buttonframe.uniformSize = True




##Label
labe=MQWidget.Label(labelframe)
labe.text="||��ȡ�����е�����||"
labe.wordWrap=True


##Label
label=MQWidget.Label(labelframe)
label.text="||���ö����е�����||"
label.wordWrap=True


#ListBox
listbox = MQWidget.ListBox(inputframe)
listbox.clearItems
listbox.currentIndex = 30
listbox.visibleRow = 30
listbox.lineHeightRate = 1.0
listbox.vertScrollVisible = True
listbox.multiSelect = True


#ListBox
listbox1 = MQWidget.ListBox(inputframe)
listbox1.clearItems
listbox1.currentIndex = 30
listbox1.visibleRow = 30
listbox1.lineHeightRate = 1.0
listbox1.vertScrollVisible = True
listbox1.multiSelect = True


##okbtn
okbtn = MQWidget.Button(buttonframe)
okbtn.text = "ok"
okbtn.modalResult = "ok"
okbtn.default = 1
okbtn.fillBeforeRate = 1






##cancelbtn
cancelbtn = MQWidget.Button(buttonframe)
cancelbtn.text = "cancel"
cancelbtn.modalResult = "cancel"
cancelbtn.default = 1
cancelbtn.fillAfterRate = 1






#add_objname
i=0
num = doc.numObject
for oi in range(0,num):
	obj = doc.object[oi]
	if obj is None: continue
	listbox.addItem(obj.name)
	listbox.setItemTag(i,oi)
	listbox1.addItem(obj.name)
	listbox1.setItemTag(i,oi)
	i+=1


result=dlg.execute()


def getSelectVertex(ObjectIndex):
	if ObjectIndex== None:return MQSystem.messageBox("��ѡ���ȡ����")
	curidx = ObjectIndex
	obj = doc.object[curidx]
	gisv = []
	gisvp =[]
	numFace = obj.numFace
	for x in range(0,numFace):
		if obj.face[x].select:
			a=0
			for y in obj.face[x].index :
				if obj.vertex[y].select:
					gisv.append(y)
					gisvp.append(obj.face[x].getCoord(a))
				a+=1
				MQSystem.println(repr(y)+"####"+repr(a))
	if len(gisv)==0:return MQSystem.messageBox("��ѡ���ȡ��")
	return gisv,gisvp


def setSelectVertex(ObjectIndex1,gisv,gisvp):
	if ObjectIndex1== None:return MQSystem.messageBox("��ѡ�����ö���")
	curidx = doc.currentObjectIndex
	obj = doc.object[curidx]
	numFace = obj.numFace
	for x in range(0,numFace):
		if obj.face[x].select:
			a=0
			for y in obj.face[x].index :
				if obj.vertex[y].select:
					obj.face[x].setCoord(a,gisvp[gisv.index(y)])
				a+=1

def getSelectItem(listbox):
	num = doc.numObject
	for oi in range(0,num):
		if listbox.getItemSelected(oi):
			return listbox.getItemTag(oi)






if result == "ok":
	if getSelectItem(listbox)==getSelectItem(listbox1):
		MQSystem.messageBox("��ȡ��������ö�������ͬ")
		dlg.close()
	gisv,gisvp=getSelectVertex(getSelectItem(listbox))
	setSelectVertex(getSelectItem(listbox1),gisv,gisvp)

