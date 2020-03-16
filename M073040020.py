#LAN=Python#
#107年演算法設計與分析 
#中山大學資工所 林晉廷 M073040020

from tkinter import *
import tkinter as tk
import tkinter.filedialog
import math
from sympy import *

#宣告介面、畫布、公共變數
cd=[]
cd1=[]
cd2=[]
cdlineout=[]
count = 0
alopenfile = 0
runed = 0
stepOver = 0
stepN = 0
outputstr = ""
win=Tk()
win.geometry('1000x620');
win.title(u"演算法程式專題")
win.resizable(0,0)
cv = Canvas(win, bg="white", width=600, height=600)	

#偵測滑鼠位置
def callback(event):
	global count, cd, runed
	if runed == 2:
		printmessage.delete('1.0', END)
		printmessage.insert(1.0, "上一次的執行結果尚未清除!!")
	else:
		printmessage.delete('1.0', END)
		cd.append([])
		cd[count].append(event.x)
		cd[count].append(event.y)
		printout = str(cd[count][0])+" "+str(cd[count][1])+"\n"
		printpoint.insert(1.0, printout)
		cv.create_oval(event.x-1,event.y-1,event.x+1,event.y+1, fill = "black")
		count = count + 1

#輸入座標位置
def insert_point():
	global count, cd, runed, stepOver
	if runed == 2:
		printmessage.delete('1.0', END)
		printmessage.insert(1.0, "上一次的執行結果尚未清除!!")
	else:
		printmessage.delete('1.0', END)
		printout = " "
		cd.append([])
		cd[count].append(int(corx.get())) 
		cd[count].append(int(cory.get()))
		printout = str(cd[count][0])+" "+str(cd[count][1])+"\n"
		printpoint.insert(1.0, printout)
		cv.create_oval(int(cd[count][0])-1,int(cd[count][1])-1,int(cd[count][0])+1,int(cd[count][1])+1,\
		fill = "black")
		count = count + 1

