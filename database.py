import mysql.connector as mysql
pas=input('Enter mysql password: ')
try:
    myco= mysql.connect(host='localhost',user='root',password= pas)
    if myco.is_connected()==True:
        print("Connection Established")
        cur=myco.cursor()
        try:
            cur.execute("create database school")
            myco.commit()
            print('Database school created')
        except:
            print('School already exists ')
       
        try:
            mycon= mysql.connect(host='localhost',user='root',password= pas,database='school')
            cursor=mycon.cursor()
            try:
                cursor.execute('create table math(Day varchar(10), 1st int, 2nd int,3rd int,4th int,5th int,6th int,7th int,8th int)')    
                cursor.execute("insert into math values('mon',6,7,8,8,null,9,null,10)")
                cursor.execute("insert into math values('tue',6,7,8,8,null,9,null,10)")
                cursor.execute("insert into math values('wed',6,7,8,8,null,9,null,10)")
                cursor.execute("insert into math values('thu',10,9,9,null,8,6,7,null)")
                cursor.execute("insert into math values('fri',10,9,9,null,8,6,7,null)")
                cursor.execute("insert into math values('sat',10,9,9,null,8,6,7,null)")
                mycon.commit()
                print('math created')
            except:
                print('math ','Already exists')

            try:
                cursor.execute('create table sci(Day varchar(10), 1st int, 2nd int,3rd int,4th int,5th int,6th int,7th int,8th int)')    
                cursor.execute("insert into sci values('mon',7,8,6,9,null,10,null,null)")
                cursor.execute("insert into sci values('tue',7,8,6,9,null,10,null,null)")
                cursor.execute("insert into sci values('wed',7,8,6,9,null,10,null,null)")
                cursor.execute("insert into sci values('thu',6,10,null,9,null,8,null,7)")
                cursor.execute("insert into sci values('fri',6,10,null,9,null,8,null,7)")
                cursor.execute("insert into sci values('sat',6,10,null,9,null,8,null,7)")
                mycon.commit()
                print('sci created')
            except:
                print('sci ','Already exists')
            try:
                cursor.execute('create table eng(Day varchar(10), 1st int, 2nd int,3rd int,4th int,5th int,6th int,7th int,8th int)')    
                cursor.execute("insert into eng values('mon',8,6,7,10,6,null,9,null)")
                cursor.execute("insert into eng values('tue',8,6,7,10,6,null,9,null)")
                cursor.execute("insert into eng values('wed',8,6,7,10,6,null,9,null)")
                cursor.execute("insert into eng values('thu',8,8,10,null,9,7,null,6)")
                cursor.execute("insert into eng values('fri',8,8,10,null,9,7,null,6)")
                cursor.execute("insert into eng values('sat',8,8,10,null,9,7,null,6)")
                mycon.commit()
                print('eng created')
            except:
                print('eng ','Already exists')

            try:
                cursor.execute('create table sst(Day varchar(10), 1st int, 2nd int,3rd int,4th int,5th int,6th int,7th int,8th int)')    
                cursor.execute("insert into sst values('mon',9,null,null,6,7,6,10,8)")
                cursor.execute("insert into sst values('tue',9,null,null,6,7,6,10,8)")
                cursor.execute("insert into sst values('wed',9,null,null,6,7,6,10,8)")
                cursor.execute("insert into sst values('thu',7,7,8,null,9,10,6,null)")
                cursor.execute("insert into sst values('fri',7,7,8,null,9,10,6,null)")
                cursor.execute("insert into sst values('sat',7,7,8,null,9,10,6,null)")
                mycon.commit()
                print('sst created')
            except:
                print('sst ','Already exists')

            try:
                cursor.execute('create table hin(Day varchar(10), 1st int, 2nd int,3rd int,4th int,5th int,6th int,7th int,8th int)')    
                cursor.execute("insert into hin values('mon',10,9,null,null,8,8,7,6)")
                cursor.execute("insert into hin values('tue',10,9,null,null,8,8,7,6)")
                cursor.execute("insert into hin values('wed',10,9,null,null,8,8,7,6)")
                cursor.execute("insert into hin values('thu',9,null,7,8,6,null,10,9)")
                cursor.execute("insert into hin values('fri',9,null,7,8,6,null,10,9)")
                cursor.execute("insert into hin values('sat',9,null,7,8,6,null,10,9)")
                mycon.commit()
                print('hin created')
            except:
                print('hin ','Already exists')

        except:
            pass
    else:
        pass
except:
    print('Connection Failed !!!')
ex=input('Press any key to exit.......')
exit()
