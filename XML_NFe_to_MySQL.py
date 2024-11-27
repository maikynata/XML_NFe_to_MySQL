from nfelib.v4_00 import leiauteNFe_sub as parser
import mysql.connector
import os

# path = 'D:\\goFisc\\teste'
path = 'C:\\Users\\Avell\\Desktop\\XML-2023\\122023'

for filename in os.listdir(path):
    nfe = parser.parse('%s\\%s' % (path, filename))

# Manual path to test:
# nfe = parser.parse('tests\\teste.xml')

    def insertXML(newlist):
        try:
            connection = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='bd_auditoria_2023')

            sql_insert_query = """ INSERT INTO `nfe122023` VALUES (NULL,%s,NULL,NULL,NULL,NULL,%s,NULL,%s,%s,%s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'bluesoft',NULL,%s,'Goias Comercio De Cosmeticos Ltda',
            NULL,'Av. Central N. 577 Qd. 197 Lt. 03',577,'Setor Empresarial',5208707,'Goiania','GO',74583350,1058,'Brasil',
            6235866377,105620947,3,NULL,17871449000985,'Goias Comercio De Cosmeticos Ltda',NULL,'Avenida Meia Ponte',
            000,'Santa Genoveva',5221858,'Goiania','GO',74670400,1058,'Brasil',6136270180,1,105650323,NULL,%s,NULL,%s,
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NULL,NULL,NULL,0,20,3,41.6700,1.32,12.0000,
            0.16,NULL,NULL,49,0.00,0.0000,0.00,NULL,NULL,49,0.00,0.0000,0.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,
            NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,
            NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,
            NULL,NULL,NULL,NULL,NULL,NULL,NULL)"""
            #insert_tuple = (versao,Id,cUF,cNF,natOp,mod,serie,nNF,dhEmi,dhSaiEnt,tpNF,idDest,cMunFG,tpImp,tpEmis,
    #cDV,tpAmb,finNFe,indFinal,indPres, procEmi)
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

    for index in range(len(nfe.infNFe.det)):
        newlist.append((
            nfe.infNFe.versao,
            nfe.infNFe.Id,
            nfe.infNFe.ide.cUF,
            nfe.infNFe.ide.cNF,
            nfe.infNFe.ide.natOp,
            nfe.infNFe.ide.mod,
            nfe.infNFe.ide.serie,
            nfe.infNFe.ide.nNF,
            nfe.infNFe.ide.dhEmi,
            nfe.infNFe.ide.dhSaiEnt,
            nfe.infNFe.ide.tpNF,
            nfe.infNFe.ide.idDest,
            nfe.infNFe.ide.cMunFG,
            nfe.infNFe.ide.tpImp,
            nfe.infNFe.ide.tpEmis,
            nfe.infNFe.ide.cDV,
            nfe.infNFe.ide.tpAmb,
            nfe.infNFe.ide.finNFe,
            nfe.infNFe.ide.indFinal,
            nfe.infNFe.ide.indPres,
            nfe.infNFe.ide.procEmi,
            nfe.infNFe.emit.CNPJ,
            nfe.infNFe.det[index].nItem,
            nfe.infNFe.det[index].prod.cProd,
            nfe.infNFe.det[index].prod.cEAN,
            nfe.infNFe.det[index].prod.xProd,
            nfe.infNFe.det[index].prod.NCM,
            nfe.infNFe.det[index].prod.CFOP,
            nfe.infNFe.det[index].prod.uCom,
            nfe.infNFe.det[index].prod.qCom,
            nfe.infNFe.det[index].prod.vUnCom,
            nfe.infNFe.det[index].prod.vProd,
            nfe.infNFe.det[index].prod.cEANTrib,
            nfe.infNFe.det[index].prod.uTrib,
            nfe.infNFe.det[index].prod.qTrib,
            nfe.infNFe.det[index].prod.vUnTrib,
            nfe.infNFe.det[index].prod.indTot
        ))

    insertXML(newlist)


############################

# print(nfe.infNFe.emit.CNPJ)

# print(nfe.infNFe.det[0].prod.cEAN)

# nfe.infNFe.det[0]

# print do nó inteiro em XML
# nfe.infNFe.emit.export(sys.stdout, 0)