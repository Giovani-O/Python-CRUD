import Conexao

def insert(nome, idade, profissao, salario):
    Conexao.cursor.execute("INSERT INTO usuario(nome, idade, profissao, salario) VALUES ('{}', {}, '{}', {})".format(nome, idade, profissao, salario))
    Conexao.connection.commit()

def delete(id):
    Conexao.cursor.execute("DELETE FROM usuario WHERE id={}".format(id))
    Conexao.connection.commit()

def selectAll():
    Conexao.cursor.execute("SELECT * FROM usuario")
    output = str(Conexao.cursor.fetchall())
    print(output.replace("}, ", "}\n"))

def select(id):
    Conexao.cursor.execute("SELECT * FROM usuario WHERE id={}".format(id))
    output = Conexao.cursor.fetchall()
    print(output)

def update(id, campo, novoDado):
    if type(novoDado)==str:
        Conexao.cursor.execute("UPDATE usuario SET {}='{}' WHERE id={}".format(campo, novoDado, id))
        Conexao.connection.commit()
    else:
        Conexao.cursor.execute("UPDATE usuario SET {}={} WHERE id={}".format(campo, novoDado, id))
        Conexao.connection.commit()