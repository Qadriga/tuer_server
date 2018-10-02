from lxml import etree as ET
class ProjectConfig:
    class __Singlton:
        def __init__(self):
            try:
                tree = ET.parse("config.xml")
            except ET.XMLSyntaxError as err:
                print("Your Configuration has Some Errors")
                print(err.errmsg)
            root = tree.getroot()            
            self.sshusername = tree.getroot().findall("SSHUSERNAME",root.nsmap)[0].text
            self.sshkeyfile = root.findall("sshkeyfilepath",root.nsmap)[0].text
            self.localusername = root.findall("LOCALDATABASEUSERNAME",root.nsmap)[0].text
            self.localdatabase = root.findall("LOCALDATABASENAME",root.nsmap)[0].text
            self.localpasswd = root.findall("LOCALDATABASEPASSWORD",root.nsmap)[0].text
            self.remoteusername = root.findall("REMOTEDATABASEUSERNAME",root.nsmap)[0].text
            self.remotepasswd = root.findall("REMOTEDATABASEPASSWORD",root.nsmap)[0].text
            self.remotedatabasename = root.findall("REMOTEDATABASENAME",root.nsmap)[0].text
            self.doorid = root.findall("DOORID",root.nsmap)[0].text
            self.sshremotename = root.findall("SSHREMOTENAME",root.nsmap)[0].text
            self.sshtunnelname = root.findall("SSHTUNNELNAME",root.nsmap)[0].text
            
        def __str__(self):
            pass
    instance = None
    
    def __init__(self):
        if not ProjectConfig.instance:
            ProjectConfig.instance = ProjectConfig.__Singlton()
    
    def getLocalDatabaseName(self):
        return ProjectConfig.instance.localdatabase
    
    def getLocalDatabaseUsername(self):
        return ProjectConfig.instance.localusername
    
    def getLocalDatabasePassword(self):
        return ProjectConfig.instance.localpasswd
    
    def getRemoteDatabaseName(self):
        return ProjectConfig.instance.remotedatabasename
    
    def getRemoteDatabaseUsername(self):
        return ProjectConfig.instance.remoteusername
    
    def getRemoteDatabasePassword(self):
        return ProjectConfig.instance.remotepasswd
    
    def getSSHUsername(self):
        return ProjectConfig.instance.sshusername
    
    def getSSHkeyfilepath(self):
        return ProjectConfig.instance.sshkeyfile
    
    def getSSHRemotename(self):
        return ProjectConfig.instance.sshremotename
    
    def getSSHTunnelname(self):
        return ProjectConfig.instance.sshtunnelname
    
    def getDOORID(self):
        return ProjectConfig.instance.doorid
        
      
      
            
ProjectConfiguration = ProjectConfig()

if __name__ == '__main__':
    print(ProjectConfiguration.getLocalDatabaseName())
    print(ProjectConfiguration.getLocalDatabaseUsername())
    print(ProjectConfiguration.getLocalDatabasePassword())
    print(ProjectConfiguration.getRemoteDatabaseName())
    print(ProjectConfiguration.getRemoteDatabaseUsername())
    print(ProjectConfiguration.getRemoteDatabasePassword())
    print(ProjectConfiguration.getSSHUsername())
    print(ProjectConfiguration.getSSHkeyfilepath())
    print(ProjectConfiguration.getSSHRemotename())
    print(ProjectConfiguration.getSSHTunnelname())
    