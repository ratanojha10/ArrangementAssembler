from tkinter import *
import mysql.connector as mysql
#defining functions
'''----------------------------------------------------------------------------------------------------------------'''
'''Setting Up Arranger Window'''
def arr():
    try:
        k=open('C:\\Users\\{}\\Desktop\\ArrangementAssembler\\Absentees.dat'.format(usr),'r')
    except:
        print('File Not Found :|')
    conn=0
    while conn==0:
        try:
            mycon= mysql.connect(host='localhost',user='root',password= pas,database='school')
            cursor=mycon.cursor()
            print ('Connection Sucessful!! :)')
            conn=1
        except:
            print('Connection Failed!!!')
# Making list of absent and available teachers
    pd_lst=['1st','2nd','3rd','4th','5th','6th','7th','8th']
    dt= k.readline()[0:3]

    t_lst=[]
    cursor.execute('show tables')
    data=list(cursor.fetchall())
    for t in data:
        t_lst+=[t[0]]

    abt=[]
    for l in range(10):
        line=k.readline()
        if len(line)==4:
            abt+=[(line[0:3])]
    ch_lst=t_lst
    for a in abt:
        ch_lst.remove(a)

# Setting-up GUI
    arw=Tk()
    arw.title('Arranger')
    arw.configure(background="black")

    head=Label(arw,text ='ARRANGER',bg='black', font= ('Gabriola',40), fg='lime')
    head.grid(row=0,column=0)

# defining scroll region
    def region(event):
        can.configure(scrollregion=can.bbox("all"),width=680,height=605)

    fr=Frame(arw)
    fr.grid(row=1,column=0)
    can=Canvas(fr,bg='black')
    can.grid(row=1,column=0)

    mainframe=Frame(can,bg='black',relief='raised',bd=5)
    scrollBar =Scrollbar(mainframe, orient='vertical')

    can.create_window(0, 0, window=mainframe,anchor='nw')
    fr.bind("<Configure>",region)

    scrollBar.config(command=can.yview)
    scrollBar.grid(row=1,column=6,rowspan=100,sticky='ns')

    can.config(yscrollcommand=scrollBar.set)

# Creating table of available teachers in GUI window
    for i in range(len(abt)):
        cursor.execute("select 1st,2nd,3rd,4th,5th,6th,7th,8th from {} where day='{}'".format(abt[i],dt))
        d=cursor.fetchone()

        tcname=Label(mainframe,text ='Absent Teacher : '+ abt[i],bg='black',height=1, font= ('Gabriola',30),fg='lime')
        tcname.grid(row=i*8+2,column=1,columnspan=10)
        
        period=Frame(mainframe,bg='black',relief='groove',bd=5)
        period.grid(row=i*8+3,column=0)
        label=Label(period,text ='PERIODS',bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=3)
        label.grid(row=i*8+3,column=0)
        for p in range(8):
            prd=Label(period,text =pd_lst[p],width=7,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=2)
            prd.grid(row=i*8+4+p,column=0)

        clas=Frame(mainframe,bg='black',relief='groove',bd=5)
        clas.grid(row=i*8+3,column=1)
        label=Label(clas,text ='CLASS',width=7,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=3)
        label.grid(row=i*8+3,column=1)
        for m in range(8):
            if (d[m])==None:
                label=Label(clas,text ='Free',width=7,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=2)
                label.grid(row=i*8+4+m,column=1)
            else:
                label=Label(clas,text =d[m],width=7,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=2)
                label.grid(row=i*8+4+m,column=1)

        avail_tch=Frame(mainframe,bg='black',relief='groove',bd=5)
        avail_tch.grid(row=i*8+3,column=2)
        label=Label(avail_tch,text ='AVAILABLE TEACHERS',width=40,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=3)
        label.grid(row=i*8+3,column=2,columnspan=3)

        cn=2
        for pd in range(8):
            for c in ch_lst:
                cursor.execute("select {} from {} where day='{}' and {} is Null".format(pd_lst[pd],c,dt,pd_lst[pd]))
                ch_data=cursor.fetchone()
                if ch_data!=None:
                    label=Label(avail_tch,text =c,width=7,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=2)
                    label.grid(row=i*8+4+pd,column=cn)
                    cn+=1
                elif cn<3:
                    label=Label(avail_tch,text ='None',width=7,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=2)
                    label.grid(row=i*8+4+pd,column=cn)
            cn=2
    mainloop()
