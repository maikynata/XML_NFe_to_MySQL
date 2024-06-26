CREATE TABLE IF NOT EXISTS nfe022019 (
    `nfeProc` INT,
    `nfeProc_versao` NUMERIC(3, 2),
    `nfeProc_xmlns` VARCHAR(34) CHARACTER SET utf8,
    `nfeProc_NFe` INT,
    `nfeProc_NFe_infNFe` INT,
    `nfeProc_NFe_infNFe_versao` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_Id` VARCHAR(47) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_ide` INT,
    `nfeProc_NFe_infNFe_ide_cUF` INT,
    `nfeProc_NFe_infNFe_ide_cNF` INT,
    `nfeProc_NFe_infNFe_ide_natOp` VARCHAR(39) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_ide_mod` INT,
    `nfeProc_NFe_infNFe_ide_serie` INT,
    `nfeProc_NFe_infNFe_ide_nNF` INT,
    `nfeProc_NFe_infNFe_ide_dhEmi` VARCHAR(25) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_ide_dhSaiEnt` VARCHAR(25) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_ide_tpNF` INT,
    `nfeProc_NFe_infNFe_ide_idDest` INT,
    `nfeProc_NFe_infNFe_ide_cMunFG` INT,
    `nfeProc_NFe_infNFe_ide_tpImp` INT,
    `nfeProc_NFe_infNFe_ide_tpEmis` INT,
    `nfeProc_NFe_infNFe_ide_cDV` INT,
    `nfeProc_NFe_infNFe_ide_tpAmb` INT,
    `nfeProc_NFe_infNFe_ide_finNFe` INT,
    `nfeProc_NFe_infNFe_ide_indFinal` INT,
    `nfeProc_NFe_infNFe_ide_indPres` INT,
    `nfeProc_NFe_infNFe_ide_procEmi` INT,
    `nfeProc_NFe_infNFe_ide_verProc` VARCHAR(15) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_emit` INT,
    `nfeProc_NFe_infNFe_emit_CNPJ` VARCHAR(14) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_emit_xNome` VARCHAR(33) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_emit_enderEmit` INT,
    `nfeProc_NFe_infNFe_emit_enderEmit_xLgr` VARCHAR(33) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_emit_enderEmit_nro` INT,
    `nfeProc_NFe_infNFe_emit_enderEmit_xBairro` VARCHAR(17) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_emit_enderEmit_cMun` INT,
    `nfeProc_NFe_infNFe_emit_enderEmit_xMun` VARCHAR(7) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_emit_enderEmit_UF` VARCHAR(2) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_emit_enderEmit_CEP` INT,
    `nfeProc_NFe_infNFe_emit_enderEmit_cPais` INT,
    `nfeProc_NFe_infNFe_emit_enderEmit_xPais` VARCHAR(6) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_emit_enderEmit_fone` VARCHAR(12) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_emit_IE` INT,
    `nfeProc_NFe_infNFe_emit_CRT` INT,
    `nfeProc_NFe_infNFe_dest` INT,
    `nfeProc_NFe_infNFe_dest_CNPJ` VARCHAR(14) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_dest_xNome` VARCHAR(33) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_dest_enderDest` INT,
    `nfeProc_NFe_infNFe_dest_enderDest_xLgr` VARCHAR(39) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_dest_enderDest_nro` INT,
    `nfeProc_NFe_infNFe_dest_enderDest_xBairro` VARCHAR(18) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_dest_enderDest_cMun` INT,
    `nfeProc_NFe_infNFe_dest_enderDest_xMun` VARCHAR(19) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_dest_enderDest_UF` VARCHAR(2) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_dest_enderDest_CEP` INT,
    `nfeProc_NFe_infNFe_dest_enderDest_cPais` INT,
    `nfeProc_NFe_infNFe_dest_enderDest_xPais` VARCHAR(6) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_dest_enderDest_fone` VARCHAR(6) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_dest_indIEDest` INT,
    `nfeProc_NFe_infNFe_dest_IE` INT,
    `nfeProc_NFe_infNFe_det` INT,
    `nfeProc_NFe_infNFe_det_nItem` INT,
    `nfeProc_NFe_infNFe_det_prod` INT,
    `nfeProc_NFe_infNFe_det_prod_cProd` INT,
    `nfeProc_NFe_infNFe_det_prod_cEAN` VARCHAR(13) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_det_prod_xProd` VARCHAR(83) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_det_prod_NCM` INT,
    `nfeProc_NFe_infNFe_det_prod_CFOP` INT,
    `nfeProc_NFe_infNFe_det_prod_uCom` VARCHAR(2) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_det_prod_qCom` NUMERIC(15, 3),
    `nfeProc_NFe_infNFe_det_prod_vUnCom` NUMERIC(15, 10),
    `nfeProc_NFe_infNFe_det_prod_vProd` NUMERIC(15, 3),
    `nfeProc_NFe_infNFe_det_prod_cEANTrib` VARCHAR(13) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_det_prod_uTrib` VARCHAR(2) CHARACTER SET utf8,
    `nfeProc_NFe_infNFe_det_prod_qTrib` NUMERIC(15, 3),
    `nfeProc_NFe_infNFe_det_prod_vUnTrib` NUMERIC(15, 10),
    `nfeProc_NFe_infNFe_det_prod_indTot` INT,
    `nfeProc_NFe_infNFe_det_imposto` INT,
    `nfeProc_NFe_infNFe_det_imposto_ICMS` INT,
    `nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS20` INT,
    `nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS20_orig` INT,
    `nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS20_CST` INT,
    `nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS20_modBC` INT,
    `nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS20_pRedBC` NUMERIC(6, 4),
    `nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS20_vBC` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS20_pICMS` NUMERIC(6, 4),
    `nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS20_vICMS` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_det_imposto_PIS` INT,
    `nfeProc_NFe_infNFe_det_imposto_PIS_PISOutr` INT,
    `nfeProc_NFe_infNFe_det_imposto_PIS_PISOutr_CST` INT,
    `nfeProc_NFe_infNFe_det_imposto_PIS_PISOutr_vBC` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_det_imposto_PIS_PISOutr_pPIS` NUMERIC(5, 4),
    `nfeProc_NFe_infNFe_det_imposto_PIS_PISOutr_vPIS` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_det_imposto_COFINS` INT,
    `nfeProc_NFe_infNFe_det_imposto_COFINS_COFINSOutr` INT,
    `nfeProc_NFe_infNFe_det_imposto_COFINS_COFINSOutr_CST` INT,
    `nfeProc_NFe_infNFe_det_imposto_COFINS_COFINSOutr_vBC` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_det_imposto_COFINS_COFINSOutr_pCOFINS` NUMERIC(5, 4),
    `nfeProc_NFe_infNFe_det_imposto_COFINS_COFINSOutr_vCOFINS` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS00` INT,
    `nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS00_orig` INT,
    `nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS00_CST` INT,
    `nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS00_modBC` INT,
    `nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS00_vBC` NUMERIC(5, 2),
    `nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS00_pICMS` NUMERIC(6, 4),
    `nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS00_vICMS` NUMERIC(4, 2),
    `nfeProc_NFe_infNFe_det_prod_CEST` INT,
    `nfeProc_NFe_infNFe_total` INT,
    `nfeProc_NFe_infNFe_total_ICMSTot` INT,
    `nfeProc_NFe_infNFe_total_ICMSTot_vBC` NUMERIC(6, 2),
    `nfeProc_NFe_infNFe_total_ICMSTot_vICMS` NUMERIC(6, 2),
    `nfeProc_NFe_infNFe_total_ICMSTot_vICMSDeson` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_total_ICMSTot_vFCP` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_total_ICMSTot_vBCST` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_total_ICMSTot_vST` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_total_ICMSTot_vFCPST` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_total_ICMSTot_vFCPSTRet` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_total_ICMSTot_vProd` NUMERIC(6, 2),
    `nfeProc_NFe_infNFe_total_ICMSTot_vFrete` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_total_ICMSTot_vSeg` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_total_ICMSTot_vDesc` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_total_ICMSTot_vII` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_total_ICMSTot_vIPI` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_total_ICMSTot_vIPIDevol` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_total_ICMSTot_vPIS` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_total_ICMSTot_vCOFINS` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_total_ICMSTot_vOutro` NUMERIC(3, 2),
    `nfeProc_NFe_infNFe_total_ICMSTot_vNF` NUMERIC(6, 2),
    `nfeProc_NFe_infNFe_transp` INT,
    `nfeProc_NFe_infNFe_transp_modFrete` INT,
    `nfeProc_NFe_infNFe_transp_vol` INT,
    `nfeProc_NFe_infNFe_transp_vol_qVol` INT,
    `nfeProc_NFe_infNFe_transp_vol_pesoL` NUMERIC(5, 3),
    `nfeProc_NFe_infNFe_transp_vol_pesoB` NUMERIC(6, 3),
    `nfeProc_NFe_infNFe_pag` INT,
    `nfeProc_NFe_infNFe_pag_detPag` INT,
    `nfeProc_NFe_infNFe_pag_detPag_tPag` INT,
    `nfeProc_NFe_infNFe_pag_detPag_vPag` NUMERIC(6, 2),
    `nfeProc_NFe_infNFe_compra` INT,
    `nfeProc_NFe_infNFe_compra_xPed` INT,
    `nfeProc_NFe_Signature` INT,
    `nfeProc_NFe_Signature_xmlns` VARCHAR(34) CHARACTER SET utf8,
    `nfeProc_NFe_Signature_SignedInfo` INT,
    `nfeProc_NFe_Signature_SignedInfo_CanonicalizationMethod` INT,
    `NFe_Signature_SignedInfo_CanonicalizationMethod_Algorithm` VARCHAR(47) CHARACTER SET utf8,
    `nfeProc_NFe_Signature_SignedInfo_SignatureMethod` INT,
    `nfeProc_NFe_Signature_SignedInfo_SignatureMethod_Algorithm` VARCHAR(42) CHARACTER SET utf8,
    `nfeProc_NFe_Signature_SignedInfo_Reference` INT,
    `nfeProc_NFe_Signature_SignedInfo_Reference_URI` VARCHAR(48) CHARACTER SET utf8,
    `nfeProc_NFe_Signature_SignedInfo_Reference_Transforms` INT,
    `nfeProc_NFe_Signature_SignedInfo_Reference_Transforms_Transform` INT,
    `Signature_SignedInfo_Reference_Transforms_Transform_Algorithm` VARCHAR(53) CHARACTER SET utf8,
    `nfeProc_NFe_Signature_SignedInfo_Reference_DigestMethod` INT,
    `NFe_Signature_SignedInfo_Reference_DigestMethod_Algorithm` VARCHAR(38) CHARACTER SET utf8,
    `nfeProc_NFe_Signature_SignedInfo_Reference_DigestValue` VARCHAR(28) CHARACTER SET utf8,
    `nfeProc_NFe_Signature_SignatureValue` VARCHAR(344) CHARACTER SET utf8,
    `nfeProc_NFe_Signature_KeyInfo` INT,
    `nfeProc_NFe_Signature_KeyInfo_X509Data` INT,
    `nfeProc_NFe_Signature_KeyInfo_X509Data_X509Certificate` VARCHAR(2648) CHARACTER SET utf8,
    `nfeProc_protNFe` INT,
    `nfeProc_protNFe_versao` NUMERIC(3, 2),
    `nfeProc_protNFe_infProt` INT,
    `nfeProc_protNFe_infProt_Id` VARCHAR(17) CHARACTER SET utf8,
    `nfeProc_protNFe_infProt_tpAmb` INT,
    `nfeProc_protNFe_infProt_verAplic` VARCHAR(5) CHARACTER SET utf8,
    `nfeProc_protNFe_infProt_chNFe` INT,
    `nfeProc_protNFe_infProt_dhRecbto` VARCHAR(25) CHARACTER SET utf8,
    `nfeProc_protNFe_infProt_nProt` INT,
    `nfeProc_protNFe_infProt_digVal` VARCHAR(28) CHARACTER SET utf8,
    `nfeProc_protNFe_infProt_cStat` INT,
    `nfeProc_protNFe_infProt_xMotivo` VARCHAR(24) CHARACTER SET utf8
);