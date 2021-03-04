from django.http.response import Http404, HttpResponse, JsonResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from pathlib import Path
import os
import json
from urllib.parse import unquote
from ast import literal_eval
from random import sample

BASE_DIR = Path(__file__).resolve().parent.parent
static_path = os.path.join(BASE_DIR, 'static')

filepath = static_path + r'\answers.json'
# print("path =>",filepath)

with open(filepath) as file:
    data = json.loads(file.read())
    # print(data.keys())

    # Extract and store all subjects from file into list
    # subjects = [] # list(data.keys())
    # start = stop = 0
    
  

# Fucntion to get question_answer range
def get_quest_range(sub, _from=4, _to=10):
    # sub for subject
    quest = list(sub.keys())[2:] # excluded 'short' and 'code'

    quest = list(map(int, quest)) # convert all quest element to integer
    
    quest_range = quest[_from-1: _to] # range requested

    return quest_range

'''
def setup(request):
    return render(request, 'setup.html', {})

def instruction(request):

    return render(request, 'instructions.html', {})
'''

def index(request):
    return HttpResponseNotFound("Start Page still in Development")


def decodeCookie(cookie):
    test_data = unquote(cookie)  # Decode the URL encoding in UTF-8
    
    test_data = test_data.strip('][').split(' ')  # Convert string list to actual list
    
    # Convert string dict to actual dict
    test_data = list(literal_eval(test_data[0]))
    
    return test_data


def test(request):
    # This Functions sends the test sheet.
    # Requires Start, stop
    # requires subjects
    # requires duration

    # Process the duration
    # receives a number string from url
    duration = request.GET.get('dur', '30') #mins
    # print(duration)
    # convert to float
    

    

    # global start, stop
    #start, stop = (10, 20)  # Query from cookie
    subjects = [] # Query from cookie
    # %2c m-> ,

    test_data = request.COOKIES['testData'] # Get testData from cookie
    # print(test_data)
    
    test_data = unquote(test_data) # Decode the URL encoding in UTF-8
    # print(test_data ,'=>', type(test_data))
    test_data = test_data.strip('][').split(' ') # Convert string list to actual list
    # print(test_data)
    test_data = list(literal_eval(test_data[0])) # Convert string dict to actual dict
    # print(test_data)
    
    # test_data ->
    ## [
    #   {'name': 'English', 'start': '1', 'stop': '10'},
    #   {'name': 'Chemistry', 'start': '1', 'stop': '10'}
    #  ]

    c = 1 # index for the dictionary
    quest_ans = {}# {}
    for each_data in test_data:
        # each_data is a dictionary
        #subjects.append(each_data['name'])
        
        name = each_data['name']
        subjects.append(name)
        sub = data[name]
        rep_ans = get_quest_range(sub, _from=int(each_data['start']), _to=int(each_data['stop']))

        temp = {'sub': name, 'code': sub['code'], 'data': rep_ans}

        quest_ans[c] = temp
        c += 1

        temp = None
        
    print(quest_ans)
    
    # print(type(quest_range[0]))
    return render(request, 'practise/test.html',
        {
            'quest_range':quest_ans.values(),
            'subjects':subjects,
            'duration': float(duration),
        })
    