'''-----------------------------------------------------------------------------------------------------------------------------------------------
Setting Up Assembler window'''
def asmf():
    def act():
        try:
            for i in t_lst:
                k.write(i.get()+'\n')
            k.flush()
            aw.destroy()
            arr()
        except:
            aw.destroy()
            fl=Tk()
            fl.title('Failure')
            label=Label(fl, text = '   File Not Found :(   ' , bg='black', fg= 'red', font =('Gabriola', 30 ))
            label.grid(row=0,column=0)
    #address of document where list of absent teachers must be saved\\//
    try:
        k=open('C:\\Users\\{}\\Desktop\\ArrangementAssembler\\Absentees.dat'.format(usr),'w')
    except:
        print('File Not Found :|')
    # Setting up GUI Interface
    aw=Tk()
    aw.title('Assembler')
    aw.configure(background="black")
    aw.resizable(False,False)

    title=Label(aw, text ='ASSEMBLER',bg='black', width=15, font= ('Gabriola',30), fg='lime',relief= 'raised',bd=5)
    title.grid(row=0, column= 1,pady=5,padx=5)
    inst1=Label(aw, text =('-> Enter 3 character teacher codes in each column.')
               ,bg='black', font= ('Gabriola',15), fg='lime')
    inst1.grid(row=2, column= 1)
    inst2=Label(aw, text =('-> Then click submit button.')
               ,bg='black', font= ('Gabriola',15), fg='lime')
    inst2.grid(row=3, column= 1)

    dt= Entry(aw,width=20)
    txt=Label(aw,text='Day of week',bg='black', width=15, font= ('Gabriola',15), fg='lime').grid(row=4,column=0)

    t1= Entry(aw,width=20)
    t2= Entry(aw,width=20)
    t3= Entry(aw,width=20)
    t4= Entry(aw,width=20)
    t5= Entry(aw,width=20)
    t6= Entry(aw,width=20)
    t7= Entry(aw,width=20)
    t8= Entry(aw,width=20)
    t9= Entry(aw,width=20)
    t10= Entry(aw,width=20)
    t_lst=[dt,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10]
    for i in range (len(t_lst)):
        if i ==0:
            t_lst[i].grid(row=i+4, column= 1,pady=5,padx=5)
        elif i >0:
            label = Label(aw, text = ("Teacher",i,':'),bg='black', width=15, font= ('Gabriola',15), fg='lime')
            label.grid(row=i+5, column= 0)
            t_lst[i].grid(row=i+5, column= 1,pady=5,padx=5)

    sub = Button(aw, text='SUBMIT',bg='black', width=15, font= ('Georgia',10), fg='lime',
                  relief='raised',bd=5 ,command= act )
    sub.grid(padx=2,row=15, column= 4)
    aw.mainloop()

