from nfelib.v4_00 import leiauteNFe_sub as parser
import mysql.connector
import os

# path = 'C:\\Users\\Avell\\Desktop\\tests'
# path = 'C:\\Users\\Avell\\Desktop\\nfce'
#
# for filename in os.listdir(path):
#     nfce = parser.parse('%s\\%s' % (path, filename))

# Manual path to test:
nfce = parser.parse('tests\\teste.xml')

    def insertXML(newlist):
        try:
            connection = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='xml')

            sql_insert_query = """ INSERT INTO `nfce022019` VALUES (NULL,%s,NULL,NULL,NULL,NULL,%s,NULL,%s,%s,%s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'RP_INFO_1.0.9.9',NULL,%s,'Goias Comercio De Cosmeticos Ltda',
            NULL,'Av. Central N. 577 Qd. 197 Lt. 03',577,'Setor Empresarial',5208707,'Goiania','GO',74583350,1058,'Brasil',
            6235866377,105620947,3,NULL,17871449000985,'Goias Comercio De Cosmeticos Ltda',NULL,'Rod. Br-040 Km 12 Gleba f Lojas 065/066',
            000,'Parque Esplanada 3',5221858,'Valparaiso De Goias','GO',72876902,1058,'Brasil',6136270180,1,105650323,NULL,%s,NULL,%s,
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NULL,NULL,NULL,0,20,3,41.6700,1.32,12.0000,
            0.16,NULL,NULL,49,0.00,0.0000,0.00,NULL,NULL,49,0.00,0.0000,0.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,
            NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,
            NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,
            NULL,NULL,NULL,NULL,NULL,NULL,NULL)"""
            #insert_tuple = (versao,Id,cUF,cNF,natOp,mod,serie,nNF,dhEmi,dhSaiEnt,tpNF,idDest,cMunFG,tpImp,tpEmis,
    #cDV,tpAmb,finnfce,indFinal,indPres, procEmi)
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
            nfce.infNFe.Id,
            nfce.infNFe.ide.cUF,
            nfce.infNFe.ide.cNF,
            nfce.infNFe.ide.natOp,
            nfce.infNFe.ide.mod,
            nfce.infNFe.ide.serie,
            nfce.infNFe.ide.nNF,
            nfce.infNFe.ide.dhEmi,
            nfce.infNFe.ide.dhSaiEnt,
            nfce.infNFe.ide.tpNF,
            nfce.infNFe.ide.idDest,
            nfce.infNFe.ide.cMunFG,
            nfce.infNFe.ide.tpImp,
            nfce.infNFe.ide.tpEmis,
            nfce.infNFe.ide.cDV,
            nfce.infNFe.ide.tpAmb,
            nfce.infNFe.ide.finnfce,
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
            nfce.infNFe.det[index].prod.indTot
        ))

    insertXML(newlist)


############################

# print(nfce.infNFe.emit.CNPJ)

# print(nfce.infNFe.det[0].prod.cEAN)

# nfce.infNFe.det[0]

# print do nó inteiro em XML
# nfce.infNFe.emit.export(sys.stdout, 0)