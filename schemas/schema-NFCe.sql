CREATE TABLE IF NOT EXISTS nfce (
    `nfce_versao` NUMERIC(3, 2),
    `nfce_Id` VARCHAR(47) CHARACTER SET utf8,
    `nfce_ide_cUF` INT,
    `nfce_ide_cNF` INT,
    `nfce_ide_natOp` VARCHAR(20) CHARACTER SET utf8,
    `nfce_ide_mod` INT,
    `nfce_ide_serie` INT,
    `nfce_ide_nNF` INT,
    `nfce_ide_dhEmi` VARCHAR(25) CHARACTER SET utf8,
    `nfce_ide_tpNF` INT,
    `nfce_ide_idDest` INT,
    `nfce_ide_cMunFG` INT,
    `nfce_ide_tpImp` INT,
    `nfce_ide_tpEmis` INT,
    `nfce_ide_cDV` INT,
    `nfce_ide_tpAmb` INT,
    `nfce_ide_finNFe` INT,
    `nfce_ide_indFinal` INT,
    `nfce_ide_indPres` INT,
    `nfce_ide_procEmi` INT,
	`nfce_emit_CNPJ` INT,
    `nfce_emit_xNome` VARCHAR(33) CHARACTER SET utf8,
    `nfce_emit_xFant` VARCHAR(29) CHARACTER SET utf8,
    `nfce_emit_enderEmit` INT,
    `nfce_emit_enderEmit_xLgr` VARCHAR(5) CHARACTER SET utf8,
    `nfce_emit_enderEmit_nro` INT,
    `nfce_emit_enderEmit_xBairro` VARCHAR(13) CHARACTER SET utf8,
    `nfce_emit_enderEmit_cMun` INT,
    `nfce_emit_enderEmit_xMun` VARCHAR(7) CHARACTER SET utf8,
    `nfce_emit_enderEmit_UF` VARCHAR(2) CHARACTER SET utf8,
    `nfce_emit_enderEmit_CEP` INT,
    `nfce_emit_enderEmit_cPais` INT,
    `nfce_emit_enderEmit_xPais` VARCHAR(6) CHARACTER SET utf8,
    `nfce_emit_enderEmit_fone` INT,
    `nfce_emit_IE` INT,
    `nfce_emit_CRT` INT,
    `nfce_det_nItem` INT,
    `nfce_det_prod_cProd` INT,
    `nfce_det_prod_cEAN` INT,
    `nfce_det_prod_xProd` VARCHAR(20) CHARACTER SET utf8,
    `nfce_det_prod_NCM` INT,
    `nfce_det_prod_CFOP` INT,
    `nfce_det_prod_uCom` VARCHAR(2) CHARACTER SET utf8,
    `nfce_det_prod_qCom` NUMERIC(5, 4),
    `nfce_det_prod_vUnCom` NUMERIC(12, 10),
    `nfce_det_prod_vProd` NUMERIC(4, 2),
    `nfce_det_prod_cEANTrib` INT,
    `nfce_det_prod_uTrib` VARCHAR(2) CHARACTER SET utf8,
    `nfce_det_prod_qTrib` NUMERIC(5, 4),
    `nfce_det_prod_vUnTrib` NUMERIC(12, 10),
    `nfce_det_prod_indTot` INT,
    `nfce_det_prod_CEST` INT
);