# Create your views here.
def practise(request):
    
    
    subjects = [
        {'code': 'ENG', 'name': 'English'},
        {'code': 'MTH', 'name': 'Mathematics'},
        {'code': 'PHY', 'name': 'Physics'},
        {'code': 'CHM', 'name': 'Chemistry'}
    ]  # Query this info from Cookie

    test_data = request.COOKIES['testData']
    # Sample output -> [{'name': 'English', 'start': '1', 'stop': '10', 'quest_range': 10}, {'name': 'Chemistry', 'start': '2', 'stop': '20', 'quest_range': 19}]
    # print(decodeCookie(test_data))
    test_data = decodeCookie(test_data)

    
    
    if request.method == 'POST':
        # print("Yes!!")
        script_data = request.POST #.keys()


        # print(script_data['ENG1'])

        # Example of script_data output
        # <QueryDict: {'ENG1': ['A'], 'ENG2': ['B'], 'ENG4': ['A'], 'ENG5': ['C'], 'ENG6': ['D'], 'CHM2': ['D'], 'CHM3': ['B'], 'CHM4': ['C'], 'CHM5': ['B'], 'CHM6': ['A']}>

        prep_data = ParseDataForMarking(test_data, subjects, script_data)

        # print(prep_data)
        # marked_bundle = [] # A list of Marked Work

        TotalScore = 0
        TotalMax = 0
        for d in prep_data:
            sub_data = d[0:2]
            script = d[2]

            marked_script = marker(script, sub_data)
            TotalScore += marked_script['obtained']
            TotalMax += marked_script['max_score']

            #print(marked_script)
            print()
        
        print("Got {} / {}".format(TotalScore, TotalMax))

            # marked_bundle.append(marked_script)

            #print(sub_data, script)
            #print()
        
        

        # MarkeWork
        # Response Format:
        # {subject_code: { question_indexNo: {'choose':str,'correct':bool, 'correction':str} }}
        # global marked_work

        response = {}
        """
        marked_work = marker(script_data)
        print(marked_work)
        

        

        # quest_ans = {}
        for i,k in enumerate(subjects):
            sub = data[subjects[i]]
            temp = {'sub':k, 'code':sub['code'],'data':marked_work}

            response[i] = temp

            temp = None
        """
        
        # print(response)
        
        return render(request, 'check_test.html',
                      {
                          'reply': response.values(),
                          'subjects': subjects
                      })
    
    
    mode = request.GET.get('m',None)

    print(mode)
    if mode == 'setup':
       
        # An API Call for the questions_data which is
        
        # All Keys
        keys = list(request.GET.keys())

        
        # print(keys[1:])
        # Subject Keys
        subjects_set = [s for s in keys if s.startswith('subject')]
        # print(subjects_set)
        data = {'good': bool(subjects_set), 'subjects':[]}

        
        
        
        
        for i in subjects_set: 
            # print(f"{i} > {request.GET[i]}")
            name = request.GET[i]
            
            code = None
            for s in subjects:
                if s['name'].lower() == name.lower():
                    code = s['code']
                    break
            # [from, to] -> default, except changed in the DOM
            start_from, to_stop = [e for e in keys if e.startswith(code)]
            
            start_from = request.GET[start_from]
            to_stop = request.GET[to_stop]

            start_from_to_range = len(list(range(int(start_from),int(to_stop)+1)))
            # print("start from {} to {}".format(start_from, to_stop))
            
            

            data['subjects'].append({'name':name, 'start':start_from, 'stop':to_stop, 'quest_range':start_from_to_range})
        
        
        
        # As for the time
        timepicked = request.GET['timeset'].replace('%3a', ':')
        time_split = timepicked.split(sep=':') # [min, sec]
        time_split = list(map(int,time_split))
        # Duration in minutes, so min + (secs/min) -> rounded to 2 decimal places
        duration = round((time_split[0]) + (time_split[1]/60),2)
        # print(duration)
        data['duration'] = duration # in minutes

        # print(data)
        return JsonResponse(data)
        
    if mode == 'instruction':
        return render(request, 'practise/instructions.html', {})
    
        
    # print(mode)
    # if mode=='setup':
    return render(request, 'practise/practiseMain.html', {'subjects':subjects})
    





def dashview(request):
    return render(request, 'dashboard/dashmain.html', {})


def profile(request):
    return render(request, "dashboard/profile.html")


def leaderBoard(request):
    return render(request, "dashboard/leaderboard.html")


def records(request):
    return render(request, "dashboard/records.html")