#按鈕執行演算法	
def run(step):
	global runed, outputstr, oc, ob, id1, stepOver
	runed = 1
	def dot2(cd,drw):
		global outputstr
		a = cd[1][0]-cd[0][0]
		b = cd[1][1]-cd[0][1]
		cdline = []; cdline.append([]); cdline.append([]);
		cdline[0].append(cd[0][0]+500*b)
		cdline[0].append(cd[0][1]-500*a)
		cdline[1].append(cd[1][0]-500*b)
		cdline[1].append(cd[1][1]+500*a)
		if drw==1 or drw==3:
			cv.create_line(cdline[0][0],cdline[0][1],cdline[1][0],cdline[1][1], fill = "red");
			if drw==3:
				outputstr =  "P " + str(cd[0][0]) + " " + str(cd[0][1]) + "\nP " + str(cd[1][0]) + " " + str(cd[1][1]) + "\n"
				outputstr =  outputstr + "E " + str(cdline[0][0]) + " " + str(cdline[0][1]) + " " + str(cdline[1][0]) + " " + str(cdline[1][1])+ "\n"
				drw = 0

		return cdline
	def dot3():
		#計算外心(公式計算)
		global outputstr
		try:
			ob = (((((cd[0][0]**2+cd[0][1]**2)-(cd[2][0]**2+cd[2][1]**2))*(cd[0][0]-cd[1][0])) \
			-(((cd[0][0]**2+cd[0][1]**2)-(cd[1][0]**2+cd[1][1]**2))*(cd[0][0]-cd[2][0]))) \
			/(((cd[0][1]-cd[2][1])*(cd[0][0]-cd[1][0]))-((cd[0][1]-cd[1][1])*(cd[0][0]-cd[2][0]))))/2
			oc = ((cd[0][0]**2+cd[0][1]**2)-(cd[1][0]**2+cd[1][1]**2)-(2*ob*(cd[0][1]-cd[1][1])))\
			/(2*(cd[0][0]-cd[1][0]))
			#cv.create_oval(oc-1,ob-1,oc+1,ob+1, fill = "blue")
		except:
			pass
		cd.sort(key=lambda x:x[1]); cd.sort(key=lambda x:x[0])
		outputstr =  "P "+str(cd[0][0]) + " " + str(cd[0][1]) + "\nP " + str(cd[1][0]) + " " + str(cd[1][1]) + "\nP " + str(cd[2][0]) + " " + str(cd[2][1])+ "\n"
		#判斷順時、逆時針(向量差積)
		if ((cd[1][0]-cd[0][0])*(cd[2][1]-cd[0][1]))-((cd[1][1]-cd[0][1])*(cd[2][0]-cd[0][0])) != 0 :
			#計算向量
			if ((cd[1][0]-cd[0][0])*(cd[2][1]-cd[0][1]))-((cd[1][1]-cd[0][1])*(cd[2][0]-cd[0][0])) > 0 : #逆時針
				cdline = []; cdline.append([]); cdline.append([]); cdline.append([])
				cdline[0].append((cd[0][0]+500*(cd[1][1]-cd[0][1]))); cdline[0].append((cd[0][1]-500*(cd[1][0]-cd[0][0]))); cdline[0].append(oc); cdline[0].append(ob)		
				cdline[1].append((cd[1][0]+500*(cd[2][1]-cd[1][1]))); cdline[1].append((cd[1][1]-500*(cd[2][0]-cd[1][0]))); cdline[1].append(oc); cdline[1].append(ob)
				cdline[2].append((cd[2][0]+500*(cd[0][1]-cd[2][1]))); cdline[2].append((cd[2][1]-500*(cd[0][0]-cd[2][0])));	cdline[2].append(oc); cdline[2].append(ob)
			elif ((cd[1][0]-cd[0][0])*(cd[2][1]-cd[0][1]))-((cd[1][1]-cd[0][1])*(cd[2][0]-cd[0][0])) <0 : #順時針
				cdline = []; cdline.append([]); cdline.append([]); cdline.append([])
				cdline[0].append((cd[0][0]-500*(cd[1][1]-cd[0][1]))); cdline[0].append((cd[0][1]+500*(cd[1][0]-cd[0][0])));	cdline[0].append(oc); cdline[0].append(ob)		
				cdline[1].append((cd[1][0]-500*(cd[2][1]-cd[1][1]))); cdline[1].append((cd[1][1]+500*(cd[2][0]-cd[1][0])));	cdline[1].append(oc); cdline[1].append(ob)
				cdline[2].append((cd[2][0]-500*(cd[0][1]-cd[2][1]))); cdline[2].append((cd[2][1]+500*(cd[0][0]-cd[2][0]))); cdline[2].append(oc); cdline[2].append(ob)
			#繪線
			cv.create_line(cdline[0][0],cdline[0][1], cdline[0][2], cdline[0][3], fill = "red")
			cv.create_line(cdline[1][0],cdline[1][1], cdline[1][2], cdline[1][3], fill = "red")
			cv.create_line(cdline[2][0],cdline[2][1], cdline[2][2], cdline[2][3], fill = "red")
			#以lexical order排序線
			cdline.sort(key=lambda x:x[3]); cdline.sort(key=lambda x:x[2]); cdline.sort(key=lambda x:x[1]); cdline.sort(key=lambda x:x[0])
			#製作輸出字串
			outputstr =  outputstr + "E " + str(cdline[0][0]) + " " + str(cdline[0][1]) +" "+ str(cdline[0][2]) + " " + str(cdline[0][3])\
			+ "\nE " + str(cdline[1][0]) + " " + str(cdline[1][1]) +" "+ str(cdline[1][2]) + " " + str(cdline[1][3])\
			+ "\nE " + str(cdline[2][0]) + " " + str(cdline[2][1]) +" "+ str(cdline[2][2]) + " " + str(cdline[2][3])+ "\n"
			
		else: #平行
			#計算向量、以lexical order排序線
			if cd[0][0] == cd[1][0]:	#水平平行
				cd.sort(key=lambda x:x[1])  #依Y大小排序
				a = cd[1][0]-cd[0][0];b = cd[1][1]-cd[0][1];c = cd[2][0]-cd[1][0];d = cd[2][1]-cd[1][1]
			else:	#垂直水平 and 無垂直平行之三點共線
				cd.sort(key=lambda x:x[0])  #依X大小排序 
				a = cd[1][0]-cd[0][0];b = cd[1][1]-cd[0][1];c = cd[2][0]-cd[1][0];d = cd[2][1]-cd[1][1]
			cdline = []; cdline.append([]); cdline.append([])
			cdline[0].append(cd[0][0]+500*b);cdline[0].append(cd[0][1]-500*a);cdline[0].append(cd[1][0]-500*b);cdline[0].append(cd[1][1]+500*a)	
			cdline[1].append(cd[1][0]+500*d);cdline[1].append(cd[1][1]-500*c);cdline[1].append(cd[2][0]-500*d);cdline[1].append(cd[2][1]+500*c)
			#繪線
			cv.create_line(cdline[0][0],cdline[0][1], cdline[0][2], cdline[0][3], fill = "red")
			cv.create_line(cdline[1][0],cdline[1][1], cdline[1][2], cdline[1][3], fill = "red")
			#製作輸出字串
			outputstr =  outputstr + "E " + str(cdline[0][0]) + " " + str(cdline[0][1]) +" "+ str(cdline[0][2]) + " " + str(cdline[0][3])\
			+ "\nE " + str(cdline[1][0]) + " " + str(cdline[1][1]) +" "+ str(cdline[1][2]) + " " + str(cdline[1][3])+ "\n"
	if count == 0:
		printmessage.delete('1.0', END)
		printmessage.insert(1.0, "座標上無點!!")
	elif count == 1:
		outputstr =  "P \n" + str(cd[0][0]) + " " + str(cd[0][1]) + "\n" + "無線段"
	elif count == 2:  #直線
		dot2(cd,3)
	elif count == 3:  #三角形
		dot3()
	elif count == 4:  #四點
		global i; i = 0;
		def outline(a,b,c,d,over):
			global i, outputstr
			cdlineout.append([]);
			cdlineout[i].append(a);cdlineout[i].append(b);cdlineout[i].append(c);cdlineout[i].append(d)
			if over==1:
				try:
					cdlineout.sort(key=lambda x:x[3]); cdlineout.sort(key=lambda x:x[2]); cdlineout.sort(key=lambda x:x[1]); cdlineout.sort(key=lambda x:x[0])
				except:
					print()
				for k in range(0,i+1,1):
					outputstr = outputstr + "E " + str(cdlineout[k][0]) + " " + str(cdlineout[k][1]) +" "+ str(cdlineout[k][2]) + " " + str(cdlineout[k][3]) + "\n"
				cdlineout.clear()
			else:
				i = i + 1
		cd1.clear(); cd2.clear();
		#以X軸排序分割
		cd.sort(key=lambda x:x[1]); cd.sort(key=lambda x:x[0]);
		outputstr =  "P "+str(cd[0][0]) + " " + str(cd[0][1]) + "\nP " + str(cd[1][0]) + " " + str(cd[1][1]) + "\nP "\
		+ str(cd[2][0]) + " " + str(cd[2][1]) + "\nP " + str(cd[3][0]) + " " + str(cd[3][1])+ "\n"
		#以Y軸排序並定義左右的點為cd1左，cd2右
		cd1.append([]);	cd1[0].append(cd[0][0]); cd1[0].append(cd[0][1])
		cd1.append([]);	cd1[1].append(cd[1][0]); cd1[1].append(cd[1][1])
		cd2.append([]); cd2[0].append(cd[2][0]); cd2[0].append(cd[2][1])
		cd2.append([]); cd2[1].append(cd[3][0]); cd2[1].append(cd[3][1])
		cd1.sort(key=lambda x:x[1]); cd2.sort(key=lambda x:x[1])
		cdline1 = dot2(cd1,0); cdline2 = dot2(cd2,0)
		if stepOver == 1:
			step = 0; cv.delete("all"); stepOver = 0;
			cv.create_oval(cd1[0][0]-1,cd1[0][1]-1,cd1[0][0]+1,cd1[0][1]+1, fill = "black")
			cv.create_oval(cd1[1][0]-1,cd1[1][1]-1,cd1[1][0]+1,cd1[1][1]+1, fill = "black")
			cv.create_oval(cd2[0][0]-1,cd2[0][1]-1,cd2[0][0]+1,cd2[0][1]+1, fill = "black")
			cv.create_oval(cd2[1][0]-1,cd2[1][1]-1,cd2[1][0]+1,cd2[1][1]+1, fill = "black")
		if step == 0 or step==1:
			cv.create_text(cd1[0][0]+10, cd1[0][1]+10, text="cd1[0]")
			cv.create_text(cd1[1][0]+10, cd1[1][1]+10, text="cd1[1]")
			cv.create_text(cd2[0][0]+10, cd2[0][1]+10, text="cd2[0]")
			cv.create_text(cd2[1][0]+10, cd2[1][1]+10, text="cd2[1]")
		#算出左右各兩點之中垂線座標
		#以中垂線座標求2個中垂線方程式
		x, y = symbols('x y')
		an = solve([cdline1[0][0]*x+y-cdline1[0][1],cdline1[1][0]*x+y-cdline1[1][1]],[x,y])
		x, y = symbols('x y')
		bn = solve([cdline2[0][0]*x+y-cdline2[0][1],cdline2[1][0]*x+y-cdline2[1][1]],[x,y])
		#用一個index交換座標，左邊之陣列為cd1i，右邊cd2i
		ind= [0, 1, 0, 1, 0, 1, 0, 1, 0]
		cd1i=0; cd2i=0;
		#同側判斷 ans<0:異側   ans>0:同側
		def sameArea(cdline1x, cdline1y, cdline2x, cdline2y, cd1x, cd1y, cd2x, cd2y):
			x, y = symbols('x y')	
			#防垂直
			try: 
				zn = solve([cdline1x*x+y-cdline1y,cdline2x*x+y-cdline2y],[x,y])
				ans = (zn[x]*cd1x+(-1*cd1y)+zn[y])*(zn[x]*cd2x+(-1*cd2y)+zn[y])
			except:
				zn = solve([cdline1x*x+y-cdline1y,x-cdline1x],[x,y])
				ans = (1*cd1x-cdline1x)*(1*cd2x-cdline1x)
			return ans
		def locate(x1,y1,x2,y2,x,y):
			ans =  (y1 - y2) * x + (x2 - x1) * y + x1 * y2 - x2 * y1
			return  ans
		def slop(x1,y1,x2,y2):
			try:
				return (y2-y1)/(x2-x1)
			except:
				return 1
		def collinear(x1,y1,x2,y2,x3,y3):  #3點共線
			return (x1-x2)*(y1-y3)-(x1-x3)*(y1-y2)
		#凸包判斷(同側方程式)
		if cd1[0][0]==cd1[1][0] and cd1[1][0]==cd2[0][0] and cd2[0][0]==cd2[1][0]:
			cd1i = 1; cd2i = 0
		if step==1:
			cv.create_line(cd1[0][0], cd1[0][1], cd1[1][0], cd1[1][1], fill = "black")
			cv.create_line(cdline1[0][0], cdline1[0][1], cdline1[1][0], cdline1[1][1], fill = "red")
		if step==2:
			cv.create_line(cd2[0][0], cd2[0][1], cd2[1][0], cd2[1][1], fill = "black")
			cv.create_line(cdline2[0][0], cdline2[0][1], cdline2[1][0], cdline2[1][1], fill = "blue")
		try:
			if sameArea(cd1[0][0],cd1[0][1],cd2[0][0],cd2[0][1],cd1[1][0],cd1[1][1],cd2[1][0],cd2[1][1]) > 0:
				cd1i = 0; cd2i = 0
			elif sameArea(cd1[0][0],cd1[0][1],cd2[0][0],cd2[0][1],cd1[1][0],cd1[1][1],cd2[1][0],cd2[1][1]) == 0:
				if sameArea(cd1[1][0],cd1[1][1],cd2[1][0],cd2[1][1],cd1[0][0],cd1[0][1],cd2[0][0],cd2[0][1]) > 0:
					cd1i = 1; cd2i = 1
				else:
					if sameArea(cd1[1][0],cd1[1][1],cd2[0][0],cd2[0][1],cd1[0][0],cd1[0][1],cd2[1][0],cd2[1][1]) >= 0:
						if cd1[1][1]>cd2[0][1]:
							cd1i = 1; cd2i = 0
						else:
							cd1i = 0; cd2i = 1
							if collinear(cd1[1][0],cd1[1][1],cd2[0][0],cd2[0][1],cd1[0][0],cd1[0][1]) == 0:
								if collinear(cd1[0][0],cd1[0][1],cd2[0][0],cd2[0][1],cd1[0][0],cd1[0][1]) == 0:
									ass = cd1[0][0]-cd2[1][0];bss= cd1[0][1]-cd2[1][1]
									if step == 0 or step == 4:
										cv.create_line(cd1[0][0]+500*bss,cd1[0][1]-500*ass, cd2[1][0]-500*bss, cd2[1][1]+500*ass, fill = "green")
					else:
						cd1i = 0; cd2i = 1
			else:
				if sameArea(cd1[1][0],cd1[1][1],cd2[0][0],cd2[0][1],cd1[0][0],cd1[0][1],cd2[1][0],cd2[1][1]) > 0 :
					cd1i = 1; cd2i = 0
				else:
					cd1i = 0; cd2i = 1
		except:
			print("e")
			cd1i = 0; cd2i = 1
		print(cd1i,cd2i)
		#求最上面兩點的方程式中點
		if(step==3):
			cv.create_line(cd1[ind[cd1i]][0], cd1[ind[cd1i]][1], cd2[ind[cd2i]][0], cd2[ind[cd2i]][1], fill = "purple")
		x0 = (cd2[ind[cd2i]][0]+cd1[ind[cd1i]][0])/2 #中點
		y0 = (cd2[ind[cd2i]][1]+cd1[ind[cd1i]][1])/2
		print(x0,y0)
		tx = cd2[ind[cd2i]][0] - cd1[ind[cd1i]][0] #原向量方向
		ty = cd2[ind[cd2i]][1] - cd1[ind[cd1i]][1]
		np1 = x0 + 10*ty; np2 = y0 - 10*tx; #原向量另一點
		x, y = symbols('x y')
		cn = solve([x0*x+y-y0,np1*x+y-np2],[x,y]) #中點和原向量另一點求向量方程式
		#求法向量與中垂線交點
		ansa={x:0,y:0};ansb={x:0,y:0}
		try:
			x, y = symbols('x y')
			ansa=solve([an[x]*x+an[y]-y,cn[x]*x+cn[y]-y],[x,y])
			x, y = symbols('x y')
			ansb=solve([bn[x]*x+bn[y]-y,cn[x]*x+cn[y]-y],[x,y])
		except:
			try:
				x, y = symbols('x y')
				ansa=solve([an[x]*x+an[y]-y,x-np1],[x,y])
				x, y = symbols('x y')
				ansb=solve([bn[x]*x+bn[y]-y,x-np1],[x,y])
			except:
				try:
					x, y = symbols('x y')
					ansa=solve([an[x]*x+an[y]-y,cn[x]*x+cn[y]-y],[x,y])
					ansb[x]=cd1[ind[cd2i]][0]; ansa[y]= cd1[ind[cd2i]][1]
				except:
					try:
						ansa[x]=cd1[ind[cd1i]][0]; ansa[y]= cd1[ind[cd1i]][1]
						x, y = symbols('x y')
						ansb=solve([bn[x]*x+bn[y]-y,x-np1],[x,y])
					except:
						ansa[x]=cd1[ind[cd1i]][0]; ansa[y]= cd1[ind[cd1i]][1]
						ansb[x]=cd1[ind[cd2i]][0]; ansa[y]= cd1[ind[cd2i]][1]
			
		#原中垂線座標以X軸排序分左右
		cdline1.sort(key=lambda x:x[0])
		cdline2.sort(key=lambda x:x[0])
		#遠處座標計算，向量向外
		if sameArea(cd1[ind[cd1i]][0], cd1[ind[cd1i]][1], cd2[ind[cd2i]][0], cd2[ind[cd2i]][1], x0+500*ty, y0-500*tx, cd1[ind[cd1i+1]][0], cd1[ind[cd1i+1]][1])<0:
			drax=x0+500*ty; dray=y0-500*tx;
		else:
			if sameArea(cd1[ind[cd1i]][0], cd1[ind[cd1i]][1], cd2[ind[cd2i]][0], cd2[ind[cd2i]][1], x0+500*ty, y0-500*tx, cd1[ind[cd1i+1]][0], cd1[ind[cd1i+1]][1])==0:
				if sameArea(cd1[ind[cd1i]][0], cd1[ind[cd1i]][1], cd2[ind[cd2i]][0], cd2[ind[cd2i]][1], x0+500*ty, y0-500*tx, cd2[ind[cd2i+1]][0], cd2[ind[cd2i+1]][1])<0:
					drax=x0+500*ty; dray=y0-500*tx;
				else:
					drax=x0-500*ty; dray=y0+500*tx;
			else:
				drax=x0-500*ty; dray=y0+500*tx;
		if collinear(cd1[0][0],cd1[0][1],cd1[1][0],cd1[1][1],cd2[0][0],cd2[0][1])==0:  #4點共線例外
			if collinear(cd1[1][0],cd1[1][1],cd2[0][0],cd2[0][1],cd2[1][0],cd2[1][1])==0:
				if step==0:
					dot2(cd1,1);dot2(cd2,1)
				if step==1:
					dot2(cd1,1)
				if step==2:
					dot2(cd2,1)
		def dis(X1,Y1,X2,Y2):
			return (X2-X1)**2+(Y2-Y1)**2
		if(ansa[x]<-99000):
			ansa[x]=99000;
		if(ansb[x]<-99000):
			ansb[x]=99000;
		if(ansa[y]<-99000):
			ansa[y]=99000;
		if(ansb[y]<-99000):
			ansb[y]=99000;
		print("ansa",ansa)
