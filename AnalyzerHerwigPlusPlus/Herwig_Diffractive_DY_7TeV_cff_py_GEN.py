# Auto generated configuration file
# using: 
# Revision: 1.381.2.2 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: GenLevelAnalyzer/AnalyzerHerwigPlusPlus/python/Herwig_Diffractive_7TeV_cff.py --step GEN --conditions auto:mc --pileup NoPileUp --eventcontent RAWSIM --datatier GEN-SIM -n 500 --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(500)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('\\$Revision: 1.0 $'),
    annotation = cms.untracked.string('Process: (Z->ll), l=e or mu'),
    name = cms.untracked.string('\\$Source: Herwig_Diffractive_UE_7TeV_cff.py,v $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('Herwig_Diffractive_DY_7TeV_cff_py_GEN.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.GlobalTag.globaltag = 'MC_53_V6::All'

process.generator = cms.EDFilter("ThePEGGeneratorFilter",
    ue_2_3 = cms.vstring('cd /Herwig/UnderlyingEvent', 
        'set KtCut:MinKT 4.0', 
        'set UECuts:MHatMin 8.0', 
        'set MPIHandler:InvRadius 1.5', 
        'cd /'),
    pdfMRST2001 = cms.vstring('cd /Herwig/Partons', 
        'create Herwig::MRST MRST2001 HwMRST.so', 
        'setup MRST2001 ${HERWIGPATH}/PDF/mrst/2001/lo2002.dat', 
        'set MRST2001:RemnantHandler HadronRemnants', 
        'cp MRST2001 cmsPDFSet', 
        'cd /'),
    ue_2_4 = cms.vstring('cd /Herwig/UnderlyingEvent', 
        'set KtCut:MinKT 4.3', 
        'set UECuts:MHatMin 8.6', 
        'set MPIHandler:InvRadius 1.2', 
        'cd /'),
    cm7TeV = cms.vstring('set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 7000.0', 
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.0*GeV'),
    diffractiveDefaults = cms.vstring('cd /Herwig/Partons', 
        '# Set the PDFs for the beams', 
        '# This is for double diffractive, comment out either the first or second', 
        '# for single diffractive', 
        'set QCDExtractor:FirstPDF  PomeronFlux', 
        'set QCDExtractor:SecondPDF PomeronFlux', 
        '## Reggeon Structure Function #################################', 
        '# MUST HAVE LHAPDF linked with ThePEG', 
        '#create ThePEG::LHAPDF PionPDF ThePEGLHAPDF.so', 
        '#set PionPDF:PDFNumber 212', 
        '#set PionPDF:PType PionOrVMD', 
        '#set PionPDF:RangeException Freeze', 
        '#create ThePEG::SoftRemnantHandler PionRemnants', 
        '#set PionRemnants:RemnantDecayer RemnantDecayer', 
        '#set PionPDF:RemnantHandler /Herwig/Partons/PionRemnants', 
        '#create Herwig::ReggeonPDF ReggeonPDF HwReggeonPDF.so', 
        '#set ReggeonPDF:PDF PionPDF', 
        '#set ReggeonPDF:RemnantHandler PionRemnants', 
        '#set /Herwig/Particles/reggeon:PDF ReggeonPDF# uncomment to switch pomeron off if only reggeon required', 
        '#set /Herwig/Particles/pomeron:PDF NULL', 
        '#Phase-space Generation for PDFs', 
        'set QCDExtractor:FlatSHatY 0', 
        '#  Cuts', 
        'cd /Herwig/Cuts', 
        'set QCDCuts:MHatMin 1.', 
        'set QCDCuts:MHatMax 20000', 
        'set QCDCuts:X2Min 1.0e-7', 
        'set QCDCuts:X2Max 1.', 
        'set QCDCuts:X1Min 1.0e-7', 
        'set QCDCuts:X1Max 1.', 
        'set JetKtCut:MinKT 10.', 
        'set LeptonKtCut:MinKT 1.', 
        '##################################################', 
        '# Matrix Elements for diffractive collisions', 
        '# (by default on QCD 2->2 switched on)', 
        '##################################################', 
        'cd /Herwig/MatrixElements/', 
        '# QCD 2->2', 
        '#insert SimpleQCD:MatrixElements[0] /Herwig/UnderlyingEvent/MEQCD2to2Fast', 
        '# Z Boson', 
        'insert SimpleQCD:MatrixElements[0] MEqq2gZ2ff', 
        'cd /Herwig/Generators', 
        '# MPI does not work', 
        'set LHCGenerator:EventHandler:CascadeHandler:MPIHandler NULL'),
    powhegDefaults = cms.vstring('#  Need to use an NLO PDF', 
        '#  and strong coupling', 
        'cp /Herwig/Partons/MRST-NLO /Herwig/Partons/cmsPDFSet', 
        'create Herwig::O2AlphaS O2AlphaS', 
        'set /Herwig/Generators/LHCGenerator:StandardModelParameters:QCD/RunningAlphaS O2AlphaS', 
        '#  Setup the POWHEG shower', 
        'cd /Herwig/Shower', 
        'set Evolver:HardEmissionMode POWHEG', 
        '# higgs + W (N.B. if considering all W decay modes useful to set )', 
        '#           (jet pT cut to zero so no cut on W decay products    )', 
        '# insert SimpleQCD:MatrixElements[0] PowhegMEPP2WH', 
        '# set /Herwig/Cuts/JetKtCut:MinKT 0.0*GeV', 
        '# higgs + Z (N.B. if considering all Z decay modes useful to set )', 
        '#           (jet pT cut to zero so no cut on Z decay products    )', 
        '# insert SimpleQCD:MatrixElements[0] PowhegMEPP2ZH', 
        '# set /Herwig/Cuts/JetKtCut:MinKT 0.0*GeV', 
        '# gg/qqbar -> Higgs', 
        '# insert SimpleQCD:MatrixElements[0] PowhegMEHiggs', 
        '# Weak boson pair production: WW / ZZ / WZ / W+Z [WpZ] / W-Z [WmZ]', 
        '# insert SimpleQCD:MatrixElements[0] PowhegMEPP2VV', 
        '# set PowhegMEPP2VV:Process WpZ'),
    reweightConstant = cms.vstring('mkdir /Herwig/Weights', 
        'cd /Herwig/Weights', 
        'create ThePEG::ReweightConstant reweightConstant ReweightConstant.so', 
        'cd /', 
        'set /Herwig/Weights/reweightConstant:C 1', 
        'insert SimpleQCD:Reweights[0] /Herwig/Weights/reweightConstant'),
    lheDefaultPDFs = cms.vstring('cd /Herwig/EventHandlers', 
        'set LHEReader:PDFA /cmsPDFSet', 
        'set LHEReader:PDFB /cmsPDFSet', 
        'cd /'),
    lheDefaults = cms.vstring('cd /Herwig/Cuts', 
        'create ThePEG::Cuts NoCuts', 
        'cd /Herwig/EventHandlers', 
        'create ThePEG::LesHouchesInterface LHEReader', 
        'set LHEReader:Cuts /Herwig/Cuts/NoCuts', 
        'create ThePEG::LesHouchesEventHandler LHEHandler', 
        'set LHEHandler:WeightOption VarWeight', 
        'set LHEHandler:PartonExtractor /Herwig/Partons/QCDExtractor', 
        'set LHEHandler:CascadeHandler /Herwig/Shower/ShowerHandler', 
        'set LHEHandler:HadronizationHandler /Herwig/Hadronization/ClusterHadHandler', 
        'set LHEHandler:DecayHandler /Herwig/Decays/DecayHandler', 
        'insert LHEHandler:LesHouchesReaders 0 LHEReader', 
        'cd /Herwig/Generators', 
        'set LHCGenerator:EventHandler /Herwig/EventHandlers/LHEHandler', 
        'cd /Herwig/Shower', 
        'set Evolver:HardVetoScaleSource Read', 
        'set Evolver:MECorrMode No', 
        'cd /'),
    cmsDefaults = cms.vstring('+pdfMRST2001', 
        '+cm7TeV', 
        '+ue_2_3', 
        '+basicSetup', 
        '+setParticlesStableForDetector'),
    pdfMRST2008LOss = cms.vstring('cp /Herwig/Partons/MRST /Herwig/Partons/cmsPDFSet'),
    generatorModule = cms.string('/Herwig/Generators/LHCGenerator'),
    basicSetup = cms.vstring('cd /Herwig/Generators', 
        'create ThePEG::RandomEngineGlue /Herwig/RandomGlue', 
        'set LHCGenerator:RandomNumberGenerator /Herwig/RandomGlue', 
        'set LHCGenerator:NumberOfEvents 10000000', 
        'set LHCGenerator:DebugLevel 1', 
        'set LHCGenerator:PrintEvent 0', 
        'set LHCGenerator:MaxErrors 10000', 
        'cd /Herwig/Particles', 
        'set K0:Width 1e300*GeV', 
        'set Kbar0:Width 1e300*GeV', 
        'cd /'),
    run = cms.string('LHC'),
    repository = cms.string('HerwigDefaults.rpo'),
    cm14TeV = cms.vstring('set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 14000.0', 
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.2*GeV'),
    dataLocation = cms.string('${HERWIGPATH}'),
    pdfCTEQ5L = cms.vstring('cd /Herwig/Partons', 
        'create ThePEG::LHAPDF CTEQ5L ThePEGLHAPDF.so', 
        'set CTEQ5L:PDFName cteq5l.LHgrid', 
        'set CTEQ5L:RemnantHandler HadronRemnants', 
        'cp CTEQ5L cmsPDFSet', 
        'cd /'),
    setParticlesStableForDetector = cms.vstring('cd /Herwig/Particles', 
        'set mu-:Stable Stable', 
        'set mu+:Stable Stable', 
        'set Sigma-:Stable Stable', 
        'set Sigmabar+:Stable Stable', 
        'set Lambda0:Stable Stable', 
        'set Lambdabar0:Stable Stable', 
        'set Sigma+:Stable Stable', 
        'set Sigmabar-:Stable Stable', 
        'set Xi-:Stable Stable', 
        'set Xibar+:Stable Stable', 
        'set Xi0:Stable Stable', 
        'set Xibar0:Stable Stable', 
        'set Omega-:Stable Stable', 
        'set Omegabar+:Stable Stable', 
        'set pi+:Stable Stable', 
        'set pi-:Stable Stable', 
        'set K+:Stable Stable', 
        'set K-:Stable Stable', 
        'set K_S0:Stable Stable', 
        'set K_L0:Stable Stable', 
        'cd /'),
    reweightPthat = cms.vstring('mkdir /Herwig/Weights', 
        'cd /Herwig/Weights', 
        'create ThePEG::ReweightMinPT reweightMinPT ReweightMinPT.so', 
        'cd /', 
        'set /Herwig/Weights/reweightMinPT:Power 4.5', 
        'set /Herwig/Weights/reweightMinPT:Scale 15*GeV', 
        'insert SimpleQCD:Reweights[0] /Herwig/Weights/reweightMinPT'),
    cm10TeV = cms.vstring('set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 10000.0', 
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.1*GeV'),
    cm8TeV = cms.vstring('set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 8000.0', 
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.0*GeV'),
    pdfCTEQ6L1 = cms.vstring('cd /Herwig/Partons', 
        'create ThePEG::LHAPDF CTEQ6L1 ThePEGLHAPDF.so', 
        'set CTEQ6L1:PDFName cteq6ll.LHpdf', 
        'set CTEQ6L1:RemnantHandler HadronRemnants', 
        'cp CTEQ6L1 cmsPDFSet', 
        'cd /'),
    eventHandlers = cms.string('/Herwig/EventHandlers'),
    configFiles = cms.vstring(),
    crossSection = cms.untracked.double(1.0),
    parameterSets = cms.vstring('cm7TeV', 
        'basicSetup', 
        'powhegDefaults', 
        'diffractiveDefaults', 
        'setParticlesStableForDetector'),
    filterEfficiency = cms.untracked.double(1.0)
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