## Function for Correction
def correction(request):
    subjects = {'ENG':'English', 'MTH':'Mathematics', 'PHY':'Physics', 'CHM':'Chemistry'}
    response = []

    scripts =[
        {
            'ENG':
                [
                    {'No': '1', 'selected': 'A', 'correct': False, 'correction': 'D'},
                    {'No': '2', 'selected': 'B', 'correct': True, 'correction': 'B'},
                    {'No': '3', 'selected': None, 'correct': False, 'correction': 'B'},
                    {'No': '4', 'selected': 'A', 'correct': False, 'correction': 'D'},
                    {'No': '5', 'selected': 'C', 'correct': True, 'correction': 'C'},
                    {'No': '6', 'selected': 'D', 'correct': False, 'correction': 'C'},
                    {'No': '7', 'selected': None, 'correct': False, 'correction': 'B'},
                    {'No': '8', 'selected': None, 'correct': False, 'correction': 'C'},
                    {'No': '9', 'selected': None, 'correct': False, 'correction': 'D'},
                    {'No': '10', 'selected': None, 'correct': False, 'correction': 'C'}
                ],
            'max_score': 10,
            'obtained': 2
        }, 
        {
            'CHM': 
                [
                    {'No': '2', 'selected': 'D', 'correct': False, 'correction': 'B'}, 
                    {'No': '3', 'selected': 'B', 'correct': False, 'correction': 'A'},
                    {'No': '4', 'selected': 'C', 'correct': False, 'correction': 'A'}, 
                    {'No': '5', 'selected': 'B', 'correct': False, 'correction': 'C'}, 
                    {'No': '6', 'selected': 'A', 'correct': False, 'correction': 'D'}, 
                    {'No': '7', 'selected': None, 'correct': False, 'correction': 'D'}, 
                    {'No': '8', 'selected': None, 'correct': False, 'correction': 'D'}, 
                    {'No': '9', 'selected': None, 'correct': False, 'correction': 'D'}, 
                    {'No': '10', 'selected': None, 'correct': True, 'correction': None}, 
                    {'No': '11', 'selected': None, 'correct': False, 'correction': 'D'}, 
                    {'No': '12', 'selected': None, 'correct': False, 'correction': 'A'}, 
                    {'No': '13', 'selected': None, 'correct': False, 'correction': 'B'}, 
                    {'No': '14', 'selected': None, 'correct': False, 'correction': 'C'}, 
                    {'No': '15', 'selected': None, 'correct': True, 'correction': None}, 
                    {'No': '16', 'selected': None, 'correct': False, 'correction': 'D'}, 
                    {'No': '17', 'selected': None, 'correct': False, 'correction': 'B'}, 
                    {'No': '18', 'selected': None, 'correct': False, 'correction': 'C'}, 
                    {'No': '19', 'selected': None, 'correct': False, 'correction': 'B'}, 
                    {'No': '20', 'selected': None, 'correct': False, 'correction': 'D'}
                ],
            'max_score': 19,
            'obtained': 0
        }
    ]


    # {name:str, code:str, script:list(dict), score_gotten:int }

    for script in scripts:
        # subject code is the first key in the script dictionary
        subCode = list(script.keys())[0] # subCode
        subName = subjects[subCode] # subject name

        subScript = script[subCode] # script
        score_obtained = script['obtained']

        temp = {'sub': subName, 'code': subCode, 'subject_data': subScript, 'score_obtained': score_obtained}
        response.append(temp)
        temp = None

    # print(response)



    # print(response)
    subject_list = list(subjects.values())

    context = {'subjects': subject_list, 'data': response}
    # print()
    # print(context['data'])
    


    return render(request, 'check_test.html', context)#,'reply': response.values()})


# Order of arguments
# testData first, userSubject second, and examSubmittedData third
def ParseDataForMarking(examData, userSubjects, examResponse):
    """
    A fucntion to Parse the Informations needed for Marking
    To use -> def ParseDataForMarking(examData, userSubjects, examResponse)

    Parameters: examData, userSubjects, examResponse
    examData(dict) -> which is testData, this is the examination or practise data (usually from Cookie or session)
        sample -> {'name': 'English', 'start': '1', 'stop': '10', 'quest_range': 10},
    
    userSubject (dict) -> subjects the user offers, usually from cookie or session
        sample -> {'code': 'ENG', 'name': 'English'},
                  {'code': 'MTH', 'name': 'Mathematics'}
    
    examResponse (dict) -> Answers submitted from exam, the main data to be marked
        sample -> {
                  'ENG1': ['A'], 'ENG2': ['B'], 'ENG4': ['A'], 'ENG5': ['C'], 
                  'ENG6': ['D'], 'CHM2': ['D'], 'CHM3': ['B'], 'CHM4': ['C'],
                  'CHM5': ['B'], 'CHM6': ['A']
                  }


    returns -> list of list
    >> format -> [ [ {subjects_info}, (question range tuple,) , {submitted test info}] ]


    """

    sub_data = []  # the big list
    subjects_info = []
    for scriptKey in examResponse.keys():
        for sub in userSubjects:
            if scriptKey.startswith(sub['code']):
                if sub not in subjects_info:
                    subjects_info.append(sub)
                else:
                    continue

    for subj in subjects_info:
        for td in examData:
            if subj['name'] == td['name']:
                start = int(td['start'])
                stop = int(td['stop'])

                scp = {k: v for k, v in examResponse.items()
                       if k.startswith(subj['code'])}
                sub_data.append([subj, (start, stop), scp])

            else:
                continue

    # print(sub_data)
    return sub_data




