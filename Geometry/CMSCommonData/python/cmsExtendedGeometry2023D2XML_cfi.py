import FWCore.ParameterSet.Config as cms

# This config was generated automatically using generate2023Geometry.py
# If you notice a mistake, please update the generating script, not just this config

XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring(
        'Geometry/CMSCommonData/data/materials.xml',
        'Geometry/CMSCommonData/data/rotations.xml',
        'Geometry/CMSCommonData/data/extend/cmsextent.xml',
        'Geometry/CMSCommonData/data/PostLS2/cms.xml',
        'Geometry/CMSCommonData/data/eta3/etaMax.xml',
        'Geometry/CMSCommonData/data/cmsMother.xml',
        'Geometry/CMSCommonData/data/cmsTracker.xml',
        'Geometry/CMSCommonData/data/PhaseII/caloBase.xml',
        'Geometry/CMSCommonData/data/cmsCalo.xml',
        'Geometry/CMSCommonData/data/PhaseII/muonBase.xml',
        'Geometry/CMSCommonData/data/cmsMuon.xml',
        'Geometry/CMSCommonData/data/mgnt.xml',
        'Geometry/CMSCommonData/data/PostLS2/beampipe.xml',
        'Geometry/CMSCommonData/data/PostLS2/cmsBeam.xml',
        'Geometry/CMSCommonData/data/muonMB.xml',
        'Geometry/CMSCommonData/data/muonMagnet.xml',
        'Geometry/CMSCommonData/data/cavern.xml',
        'Geometry/TrackerCommonData/data/PhaseII/trackerParameters.xml',
        'Geometry/TrackerCommonData/data/pixfwdCommon.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdMaterials.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdCylinder.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwd.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdDisks.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdInnerDisk1.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdInnerDisk2.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdInnerDisk3.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdInnerDisk4.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdInnerDisk5.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdInnerDisk6.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdInnerDisk7.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdOuterDisk1.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdOuterDisk2.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdOuterDisk3.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdOuterDisk4.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdOuterDisk5.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdOuterDisk6.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdOuterDisk7.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdOuterDisk8.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdOuterDisk9.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdOuterDisk10.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdblade1.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdblade2.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdblade3.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdblade4.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdblade5.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdblade6.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdblade7.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdblade8.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdblade9.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixfwdblade10.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarmaterial.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarladder.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarladderfull0.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarladderfull1.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarladderfull2.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarladderfull3.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer0.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer1.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer2.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer3.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/pixbar.xml',
        'Geometry/TrackerCommonData/data/trackermaterial.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/tracker.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/trackerbar.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/trackerfwd.xml',
        'Geometry/TrackerCommonData/data/PhaseII/FlatTracker/trackerStructureTopology.xml',
        'Geometry/TrackerSimData/data/PhaseII/FlatTracker/trackersens.xml',
        'Geometry/TrackerRecoData/data/PhaseII/FlatTracker/trackerRecoMaterial.xml',
        'Geometry/TrackerSimData/data/PhaseII/FlatTracker/trackerProdCuts.xml',
        'Geometry/TrackerSimData/data/trackerProdCutsBEAM.xml',
        'Geometry/EcalCommonData/data/PhaseII/ShortEE/eregalgo.xml',
        'Geometry/EcalCommonData/data/ebalgo.xml',
        'Geometry/EcalCommonData/data/ebcon.xml',
        'Geometry/EcalCommonData/data/ebrot.xml',
        'Geometry/EcalCommonData/data/eecon.xml',
        'Geometry/EcalCommonData/data/PhaseII/ShortEE/eefixed.xml',
        'Geometry/EcalCommonData/data/PhaseII/ShortEE/eehier.xml',
        'Geometry/EcalCommonData/data/eealgo.xml',
        'Geometry/EcalCommonData/data/escon.xml',
        'Geometry/EcalCommonData/data/esalgo.xml',
        'Geometry/EcalCommonData/data/eeF.xml',
        'Geometry/EcalCommonData/data/eeB.xml',
        'Geometry/EcalCommonData/data/ectkcable.xml',
        'Geometry/HcalCommonData/data/hcalrotations.xml',
        'Geometry/HcalCommonData/data/PhaseII/hcalalgo.xml',
        'Geometry/HcalCommonData/data/hcalcablealgo.xml',
        'Geometry/HcalCommonData/data/hcalbarrelalgo.xml',
        'Geometry/HcalCommonData/data/PhaseII/hcalendcapalgo.xml',
        'Geometry/HcalCommonData/data/hcalouteralgo.xml',
        'Geometry/HcalCommonData/data/hcalforwardalgo.xml',
        'Geometry/HcalCommonData/data/Run2/hcalSimNumbering16a.xml',
        'Geometry/HcalCommonData/data/Run2/hcalRecNumbering16a.xml',
        'Geometry/HcalCommonData/data/average/hcalforwardmaterial.xml',
        'Geometry/MuonCommonData/data/v1/mbCommon.xml',
        'Geometry/MuonCommonData/data/v1/mb1.xml',
        'Geometry/MuonCommonData/data/v1/mb2.xml',
        'Geometry/MuonCommonData/data/v1/mb3.xml',
        'Geometry/MuonCommonData/data/v1/mb4.xml',
        'Geometry/MuonCommonData/data/design/muonYoke.xml',
        'Geometry/MuonCommonData/data/PhaseII/mf.xml',
        'Geometry/MuonCommonData/data/PhaseII/rpcf.xml',
        'Geometry/MuonCommonData/data/PhaseII/gemf.xml',
        'Geometry/MuonCommonData/data/PhaseII/TDR_BaseLine/gem11.xml',
        'Geometry/MuonCommonData/data/PhaseII/TDR_BaseLine/gem21.xml',
        'Geometry/MuonCommonData/data/v2/csc.xml',
        'Geometry/MuonCommonData/data/PhaseII/mfshield.xml',
        'Geometry/MuonCommonData/data/PhaseII/TDR_BaseLine/me0.xml',
        'Geometry/ForwardCommonData/data/v2/forwardshield.xml',
        'Geometry/ForwardCommonData/data/brmrotations.xml',
        'Geometry/ForwardCommonData/data/PostLS2/brm.xml',
        'Geometry/ForwardCommonData/data/zdcmaterials.xml',
        'Geometry/ForwardCommonData/data/lumimaterials.xml',
        'Geometry/ForwardCommonData/data/zdcrotations.xml',
        'Geometry/ForwardCommonData/data/lumirotations.xml',
        'Geometry/ForwardCommonData/data/zdc.xml',
        'Geometry/ForwardCommonData/data/zdclumi.xml',
        'Geometry/ForwardCommonData/data/cmszdc.xml',
    )+
    cms.vstring(
        'Geometry/MuonCommonData/data/PhaseII/muonNumbering.xml',
        'Geometry/EcalSimData/data/ecalsens.xml',
        'Geometry/HcalCommonData/data/Phase0/hcalsenspmf.xml',
        'Geometry/HcalSimData/data/hf.xml',
        'Geometry/HcalSimData/data/hfpmt.xml',
        'Geometry/HcalSimData/data/hffibrebundle.xml',
        'Geometry/HcalSimData/data/CaloUtil.xml',
        'Geometry/MuonSimData/data/PhaseII/muonSens.xml',
        'Geometry/DTGeometryBuilder/data/dtSpecsFilter.xml',
        'Geometry/CSCGeometryBuilder/data/cscSpecsFilter.xml',
        'Geometry/CSCGeometryBuilder/data/cscSpecs.xml',
        'Geometry/RPCGeometryBuilder/data/PhaseII/RPCSpecs.xml',
        'Geometry/GEMGeometryBuilder/data/GEMSpecsFilter.xml',
        'Geometry/GEMGeometryBuilder/data/v5/GEMSpecs.xml',
        'Geometry/ForwardCommonData/data/brmsens.xml',
        'Geometry/ForwardSimData/data/zdcsens.xml',
        'Geometry/HcalSimData/data/HcalProdCuts.xml',
        'Geometry/EcalSimData/data/EcalProdCuts.xml',
        'Geometry/EcalSimData/data/ESProdCuts.xml',
        'Geometry/MuonSimData/data/PhaseII/muonProdCuts.xml',
        'Geometry/ForwardSimData/data/zdcProdCuts.xml',
        'Geometry/ForwardSimData/data/ForwardShieldProdCuts.xml',
        'Geometry/CMSCommonData/data/FieldParameters.xml',
    ),
    rootNodeName = cms.string('cms:OCMS')
)
