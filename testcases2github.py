#!/usr/bin/python
# Author: Peter Withers
# Date: 2014/02/26

# modified to create test plan milestones and tickets
# Date: 2014/07/25

import csv
from base64 import encodestring
import json
import sys
import time
import urllib
import urllib2

githubUsername = sys.argv[1]
githubProject = sys.argv[2]
githubRepository = sys.argv[3]
print 'GitHub username: ', githubUsername
print 'GitHub project:', githubProject
print 'GitHub repository: ', githubRepository
testCasesUrl = 'KinOathtestcases.txt'
#githubApiUrl = 'https://api.github.com'
githubApiUrl = 'localhost'

milestoneUrl = githubApiUrl + '/repos/%s/%s/milestones' % (githubProject, githubRepository)
issuesUrl = githubApiUrl + '/repos/%s/%s/issues' % (githubProject, githubRepository)
print(milestoneUrl)
print(issuesUrl)

knownMilestones = {}

def getAllMileStones():
    response = urllib.urlopen(milestoneUrl)
    if response.getcode() == 200:
        content = response.read()
        #print(content)
        milestones = json.loads(content)
        #print(milestones)
        # del knownMilestones[:]
        for entry in milestones:
            print entry['number'], ' : ', entry['title']
            knownMilestones[entry['title']] = entry['number']

def getMileStoneId(milestoneTitle):
    #print milestoneTitle
    #print knownMilestones
    if len(milestoneTitle) == 0:
        # the milestone is blank or the list of milestones is empty, so we return here
        return ""
    if not milestoneTitle in knownMilestones:
        data=json.dumps({'title': milestoneTitle, 'state': 'open'})
        #data=json.dumps({'title': 'milestone', 'state': 'open', 'desription': '.', 'due_on': '2012-10-09T23:39:01Z'})
        print(data)
        datalength = len(data)
        request = urllib2.Request(milestoneUrl, data, {'Content-Type': 'application/json', 'Content-Length': datalength})
        #request = urllib2.Request(milestoneUrl, data)
        #, 'Content-Length': datalength}
        request.add_header('Authorization', 'Basic %s' % base64string)
        response = urllib2.urlopen(request)
        #print(response)
        knownMilestones[milestoneTitle] = 0 # this value will be replaced when getAllMileStones is next called
        #knownMilestones.append(milestoneTitle)
        time.sleep(1)
    return knownMilestones[milestoneTitle]

def createRequiredEmptyTickets(testCount):
    print 'total ticket count: ', testCount
    response = urllib.urlopen(issuesUrl)
    content = response.read()
    tickets = json.loads(content)
    #print(tickets)
    if len(tickets) > 0:
        currentIssueCount = tickets[0]['number']
    else:
        currentIssueCount = 0
    while testCount > currentIssueCount:
        currentIssueCount = currentIssueCount + 1
        makeEmptyIssueRequest()

def makeEmptyIssueRequest():
    data=json.dumps({'title': 'dummy ticket to allow imports with the correct ticket id'})
    datalength = len(data)
    request = urllib2.Request(issuesUrl, data, {'Content-Type': 'application/json', 'Content-Length': datalength})
    request.add_header('Authorization', 'Basic %s' % base64string)
    response = urllib2.urlopen(request)
    print(response)
    time.sleep(1)

def makeIssueRequest(ticketId, data):
    print (ticketId)
    print(data)
    datalength = len(data)
    request = urllib2.Request(issuesUrl + '/' + ticketId, data, {'Content-Type': 'application/json', 'Content-Length': datalength})
    request.add_header('Authorization', 'Basic %s' % base64string)
    response = urllib2.urlopen(request)
    print(response)
    time.sleep(1)

getAllMileStones()

githubToken = raw_input("GitHub Password:")
base64string = encodestring('%s:%s' % (githubUsername, githubToken)).replace('\n', '')

testPlanCSV = urllib.urlopen(testCasesUrl)
testPlanList = csv.DictReader(testPlanCSV)

# print(testPlanList)
# create any missing milestones
print 'adding milestones'
testCount = 0
for ticket in testPlanList:
    testCount = testCount + 1
    milestoneId = getMileStoneId(ticket['milestone'])
# make sure the milestone list is up to date
knownMilestones = {}
getAllMileStones()
print 'adding tickets'
createRequiredEmptyTickets(testCount)
# insert the tickets as issues
testCasesCSV = urllib.urlopen(testCasesUrl)
testCases = csv.DictReader(testCasesCSV)
currentTicket = 0
for testCase in testCases:
    #print (ticket)    
    currentTicket = currentTicket + 1
    milestoneId = getMileStoneId(ticket['milestone'].strip())
    print 'milestone: ', milestoneId
    #if currentTicket > 394:
    if ticket['status'] == 'closed':
        status = 'closed'
    else:
        status = 'open'
    labels =  [ticket['component'], ticket['type'], ticket['priority'], ticket['resolution']]
    while labels.count("") > 0:
        labels.remove("")
    # add a link into trac from the imported github tickets
    tracLink = "https://trac.mpi.nl/ticket/" + ticket['id'].strip();
    descriptionMarkup = ticket['description'].strip() + '\n- trac-id:' + ticket['id'].strip() + '\n- trac-time:' + ticket['time'].strip() + '\n- trac-changetime:' + ticket['changetime'].strip() + '\n- trac-reporter:' + ticket['reporter'].strip() + '\n- trac-keywords:' + ticket['keywords'].strip() + '\n- trac-cc:' + ticket['cc'].strip() + '\n- trac-owner:' + ticket['owner'].strip() + '\n- trac-owner:' + ticket['owner'].strip() + '\n- trac-version:' + ticket['version'].strip()+ '\n- ' + tracLink
    if milestoneId == "":
        # if there is no milestone then we must not pass it as a parameter
        data=json.dumps({'title': ticket['summary'].strip(), 'body': descriptionMarkup, "state": status, 'labels': labels})
    else:
        data=json.dumps({'title': ticket['summary'].strip(), 'body': descriptionMarkup, 'milestone': milestoneId, "state": status, 'labels': labels})
    # so far unused fields: col=id& &col=time &col=changetime &col=reporter &col=keywords &col=cc 'assignee': ticket['owner'], , ticket['version']
    #if currentTicket > 223: # ticket 224 has issues that are as yet un identified, ticket 147 is the fist one to not have a milestone
    makeIssueRequest(str(currentTicket), data) # ticket['id']
exit(0)