## Function that Does the Marking
def marker(practise_data, user_practise_data, addBonus=False):
    # Mark A subject once at a time
    """
    Mark A subject once at a time
    To use -> def marker(practise_data, user_practise_data)
    returns -> dict {subject_code(str): [{question_indexNo: str, 'selected':str,'correct':bool, 'correction':str }], max_score: int, obtained: int }

    where:
        practise_data -> dictionary of submitted answers of the subjects 
            e.g-- { 'CHM2': ['D'], 'CHM3': ['B'],...,'CHM6': ['A'], 'CHM10':['D'] }
        
        user_practise_data -> list of subject information(dict) and question range(tuple) 
        (i.e [{code: str, name: str}, (start, stop)])

            e.g-- [ {'code': 'CHM', 'name': 'Chemistry'}, (1, 10)]
        
        addBonus (positional) -> Bool (True by default)
            if addBonus is True, then if answer selected is None and Correct answer is None too
            then it will add 1 to the score
    """
    # user_practise_data # data to be received from Any function calling it

    user_data = user_practise_data[0]
    start, stop = user_practise_data[1]  # (2, 20)

    # Get the subject name and map to subject code
    # user_data is a variable having the subject info

    # subject code:Subject Name
    subject_names = {user_data['code']: user_data['name']}
    # print(subject_codes, subjects)
    # print(subject_names)

    # Create Dictionary that should contain subject code:list of answers
    # Iterate throught the subject codes
    # Get the subjects key name in the file
    # get the list of all questions attempted
    # update result dictionary with subject code: question list

    # Create Dictionary => result
    # Create with suject codes as keys
    # Result dictionary holds the marked data

    # Make Result a dictionary of this format
    # {subject_code: [{question_indexNo: int, 'selected':str,'correct':bool, 'correction':str }]}

    result = {}

    # maximum score obtainable and score obtained
    max_score = 0
    score = 0
    # remark: add Remark feature later

    for scode, sname in subject_names.items():
        # sname = subject_names[scode]
        quest_list = get_quest_range(data[sname], _from=start, _to=stop)

        quest_list = list(map(str, quest_list))

        # add max score to result
        # which is the how many questions attempted
        # e.g if start is 1 and stop is 10, max_score = 10
        max_score = len(quest_list)

        # set the question index ranges  to subject code
        result[scode] = quest_list

    # Result sample output -> {'MTH': []}
    # print(result)

    for code, value in result.items():

        # Return the subject's data using subject code
        subj = data[subject_names[code]]  # Marking Guide for that subject
        # subj sample output -> {'short': 'Maths', 'code': 'MTH', '1': 'B', '2': 'C', '3': 'C', '4': 'A', '5': 'B'}
        # print(subj)

        # Value is a list -> [],
        # which will contain [{question_indexNo: int, 'selected':str,'correct':bool, 'correction':str }]
        # as elements

        # Seperate the code from index number
        # sample:  ENG11 -> 11, i.e English number 11
        # print(practise_data)
        # list of all the answers selected index number of that subject
        ans_index = [n.replace(code, '')
                     for n in practise_data.keys() if n.startswith(code)]
        # print(code, "=>", ans_index)
        # print()

        # result[code].extend(quest_list)

        # Mark the answers selcted at that index
        # like mark the option selected at English number 11
        # e.g A was selected, then compare if A is the correct answer in the Guide
        for each in quest_list:  # ans_index:
            # each answer is assumed to be present within the range
            # So each is assumed

            temp_ans = {'No': each}  # No means Number

            correct_one = subj[each]  # Get correct answer from Guide
            if each in ans_index:  # value #.keys():

                # Get answer from practise_data
                # [0] if the answers are likr this ['A']
                option_gotten = practise_data[code+each][0]
                # Check if correct, incorrect or Bonus.
                # Bonus is when correct_one is None
                isCorrect = option_gotten == correct_one if correct_one is not None else correct_one

                if isCorrect is True:

                    score += 1

                # Keep this line for future marking debug
                # print("For {}) Choose => {}, correct => {}, {}".format(code+each, option_gotten, correct_one, (isCorrect, 'Bonus')[isCorrect is None]))
                # print()

                # Replace the Old None with dictionary value
                # value[each] = {'selected': option_gotten,'correct': isCorrect, 'correction': correct_one}
                temp_ans.update({'selected': option_gotten,
                             'correct': isCorrect, 'correction': correct_one})

                num_index = quest_list.index(each)

                value[num_index] = temp_ans
            else:
                # if the code get here, that means that answer index was not answered (untouched)
                # As for the untouched values.
                # if there be any option that was not answered, which should be None
                # set option to None, which could evaluate to Bonus if correct_option is None also

                # correct_one = subj[each]
                option_gotten = None
                isCorrect = option_gotten == correct_one

                # print(isCorrect)
                # Give Bonus if there is no answer and addBonus is True
                if isCorrect and addBonus:
                    score += 1

                temp_ans.update({'selected': option_gotten,
                             'correct': isCorrect, 'correction': correct_one})

                num_index = quest_list.index(each)

                value[num_index] = temp_ans

    # Format-> { subject_code: { question_indexNo:
    #                                  { 'choose':str,'correct':bool, 'correction':str} }
    #           }

    # before leaving the function
    # qucikly add the score to result
    # and max_score to result
    result['max_score'] = max_score
    result['obtained'] = score

    return result  # Marked :)

    


    


