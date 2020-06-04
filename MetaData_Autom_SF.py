""" This code File automates the Meta Data Update Process """

# Importing Required Modules
import xml.etree.ElementTree as ET
from datetime import date

# Input and Output Path Declaration
InputPath = "/Users/deepak/Documents/GRA/Meta Data Automation/Test Files/Washington DC/AAHTrailPt/"
InputFileName = "AAHTrailPt.shp.xml"

OutputFileName = InputPath + "Updatedn" + "_" + InputFileName

# --------------------- Declaring Variables to be Updated in respective Tabs ---------------------

# Tab 1. Identification Info
county = "Arlington County"  # Specify the County or City for which the Meta data is being updated
StateAbb = "VA"  # State Abbreviation
StateFF = "Virginia"  # State Full form
Year = "2009"  # Year in which the Meta Data was created/Updated
CD_Obtained_Date = "2011"  # The year in which the Dataset was copied from the CD

pubdate = Year
ID_title = "Enter Title here" + "," + " " + county + "," + " " + StateAbb + " " + Year
ID_accconst = "None, Please see 'Distribution Info' for details"
ID_abstract = "This dataset represents the County Parks in" + " " + county + "," + " " + StateAbb + " " + Year
ID_purpose = "This dataset is intended for researchers, students, and policy makers for reference and mapping " \
             "purposes,and may be used for basic applications such as viewing, querying, and map output production, " \
             "or to provide a base map to support graphical overlays and analysis with other spatial data "
ID_useconst = "None. Users are advised to read the data set's metadata thoroughly to understand appropriate use and " \
              "data limitations. "

# Contact Info
ID_cntorg = "Arlington County DES GIS Mapping Center"
ID_cntper = ""
ID_cntpos = "Cartographer"
ID_cntvoice = "703-993-2240"
ID_addrtype = "mailing and physical"
ID_address = "2100 Clarendon Blvd Suite 813"
ID_city = "Arlington"
ID_state = "VA"
ID_postal = "22201"
ID_cntemail = "gismc@arlingtonva.us"

# Theme Keywords
MainKeyword = "Recreation"
Keyword1 = "Parks"
Keyword2 = "Public"
# Tab 2.Data Quality
DQ_attraccr = "No formal attribute accuracy tests were conducted"
DQ_logic = "No formal logical accuracy tests were conducted"
DQ_complete = "Data set is considered complete for the information presented, as described in the abstract. Users " \
              "are advised to read the rest of the metadata record carefully for additional details "
DQ_horizpar = "A formal accuracy assessment of the horizontal positional information in the data set has either not " \
              "been conducted, or is not applicable. "
DQ_vertaccr = "A formal accuracy assessment of the vertical positional information in the data set has either not " \
              "been conducted, or is not applicable "
DQ_procdesc = "Dataset copied from the cd obtained from" + " " + county + "," + " " + StateAbb + " " + CD_Obtained_Date
DQ_procdate = "Unknown"

# Tab 3 and 4 Have to be updated Manually

# Tab 5. Distribution Info
# For Tab 5 the duplicate Variables are not declared here; rather it is declared in Tab 6 below
DI_distliab = "Distributor assumes no liability for misuse of data."
DI_fees = "None. No fees are applicable for obtaining the data set"

# Tab 6. Meta Info
MI_cntorg = "George Mason University Libraries"
MI_cntper = "Digital Scholarship Center"
MI_cntvoice = "703-993-2240"
MI_cntemail = "datahelp@gmu.edu"
MI_addrtype = "mailing and physical"
MI_address = "4400 University Drive"
MI_city = "Fairfax"
MI_state = "VA"
MI_postal = "22030"
MI_metstdn = "FGDC Content Standards for Digital Geospatial Metadata"
MI_metstdv = "FGDC-STD-001-1998"

today = date.today()  # Getting Current Date
Date = today.strftime("%Y%m%d")  # Converting Date time to string in Y-m-d format
MI_metd = Date  # Assinging the current date to variables

# --------------------------- Main Code body Starts here   ---------------------------

tree = ET.parse(InputPath + InputFileName)
root = tree.getroot()

for child in root:
    print(child.tag)

# Tab 1:Identification Info #todo add exception handling
tree.find('idinfo/citation/citeinfo/title').text = ID_title
tree.find('idinfo/citation/citeinfo/pubdate').text = pubdate
tree.find('idinfo/accconst').text = ID_accconst
tree.find('idinfo/useconst').text = ID_useconst
tree.find('idinfo/descript/abstract').text = ID_abstract
tree.find('idinfo/descript/purpose').text = ID_purpose

POC = tree.find('idinfo/ptcontac')
for child in list(POC):
    POC.remove(child)

ptcontac = tree.find('idinfo/ptcontac')
cntinfo = ET.SubElement(ptcontac, 'cntinfo')
cntorgp = ET.SubElement(cntinfo, 'cntorgp')
cntorg = ET.SubElement(cntorgp, 'cntorg')
cntper = ET.SubElement(cntorgp, 'cntper')
cntorg.text = ID_cntorg
cntper.text = ID_cntper
cntpos = ET.SubElement(cntinfo, 'cntpos')
cntpos.text = ID_cntpos
cntaddr = ET.SubElement(cntinfo, 'cntaddr')
addrtype = ET.SubElement(cntinfo, 'addrtype')
address = ET.SubElement(cntinfo, 'address')
city = ET.SubElement(cntinfo, 'city')
state = ET.SubElement(cntinfo, 'state')
postal = ET.SubElement(cntinfo, 'postal')
addrtype.text = ID_addrtype
address.text = ID_address
city.text = ID_city
state.text = ID_state
postal.text = ID_postal
cntvoice = ET.SubElement(cntinfo, 'cntvoice')
cntvoice.text = ID_cntvoice
cntemail = ET.SubElement(cntinfo, 'cntemail')
cntemail.text = ID_cntemail

