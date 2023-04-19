import sqlite3 

class Database: 
    def __init__(self, path ) -> None:
        self.con = sqlite3.connect( path )
        self.path = path
        self.cursor = self.con.cursor()
        self.create_tables() 

    def create_tables( self ): 
        # Cria tabela de usuários
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS 
                user(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username VARCHAR(32) NOT NULL,
                    password VARCHAR(32) NOT NULL,
                    pet_name VARCHAR(32) NOT NULL,
                    pet_age INTEGER,
                    pet_photo INTEGER
                )
            '''
        )
        self.con.commit() 


    def create_user( self, username : str, password : str, pet_name : str, pet_age : str, pet_photo : str, __debug : bool = False ) -> bool:
        # Procura o ID de um usuário com o mesmo username 
        self.cursor.execute( 'SELECT id FROM user WHERE username = ?', ( username, ) )
        has_user = self.cursor.fetchall()
        # Se encontrar um ID então já existe usuário com esse username
        if has_user:
            if __debug:
                print( f'Username already registered at {username}')
            return False
        # Caso contrário deve criar um novo
        else:  
            # Adiciona o novo membro dentro da tabela
            self.cursor.execute( 'INSERT INTO user( username, password, pet_name, pet_age, pet_photo ) VALUES(?,?,?,?,?)', ( username, password, pet_name, pet_age, pet_photo ) )
            self.con.commit()
            if __debug:
                print(f'Username {username} registered.')
        return True


    def login( self, user : str, password : str, __debug : bool = False ) -> bool:
        # Procura a senha do usuário cadastrado com o username 
        self.cursor.execute( 'SELECT password FROM user WHERE username = ?', ( user, ) )
        user_data = self.cursor.fetchall()
        # Se não há nenhum usuário cadastrado, não retorna nada 
        if not user_data: 
            if __debug:
                print( f'Não possui nenhum usuário cadastrado como {user}')
            return False 
        # Se não, basta comparar as senhas
        if user_data[0][0] == password:
            if __debug:   
                print( f'Username {user} found and psd check' )
            return True 
        else:
            if __debug:
                print( f'Username {user} and psd dont check')
            return False


    def get_photo( self, username : str, __debug : bool = False ) -> bytearray:
        try: 
            self.cursor.execute( 'SELECT pet_photo FROM user WHERE username = ?', ( username, ) )
            photo =  self.cursor.fetchall()[0]
            if __debug: 
                print( f'[{username}] A photo has found')
            return photo[0]
        except:
            print( f'{username} dont have a photo updated. Can use datebase.att_photo method.')
            return False 
        


if __name__ == '__main__':
    db = Database('db\\database.db') 
    # print( db.create_user( 'Bruno', '12345', 'Tata', 10, 1, ))
    # print( db.login( 'Bruno', '12345' ) ) 
    print( db.get_photo( 'Bruno'  ) ) 
    # db.att_profit( 'iosnaaente', 1500 )
    # print( db.get_family_profit( 'Sampaio', True ) )  