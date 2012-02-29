"""

TestLinkAPI - v0.20
Created on 5 nov. 2011
@author: Olivier Renault (admin@sqaopen.net)

Initialy based on the James Stock testlink-api-python-client R7.
 

"""
import xmlrpc.client

class TestlinkAPIClient:        
  
    def __init__(self, server_url, devKey):
        self.server = xmlrpc.client.Server(server_url)
        self.devKey = devKey
        self.stepsList = []

    #
    #  BUILT-IN API CALLS
    #
    
    def checkDevKey(self):
        """ checkDevKey :
        check if Developer Key exists   
        """
        argsAPI = {'devKey' : self.devKey}     
        return self.server.tl.checkDevKey(argsAPI)  
    
    def about(self):
        """ about :
        Gives basic information about the API    
        """
        return self.server.tl.about()
  
    def ping(self):
        """ ping :   
        """
        return self.server.tl.ping()

    def echo(self, message):
        return self.server.tl.repeat({'str': message})

    def doesUserExist(self, user):
        """ doesUserExist :
        Checks if a user name exists 
        """
        argsAPI = {'devKey' : self.devKey,
                'user':str(user)}   
        return self.server.tl.doesUserExist(argsAPI)
        
    def getBuildsForTestPlan(self, testplanid):
        """ getBuildsForTestPlan :
        Gets a list of builds within a test plan 
        """
        argsAPI = {'devKey' : self.devKey,
                'testplanid':str(testplanid)}   
        return self.server.tl.getBuildsForTestPlan(argsAPI)
	  	  
    def getFirstLevelTestSuitesForTestProject(self,testprojectid):
        """ getFirstLevelTestSuitesForTestProject :
        Get set of test suites AT TOP LEVEL of tree on a Test Project 
        """  
        argsAPI = {'devKey' : self.devKey,
                'testprojectid':str(testprojectid)}   
        return self.server.tl.getFirstLevelTestSuitesForTestProject(argsAPI)
        
    def getFullPath(self,nodeid):
        """ getFullPath :
        Gets full path from the given node till the top using 
        nodes_hierarchy_table 
        """
        argsAPI = {'devKey' : self.devKey,
                'nodeid':str(nodeid)}    
        return self.server.tl.getFullPath(argsAPI)

    def getLastExecutionResult(self, testplanid, testcaseid):
        """ getLastExecutionResult :
        Gets the result of LAST EXECUTION for a particular testcase on a 
        test plan, but WITHOUT checking for a particular build 
        """
        argsAPI = {'devKey' : self.devKey,
                'testplanid' : str(testplanid),
                'testcaseid' : str(testcaseid)}     
        return self.server.tl.getLastExecutionResult(argsAPI)

    def getLatestBuildForTestPlan(self, testplanid):
        """ getLastExecutionResult :
        Gets the latest build by choosing the maximum build id for a 
        specific test plan  
        """  
        argsAPI = {'devKey' : self.devKey,
                'testplanid':str(testplanid)}  
        return self.server.tl.getLatestBuildForTestPlan(argsAPI)

    def getProjects(self):
        """ getProjects: 
        Gets a list of all projects 
        """
        argsAPI = {'devKey' : self.devKey} 
        return self.server.tl.getProjects(argsAPI)

    def getProjectTestPlans(self, testprojectid):
        """ getLastExecutionResult :
        Gets a list of test plans within a project 
        """ 
        argsAPI = {'devKey' : self.devKey,
                'testprojectid':str(testprojectid)}  
        return self.server.tl.getProjectTestPlans(argsAPI)

    def getTestCase(self, testcaseid):
        """ getTestCase :
        Gets test case specification using external or internal id  
        """
        argsAPI = {'devKey' : self.devKey,
                'testcaseid' : str(testcaseid)}  
        return self.server.tl.getTestCase(argsAPI)          

    def getTestCaseAttachments(self, testcaseid):
        """ getTestCaseAttachments :
        Gets attachments for specified test case  
        """
        argsAPI = {'devKey' : self.devKey,
                'testcaseID':str(testcaseid)}  
        return self.server.tl.getTestCaseAttachments(argsAPI)    

    def getTestCaseCustomFieldDesignValue(self, testcaseexternalid, version, 
                                     testprojectid, customfieldname, details):
        """ getTestCaseCustomFieldDesignValue :
        Gets value of a Custom Field with scope='design' for a given Test case  
        """
        argsAPI = {'devKey' : self.devKey,
                'testcaseexternalid' : str(testcaseexternalid),
                'version' : str(version),
                'testprojectid' : str(testprojectid),
                'customfieldname' : str(customfieldname),
                'details' : str(details)}
        return self.server.tl.getTestCaseCustomFieldDesignValue(argsAPI)                                                

    def getTestCaseIDByName(self, testCaseName):
        """ getTestCaseIDByName :
        Find a test case by its name   
        """    
        argsAPI = {'devKey' : self.devKey,
                'testcasename':str(testCaseName)}
        return self.server.tl.getTestCaseIDByName(argsAPI)
                                                   
    def getTestCasesForTestPlan(self, *args):
        """ getTestCasesForTestPlan :
        List test cases linked to a test plan    
            Mandatory parameters : testplanid
            Optional parameters : testcaseid, buildid, keywordid, keywords,
                executed, assignedto, executestatus, executiontype, getstepinfo 
        """        
        testplanid = args[0]
        argsAPI = {'devKey' : self.devKey,
                'testplanid' : str(testplanid)}
        if len(args)>1:
            params = args[1:] 
            for param in params:
              paramlist = param.split("=")                     
              argsAPI[paramlist[0]] = paramlist[1]  
        return self.server.tl.getTestCasesForTestPlan(argsAPI)   
            
    def getTestCasesForTestSuite(self, testsuiteid, deep, details):
        """ getTestCasesForTestSuite :
        List test cases within a test suite    
        """        
        argsAPI = {'devKey' : self.devKey,
                'testsuiteid' : str(testsuiteid),
                'deep' : str(deep),
                'details' : str(details)}                  
        return self.server.tl.getTestCasesForTestSuite(argsAPI)
  
    def getTestPlanByName(self, testprojectname, testplanname):
        """ getTestPlanByName :
        Gets info about target test project   
        """
        argsAPI = {'devKey' : self.devKey,
                'testprojectname' : str(testprojectname),
                'testplanname' : str(testplanname)}    
        return self.server.tl.getTestPlanByName(argsAPI)

    def getTestPlanPlatforms(self, testplanid):
        """ getTestPlanPlatforms :
        Returns the list of platforms associated to a given test plan    
        """
        argsAPI = {'devKey' : self.devKey,
                'testplanid' : str(testplanid)}    
        return self.server.tl.getTestPlanPlatforms(argsAPI)  

    def getTestProjectByName(self, testprojectname):
        """ getTestProjectByName :
        Gets info about target test project    
        """
        argsAPI = {'devKey' : self.devKey,
                'testprojectname' : str(testprojectname)}    
        return self.server.tl.getTestProjectByName(argsAPI)    
  
    def getTestSuiteByID(self, testsuiteid):
        """ getTestSuiteByID :
        Return a TestSuite by ID    
        """
        argsAPI = {'devKey' : self.devKey,
                'testsuiteid' : str(testsuiteid)}    
        return self.server.tl.getTestSuiteByID(argsAPI)   
  
    def getTestSuitesForTestPlan(self, testplanid):
        """ getTestSuitesForTestPlan :
        List test suites within a test plan alphabetically     
        """
        argsAPI = {'devKey' : self.devKey,
                'testplanid' : str(testplanid)}    
        return self.server.tl.getTestSuitesForTestPlan(argsAPI)  
        
    def getTestSuitesForTestSuite(self, testsuiteid):
        """ getTestSuitesForTestSuite :
        get list of TestSuites which are DIRECT children of a given TestSuite     
        """
        argsAPI = {'devKey' : self.devKey,
                'testsuiteid' : str(testsuiteid)}    
        return self.server.tl.getTestSuitesForTestSuite(argsAPI)        
        
    def getTotalsForTestPlan(self, testplanid):
        """ getTotalsForTestPlan :
        Gets the summarized results grouped by platform    
        """
        argsAPI = {'devKey' : self.devKey,
                'testplanid' : str(testplanid)}    
        return self.server.tl.getTotalsForTestPlan(argsAPI)  

    def createTestProject(self, *args):
        """ createTestProject :
        Create a test project  
            Mandatory parameters : testprojectname, testcaseprefix
            Optional parameters : notes, options, active, public
            Options: map of requirementsEnabled, testPriorityEnabled, 
                            automationEnabled, inventoryEnabled 
        """        
        testprojectname = args[0]
        testcaseprefix = args[1]
        options={}
        argsAPI = {'devKey' : self.devKey,
                   'testprojectname' : str(testprojectname), 
                   'testcaseprefix' : str(testcaseprefix)}
        if len(args)>2:
            params = args[2:] 
            for param in params:
              paramlist = param.split("=")
              if paramlist[0] == "options":
                  optionlist = paramlist[1].split(",")
                  for option in optionlist:
                      optiontuple = option.split(":")
                      options[optiontuple[0]] = optiontuple[1]  
                  argsAPI[paramlist[0]] = options   
              else:
                  argsAPI[paramlist[0]] = paramlist[1]  
        return self.server.tl.createTestProject(argsAPI)
        
    def createBuild(self, testplanid, buildname, buildnotes):
        """ createBuild :
        Creates a new build for a specific test plan     
        """
        argsAPI = {'devKey' : self.devKey,
                'testplanid' : str(testplanid),
                'buildname' : str(buildname),
                'buildnotes' : str(buildnotes)}                  
        return self.server.tl.createBuild(argsAPI)        
    
    def createTestPlan(self, *args):
        """ createTestPlan :
        Create a test plan 
            Mandatory parameters : testplanname, testprojectname
            Optional parameters : notes, active, public   
        """        
        testplanname = args[0]
        testprojectname = args[1]
        argsAPI = {'devKey' : self.devKey,
                'testplanname' : str(testplanname),
                'testprojectname' : str(testprojectname)}
        if len(args)>2:
            params = args[2:] 
            for param in params:
              paramlist = param.split("=")       
              argsAPI[paramlist[0]] = paramlist[1]  
        return self.server.tl.createTestPlan(argsAPI)    
 
    def createTestSuite(self, *args):
        """ createTestSuite :
        Create a test suite  
          Mandatory parameters : testprojectid, testsuitename, details
          Optional parameters : parentid, order, checkduplicatedname, 
                                actiononduplicatedname   
        """        
        argsAPI = {'devKey' : self.devKey,
                'testprojectid' : str(args[0]),
                'testsuitename' : str(args[1]),
                'details' : str(args[2])}
        if len(args)>3:
            params = args[3:] 
            for param in params:
              paramlist = param.split("=")       
              argsAPI[paramlist[0]] = paramlist[1]  
        return self.server.tl.createTestSuite(argsAPI)       

    def createTestCase(self, *args):
        """ createTestCase :
        Create a test case  
          Mandatory parameters : testcasename, testsuiteid, testprojectid, 
                                 authorlogin, summary, steps 
          Optional parameters : preconditions, importance, execution, order, 
                       internalid, checkduplicatedname, actiononduplicatedname   
        """
        argsAPI = {'devKey' : self.devKey,
                'testcasename' : str(args[0]),
                'testsuiteid' : str(args[1]),
                'testprojectid' : str(args[2]),
                'authorlogin' : str(args[3]),
                'summary' : str(args[4]),
                'steps' : self.stepsList}
        if len(args)>5:
            params = args[5:] 
            for param in params:
              paramlist = param.split("=")       
              argsAPI[paramlist[0]] = paramlist[1]
        ret = self.server.tl.createTestCase(argsAPI) 
        self.stepsList = []                    
        return ret 

                        
    #
    #  ADDITIONNAL FUNCTIONS
    #                                   

    def countProjects(self):
        """ countProjects :
        Count all the test project   
        """
        projects=TestlinkAPIClient.getProjects(self)
        return len(projects)
    
    def countTestPlans(self):
        """ countProjects :
        Count all the test plans   
        """
        projects=TestlinkAPIClient.getProjects(self)
        nbTP = 0
        for project in projects:
            ret = TestlinkAPIClient.getProjectTestPlans(self,project['id'])
            nbTP += len(ret)
        return nbTP

    def countTestSuites(self):
        """ countProjects :
        Count all the test suites   
        """
        projects=TestlinkAPIClient.getProjects(self)
        nbTS = 0
        for project in projects:
            TestPlans = TestlinkAPIClient.getProjectTestPlans(self,
                                                                 project['id'])
            for TestPlan in TestPlans:
                TestSuites = TestlinkAPIClient.getTestSuitesForTestPlan(self, 
                                                                TestPlan['id'])
                nbTS += len(TestSuites)
        return nbTS
               
    def countTestCasesTP(self):
        """ countProjects :
        Count all the test cases linked to a Test Plan   
        """
        projects=TestlinkAPIClient.getProjects(self)
        nbTC = 0
        for project in projects:
            TestPlans = TestlinkAPIClient.getProjectTestPlans(self, 
                                                                 project['id'])
            for TestPlan in TestPlans:
                TestCases = TestlinkAPIClient.getTestCasesForTestPlan(self,
                                                                TestPlan['id'])
                nbTC += len(TestCases)
        return nbTC
        
    def countTestCasesTS(self):
        """ countProjects :
        Count all the test cases linked to a Test Suite   
        """
        projects=TestlinkAPIClient.getProjects(self)
        nbTC = 0
        for project in projects:
            TestPlans = TestlinkAPIClient.getProjectTestPlans(self,
                                                                 project['id'])
            for TestPlan in TestPlans:
                TestSuites = TestlinkAPIClient.getTestSuitesForTestPlan(self,
                                                                TestPlan['id'])
                for TestSuite in TestSuites:
                    TestCases = TestlinkAPIClient.getTestCasesForTestSuite(self,
                                                 TestSuite['id'],'true','full')
                    for TestCase in TestCases:
                        nbTC += len(TestCases)
        return nbTC

    def countPlatforms(self):
        """ countPlatforms :
        Count all the Platforms  
        """
        projects=TestlinkAPIClient.getProjects(self)
        nbPlatforms = 0
        for project in projects:
            TestPlans = TestlinkAPIClient.getProjectTestPlans(self,
                                                                 project['id'])
            for TestPlan in TestPlans:
                Platforms = TestlinkAPIClient.getTestPlanPlatforms(self,
                                                                TestPlan['id'])
                nbPlatforms += len(Platforms)
        return nbPlatforms
        
    def countBuilds(self):
        """ countBuilds :
        Count all the Builds  
        """
        projects=TestlinkAPIClient.getProjects(self)
        nbBuilds = 0
        for project in projects:
            TestPlans = TestlinkAPIClient.getProjectTestPlans(self,
                                                                 project['id'])
            for TestPlan in TestPlans:
                Builds = TestlinkAPIClient.getBuildsForTestPlan(self,
                                                                TestPlan['id'])
                nbBuilds += len(Builds)
        return nbBuilds
        
    def listProjects(self):
        """ listProjects :
        Lists the Projects (display Name & ID)  
        """
        projects=TestlinkAPIClient.getProjects(self)
        for project in projects:
          print ("Name: %s ID: %s " % (project['name'], project['id']))
  

    def initStep(self, actions, expected_results, execution_type):
        """ initStep :
        Initializes the list which stores the Steps of a Test Case to create  
        """
        self.stepsList = []
        list = {}
        list['step_number'] = '1'
        list['actions'] = actions
        list['expected_results'] = expected_results
        list['execution_type'] = str(execution_type)
        self.stepsList.append(list)
        return True
        
    def appendStep(self, actions, expected_results, execution_type):
        """ appendStep :
        Appends a step to the steps list  
        """
        list = {}
        list['step_number'] = str(len(self.stepsList)+1)
        list['actions'] = actions
        list['expected_results'] = expected_results
        list['execution_type'] = str(execution_type)
        self.stepsList.append(list)
        return True                
                                        
    def getProjectIDByName(self, projectName):   
	  	  projects=self.server.tl.getProjects({'devKey' : self.devKey})
	  	  for project in projects:
		  	    if (project['name'] == projectName): 
		    	  	  result = project['id']
		  	    else:
		    	  	  result = -1
	  	  return result
	  	  
if __name__ == "__main__":    
    myTestLinkServer = "http://YOURSERVER/testlink/lib/api/xmlrpc.php"  #change
    myDevKey = "" # Put here your devKey
    myTestLink = TestlinkAPIClient(myTestLinkServer, myDevKey)
    print ("TestLinkAPIClient - v0.2")      
    print ("@author: Olivier Renault (admin@sqaopen.net)")
    print ("")
    if myTestLink.checkDevKey() == True:      
        methodList = [method for method in TestlinkAPIClient.__dict__]
        for method in methodList:
            if method[0:2] != "__": 
                print (method)
        print ("")
    else:
        print ("Incorrect DevKey.")
