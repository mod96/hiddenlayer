#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
from PyQt5.QtWidgets import QAction, QApplication, QButtonGroup, QHeaderView, QMainWindow, QPushButton, QTextEdit, QWidget
from PyQt5.QtCore import QVariant
from PyQt5 import uic
from copy import deepcopy
form_class = uic.loadUiType("simple.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.btn_execute.clicked.connect(self.EX)
        self.btn_clear.clicked.connect(self.CL)
        
    def CL(self):
        self.textEdit.clear()
        
    ########################################################################################
    def trueEraser(self,x):
        P=deepcopy(x)
        ind1=[0]; ind2=[]
        for i in range(P.count('$Zbigcirc$')):
            ind1.append(P.find('$Zbigcirc$',ind1[i]+1))
            ind2.append(P.find('TFQT',ind1[i+1]))
        del ind1[0]
        if -1 in ind2:
            ind2.remove(-1)
            ind2.append(len(P))
        ind1.reverse()
        ind2.reverse()
        for i in range(len(ind1)):
            P=P[:ind1[i]+11]+P[ind2[i]:]    
        return P

    def falseEraser(self,x):
        P=deepcopy(x)
        ind1=[0]; ind2=[]
        for i in range(P.count('$Ztimes$')):
            ind1.append(P.find('$Ztimes$',ind1[i]+1))
            ind2.append(P.find('TFQT',ind1[i+1]))
        del ind1[0]
        if -1 in ind2:
            ind2.remove(-1)
            ind2.append(len(P))
        ind1.reverse()
        ind2.reverse()
        for i in range(len(ind1)):
            P=P[:ind1[i]+9]+P[ind2[i]:]    
        return P
    ########################################################################################
    def gtn1(self,x):
        Temp2=x[0:x.find('begin{parts}')-1]
        Temp3=x[x.find('begin{parts}')+12:]
        Temp=Temp3.replace('Zpart',' TFQT '+Temp2)
        return Temp
    def gtn2(self,x):
        Temp2=x[0:x.find('begin{parts}')-1]
        Temp3=x[x.find('begin{parts}')+12:]
        Temp=Temp3.replace('Zpart',' MCQT '+Temp2)
        return Temp
    def ftn(self,x):
        if x.find('$Ztimes$')>0 or x.find('$Zbigcirc$')>0:
            if x.find('begin{parts}')>0:
                return self.trueEraser(self.falseEraser( self.gtn1(x)))
            else:
                return self.trueEraser(self.falseEraser(' TFQT '+x))
        else:
            if x.find('begin{parts}')>0:
                return self.gtn2(x)
            else:
                return ' MCQT '+x

    def ktn(self,K,x):
        if x.find('TFQT')>0:
            return K+x
        else:
            y=deepcopy(x)
            for f in range(x.count('MCQT')):
                Temp1=''
                Temp2=''

                ind3=[0]
                for h in range(y.count('Zend{enumerate}')):
                    ind3.append(y.find('Zend{enumerate}',ind3[h]+1))
                del ind3[0]

                ind4=[0]
                for h in range(y.count('MCQT')):
                    ind4.append(y.find('MCQT',ind4[h]+1))
                del ind4[0]
                ind4.append(len(y))

                if y.count('MCQT')>1.5:
                    for g in range(y.find('Zend{enumerate}')+15,y.find('Zend{enumerate}')+20):
                        Temp2=Temp2+y[g]
                else:
                    Temp2=y[y.find('Zend{enumerate}')+15:y.find('Zend{enumerate}')+20]

                if y.count('MCQT')>1.5:
                    for g in range(y.find('Zbegin{enumerate}')+17,ind4[f+1]-1):
                        Temp1=Temp1+y[g]
                else:
                    Temp1=y[y.find('Zbegin{enumerate}')+17:]

                ind5=[0];
                for h in range(4):
                    ind5.append(Temp1.find('Zitem',ind5[h]+1))
                del ind5[0] 

                if Temp2.find('(1)')>0 or Temp2.find('(1) ')>0:
                    Temp1=Temp1[:ind5[1]]+' AAAAAAAAAA '+Temp1[ind5[1]+5:]
                    ind5.append(Temp1.find('Zend{enumerate}'))
                    Temp1=Temp1[:ind5[4]]+' BBBBBBBBBB '+Temp1[ind5[4]:]
                elif Temp2.find('(2)')>0 or Temp2.find('(2) ')>0:
                    Temp1=Temp1[:ind5[2]]+' AAAAAAAAAA '+Temp1[ind5[2]+5:]
                    ind5.append(Temp1.find('Zend{enumerate}'))
                    Temp1=Temp1[:ind5[4]]+' BBBBBBBBBB '+Temp1[ind5[4]:]
                elif Temp2.find('(3)')>0 or Temp2.find('(3) ')>0:
                    Temp1=Temp1[:ind5[3]]+' AAAAAAAAAA '+Temp1[ind5[3]+5:]
                    ind5.append(Temp1.find('Zend{enumerate}'))
                    Temp1=Temp1[:ind5[4]]+' BBBBBBBBBB '+Temp1[ind5[4]:]
                elif Temp2.find('(4)')>0 or Temp2.find('(4) ')>0:
                    ind5.append(Temp1.find('Zend{enumerate}'))
                    Temp1=Temp1[:ind5[4]]+' AAAAAAAAAA '+Temp1[ind5[4]:]
                else:
                    Temp1=Temp1+' XXXXXXXXXXXXXXXXXXXXXX '


                Temp1=Temp1[:Temp1.find('Zend{enumerate}')]
                Temp1=Temp1[:Temp1.find('Zitem')]+' DUMMY '+Temp1[Temp1.find('Zitem')+5:]
                Temp1=Temp1.replace('Zitem',' BBBBBBBBBB ')

                ind4=[0]
                for h in range(y.count('MCQT')):
                    ind4.append(y.find('MCQT',ind4[h]+1))
                del ind4[0]
                ind4.append(len(y))

                y=y[:y.find('Zbegin{enumerate}')-1]+' '+Temp1+' '+y[ind4[f+1]:]

            return K+y

    ############################################   
 
    #PlainTextEdit과 관련된 함수
    def EX(self) :
        B=str(self.textEdit.toPlainText());
        B=B.replace('\t',' ')
        B=B.replace('\n',' ')
        B=B.replace('\\','Z')
        B=B.replace('Z[','$')
        B=B.replace('Z]','$')
        B=B.replace('Zbegin{equation}','$')
        B=B.replace('Zend{equation}','$')
        B=B.replace('Zbegin{eqnarray*}','$')
        B=B.replace('Zend{eqnarray*}','$')
        B=B.replace('Zquestion[1]','Zquestion ')
        B=B.replace('Zquestion[2]','Zquestion ')
        B=B.replace('Zquestion[3]','Zquestion ')
        B=B.replace('Zquestion[4]','Zquestion ')
        B=B.replace('Zquestion[5]','Zquestion ')
        B=B.replace('Zquestion[6]','Zquestion ')
        B=B.replace('Zquestion[7]','Zquestion ')
        B=B.replace('Zquestion[8]','Zquestion ')
        B=B.replace('Zquestion[9]','Zquestion ')
        B=B.replace('Zquestion[10]','Zquestion ')
        B=B.replace('Zquestion[11]','Zquestion ')
        B=B.replace('  ',' ')
        A=list(B)
        K=False
        i=0
        while i<len(A)-1:
            if A[i]=='$':
                K=not K
            elif A[i]=='Z' and A[i+1]=='Z' and K==False:
                del A[i]
                del A[i]
                i=i-1
            elif A[i]==' ' and A[i+1]==' ' and K==False:
                del A[i]
                i=i-1
            while K==True:
                i=i+1
                if A[i]=='$':
                    K=not K
                elif A[i]==' ' and A[i+1]==' ':
                    del A[i]
                    i=i-1
            i=i+1
        i=0
        while i<len(A)-1:
            if A[i]==' ' and A[i+1]==' ':
                del A[i]
                i=i-1
            i=i+1
        B = ''.join(A)
        B=B.replace('Zpartial',' QWERTY ')     
        index=[0]
        for i in range(B.count('Zquestion')):
            index.append(B.find('Zquestion',index[i]))
            B=B[:index[i+1]]+B[index[i+1]+1:]
        del index[0]
        index.append(len(B))

        K=''
        for i in range(len(index)-1):
            Temp=''
            for j in range(index[i]+9,index[i+1]-1):
                Temp=Temp+B[j]
            K=self.ktn(K,self.ftn(Temp))

        K=K.replace(' QWERTY ','Zpartial ')  
        for i in range(K.count('begin{center}')):
            ind1=K.find('Zbegin{center}')
            ind2=K.find('Zend{center}')
            K=K[:ind1]+K[ind2+12:]
        A=list(K)
        K=False
        i=0
        while i<len(A)-1:
            if A[i]=='$':
                K=not K
            elif A[i]=='Z' and A[i+1]=='Z' and K==False:
                del A[i]
                del A[i]
                i=i-1
            elif A[i]==' ' and A[i+1]==' ' and K==False:
                del A[i]
                i=i-1
            i=i+1
        i=0
        while i<len(A)-1:
            if A[i]==' ' and A[i+1]==' ':
                del A[i]
                i=i-1
            i=i+1
        ########################################################################################
        st=''.join(A)
        st=st.replace('$','$$')
        st=st.replace('&=&','=')
        st=st.replace('Zbegin{parts}','')
        st=st.replace('Zend{parts}','')
        st=st.replace('Zend{parts','')
        st=st.replace('Zbegin{enumerate}','')
        st=st.replace('Zend{enumerate}','')
        st=st.replace('Zend{enumerate','')
        st=st.replace(' BBBBBBBBBB ','\tincorrect\t')
        st=st.replace(' AAAAAAAAAA ','\tcorrect\t')
        st=st.replace(' DUMMY ','\t')
        st=st.replace('Zmathbbm','Zmathbb')
        st=st.replace('MCQT','\nMC\t')
        st=st.replace('MCQT ','\nMC\t')
        st=st.replace('TFQT','\nMC\t')
        st=st.replace('TFQT ','\nMC\t')
        st=st.replace('Ztextbf{A:}','')
        st=st.replace('$$Ztimes$$','\t'+'true'+'\t'+'incorrect'+'\t'+'false'+'\t'+'correct'+'\t'+'pass'+'\t'+'incorrect')
        st=st.replace('$$Zbigcirc$$','\t'+'true'+'\t'+'correct'+'\t'+'false'+'\t'+'incorrect'+'\t'+'pass'+'\t'+'incorrect')
        st=st.replace('Z','\\')
        ########################################################################################
        file=open('result.txt','w')
        file.write(st)
        file.close()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 