KW = tree.find('idinfo/keywords')
for child in list(KW):
    KW.remove(child)

keywords = tree.find('idinfo/keywords')

theme = ET.SubElement(keywords, 'theme')
themekt = ET.SubElement(theme, 'themekt')
themekt.text = MainKeyword
themekey = ET.SubElement(theme, 'themekey')
themekey.text = Keyword1
themekey = ET.SubElement(theme, 'themekey')
themekey.text = Keyword2

place = ET.SubElement(keywords, 'place')
placekt = ET.SubElement(place, 'placekt')
placekt.text = county + "," + " " + StateAbb
placekey = ET.SubElement(place, 'placekey')
placekey.text = StateFF
placekey = ET.SubElement(place, 'placekey')
placekey.text = StateAbb

# Tab 2: Data Quality #todo add exception handling
tree.find('dataqual/attracc/attraccr').text = DQ_attraccr
tree.find('dataqual/logic').text = DQ_logic
tree.find('dataqual/complete').text = DQ_complete
tree.find('dataqual/posacc/horizpa/horizpar').text = DQ_horizpar
tree.find('dataqual/lineage/procstep/procdate').text = DQ_procdate
tree.find('dataqual/lineage/procstep/procdesc').text = DQ_procdesc
tree.find('dataqual/posacc/vertacc/vertaccr').text = DQ_vertaccr

# Tab 5. Distribution info
Distributioninfo = root.find('distinfo')
for child in list(Distributioninfo):
    Distributioninfo.remove(child)
root.remove(Distributioninfo)

distinfo = ET.Element("distinfo")
distrib = ET.SubElement(distinfo, 'distrib')
cntinfo = ET.SubElement(distrib, 'cntinfo')
cntorgp = ET.SubElement(cntinfo, 'cntorgp')
cntorg = ET.SubElement(cntorgp, 'cntorg')
cntper = ET.SubElement(cntorgp, 'cntper')
cntorg.text = MI_cntorg
cntper.text = MI_cntper
cntaddr = ET.SubElement(cntinfo, 'cntaddr')
addrtype = ET.SubElement(cntinfo, 'addrtype')
address = ET.SubElement(cntinfo, 'address')
city = ET.SubElement(cntinfo, 'city')
state = ET.SubElement(cntinfo, 'state')
postal = ET.SubElement(cntinfo, 'postal')
addrtype.text = MI_addrtype
address.text = MI_address
city.text = MI_city
state.text = MI_state
postal.text = MI_postal
cntvoice = ET.SubElement(cntinfo, 'cntvoice')
cntvoice.text = MI_cntvoice
cntemail = ET.SubElement(cntinfo, 'cntemail')
cntemail.text = MI_cntemail
distliab = ET.SubElement(distinfo, 'distliab')
distliab.text = DI_distliab
stdorder = ET.SubElement(distinfo, 'stdorder')
digform = ET.SubElement(stdorder, 'digform')
digtinfo = ET.SubElement(digform, 'digform')
formname = ET.SubElement(digtinfo, 'formname')
formname.text = "Digital Data"
digtopt = ET.SubElement(digform, 'digtopt')
onlinopt = ET.SubElement(digtopt, 'onlinopt')
computer = ET.SubElement(onlinopt, 'computer')
networka = ET.SubElement(computer, 'networka')
networkr = ET.SubElement(networka, 'networkr')
fees = ET.SubElement(stdorder, 'fees')
fees.text = DI_fees
resdesc = ET.SubElement(distinfo, 'resdesc')
resdesc.text = "Downloadable Data"
resdesc.set('Sync', "TRUE")

root.append(distinfo)

# Tab 6 : Meta Data Info Update
Metadatainfo = root.find('metainfo')
for child in list(Metadatainfo):
    Metadatainfo.remove(child)
root.remove(Metadatainfo)

metainfo = ET.Element("metainfo")
metd = ET.SubElement(metainfo, 'metd')
metd.text = MI_metd
metc = ET.SubElement(metainfo, 'metc')
cntinfo = ET.SubElement(metc, 'cntinfo')
cntorgp = ET.SubElement(cntinfo, 'cntorgp')
cntorg = ET.SubElement(cntorgp, 'cntorg')
cntper = ET.SubElement(cntorgp, 'cntper')
cntorg.text = MI_cntorg
cntper.text = MI_cntper
cntaddr = ET.SubElement(cntinfo, 'cntaddr')
addrtype = ET.SubElement(cntinfo, 'addrtype')
address = ET.SubElement(cntinfo, 'address')
city = ET.SubElement(cntinfo, 'city')
state = ET.SubElement(cntinfo, 'state')
postal = ET.SubElement(cntinfo, 'postal')
addrtype.text = MI_addrtype
address.text = MI_address
city.text = MI_city
state.text = MI_state
postal.text = MI_postal
cntvoice = ET.SubElement(cntinfo, 'cntvoice')
cntvoice.text = MI_cntvoice
cntemail = ET.SubElement(cntinfo, 'cntemail')
cntemail.text = MI_cntemail
metstdn = ET.SubElement(metainfo, 'metstdn')
metstdn.text = MI_metstdn
metstdv = ET.SubElement(metainfo, 'metstdv')
metstdv.text = MI_metstdv
mettc = ET.SubElement(metainfo, 'mettc')
mettc.text = "local time"
mettc.set('Sync', "TRUE")
root.append(metainfo)

tree.write(OutputFileName)