#-------------------------------------------------------------------------------------------------
		if dis(ansa[x],ansa[y],drax,dray) < dis(ansb[x],ansb[y],drax,dray): 	#跟an(左邊)紅相交
			print("左邊相交")
			if(step==0 or step==4):
				cv.create_line(ansa[x], ansa[y], drax, dray, fill = "green")
				if step == 0:
					outline(ansa[x], ansa[y], drax, dray,0)
			cd1i = cd1i+1 #下一層
			x0 = ansa[x]; 
			y0 = ansa[y] #第一交點
			tx = cd2[ind[cd2i]][0] - cd1[ind[cd1i]][0] #原向量方向
			ty = cd2[ind[cd2i]][1] - cd1[ind[cd1i]][1]
			np1 = x0 + 10*ty; np2 = y0 - 10*tx; #原向量另一點
			x, y = symbols('x y')
			cn = solve([x0*x+y-y0,np1*x+y-np2],[x,y]) #第一交點和原向量另一點求向量方程式
			x, y = symbols('x y') 
			try: #防垂直
				ansc=solve([bn[x]*x+bn[y]-y,cn[x]*x+cn[y]-y],[x,y]) #求法向量與第二中垂線交點
			except:
				ansc=solve([bn[x]*x+bn[y]-y,x-x0],[x,y]) #求法向量與第二中垂線交點
			print(x0, y0, ansc[x], ansc[y])
			if(step==0 or step==4):
				cv.create_line(x0, y0, ansc[x], ansc[y], fill = "green")
				if step == 0:
					outline(x0, y0, ansc[x], ansc[y],0)
			cd2i = cd2i+1 #下一層
			x0 = ansc[x]; 
			y0 = ansc[y] #第二交點
			tx = cd2[ind[cd2i]][0] - cd1[ind[cd1i]][0] #原向量方向
			ty = cd2[ind[cd2i]][1] - cd1[ind[cd1i]][1]
			np1 = x0 + 10*ty; np2 = y0 - 10*tx; #原向量另一點
			x, y = symbols('x y')
			dn = solve([x0*x+y-y0,np1*x+y-np2],[x,y]) #第二交點和原向量另一點求向量方程				
			x, y = symbols('x y')
			try: #防垂直
				ansd=solve([an[x]*x+an[y]-y,dn[x]*x+dn[y]-y],[x,y]) #求法向量與第二中垂線交點
			except:
				ansd=solve([an[x]*x+an[y]-y,x-x0],[x,y])
			print(ansa,ansd)
			if sameArea(cdline2[0][0],cdline2[0][1],cdline2[1][0],cdline2[1][1],ansa[x],ansa[y],ansd[x],ansd[y])>=0 or ansd[x]<-19000 or ansd[y]<-19000:
				print("mode1")
				if(step==3):
					cv.create_line(cd1[ind[cd1i]][0], cd1[ind[cd1i]][1], cd2[ind[cd2i]][0], cd2[ind[cd2i]][1], fill = "yellow")
				tx = cd2[ind[cd2i]][0] - cd1[ind[cd1i]][0]; ty = cd2[ind[cd2i]][1] - cd1[ind[cd1i]][1] #下面兩點向量
				if sameArea(cd1[ind[cd1i]][0], cd1[ind[cd1i]][1], cd2[ind[cd2i]][0], cd2[ind[cd2i]][1],cd2[ind[cd2i+1]][0], cd2[ind[cd2i+1]][1], ansc[x]+500*ty, ansc[y]-500*tx)<0:
					drax2=ansc[x]+500*ty; dray2=ansc[y]-500*tx;
				else:
					if sameArea(cd1[ind[cd1i]][0], cd1[ind[cd1i]][1], cd2[ind[cd2i]][0], cd2[ind[cd2i]][1],cd2[ind[cd2i+1]][0], cd2[ind[cd2i+1]][1],ansc[x]+500*ty,ansc[y]-500*tx)==0:
						if sameArea(cd1[ind[cd1i]][0], cd1[ind[cd1i]][1], cd2[ind[cd2i]][0], cd2[ind[cd2i]][1], cd1[ind[cd1i+1]][0], cd1[ind[cd1i+1]][1],ansc[x]+500*ty,ansc[y]-500*tx)<=0:
							drax2=ansc[x]+500*ty; dray2=ansc[y]-500*tx;
						else:
							drax2=ansc[x]-500*ty; dray2=ansc[y]+500*tx;
					else:
						drax2=ansc[x]-500*ty; dray2=ansc[y]+500*tx;
				if(step==0 or step==4):
					cv.create_line(ansc[x], ansc[y], drax2, dray2, fill = "green")
					if step == 0:
						outline(ansc[x], ansc[y], drax2, dray2,0)
					stepOver = 1
				if sameArea(ansa[x], ansa[y], drax, dray, ansc[x], ansc[y], cdline1[0][0], cdline1[0][1]) < 0:
					if(step==0):
						cv.create_line(cdline1[0][0], cdline1[0][1], ansa[x], ansa[y], fill = "red")
						outline(cdline1[0][0], cdline1[0][1], ansa[x], ansa[y],0)
				else:
					if(step==0):
						cv.create_line(cdline1[1][0], cdline1[1][1], ansa[x], ansa[y], fill = "red")
						outline(cdline1[1][0], cdline1[1][1], ansa[x], ansa[y],0)
				if sameArea(ansc[x], ansc[y], drax2, dray2, ansa[x], ansa[y], cdline2[0][0], cdline2[0][1]) < 0:
					if(step==0):
						cv.create_line(cdline2[0][0], cdline2[0][1], ansc[x], ansc[y], fill = "orange")
						outline(cdline2[0][0], cdline2[0][1], ansc[x], ansc[y],1)
				else:
					if(step==0):
						cv.create_line(cdline2[1][0], cdline2[1][1], ansc[x], ansc[y], fill = "orange")
						outline(cdline2[1][0], cdline2[1][1], ansc[x], ansc[y],1)
			else:
				print("mode2")
				if(step==0 or step==4):
					cv.create_line(ansc[x], ansc[y], ansd[x], ansd[y], fill = "green")
					if step == 0:
						outline(ansc[x], ansc[y], ansd[x], ansd[y],0)
				if sameArea(ansc[x], ansc[y], ansd[x], ansd[y], ansa[x], ansa[y], cdline2[0][0], cdline2[0][1]) < 0:
					if(step==0):
						cv.create_line(cdline2[0][0], cdline2[0][1], ansc[x], ansc[y], fill = "orange")
						outline(cdline2[0][0], cdline2[0][1], ansc[x], ansc[y],0)
				else:
					if(step==0):
						cv.create_line(cdline2[1][0], cdline2[1][1], ansc[x], ansc[y], fill = "orange")
						outline(cdline2[1][0], cdline2[1][1], ansc[x], ansc[y],0)
				cd1i = cd1i+1 #下一層
				if(step==3):
					cv.create_line(cd1[ind[cd1i]][0], cd1[ind[cd1i]][1], cd2[ind[cd2i]][0], cd2[ind[cd2i]][1], fill = "yellow")
				x0 = ansd[x]; 
				y0 = ansd[y] #第三交點
				tx = cd2[ind[cd2i]][0] - cd1[ind[cd1i]][0] #原向量方向
				ty = cd2[ind[cd2i]][1] - cd1[ind[cd1i]][1]
				if sameArea(cd1[ind[cd1i]][0], cd1[ind[cd1i]][1], cd2[ind[cd2i]][0], cd2[ind[cd2i]][1],cd2[ind[cd2i+1]][0], cd2[ind[cd2i+1]][1], x0+500*ty, y0-500*tx)<0:
					drax2=x0+500*ty; dray2=y0-500*tx;
				else:
					if sameArea(cd1[ind[cd1i]][0], cd1[ind[cd1i]][1], cd2[ind[cd2i]][0], cd2[ind[cd2i]][1],cd2[ind[cd2i+1]][0], cd2[ind[cd2i+1]][1], x0+500*ty, y0-500*tx)==0:
						if sameArea(cd1[ind[cd1i]][0], cd1[ind[cd1i]][1], cd2[ind[cd2i]][0], cd2[ind[cd2i]][1],cd1[ind[cd1i+1]][0], cd1[ind[cd1i+1]][1], x0+500*ty, y0-500*tx)<=0:
							drax2=x0+500*ty; dray2=y0-500*tx;
						else:
							drax2=x0-500*ty; dray2=y0+500*tx;
					else:
						drax2=x0-500*ty; dray2=y0+500*tx;
				if(step==0 or step==4):
					cv.create_line(ansd[x], ansd[y], drax2, dray2, fill = "green")
					if step == 0:
						outline(ansd[x], ansd[y], drax2, dray2,0)
					stepOver = 1
				if(step==0):
					cv.create_line(ansd[x], ansd[y], ansa[x], ansa[y], fill = "gray")
					outline(ansd[x], ansd[y], ansa[x], ansa[y],1)

		else:					#跟bn(右邊)藍相交
			print("右邊相交")
			if(step==0 or step==4):
				cv.create_line(ansb[x], ansb[y], drax, dray, fill = "green")
				if step == 0:
					outline(ansb[x], ansb[y], drax, dray,0)
			cd2i = cd2i+1 #下一層
			x0 = ansb[x]
			y0 = ansb[y] #第一交點
			tx = cd2[ind[cd2i]][0] - cd1[ind[cd1i]][0] #原向量方向
			ty = cd2[ind[cd2i]][1] - cd1[ind[cd1i]][1]
			np1 = x0 + 10*ty; np2 = y0 - 10*tx; #原向量另一點
			x, y = symbols('x y')
			cn = solve([x0*x+y-y0,np1*x+y-np2],[x,y]) #第一交點和原向量另一點求向量方程式
			x, y = symbols('x y') 
			try: #防垂直
				ansc=solve([an[x]*x+an[y]-y,cn[x]*x+cn[y]-y],[x,y]) #求法向量與第二中垂線交點
			except:
				ansc=solve([an[x]*x+an[y]-y,x-x0],[x,y])
			if(step==0 or step==4):
				cv.create_line(x0, y0, ansc[x], ansc[y], fill = "green")
				if step == 0:
					outline(x0, y0, ansc[x], ansc[y],0)
			cd1i = cd1i+1 #下一層
			x0 = ansc[x]
			y0 = ansc[y] #第二交點
			tx = cd2[ind[cd2i]][0] - cd1[ind[cd1i]][0] #原向量方向
			ty = cd2[ind[cd2i]][1] - cd1[ind[cd1i]][1]
			np1 = x0 + 10*ty; np2 = y0 - 10*tx; #原向量另一點
			x, y = symbols('x y')
			dn = solve([x0*x+y-y0,np1*x+y-np2],[x,y]) #第二交點和原向量另一點求向量方程式
			x, y = symbols('x y')
			try: #防垂直
				ansd=solve([bn[x]*x+bn[y]-y,dn[x]*x+dn[y]-y],[x,y]) #求法向量與第二中垂線交點
			except:
				ansd=solve([bn[x]*x+bn[y]-y,x-x0],[x,y])
			#print(y0,ansd[y])
			if sameArea(cdline1[0][0],cdline1[0][1],cdline1[1][0],cdline1[1][1],ansb[x],ansb[y],ansd[x],ansd[y])>=0 or ansd[x]<-19000 or ansd[y]<-19000:
				print("mode3")
				if(step==3):
					cv.create_line(cd1[ind[cd1i]][0], cd1[ind[cd1i]][1], cd2[ind[cd2i]][0], cd2[ind[cd2i]][1], fill = "yellow")
				tx = cd2[ind[cd2i]][0] - cd1[ind[cd1i]][0]; ty = cd2[ind[cd2i]][1] - cd1[ind[cd1i]][1] #下面兩點向量
				if sameArea(cd1[ind[cd1i]][0], cd1[ind[cd1i]][1], cd2[ind[cd2i]][0], cd2[ind[cd2i]][1],cd2[ind[cd2i+1]][0], cd2[ind[cd2i+1]][1],ansc[x]+500*ty,ansc[y]-500*tx)<0:
					drax2=ansc[x]+500*ty; dray2=ansc[y]-500*tx;
				else:
					if sameArea(cd1[ind[cd1i]][0], cd1[ind[cd1i]][1], cd2[ind[cd2i]][0], cd2[ind[cd2i]][1],cd2[ind[cd2i+1]][0], cd2[ind[cd2i+1]][1],ansc[x]+500*ty,ansc[y]-500*tx)==0:
						if sameArea(cd1[ind[cd1i]][0], cd1[ind[cd1i]][1], cd2[ind[cd2i]][0], cd2[ind[cd2i]][1],cd1[ind[cd1i+1]][0], cd1[ind[cd1i+1]][1],ansc[x]+500*ty,ansc[y]-500*tx)<=0:
							drax2=ansc[x]+500*ty; dray2=ansc[y]-500*tx;
						else:
							drax2=ansc[x]-500*ty; dray2=ansc[y]+500*tx;
					else:
						drax2=ansc[x]-500*ty; dray2=ansc[y]+500*tx;
				if(step==0 or step==4):
					cv.create_line(ansc[x], ansc[y], drax2, dray2, fill = "green")
					if step == 0:
						outline(ansc[x], ansc[y], drax2, dray2,0)
					stepOver = 1
				if sameArea(ansb[x], ansb[y], drax, dray, ansc[x], ansc[y], cdline2[0][0], cdline2[0][1]) < 0:
					if(step==0):
						cv.create_line(cdline2[0][0], cdline2[0][1], ansb[x], ansb[y], fill = "red")
						outline(cdline2[0][0], cdline2[0][1], ansb[x], ansb[y],0)
				else:
					if(step==0):
						cv.create_line(cdline2[1][0], cdline2[1][1], ansb[x], ansb[y], fill = "red")
						outline(cdline2[1][0], cdline2[1][1], ansb[x], ansb[y],0)
				if sameArea(ansc[x], ansc[y], drax2, dray2, ansb[x], ansb[y], cdline1[0][0], cdline1[0][1]) < 0: #畫右邊
					if(step==0):
						cv.create_line(cdline1[0][0], cdline1[0][1], ansc[x], ansc[y], fill = "orange")
						outline(cdline1[0][0], cdline1[0][1], ansc[x], ansc[y],1)
				else:
					if(step==0):
						cv.create_line(cdline1[1][0], cdline1[1][1], ansc[x], ansc[y], fill = "orange")
						outline(cdline1[1][0], cdline1[1][1], ansc[x], ansc[y],1)
			else:
				print("mode4")
				if(step==0 or step==4):
					cv.create_line(ansc[x], ansc[y], ansd[x], ansd[y], fill = "green")
					if step == 0:
						outline(ansc[x], ansc[y], ansd[x], ansd[y],0)
				if sameArea(ansc[x], ansc[y], ansd[x], ansd[y], ansb[x], ansb[y], cdline1[0][0], cdline1[0][1]) < 0: #畫右邊
					if(step==0):
						cv.create_line(cdline1[0][0], cdline1[0][1], ansc[x], ansc[y], fill = "orange")
						outline(cdline1[0][0], cdline1[0][1], ansc[x], ansc[y],0)
				else:
					if(step==0):
						cv.create_line(cdline1[1][0], cdline1[1][1], ansc[x], ansc[y], fill = "orange")
						outline(cdline1[1][0], cdline1[1][1], ansc[x], ansc[y],0)
				cd2i = cd2i+1 #下一層
				if(step==3):
					cv.create_line(cd1[ind[cd1i]][0], cd1[ind[cd1i]][1], cd2[ind[cd2i]][0], cd2[ind[cd2i]][1], fill = "yellow")
				x0 = ansd[x]; 
				y0 = ansd[y] #第三交點
				tx = cd2[ind[cd2i]][0] - cd1[ind[cd1i]][0] #原向量方向
				ty = cd2[ind[cd2i]][1] - cd1[ind[cd1i]][1]
				if sameArea(cd1[ind[cd1i]][0], cd1[ind[cd1i]][1], cd2[ind[cd2i]][0], cd2[ind[cd2i]][1],cd2[ind[cd2i+1]][0], cd2[ind[cd2i+1]][1],x0+500*ty, y0-500*tx)<0:
					drax2=x0+500*ty; dray2=y0-500*tx;
				else:
					if sameArea(cd1[ind[cd1i]][0], cd1[ind[cd1i]][1], cd2[ind[cd2i]][0], cd2[ind[cd2i]][1],cd2[ind[cd2i+1]][0], cd2[ind[cd2i+1]][1],x0+500*ty, y0-500*tx)==0:
						if sameArea(cd1[ind[cd1i]][0], cd1[ind[cd1i]][1], cd2[ind[cd2i]][0], cd2[ind[cd2i]][1],cd1[ind[cd1i+1]][0], cd1[ind[cd1i+1]][1],x0+500*ty, y0-500*tx)<0:
							drax2=x0+500*ty; dray2=y0-500*tx;
						else:
							drax2=x0-500*ty; dray2=y0+500*tx;
					else:
						drax2=x0-500*ty; dray2=y0+500*tx;
				if(step==0 or step==4):
					cv.create_line(ansd[x], ansd[y], drax2, dray2, fill = "green")
					if step == 0:
						outline(ansd[x], ansd[y], drax2, dray2,0)
					stepOver = 1
				if(step==0):
					cv.create_line(ansd[x], ansd[y], ansb[x], ansb[y], fill = "gray")
					outline(ansd[x], ansd[y], ansb[x], ansb[y],1)
	else:
		printmessage.insert(1.0, "目前沒有支援4點以上!!")
