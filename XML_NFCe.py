from nfelib.v4_00 import leiauteNFe_sub as parser
import mysql.connector
import os

# path = 'C:\\Users\\Avell\\Desktop\\tests'
path = 'C:\\Users\\Avell\\Desktop\\xml-nfce-001-2018'
#
for filename in os.listdir(path):
    nfce = parser.parse('%s\\%s' % (path, filename))

# Manual path to test:
# nfce = parser.parse('tests\\nfce-dist.xml')

    def insertXML(newlist):
        try:
            connection = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='xml')

            sql_insert_query = """ INSERT INTO `nfce_001_2018` VALUES (%s,%s,
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
            'Goias Comercio De Cosmeticos Ltda',NULL,NULL,'Av. Central N. 577 Qd. 197 Lt. 03',577,'Setor Empresarial',5208707,'Goiania','GO',74583350,1058,'Brasil',6235866377,105620947,3,
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

            insert_tuple = newlist
            cursor = connection.cursor(prepared=True)

            result  = cursor.executemany(sql_insert_query, insert_tuple)
            connection.commit()
            print(cursor.rowcount , "Record inserted successfully into xml table")
            print ("The XML was inserted successfully into xml table")
        except mysql.connector.Error as error :
            connection.rollback()
            print("Failed to insert the XML into MySQL table {}".format(error))
        finally:
            # Close the database connection.
            if(connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    newlist = []

    for index in range(len(nfce.infNFe.det)):
        newlist.append((
            nfce.infNFe.versao,
            nfce.infNFe.Id[3:],
            nfce.infNFe.ide.cUF,
            nfce.infNFe.ide.cNF,
            nfce.infNFe.ide.natOp,
            nfce.infNFe.ide.mod,
            nfce.infNFe.ide.serie,
            nfce.infNFe.ide.nNF,
            nfce.infNFe.ide.dhEmi,
            nfce.infNFe.ide.tpNF,
            nfce.infNFe.ide.idDest,
            nfce.infNFe.ide.cMunFG,
            nfce.infNFe.ide.tpImp,
            nfce.infNFe.ide.tpEmis,
            nfce.infNFe.ide.cDV,
            nfce.infNFe.ide.tpAmb,
            nfce.infNFe.ide.finNFe,
            nfce.infNFe.ide.indFinal,
            nfce.infNFe.ide.indPres,
            nfce.infNFe.ide.procEmi,
            nfce.infNFe.emit.CNPJ,
            nfce.infNFe.det[index].nItem,
            nfce.infNFe.det[index].prod.cProd,
            nfce.infNFe.det[index].prod.cEAN,
            nfce.infNFe.det[index].prod.xProd,
            nfce.infNFe.det[index].prod.NCM,
            nfce.infNFe.det[index].prod.CFOP,
            nfce.infNFe.det[index].prod.uCom,
            nfce.infNFe.det[index].prod.qCom,
            nfce.infNFe.det[index].prod.vUnCom,
            nfce.infNFe.det[index].prod.vProd,
            nfce.infNFe.det[index].prod.cEANTrib,
            nfce.infNFe.det[index].prod.uTrib,
            nfce.infNFe.det[index].prod.qTrib,
            nfce.infNFe.det[index].prod.vUnTrib,
            nfce.infNFe.det[index].prod.indTot,
            nfce.infNFe.det[index].prod.CEST
        ))

    insertXML(newlist)

############################

# print(nfce.infNFe.emit.CNPJ)

# print(nfce.infNFe.det[0].prod.cEAN)

# nfce.infNFe.det[0]

# print do nó inteiro em XML
# nfce.infNFe.emit.export(sys.stdout, 0)