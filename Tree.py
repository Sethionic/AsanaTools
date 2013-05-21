#!python

from asana import asana
APIKEY=''
with open("API.key") as f: APIKEY=f.readline().strip()
#print "API Key: ",APIKEY

#Redefine function:

def list_tasks(self,workspace,assignee):
    """List tasks

    :param workspace: workspace id
    :param assignee: assignee
    """
    target = "tasks?workspace={0}".format(workspace)
    return self._asana(target)
    asana.AsanaAPI.list_tasks=list_tasks

AAPI=asana.AsanaAPI(APIKEY,debug=True)
AAPI.list_tasks=list_tasks

WSpaces=AAPI.list_workspaces() #Workspaces
for WS in WSpaces:
    print "Workspace: {0}".format(WS['name'])
    Users=AAPI.list_users(WS['id'])
    print " Users: {0}".format(reduce(lambda x,y:x+", "+y,[i['name'] for i in Users]))
    tasks=AAPI._asana("tasks?workspace={0}".format(WS['id']))












#AAPI.get_task(AAPI.list_tasks(AAPI.list_workspaces()[1]['id'],AAPI.list_users()[0]['id'])[0]['id'])