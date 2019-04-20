from nfelib.v4_00 import leiauteNFe_sub as parser
import mysql.connector

nfe = parser.parse('tests\\novo.xml')

db = mysql.connector.Connect(host='127.0.0.1', user='root', password='', database='test')
query = "SELECT * FROM test.teste LIMIT 10"
cur = db.cursor()
cur.execute(query)
records = cur.fetchall()
print(records)

# teste 123

print(nota.infNFe.emit.CNPJ)

print(nota.infNFe.det[0].prod.cEAN)

nota.infNFe.det[0]

# print do nó inteiro
# nota.infNFe.emit.export(sys.stdout, 0)
