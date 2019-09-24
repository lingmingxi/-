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
	MQSystem.println(obj.name)
	gisv = []
	gisvp =[]
	gnumVert = obj.numVertex
	for i in range(0,gnumVert):
		if doc.isSelectVertex(curidx,i):
			gisv.append(i)
			gisvp.append(obj.vertex[i].getPos())
			if len(gisv)==0:return MQSystem.messageBox("��ѡ���ȡ��")
	return gisv,gisvp,gnumVert


def setSelectVertex(ObjectIndex1,gisv,gisvp,gnumVert):
	if ObjectIndex1== None:return MQSystem.messageBox("��ѡ�����ö���")
	curidx = doc.currentObjectIndex
	obj = doc.object[curidx]
	MQSystem.println(obj.name)
	snumVert = obj.numVertex
	if snumVert!=gnumVert:
		return MQSystem.messageBox("��������ĵ���������ͬ")
	for i in range(0,snumVert):
		if doc.isSelectVertex(curidx,i):
			if i in gisv:
				obj.vertex[i].setPos(gisvp[gisv.index(i)])


def getSelectItem(listbox):
	num = doc.numObject
	for oi in range(0,num):
		if listbox.getItemSelected(oi):
			return listbox.getItemTag(oi)






if result == "ok":
	if getSelectItem(listbox)==getSelectItem(listbox1):
		MQSystem.messageBox("��ȡ��������ö�������ͬ")
		dlg.close()
	gisv,gisvp,gnumVert=getSelectVertex(getSelectItem(listbox))
	setSelectVertex(getSelectItem(listbox1),gisv,gisvp,gnumVert)