'''-------------------------------------------------------------------------------------------------------------------------------------------------------
Setting Up Database window'''
def dbf():
    def inp(c):
        if len(plst[c].get())==0:
            return('null')
        else:
            return(plst[c].get())

    def crate():
        try:
            cursor.execute('create table {}(Day varchar(10), 1st int, 2nd int,3rd int,4th int,5th int,6th int,7th int,8th int)'.format(tnm.get()))
        except:
            pass
        tchnm=tnm.get()
        for d in range(6):
            k=d*9+1
            cursor.execute("insert into {} values('{}',{},{},{},{},{},{},{},{})".format(
                tchnm,dys[d],inp(k),inp(k+1),inp(k+2),inp(k+3),inp(k+4),inp(k+5),inp(k+6),inp(k+7)))
            mycon.commit()
        print(' THANK YOU !!!! :)')
        tt_cret.destroy()
        
    conn=0
    if conn==0:
        try:
            mycon= mysql.connect(host='localhost',user='root',password= pas,database='school')
            cursor=mycon.cursor()
            print ('Connection Sucessful!! :)')
            conn=1
        except:
            print('Connection Failed!!! :[')
            
    tt_cret=Tk()
    tt_cret.title('Time-Table Synthesis')
    tt_cret.configure(background="black")
    tt_cret.resizable(False,False)
    head=Label(tt_cret,text ='Time-Table Synthesis',bg='black', font= ('Gabriola',40), fg='lime')
    head.grid(row=0,column=1)

    tcname=Label(tt_cret,text ='Enter Teacher Code :',bg='black',height=1, font= ('Gabriola',20), fg='lime')
    tcname.grid(row=1,column=0,padx=5)

    tnm= Entry(tt_cret,width=20)
    tnm.grid(row=1,column=1)

    day=Frame(tt_cret,bg='black',bd=5)
    day.grid(row=2,column=0,columnspan=9,sticky='nw')
    p_d=Label(day,text ='Periods-> \n Days \\/',bg='black',height=2, font= ('Gabriola',20), fg='lime',relief='raised',bd=3)
    p_d.grid(row=0,column=0)

    for i in range (1,9):
        label=Label(day,text =i,height=2,width=7,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=3)
        label.grid(row=0,column=i)


    m=Label(day,text ='Monday',width=8,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=3)
    m1=Entry(day,width=7,font= ('Gabriola',20))
    m2=Entry(day,width=7,font= ('Gabriola',20))
    m3=Entry(day,width=7,font= ('Gabriola',20))
    m4=Entry(day,width=7,font= ('Gabriola',20))
    m5=Entry(day,width=7,font= ('Gabriola',20))
    m6=Entry(day,width=7,font= ('Gabriola',20))
    m7=Entry(day,width=7,font= ('Gabriola',20))
    m8=Entry(day,width=7,font= ('Gabriola',20))


    t=Label(day,text ='Tuesday',width=8,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=3)
    t1=Entry(day,width=7,font= ('Gabriola',20))
    t2=Entry(day,width=7,font= ('Gabriola',20))
    t3=Entry(day,width=7,font= ('Gabriola',20))
    t4=Entry(day,width=7,font= ('Gabriola',20))
    t5=Entry(day,width=7,font= ('Gabriola',20))
    t6=Entry(day,width=7,font= ('Gabriola',20))
    t7=Entry(day,width=7,font= ('Gabriola',20))
    t8=Entry(day,width=7,font= ('Gabriola',20))

    w=Label(day,text ='Wednesday',width=8,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=3)
    w1=Entry(day,width=7,font= ('Gabriola',20))
    w2=Entry(day,width=7,font= ('Gabriola',20))
    w3=Entry(day,width=7,font= ('Gabriola',20))
    w4=Entry(day,width=7,font= ('Gabriola',20))
    w5=Entry(day,width=7,font= ('Gabriola',20))
    w6=Entry(day,width=7,font= ('Gabriola',20))
    w7=Entry(day,width=7,font= ('Gabriola',20))
    w8=Entry(day,width=7,font= ('Gabriola',20))

    th=Label(day,text ='Thursday',width=8,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=3)
    th1=Entry(day,width=7,font= ('Gabriola',20))
    th2=Entry(day,width=7,font= ('Gabriola',20))
    th3=Entry(day,width=7,font= ('Gabriola',20))
    th4=Entry(day,width=7,font= ('Gabriola',20))
    th5=Entry(day,width=7,font= ('Gabriola',20))
    th6=Entry(day,width=7,font= ('Gabriola',20))
    th7=Entry(day,width=7,font= ('Gabriola',20))
    th8=Entry(day,width=7,font= ('Gabriola',20))

    f=Label(day,text ='Friday',width=8,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=3)
    f1=Entry(day,width=7,font= ('Gabriola',20))
    f2=Entry(day,width=7,font= ('Gabriola',20))
    f3=Entry(day,width=7,font= ('Gabriola',20))
    f4=Entry(day,width=7,font= ('Gabriola',20))
    f5=Entry(day,width=7,font= ('Gabriola',20))
    f6=Entry(day,width=7,font= ('Gabriola',20))
    f7=Entry(day,width=7,font= ('Gabriola',20))
    f8=Entry(day,width=7,font= ('Gabriola',20))

    s=Label(day,text ='Saturday',width=8,bg='black', font= ('Gabriola',20), fg='lime',relief='raised',bd=3)
    s1=Entry(day,width=7,font= ('Gabriola',20))
    s2=Entry(day,width=7,font= ('Gabriola',20))
    s3=Entry(day,width=7,font= ('Gabriola',20))
    s4=Entry(day,width=7,font= ('Gabriola',20))
    s5=Entry(day,width=7,font= ('Gabriola',20))
    s6=Entry(day,width=7,font= ('Gabriola',20))
    s7=Entry(day,width=7,font= ('Gabriola',20))
    s8=Entry(day,width=7,font= ('Gabriola',20))

    plst=[m,m1,m2,m3,m4,m5,m6,m7,m8,
          t,t1,t2,t3,t4,t5,t6,t7,t8,
          w,w1,w2,w3,w4,w5,w6,w7,w8,
          th,th1,th2,th3,th4,th5,th6,th7,th8,
          f,f1,f2,f3,f4,f5,f6,f7,f8,
          s,s1,s2,s3,s4,s5,s6,s7,s8]
    dys=['mon','tue','wed','thu','fri','sat']
    for i in range (0,54,9):
        for j in range (0,9):
            plst[i+j].grid(row=int(i/8)+1,column=j)
            
    sub = Button(tt_cret, text='SUBMIT',bg='black', width=15, font= ('Georgia',10), fg='lime',
                  relief='raised',bd=5 ,command= crate )
    sub.grid(padx=2,row=15, column= 4)
    mainloop()

