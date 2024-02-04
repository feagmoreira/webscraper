# Scraping pattern constants for scraping AptoideApp´s attributes from Aptoide Website
SCRAPING_PATTERNS: dict[str,str] = {
  "name": r'<strong>Name.*?</strong>(.*?)</span>',
  "version": r'<strong>Version.*?</strong>(.*?)</span>',
  "downloads": r'<strong>Downloads.*?</strong>(.*?)</span>',
  "release_date": r'<strong>Release Date.*?</strong>(.*?)</span>',
  "description": r'\"media\":.*?\"description\":\"(.*?)\",\"summary\":',
  }



class AptoideApp:
  """
  A class used to represent apps retrieved from Aptoide app store website

  Attributes
    ----------
    name : str
        the app name
    version : str
        the version number of the app
    downloads : str
        the quantity of downloads
    release_date : str
        the date and time when the app was released on Aptoide app store
    description : str
        the app description 

  """

  def __init__(self, name: str, version:str, downloads: str, release_date: str, description: str):
    """
     Parameters
     ----------
     name : str
        the app name
     version : str
        the version number of the app
     downloads : str
        the number of app downloads in millions
     release_date : str
        the date and time when the app was released on Apptoid app store
     description : str
        the app description 
    """
    self.name = name
    self.version = version
    self.downloads  = downloads
    self.release_date = release_date
    self.description = description

  def __str__(self) -> str:
    """
    String representation of AptoideAPP object
    """
    return "Name: " + self.name + "\n" + \
               "Version: " + self.version + "\n" + \
               "Downloads: " + self.downloads + "\n" + \
               "Release Date: " + self.release_date + "\n" + \
               "Description: " + self.description  
  
  
