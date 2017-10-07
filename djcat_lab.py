import datajoint as dj

schema = dj.schema(dj.config['names.%s' % __name__], locals())

@schema
class Lab(dj.Manual): 
    definition = """ # Lab
    lab : varchar(255)  #  lab conducting the study
    ----
    instition  : varchar(255)  # Institution to which the lab belongs
    """

@schema
class Keyword(dj.Lookup):
    definition = """
    # Tag of study types
    keyword : varchar(24)  
    """
    contents = zip(['behavior', 'extracellular', 'photostim'])

@schema
class Study(dj.Manual):
    definition = """
    # Study 
    study : varchar(8)    # short name of the study
    --- 
    study_description : varchar(255)   #  
    -> Lab
    reference_atlas : varchar(255)   # e.g. "paxinos"
    """
    
@schema
class StudyKeyword(dj.Manual):
    definition = """
    # Study keyword (see general/notes)
    -> Study
    -> Keyword
    """

@schema
class Publication(dj.Manual):
    definition = """
    # Publication
    doi  : varchar(60)   # publication DOI
    ----
    full_citation : varchar(4000)
    authors='' : varchar(4000)
    title=''   : varchar(1024)
    """
    
@schema
class RelatedPublication(dj.Manual):
    definition = """
    -> Study
    -> Publication
    """

@schema
class Subject(dj.Manual):
    definition = """
    subject_id  : int   # institution animal ID  
    --- 
    species        : varchar(30)
    date_of_birth  : date   
    sex            : enum('M','F','Unknown')
    animal_source  : varchar(30)
    """