'''------------------------------------------------------------------------------------------------------------------------------
Setting Up Welcome window'''
def mwin():
    global usr,pas
    pas=paswrd.get()
    usr=user.get()
    #add here your address of welcome document where it is saved \\//
    try:
        hlo=open('C:\\Users\\{}\\Desktop\\ArrangementAssembler\\welcome.dat'.format(usr))
    except:
        print('File Not Found :|')
    home.destroy()
    #setting-up parent window
    m_win=Tk()
    m_win.title('Arrangement Assembler')
    m_win.configure(background="black")
    m_win.resizable(False,False)
    #setting-up buttons
    buttonfr=Frame(m_win, bg='black')
    buttonfr.grid(row=0, column=0,columnspan=6)

    asm= Button(buttonfr, text='Assembler', height= 1,bd=5, font= ('Georgia',8), bg='black',fg='lime', relief= 'raised'
                ,command=asmf)
    asm.grid(padx=2, pady=2, row=0, column= 0)
    dbb= Button (buttonfr, text='Database', height= 1,bd=5, font= ('Georgia',8), bg='black',fg='lime', relief= 'raised'
                 ,command= dbf)
    dbb.grid(padx=2, pady=2, row=0, column= 1)
    exb=Button (buttonfr, text='Exit',width=10,height= 1,bd=5, font= ('Georgia',8), bg='black',fg='lime', relief= 'raised',
                command=m_win.destroy )
    exb.grid(padx=2, pady=2, row=0, column= 5)

    #displaying the logo
    pageframe=Frame(m_win,bg='black')
    pageframe.grid(row=1,column=0,columnspan=6)

    try:
        lg = Canvas(pageframe, width = 270, height = 295, bg='black',relief= 'groove' )
        logo = PhotoImage(file=r'C:\Users\{}\Desktop\ArrangementAssembler\logo.png'.format(usr))      
        lg.create_image(2,2, anchor=NW, image=logo)
        lg.grid(row=1, column= 3)
    except:
        label=Label(pageframe , text = '        File Not Found :(         '
                    , bg='black', fg= 'red', font =('Gabriola', 30 ))
        label.grid(row=1,column=3)
    #displaying welcome message
    try:
        wlc = Label(pageframe , text = hlo.read() , bg='black', fg= 'lime', font =('Gabriola', 18 ))
        wlc.grid(row=2, column= 2,columnspan=3)
    except:
        pass
    end=Label(m_win, bg='black' ).grid(row=3, column= 0)

    m_win.mainloop()

'''--------------------------------------------------------------------------------------------------------------------------------------------------------
Setting Up U&P window'''
home=Tk()
home.title('Arrangement Assembler')
home.configure(background="black")
home.resizable(False,False)
label=Label(home , text = 'Computer Username : ' , bg='black', fg= 'powder blue', font =('Gabriola', 20 ))
label.grid(padx=2, pady=2,row=1,column=1,columnspan=2)
user=Entry(home,width=20,font= ('Sans',10,'bold'))
user.grid(padx=10, pady=2,row=1,column=3,columnspan=2)
label=Label(home , text = 'MYSQL Password : ' , bg='black', fg= 'powder blue', font =('Gabriola', 20 ))
label.grid(padx=2, pady=2,row=2,column=1,columnspan=2)
paswrd=Entry(home,width=20,show='*',font= ('Sans',10,'bold'))
paswrd.grid(padx=10, pady=2,row=2,column=3,columnspan=2)
nxt=Button (home, text='NEXT',width=10,height= 1,bd=5, font= ('Georgia',8), bg='black',fg='powder blue', relief= 'raised',
            command=mwin)
nxt.grid(padx=2, pady=2, row=3, column= 2)
home.mainloop()
'''>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>THANK YOU<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'''
