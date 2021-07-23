OPTION, ECHO=FALSE;
 OPTION, INFO=FALSE;
		OPTION, STATDUMPFREQ = 10;
	OPTION, PSDUMPFREQ = 300000000;
OPTION, AUTOPHASE=4;
		Option, VERSION=20200;
Option, ENABLEHDF5=TRUE;
 
Title, string="LCLS2";

REAL rf_freq         	     = 187.0e6;
        REAL n_particles             = 5e4;
            REAL beam_bunch_charge       = 100.0*1e-12;
    REAL beam_current            = rf_freq*beam_bunch_charge*1e6;

REAL Edes    = 1.4e-9;
REAL gamma   = (Edes+EMASS)/EMASS;
REAL beta    = sqrt(1-(1/gamma^2));
REAL P0      = gamma*beta*EMASS;

value , {Edes, P0};
 					
REAL deg=PI/180.0;

GUN:    RFCavity, L = 0.199, VOLT = 20.0, , TYPE = "STANDING",        FMAPFN = "../../fieldmaps/rfgunb_187MHz.txt",        FREQ = 187.0, LAG = 8.5*deg;

BUNCHER:    RFCavity, L = 0.358, VOLT = 1.8, Z = 0.809116, TYPE = "STANDING",            FMAPFN = "../../fieldmaps/rfgunb_buncher.txt",            FREQ = 1300.0, LAG = -88.5*deg;

SOLBF:  Solenoid, L = 0.48, ELEMEDGE= -0.062, KS = 0.0,        FMAPFN = "/fieldmaps/rfgunb_bucking.txt";

SOL1:   Solenoid, L = 0.48, Z = 0.24653, KS = 0.056,        FMAPFN = "../../fieldmaps/rfgunb_solenoid.txt";

SOL2:   Solenoid, L = 0.48, Z = 1.64581, KS = 0.03,        FMAPFN = "../../fieldmaps/rfgunb_solenoid.txt";

EIC:  Line = (GUN, SOL1, BUNCHER, SOL2);

REAL lcav = 1.3836;

REAL d1 = 3.3428;
REAL d2 = d1 + lcav;
REAL d3 = d2 + lcav;
REAL d4 = d3 + lcav;
REAL d5 = d4 + lcav;
REAL d6 = d5 + lcav;
REAL d7 = d6 + lcav;
REAL d8 = d7 + lcav;
REAL deg = PI/180.0;

C1: RFCavity, L = 1.3836, VOLT = 11.0, Z = 3.3428, TYPE = "STANDING",    FMAPFN = "../../fieldmaps/L0B_9cell.txt",    FREQ = 1.3e3, LAG = 8*deg;

C2: RFCavity, L = 1.3836, VOLT = 1.0E-5, Z = 4.7264, TYPE = "STANDING",    FMAPFN = "../../fieldmaps/L0B_9cell.txt",    FREQ = 1.3e3, LAG = -9.0*deg;

C3: RFCavity, L = 1.3836, VOLT = 26.0, Z = 6.11, TYPE = "STANDING",    FMAPFN = "../../fieldmaps/L0B_9cell.txt",    FREQ = 1.3e3, LAG = -20.0*deg;

C4: RFCavity, L = 1.3836, VOLT = 24.0, Z = 7.4936, TYPE = "STANDING",    FMAPFN = "../../fieldmaps/L0B_9cell.txt",    FREQ = 1.3e3, LAG = -18.0*deg;

C5: RFCavity, L = 1.3836, VOLT = 32.0, Z = 8.8772, TYPE = "STANDING",    FMAPFN = "../../fieldmaps/L0B_9cell.txt",    FREQ = 1.3e3, LAG = 0.0*deg;

C6: RFCavity, L = 1.3836, VOLT = 32.0, Z = 10.2608, TYPE = "STANDING",    FMAPFN = "../../fieldmaps/L0B_9cell.txt",    FREQ = 1.3e3, LAG = 0.0*deg;

C7: RFCavity, L = 1.3836, VOLT = 32.0, Z = 11.6444, TYPE = "STANDING",    FMAPFN = "../../fieldmaps/L0B_9cell.txt",    FREQ = 1.3e3, LAG = 0.0*deg;

C8: RFCavity, L = 1.3836, VOLT = 32.0, Z = 13.028, TYPE = "STANDING",    FMAPFN = "../../fieldmaps/L0B_9cell.txt",    FREQ = 1.3e3, LAG = -20.0*deg;

CM1:  Line = (C1,C2,C3,C4,C5,C6,C7,C8);

DR1: DRIFT, L = 5.0, Z = 13.0;
 
Col:ECOLLIMATOR, L=15.0, , XSIZE=30E-3,    YSIZE=30E-3, OUTFN="col.h5";

SC_INJ:  Line = (Col, EIC, CM1, DR1);

Dist:DISTRIBUTION, TYPE = FROMFILE,                   FNAME = "opal_50k.txt",                   EMITTED = TRUE,                   EMISSIONMODEL = NONE,                   EMISSIONSTEPS = 100,                   EKIN=0;

FS_SC: Fieldsolver, FSTYPE = FFT,                     MX = 32, MY = 32, MT = 32,		            PARFFTX = false, 		            PARFFTY = false, 		            PARFFTT = true,		            BCFFTX = open, 		            BCFFTY = open, 		            BCFFTT = open,		            BBOXINCR = 1, 		            GREENSF = INTEGRATED;

BEAM1: BEAM, PARTICLE = ELECTRON,       pc = P0, NPART = n_particles, BFREQ = rf_freq,       BCURRENT = beam_current, CHARGE = -1;

TRACK, LINE = SC_INJ, BEAM = BEAM1, MAXSTEPS = 1900000, DT = {5.0e-13, 5.0e-12}, ZSTOP={0.2, 15.0};
RUN, METHOD = "PARALLEL-T", BEAM = BEAM1, FIELDSOLVER = FS_SC, DISTRIBUTION = Dist;
ENDTRACK;

Stop;
 Quit;

