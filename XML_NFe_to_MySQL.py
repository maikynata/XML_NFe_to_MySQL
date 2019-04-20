from nfelib.v4_00 import leiauteNFe_sub as parser
import mysql.connector

nfe = parser.parse('tests\\novo.xml')

def insertXML(versao,Id,cUF,cNF,natOp,mod,serie,nNF,dhEmi,dhSaiEnt,tpNF,idDest,cMunFG,tpImp,tpEmis,
cDV,tpAmb,finNFe,indFinal,indPres, procEmi):
    try:
        connection = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='test')

        cursor = connection.cursor(prepared=True)

        sql_insert_query = """ INSERT INTO `teste` VALUES (NULL,%s,NULL,NULL,NULL,NULL,%s,NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'RP_INFO_1.0.2.0',NULL,17871449000128,'Goias Comercio De Cosmeticos Ltda',NULL,'Av. Central N. 577 Qd. 197 Lt. 03',577,'Setor Empresarial',5208707,'Goiania','GO',74583350,1058,'Brasil',6235866377,105620947,3,NULL,17871449000985,'Goias Comercio De Cosmeticos Ltda',NULL,'Rod. Br-040 Km 12 Gleba f Lojas 065/066',000,'Parque Esplanada 3',5221858,'Valparaiso De Goias','GO',72876902,1058,'Brasil',6136270180,1,105650323,NULL,1,NULL,162442,'7896007540631','Absorvente 8 Un Normal Com Abas Seca Intimus Gel UN',96190000,5152,'UN',1.0000,2.2700000000,2.27,'7896007540631','UN',1.0000,2.2700000000,1,NULL,NULL,NULL,0,20,3,41.6700,1.32,12.0000,0.16,NULL,NULL,49,0.00,0.0000,0.00,NULL,NULL,49,0.00,0.0000,0.00,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL)"""
        insert_tuple = (versao,Id,cUF,cNF,natOp,mod,serie,nNF,dhEmi,dhSaiEnt,tpNF,idDest,cMunFG,tpImp,tpEmis,
cDV,tpAmb,finNFe,indFinal,indPres, procEmi)

        cursor.execute(sql_insert_query, insert_tuple)
        connection.commit()
        print ("The XML was inserted successfully into teste table")
    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed to insert the XML into MySQL table {}".format(error))
    finally:
        # Close the database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertXML(nfe.infNFe.versao,
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
    nfe.infNFe.ide.procEmi)

############################

# print(nfe.infNFe.emit.CNPJ)

# print(nfe.infNFe.det[0].prod.cEAN)

# nfe.infNFe.det[0]

# print do nó inteiro
# nfe.infNFe.emit.export(sys.stdout, 0)