#step by step
def step():
	global stepN
	stepN = stepN + 1
	run(stepN)
		
		
#清空畫布
def clean():
	global count, runed, stepN, stepOver, outputstr
	count = 0
	runed = 0
	stepN = 0
	stepOver = 0
	outputstr = ""
	cv.delete("all")
	cd.clear(); cd1.clear(); cd2.clear()
	printpoint.delete('1.0', END)
	printmessage.delete('1.0', END)

#讀取檔案	
def ReadF():
	global fp, filename
	clean()
	printfile = ""
	filename = tkinter.filedialog.askopenfilename()
	try:
		fp = open(filename, "r")
	except:
		printmessage.delete('1.0', END)
		printmessage.insert(1.0, "沒有讀到正確的檔案!!")
	afterfo()

#NEXT(需先開檔)
def afterfo():
	global fp, count, cd, line2
	clean()
	try:
		line = fp.readline()
		#讀到換行、#則跳過
		while line.startswith('#')%2 == 1 or line.startswith('\n')%2 == 1:
			line = fp.readline()
		#讀到0檔案結束
		if line.startswith('0')%2 == 1:
			printmessage.delete('1.0', END)
			printmessage.insert(1.0, "讀入點數為零，檔案測試停止!!")
			fp.close()
		#讀到P輸入點
		elif line.startswith('P')%2 == 1:
			while line.startswith('P')%2 == 1:
				li = line.split('\n'); point = li[0].split(' ')
				cd.append([]); cd[count].append(int(point[1])); cd[count].append(int(point[2]))
				printout = str(cd[count][0])+" "+str(cd[count][1])+"\n"
				printpoint.insert(1.0, printout)
				cv.create_oval(int(point[1])-1,int(point[2])-1,int(point[1])+1,int(point[2])+1, fill = "black")
				count = count + 1
				line = fp.readline()
			run(0)
			printmessage.delete('1.0', END)
			printmessage.insert(1.0, "檔案結束!!!!!!")
			fp.close()
		else:
			q = int(line)
			for i in range(0,q,1):
				line = fp.readline()
				point = line.split(' ')
				cd.append([])
				cd[count].append(int(point[0])) 
				cd[count].append(int(point[1]))
				printout = str(cd[count][0])+" "+str(cd[count][1])+"\n"
				printpoint.insert(1.0, printout)
				cv.create_oval(int(point[0])-1,int(point[1])-1,int(point[0])+1,int(point[1])+1, fill = "black")
				count = count + 1
	except:
		printmessage.delete('1.0', END)
		printmessage.insert(1.0, "沒有開啟檔案!!!!!!")

