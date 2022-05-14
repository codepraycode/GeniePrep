from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Questions, TestLogs
from users.models import Users

# Create your views here.


class QuestionView(APIView):

    def get(self, request, format=None):
        
        _from = request.GET.get('fr',None)
        _to = request.GET.get('to', 0)
        _limit = request.GET.get('li', "")
        
        allquestions = Questions.objects.all()
        
        questions = []
        
        try:
            _from = int(_from)
            _to = int(_to)
            # _limit = int(limit)
        except :
            _from = None
            _to = 0
            # _limit= 0
            
        if(_from is not None):

            for ec in allquestions:
                ind = ec.index
                
                if (int(ind) >= _from):
                    if((_to > _from) and int(ind) > _to):
                        break
                    questions.append(ec.data)
            
        else:
            for e in allquestions:#.values():
                # print(e)
                questions.append(e.data)
        
        
        if(_limit.isnumeric()):
            _limit = int(_limit)
            questions = questions[:_limit]
        
        
        # print(questions)
        return Response(questions, status=status.HTTP_200_OK);

class TestView(APIView):
    # serializer_class = SubmitSerializer
    
    def post(self, req):
        
        # print("Data >> ",req.data)
        fellow = Users.objects.last()
        res = getReport(req.data, fellow)
        
        return Response(res, status=status.HTTP_200_OK)

    def get(self, req, testId=None):
        # print(testId)
        fellow = Users.objects.last()
        
        if(testId is not None):
            
            logs = TestLogs.objects.filter(user=fellow.id, id=testId)
        else:
            logs = TestLogs.objects.filter(user=fellow.id)
        
        res = []
        
        for i in logs:
            res.append(i.getLog())
        
        return Response(res, status=status.HTTP_200_OK)
        

def getReport(data, user):
    ''' 
    [
        {
            "id": 1,
            "answer": "option-1"
        },
        {
            "id": 2,
            "answer": "option-2"
        }
    ] 
    '''
    
    markings =  []
    obtained = 0
    
    total = len(data)

    for each in data:
        correct = None
        try:
            d_quest = Questions.objects.get(id=each['id'])
        except:
            # The Question Was Not Found
            print("not found")
            markings.append({
                **each,
                "correct": correct
            })
            continue

        answer = each['answer'].split("-")[-1]
        # print(answer)
        correct = d_quest.isCorrect(answer)
        
        if(correct):
            obtained += 1

        markings.append({
            **each,
            "correct": correct
        })

    # percentage = round(obtained/total, 2)
    
    # Add the Log
    log = TestLogs.objects.create(user=user, obtained=obtained, max_obtainable=total, data=f"""{markings}""")
    
    log.save()
    
    return log.getLog()
