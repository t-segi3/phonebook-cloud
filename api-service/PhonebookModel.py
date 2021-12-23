import mysql.connector
from mysql.connector import Error
import uuid
import os

class PhoneBook:
    def __init__(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                passwd="root",
                database="phonebookservice"
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        self.connection = connection

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    def execute_read_query(self, query):
        cursor =  self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")

    def execute_readone_query(self, query):
        cursor =  self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchone()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")

    def list(self):
        query = "SELECT * from phonebook"
        try:
            results = self.execute_read_query(query)
            return dict(status='OK',data=results)
        except:
            return dict(status='ERR',msg='Error')

    def create(self, data):
        id = str(uuid.uuid1())
        try:
            query = "INSERT INTO phonebook (id, name, address, phone) VALUES('{0}', '{1}', '{2}', '{3}')".format(id, data['name'],data['address'],data['phone'])
            self.execute_query(query)
            return dict(status='OK',id=id)
        except:
            return dict(status='ERR',msg='Tidak bisa Create')
    
    def delete(self, id):
        try:
            query = "DELETE FROM phonebook WHERE id = '{0}'".format(id)
            self.execute_query(query)
            return dict(status='OK',msg='{} deleted' . format(id), id=id)
        except:
            return dict(status='ERR',msg='Tidak bisa Delete')

    def update(self, id, data):

        try:
            toUpdate = ""
            for idx, column in enumerate(data):
                if (idx>0):
                    toUpdate += ", "
                toUpdate +=  column + " = '" + data[column] + "' "
            query = "UPDATE phonebook set {0} WHERE id = '{1}'".format(toUpdate, id)
            self.execute_query(query)
            return dict(status='OK',msg='{} updated' . format(id), id=id)
        except:
            return dict(status='ERR',msg='Tidak bisa Update')
    
    def read(self, id):
        query = "SELECT * from phonebook WHERE id = '{0}'".format(id)
        try:
            results = self.execute_readone_query(query)
            return dict(status='OK',id=id,data=results)
        except:
            return dict(status='ERR',msg='Tidak Ketemu')

    def measure(self):
        query = "SELECT COUNT(*) FROM phonebook"
        try:
            results = self.execute_readone_query(query)
            return dict(status="OK",data=dict(record=results))
        except:
            return dict(status='ERR',msg='Gagal measure')



if __name__=='__main__':
    pd = PhoneBook()
#    ----------- create
#    result = pd.create(dict(nama='royyana',alamat='ketintang',notelp='6212345'))
#    print(result)
#    result = pd.create(dict(nama='ibrahim',alamat='ketintang',notelp='6212341'))
#    print(result)
#    result = pd.create(dict(nama='Ananda', alamat='Dinoyo Sekolahan', notelp='6212345'))
#    print(result)
#    ------------ list
    data = {}
    data['name'] = 'edit'
    data['address'] = 'jakarta'
    data['phone'] = '12345'
    # pd.create(data)
    # pd.delete('2')
    # pd.update('2', data)
    # print(pd.list())
    # print(pd.read('2'))
    print(pd.measure())
#    ------------ info
#    print(pd.read('c516b780-2fa2-11eb-bf35-7fc0bd24c845'))