#寫檔(需先開檔)
def outputf():
	global outputstr
	fp = open('output.txt', 'w')
	fp.write(outputstr)
	printmessage.insert(1.0, "寫檔完成!!")

#布建介面
cv.grid(row=0, column=0, rowspan=10)
cv.configure(scrollregion = cv.bbox("ALL"))	
corx = tk.Entry(win,width=6)
corx.grid(column=2,row=0, padx=4, columnspan=2)
cory = tk.Entry(win,width=6)
cory.grid(column=4,row=0, padx=4, columnspan=2)
b1 = tk.Button(win,text="新增點",command=insert_point)
b1.grid(column=7, row=0, padx=4)
b2 = tk.Button(win, text="Clean", command=clean)
b2.grid(column=8, row=0,padx=2)
b3 = tk.Button(win, text="Run", command=lambda: run(0))
b3.grid(column=1, row=1, padx=2)
b4 = tk.Button(win, text="Next", command=afterfo)
b4.grid(column=3, row=1, padx=2)
b5 = tk.Button(win, text="Step by step", command=step)
b5.grid(column=4, row=1, padx=2)
b6 = tk.Button(win, text="讀檔", command=ReadF)
b6.grid(column=7, row=1, padx=2)
b7 = tk.Button(win, text="寫檔", command=outputf)
b7.grid(column=8, row=1, padx=2)
printmessage = tk.Text(win, height=3, yscrollcommand=1,width=45)
printmessage.grid(column=2,row=2, columnspan=20)
printpoint = tk.Text(win, height=20, yscrollcommand=1,width=45)
printpoint.grid(column=2,row=3, columnspan=20)

#bind與主程式
cv.bind('<Button-1>', callback)
win.mainloop()
