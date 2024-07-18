import sys
sys.setrecursionlimit(1000000)
from collections import defaultdict
from math import *
from heapq import*
import time
import turtle as t
lang=0
image1 = "Webp.net-resizeimage.gif"
t.bgpic(image1)
tt=t.Turtle()
tt.penup()
tt.goto(0,0)
tt.pensize(5)
tt.color('red')
# lang = 0 -> 한국어(초기설정)
# lang = 1 -> 영어
# lang = 2 -> 일본어
def intinput(a):
    t=''
    for i in a:
        if '0'<=i<='9':
            t+=i
    if len(t)==0:
        if lang==0:
            print('무언가 잘못되었습니다.')
            return intinput(input("다시 입력"))
        elif lang==1:
            print('Something is Wrong')
            return intinput(input('Re-enter'))
        else:
            print('入力が間違っています')
            return intinput(input("もう一度入力お願いします"))
    return int(t)
def 학반(a):
    if ('학년' in a) and ('반' in a):
        a.replace(' ','')
        a.replace('학년','-')
        a.replace('반','')
    return a
graph={
    '진로관 1층 계단':{'진로관 2층 계단':18000,'진로관 1층 중앙':5000},
    '진로관 1층 중앙':{'시청각실':10000,'교과교실2':13500,'진로관 1층 화장실':8000,'진로관 1층 계단':5000},
    '1층통로':{'교과교실1':23000,'2층통로':18000,'과학교실3':4500,'창학관 - 세종관 이음길':10000},
    '시청각실':{'진로관 1층 중앙':10000},
    '교과교실2':{'진로관 1층 중앙':13500,'교과교실1':9000},
    '교과교실1':{'1층통로':23000,'교과교실2':9000},
    '진로관 1층 화장실':{'진로관 1층 중앙':8000},
    '진로관 2층 중앙':{'진로관 2층 화장실':8000,'진로관 2층 계단':5000,'3학년 교무실':9000,'3-2':9000},
    '진로관 2층 계단':{'진로관 2층 중앙':5000,'진로관 1층 계단':18000,'진로관 3층 계단':18000},
    '진로관 2층 화장실':{'진로관 2층 중앙':8000},
    '3-2':{'3-3':9000,'진로관 2층 중앙':9000},
    '3-3':{'3-2':9000},
    '3-1':{'3학년 교무실':9000,'2층통로':40500},
    '3학년 교무실':{'진로관 2층 중앙':9000,'3-1':9000},
    '2층통로':{'1층통로':18000,'3-1':40500, '3층통로':18000,'창의융합실':12500},
    '진로관 3층 계단':{'진로관 3층 중앙':5000,'진로관 2층 계단':18000},
    '진로관 3층 중앙':{'진로관 3층 화장실':8000,'진로관 3층 계단':5000,'3-7':13500,'3-6':13500},
    '진로관 3층 화장실':{'진로관 3층 중앙':8000},
    '3-7':{'진로관 3층 중앙':13500,'3-8':9000},
    '3-8':{'3-7':9000},
    '3-6':{'진로관 3층 중앙':13500,'3-5':9000},
    '3-5':{'3-6':9000,'3-4':9000},
    '3-4':{'교과교실3':9000,'3-5':9000},
    '교과교실3':{'3-4':9000,'3층통로':22500},
    '3층통로':{'교과교실3':22500,'2층통로':18000,'프로파일실':9000},
    
    '과학교실3':{'1층통로':4500,'공동교육과정 온라인교실':9000,'생물실':9000},
    '공동교육과정 온라인교실':{'과학교실3':9000,'창학관 1층 중앙':10000,'생물실':9000},
    '창학관 1층 중앙':{'창학관 1층 현관':5000,'공동교육과정 온라인교실':10000,'다락':9000,'창학관 1층 화장실':18000,'통로':14000,'창학관 1층 계단':2500},
    '창학관 1층 화장실':{'창학관 1층 중앙':18000},
    '다락':{'창학관 1층 중앙':9000},
    '창학관 1층 계단':{'창학관 1층 중앙':2500,'창학관 2층 계단':15000},
    '창학관 1층 현관':{'본관 2층 중앙':50000,'창학관 1층 중앙':5000},
    '생물실':{'공동교육과정 온라인교실':9000,'과학교실3':9000},

    '창학관 2층 계단':{'창학관 1층 계단':15000,'창학관 2층 중앙':2500,'창학관 3층 계단':15000},
    '창학관 2층 중앙':{'융합교육부':15000,'창학관 2층 화장실':7500,'컴퓨터실':9000,'과학 동아리실':2500,'지구과학실':9000,'창의융합실':6000,'창학관 2층 계단':2500},
    '창의융합실':{'창학관 2층 중앙':6000,'2층통로':12500,'지구과학실':4000},
    '지구과학실':{'창학관 2층 중앙':9000,'창의융합실':4000},
    '창학관 2층 화장실':{'창학관 2층 중앙':7500},
    '컴퓨터실':{'창학관 2층 중앙':9000},
    '과학 동아리실':{'창학관 2층 중앙':2500},
    '융합교육부':{'창학관 2층 중앙':15000},

    '창학관 3층 계단':{'창학관 2층 계단':15000,'창학관 3층 중앙':4000},
    '창학관 3층 중앙':{'창학관 3층 화장실':7500,'창학관 3층 계단':4000,'연구실':15000,'멀티미디어실':6500,'Wee class':2500},
    '창학관 3층 화장실':{'창학관 3층 중앙':7500,'연구실':5000},
    '연구실':{'창학관 3층 화장실':5000},
    '멀티미디어실':{'창학관 3층 중앙':6500},
    '화학실':{'창학관 3층 중앙':9000},
    'Wee class':{'창학관 3층 중앙':2500,'화학실':9500},
    '화학실':{'Wee class':9500,'프로파일실':2500},
    '프로파일실':{'화학실':2500,'3층통로':9000},
    
    '통로':{'창학관 1층 중앙':14000,'본관 2층 우측 계단':27000,'세종관 입구':15000},
    
    '본관 2층 우측 계단':{'통로':27000,'본관 2층 우측 화장실':4000,'보건실':8500,'본관 3층 우측 계단':15000},
    '본관 2층 우측 화장실':{'본관 2층 우측 계단':4000},
    '보건실':{'본관 2층 우측 계단':8500,'교육정보실':9000},
    '교육정보실':{'보건실':9000,'학생생활안전교육부':9000},
    '학생생활안전교육부':{'교육정보실':9000,'본관 2층 중앙':9000},
    '본관 2층 중앙':{'창학관 1층 현관':50000,'학생생활안전교육부':9000,'본관 2층 중앙 계단':9000,'후관 입구':15000},
    '본관 2층 중앙 계단':{'본관 2층 중앙':9000,'본관 3층 중앙 계단':15000,'방송실':4500,'본관 1층 우측 계단':15000},
    '방송실':{'본관 2층 중앙 계단':4500,'교무실':13500},
    '교무실':{'방송실':13500,'2층 원형 계단':2500,'교장실':13500},
    '2층 원형 계단':{'교무실':2500,'1층 원형 계단':15000},
    '교장실':{'교무실':13500,'창의인재부':9000},
    '창의인재부':{'교장실':9000,'본관 2층 좌측 계단':6500},
    '본관 2층 좌측 화장실':{'본관 2층 좌측 계단':2500},
    '본관 2층 좌측 계단':{'본관 2층 좌측 화장실':2500,'본관 1층 좌측 계단':15000,'본관 3층 좌측 계단':15000,'창의인재부':6500},
    
    '본관 1층 우측 계단':{'본관 2층 중앙 계단':15000,'발간실':4500,'보일러실':4500},
    '보일러실':{'본관 1층 우측 계단':4500},
    '발간실':{'본관 1층 우측 계단':4500,'행정실':9000},
    '행정실':{'발간실':9000,'본관 1층 중앙':4500},
    '본관 1층 중앙':{'행정실':4500,'1층 원형 계단':2500,'문서고':7000},
    '1층 원형 계단':{'본관 1층 중앙':2500,'2층 원형 계단':15000},
    '문서고':{'본관 1층 중앙':7000,'학습도움실2':6500},
    '학습도움실2':{'문서고':6500,'학습도움실1':9000},
    '학습도움실1':{'학습도움실2':9000,'본관 1층 좌측 계단':6500},
    '본관 1층 화장실':{'본관 1층 좌측 계단':2500},
    '본관 1층 좌측 계단':{'본관 1층 화장실':2500,'본관 2층 좌측 계단':15000,'학습도움실1':6500,'경비실':1},
    
    '본관 3층 우측 계단':{'본관 2층 우측 계단':15000,'본관 4층 우측 계단':15000,'본관 3층 우측 화장실':2000,'1-8':8500},
    '본관 3층 우측 화장실':{'본관 3층 우측 계단':2000},
    '1-8':{'본관 3층 우측 계단':8500,'1-7':9000},
    '1-7':{'1-8':9000,'1-6':9000},
    '1-6':{'1-7':9000,'3층 홈베이스':2500,'1-5':9000},
    '1-5':{'1-6':9000,'본관 3층 중앙 계단':9000},
    '3층 홈베이스':{'1-6':2500,'후관 2층 계단':15000,'후관 3층 좌측 계단':15000},
    '본관 3층 중앙 계단':{'본관 2층 중앙 계단':15000,'본관 4층 중앙 계단':15000,'1학년 교무실':4500,'1-5':9000},
    '1학년 교무실':{'본관 3층 중앙 계단':4500,'1-4':9000},
    '1-4':{'1학년 교무실':9000,'1-3':9000},
    '1-3':{'1-4':9000,'1-2':9000},
    '1-2':{'1-3':9000,'1-1':9000},
    '1-1':{'1-2':9000,'본관 3층 좌측 계단':6500},
    '본관 3층 좌측 계단':{'본관 3층 좌측 화장실':2500,'본관 2층 좌측 계단':15000,'본관 4층 좌측 계단':15000,'1-1':6500},
    '본관 3층 좌측 화장실':{'본관 3층 좌측 계단':2500},
    
    '본관 4층 우측 계단':{'본관 3층 우측 계단':15000,'본관 4층 우측 화장실':2000,'2-8':8500},
    '본관 4층 우측 화장실':{'본관 4층 우측 계단':2000},
    '2-8':{'본관 4층 우측 계단':8500,'2-7':9000},
    '2-7':{'2-8':9000,'2-6':9000},
    '2-6':{'2-7':9000,'4층 홈베이스':2500,'2-5':9000},
    '2-5':{'2-6':9000,'본관 4층 중앙 계단':9000},
    '4층 홈베이스':{'2-6':2500,'후관 3층 좌측 계단':15000,'후관 4층 좌측 계단':15000},
    '본관 4층 중앙 계단':{'본관 3층 중앙 계단':15000,'2학년 교무실':4500,'2-5':9000},
    '2학년 교무실':{'본관 4층 중앙 계단':4500,'2-4':9000},
    '2-4':{'2학년 교무실':9000,'2-3':9000},
    '2-3':{'2-4':9000,'2-2':9000},
    '2-2':{'2-3':9000,'2-1':9000},
    '2-1':{'2-2':9000,'본관 4층 좌측 계단':6500},
    '본관 4층 좌측 계단':{'본관 4층 좌측 화장실':2500,'본관 3층 좌측 계단':15000,'2-1':6500},
    '본관 4층 좌측 화장실':{'본관 4층 좌측 계단':2500},
    
    '후관 입구':{'본관 2층 중앙':15000,'후관 2층 계단':7500,'미술실':10000},
    '후관 2층 계단':{'후관 입구':7500,'3층 홈베이스':15000,'후관 3층 좌측 계단':7500},
    '미술실':{'후관 입구':10000},
    '후관 3층 좌측 계단':{'3층 홈베이스':15000,'후관 2층 계단':7500,'방통고협의실':2250,'후관 4층 좌측 계단':15000,'4층 홈베이스':15000},
    '방통고협의실':{'후관 3층 좌측 계단':2250,'방송통신고 교무실':4500},
    '방송통신고 교무실':{'방통고협의실':4500,'영어교실':9000},
    '영어교실':{'방송통신고 교무실':9000,'국어교실':9000},
    '국어교실':{'영어교실':9000,'후관 3층 우측계단':6500},
    '후관 3층 화장실':{'후관 3층 우측계단':2500},
    '후관 3층 우측계단':{'국어교실':6500,'후관 3층 화장실':2500,'후관 4층 우측 계단':10000},
    '후관 4층 좌측 계단':{'4층 홈베이스':15000,'후관 3층 좌측 계단':15000,'사회교실1':4500},
    '사회교실1':{'후관 4층 좌측 계단':4500,'수학교실1':9000},
    '수학교실1':{'사회교실1':9000,'수학교실2':9000},
    '수학교실2':{'수학교실1':9000,'후관 4층 우측 계단':6500},
    '후관 4층 화장실':{'후관 4층 우측 계단':2500},
    '후관 4층 우측 계단':{'수학교실2':6500,'후관 3층 우측계단':10000,'후관 4층 화장실':2500},
    '세종관 입구':{'통로':15000,'매점':10000,'세종관 1층 중앙':6200},
    '세종관 1층 중앙':{'세종관 입구':6200,'진로진학상담부':3600,'세종관 1층 화장실':4250,'세종관 1층 계단':3000,'인문사회부':6200,'도서관':3600},
    '진로진학상담부':{'세종관 1층 중앙':3600},
    '세종관 1층 화장실':{'세종관 1층 중앙':4250},
    '인문사회부':{'세종관 1층 중앙':6200},
    '도서관':{'세종관 1층 중앙':3600},
    '세종관 1층 계단':{'세종관 1층 중앙':3000,'세종관 2층 계단':12000},
    '세종관 2층 계단':{'세종관 1층 계단':12000,'2학년 야자실':3000,'세종관 3층 계단':12000},
    '2학년 야자실':{'세종관 2층 계단':3000},
    '세종관 3층 계단':{'세종관 2층 계단':12000,'1학년 야자실':3000},
    '1학년 야자실':{'세종관 3층 계단':3000},
    '매점':{'세종관 입구':10000,'창학관 - 세종관 이음길':10000},
    '경비실':{'본관 1층 좌측 계단':1},
    '창학관 - 세종관 이음길' : {'매점': 10000,'1층통로':10000},
}
English_keys = {
        '진로관 1층 계단': 'The stairs on the 1st floor of the Jinro building',
        '진로관 1층 중앙': 'The center of the 1st floor of Jinro Building',
        '1층통로': 'a first-floor passageway',
        '시청각실': 'AV room',
        '교과교실2': 'Curriculum Classroom 2',
        '교과교실1': 'Curriculum Classroom 1',
        '진로관 1층 화장실': 'restroom on the 1st floor of Jinro Building',
        '진로관 2층 중앙': 'The center of the 2nd floor of Jinro Building',
        '진로관 2층 계단': 'The stairs on the 2nd floor of the Jinro building',
        '진로관 2층 화장실': 'restroom on the 2nd floor of Jinro Building',
        '3-2': '3-2',
        '3-3': '3-3',
        '3-1': '3-1',
        '3학년 교무실': "Teachers' Office for 3rd Graders",
        '2층통로': 'a two-story passageway',
        '진로관 3층 계단': 'The stairs on the 3rd floor of the Jinro building',
        '진로관 3층 중앙': 'The center of the 3rd floor of Jinro Building',
        '진로관 3층 화장실': 'restroom on the 3rd floor of Jinro Building',
        '3-7': '3-7',
        '3-8': '3-8',
        '3-6': '3-6',
        '3-5': '3-5',
        '3-4': '3-4',
        '교과교실3': 'Curriculum Classroom 3',
        '3층통로': 'a third-floor passageway',
        '과학교실3': 'a science Classroom 3',
        '공동교육과정 온라인교실': 'an online classroom in a joint curriculum',
        '창학관 1층 중앙': 'The center of the 1st floor of Changhak building',
        '창학관 1층 화장실': 'The restroom on the 1st floor of Changhak building',
        '다락': 'Darak',
        '창학관 1층 계단': 'The stairs on the 1st floor of the Changhak building',
        '창학관 1층 현관': 'The entrance to the 1st floor of Changhak Building',
        '생물실': 'a living room',
        
        '창학관 2층 계단': 'The stairs on the 2nd floor of the Changhak building',
        '창학관 2층 중앙': 'The center of the 2nd floor of Changhak building',
        '창의융합실': 'a creative fusion room',
        '지구과학실': 'Earth Science room',
        '창학관 2층 화장실': 'The restroom on the 2nd floor of Changhak building',
        '컴퓨터실': 'Computer Lab',
        '과학 동아리실': 'Science club room',
        '융합교육부': 'Ministry of Convergence Education',
        
        '창학관 3층 계단': 'The stairs on the 3rd floor of the Changhak building',
        '창학관 3층 중앙': 'The center of the 3rd floor of Changhak building',
        '창학관 3층 화장실': 'The restroom on the 3rd floor of Changhak building',
        '연구실': 'a laboratory',
        '멀티미디어실': 'Multimedia room',
        '화학실': 'a chemistry room',
        'Wee class': 'Wee class',
        '프로파일실': 'Profile room',
        
        '통로': 'passageway',
        
        '본관 2층 우측 계단': 'the stairs to the right on the 2nd floor of the main building',
        '본관 2층 우측 화장실': 'the restroom on the right side of the 2nd floor of the main building',
        '보건실': 'Health Room',
        '교육정보실': 'Education Information Office',
        '학생생활안전교육부': 'Ministry of Student Life Safety and Education',
        '본관 2층 중앙':'the center on the 2nd floor of the main building',
        '본관 2층 중앙 계단': 'the center stairs on the 2nd floor of the main building',
        '방송실': 'Broadcasting room',
        '교무실': "Teachers' Office",
        '2층 원형 계단': 'The circular staircase on the 2nd floor',
        '교장실': "principal's Office",
        '창의인재부': 'the Ministry of Creative Resources',
        '본관 2층 좌측 화장실': 'the restroom on the left side of the 2nd floor of the main building',
        '본관 2층 좌측 계단': 'the stairs to the left on the 2nd floor of the main building',
        
        '본관 1층 우측 계단': 'the stairs to the right on the 1st floor of the main building',
        '보일러실': 'a boiler room',
        '발간실': 'a publishing room',
        '행정실': 'administrative office',
        '본관 1층 중앙': 'The center of the 1st floor of the main building',
        '1층 원형 계단': 'The circular staircase on the 1st floor',
        '문서고': 'an archive',
        '학습도움실2': 'Learning Help Room 2',
        '학습도움실1': 'Learning Help Room 1',
        '본관 1층 화장실': 'the restroom of the 1st floor of the main building',
        '본관 1층 좌측 계단': 'the stairs to the left on the 1st floor of the main building',
        
        '본관 3층 우측 계단': 'the stairs to the right on the 3rd floor of the main building',
        '본관 3층 우측 화장실': 'the restroom on the right side of the 3rd floor of the main building',
        '1-8': '1-8',
        '1-7': '1-7',
        '1-6': '1-6',
        '1-5': '1-5',
        '3층 홈베이스': 'the home base on the 3rd floor',
        '본관 3층 중앙 계단': 'the center stairs on the 3rd floor of the main building',
        '1학년 교무실': "Teachers' Office for 1st Graders",
        '1-4': '1-4',
        '1-3': '1-3',
        '1-2': '1-2',
        '1-1': '1-1',
        '본관 3층 좌측 계단': 'the stairs to the left on the 3rd floor of the main building',
        '본관 3층 좌측 화장실': 'the restroom on the left side of the 3rd floor of the main building',
        
        '본관 4층 우측 계단': 'the stairs to the right on the 4th floor of the main building',
        '본관 4층 우측 화장실': 'the restroom on the right side of the 4th floor of the main building',
        '2-8': '2-8',
        '2-7': '2-7',
        '2-6': '2-6',
        '2-5': '2-5',
        '4층 홈베이스': 'the home base on the 4th floor',
        '본관 4층 중앙 계단': 'the center stairs on the 4th floor of the main building',
        '2학년 교무실': "Teachers' Office for 2nd Graders",
        '2-4': '2-4',
        '2-3': '2-3',
        '2-2': '2-2',
        '2-1': '2-1',
        '본관 4층 좌측 계단': 'the stairs to the left on the 4th floor of the main building',
        '본관 4층 좌측 화장실': 'the restroom on the left side of the 4th floor of the main building',
        '후관 입구':'the entrance to the rear building',
        '후관 2층 계단':'the 2nd floor of the rear building',
        '미술실':'art room',
        '후관 3층 좌측 계단':'the left staircase on the 3rd floor of the rear building',
        '방통고협의실':'Open Secondary Schools a consultation room',
        '방송통신고 교무실':"Open Secondary Schools Teachers' Office",
        '영어교실':'English room',
        '국어교실':'Korean room',
        '후관 3층 화장실':'a restroom on the 3rd floor of the rear building',
        '후관 3층 우측계단':'the right staircase on the 3rd floor of the rear building',
        '후관 4층 좌측 계단':'the left staircase on the 4th floor of the rear building',
        '사회교실1':'social room 1',
        '수학교실1':'math room 1',
        '수학교실2':'math room 2',
        '후관 4층 화장실':'a restroom on the 4th floor of the rear building',
        '후관 4층 우측 계단':'the right staircase on the 4th floor of the rear building',
        '세종관 입구':'Entrance of Sejong Building',
        '세종관 1층 중앙':'The center of the 1st floor of Sejong Building',
        '진로진학상담부':'Career counseling department',
        '세종관 1층 화장실':'1st floor restroom of Sejong Building',
        '인문사회부':'Department of Humanities and Social Affairs',
        '도서관':'Library of Ruina',
        '세종관 1층 계단':'1st floor stairs of Sejong Building',
        '세종관 2층 계단':'2nd floor stairs of Sejong Building',
        '2학년 야자실':'A self-study room for 2nd Graders',
        '세종관 3층 계단':'3st floor stairs of Sejong Building',
        '1학년 야자실':'A self-study room for 1st Graders',
        '매점':'store',
    '경비실':'A security office',
    '창학관 - 세종관 이음길':'Changhak Building - Road to Sejong Building',
}

Japanese_keys = {
        '진로관 1층 계단': 'ジンロ館一階の階段',
        '진로관 1층 중앙': 'ジンロ館1階中央',
        '1층통로': '1階通路',
        '시청각실': '視聴覚室',
        '교과교실2': '教科教室2',
        '교과교실1': '教科教室1',
        '진로관 1층 화장실': 'ジンロ館1階トイレ',
        '진로관 2층 중앙': 'ジンロ館2階中央',
        '진로관 2층 계단': 'ジンロ館二階の階段',
        '진로관 2층 화장실': 'ジンロ館2階トイレ',
        '3-2': '3-2',
        '3-3': '3-3',
        '3-1': '3-1',
        '3학년 교무실': '三年生の職員室',
        '2층통로': '2階通路',
        '진로관 3층 계단': 'ジンロ館三階の階段',
        '진로관 3층 중앙': 'ジンロ館3階中央',
        '진로관 3층 화장실': 'ジンロ館3階トイレ',
        '3-7': '3-7',
        '3-8': '3-8',
        '3-6': '3-6',
        '3-5': '3-5',
        '3-4': '3-4',
        '교과교실3': '教科教室3',
        '3층통로': '3階通路',
        '과학교실3': '科学教室3',
        '공동교육과정 온라인교실': '共同教育課程 オンライン教室',
        '창학관 1층 중앙': 'チャンハク館1階中央',
        '창학관 1층 화장실': 'チャンハク館1階のトイレ',
        '다락': '多樂',
        '창학관 1층 계단': 'チャンハク館1階の階段',
        '창학관 1층 현관':'チャンハク館1階の玄関',
        '생물실': '生物室',
        
        '창학관 2층 계단': 'チャンハク館2階の階段',
        '창학관 2층 중앙': 'チャンハク館2階中央',
        '창의융합실': '創意融合室',
        '지구과학실': '地球科学室',
        '창학관 2층 화장실': 'チャンハク館2階のトイレ',
        '컴퓨터실': 'コンピューター室',
        '과학 동아리실': '科学部室',
        '융합교육부': '融合教育部',
        
        '창학관 3층 계단': 'チャンハク館3階の階段',
        '창학관 3층 중앙': 'チャンハク館3階中央',
        '창학관 3층 화장실': 'チャンハク館3階のトイレ',
        '연구실': '研究室',
        '멀티미디어실': 'マルチメディア室',
        '화학실': '化学室',
        'Wee class': 'Wee class',
        '프로파일실': 'プロファイル室',

        '통로': '通路',

        '본관 2층 우측 계단': '本館2階右側の階段',
        '본관 2층 우측 화장실': '本館2階右側のトイレ',
        '보건실': '保健室',
        '교육정보실': '教育情報室',
        '학생생활안전교육부': '学生生活安全教育部',
        '본관 2층 중앙':'本館2階 中央',
        '본관 2층 중앙 계단': '本館2階 中央 かに段',
        '방송실': '放送室',
        '교무실': '職員室',
        '2층 원형 계단': '二階 円形 階段',
        '교장실': '校長室',
        '창의인재부': '創意人材部',
        '본관 2층 좌측 화장실': '本館2階左側のトイレ',
        '본관 2층 좌측 계단': '本館2階左側の階段',
        '본관 1층 우측 계단': '本館1階右側の階段',
        '보일러실': 'ボイラー室',
        '발간실': '発刊室',
        '행정실': '行政室',
        '본관 1층 중앙': '本館1階 中央 ',
        '1층 원형 계단': '一階 円形 階段',
        '문서고': '文書庫',
        '학습도움실2': '学習支援室2',
        '학습도움실1': '学習支援室1',
        '본관 1층 화장실': '本館1階トイレ',
        '본관 1층 좌측 계단': '本館1階左側の階段',
        '본관 3층 우측 계단': '本館3階右側の階段',
        '본관 3층 우측 화장실': '本館3階右側のトイレ',
        '1-8': '1-8',
        '1-7': '1-7',
        '1-6': '1-6',
        '1-5': '1-5',
        '3층 홈베이스': '3階 ホームベース',
        '본관 3층 중앙 계단': '本館3階 中央 かに段',
        '1학년 교무실': '一年生の職員室',
        '1-4': '1-4',
        '1-3': '1-3',
        '1-2': '1-2',
        '1-1': '1-1',
        '본관 3층 좌측 계단': '本館3階左側の階段',
        '본관 3층 좌측 화장실': '本館3階左側のトイレ',
        '본관 4층 우측 계단': '本館4階右側の階段',
        '본관 4층 우측 화장실': '本館4階右側のトイレ',
        '2-8': '2-8',
        '2-7': '2-7',
        '2-6': '2-6',
        '2-5': '2-5',
        '4층 홈베이스': '4階 ホームベース',
        '본관 4층 중앙 계단': '本館4階 中央 かに段',
        '2학년 교무실': '二年生の職員室',
        '2-4': '2-4',
        '2-3': '2-3',
        '2-2': '2-2',
        '2-1': '2-1',
        '본관 4층 좌측 계단': '本館4階左側の階段',
        '본관 4층 좌측 화장실': '本館4階左側のトイレ','후관 입구':'後管入口',
        '후관 2층 계단':'後館二階階段',
        '미술실':'美術室',
        '후관 3층 좌측 계단':'後館3階左側の階段',
        '방통고협의실':'放送通信高等學校協議室',
        '방송통신고 교무실':'放送通信高等學校の職員室',
        '영어교실':'英語教室',
        '국어교실':'国語教室',
        '후관 3층 화장실':'後館3階トイレ',
        '후관 3층 우측계단':'後館3階右側階段',
        '후관 4층 좌측 계단':'後館4階左側の階段',
        '사회교실1':'社会教室1',
        '수학교실1':'数学教室1',
        '수학교실2':'数学教室2',
        '후관 4층 화장실':'後館4階トイレ',
        '후관 4층 우측 계단':'後館4階右側階段',
        '세종관 입구':'世宗館入口',
        '세종관 1층 중앙':'世宗館1階中央',
        '진로진학상담부':'進路進学相談部',
        '세종관 1층 화장실':'世宗館1階のトイレ',
        '인문사회부':'人文社会部',
        '도서관':'図書館',
        '세종관 1층 계단':'世宗館1階の階段',
        '세종관 2층 계단':'世宗館2階の階段',
        '2학년 야자실':'2年生の夜間自律学習室',
        '세종관 3층 계단':'世宗館3階の階段',
        '1학년 야자실':'1年生の夜間自律学習室',
        '매점':'売店',
        '경비실':'警備室',
        '창학관 - 세종관 이음길':'チャンハク館 - 世宗館館の結ぶ道',
}

coor={
    '진로관 1층 계단':(448,0),
    '진로관 1층 중앙':(448,0),
    '1층통로':(310,-15),
    '시청각실':(460,15),
    '교과교실2':(430,-15),
    '교과교실1':(400,-15),
    '진로관 1층 화장실':(460,-30),
    
    '진로관 2층 중앙':(448,55),
    '진로관 2층 계단':(448,55),
    '진로관 2층 화장실':(460,45),
    '3-2':(460,75),
    '3-3':(460,95),
    '3-1':(370,45),
    '3학년 교무실':(400,45),
    '2층통로':(310,45),
    
    '진로관 3층 계단':(448,118),
    '진로관 3층 중앙':(448,118),
    '진로관 3층 화장실':(460,110),
    '3-7':(460,150),
    '3-8':(460,160),
    '3-6':(430,110),
    '3-5':(400,110),
    '3-4':(370,110),
    '교과교실3':(330,110),
    '3층통로':(310,110),
    
    '과학교실3':(250,-10),
    '공동교육과정 온라인교실':(200,-10),
    '창학관 1층 중앙':(200,-35),
    '창학관 1층 화장실':(130,-10),
    '다락':(150,-50),
    '창학관 1층 계단':(170,-10),
    '생물실':(250,-50),
    '창학관 1층 현관':(200,-50),
    '창학관 2층 계단':(200,60),
    '창학관 2층 중앙':(200,40),
    '창의융합실':(250,60),
    '지구과학실':(250,25),
    '창학관 2층 화장실':(170,60),
    '컴퓨터실':(130,25),
    '과학 동아리실':(200,25),
    '융합교육부':(130,60),
    
    '창학관 3층 계단':(200,130),
    '창학관 3층 중앙':(200,110),
    '창학관 3층 화장실':(170,130),
    '연구실':(130,130),
    '멀티미디어실':(150,90),
    '화학실':(250,90),
    'Wee class':(230,130),
    '프로파일실':(270,130),
    
    '통로':(0,160),
    
    '본관 2층 우측 계단':(-120,145),
    '본관 2층 우측 화장실':(-120,160),
    '보건실':(-120,130),
    '교육정보실':(-120,100),
    '학생생활안전교육부':(-120,70),
    '본관 2층 중앙 계단':(-120,-10),
    '본관 2층 중앙':(-120,20),
    '방송실':(-120,-30),
    '교무실':(-120,-70),
    '2층 원형 계단':(-150,-80),
    '교장실':(-120,-90),
    '창의인재부':(-120,-140),
    '본관 2층 좌측 화장실':(-120,-180),
    '본관 2층 좌측 계단':(-120,-160),
    
    '본관 1층 우측 계단':(-100,-10),
    '보일러실':(-100,47),
    '발간실':(-100,5),
    '행정실':(-100,-30),
    '본관 1층 중앙':(-100,-50),
    '1층 원형 계단':(-100,-80),
    '문서고':(-100,-70),
    '학습도움실2':(-100,-90),
    '학습도움실1':(-100,-140),
    '본관 1층 화장실':(-100,-180),
    '본관 1층 좌측 계단':(-100,-160),
    
    '본관 3층 우측 계단':(-160,145),
    '본관 3층 우측 화장실':(-160,160),
    '1-8':(-160,130),
    '1-7':(-160,100),
    '1-6':(-160,70),
    '1-5':(-160,47),
    '3층 홈베이스':(-160,20),
    '본관 3층 중앙 계단':(-160,5),
    '1학년 교무실':(-160,-30),
    '1-4':(-160,-50),
    '1-3':(-160,-70),
    '1-2':(-160,-90),
    '1-1':(-160,-140),
    '본관 3층 좌측 계단':(-160,-160),
    '본관 3층 좌측 화장실':(-160,-180),
    
    '본관 4층 우측 계단':(-200,145),
    '본관 4층 우측 화장실':(-200,160),
    '2-8':(-200,130),
    '2-7':(-200,100),
    '2-6':(-200,70),
    '2-5':(-200,47),
    '4층 홈베이스':(-200,20),
    '본관 4층 중앙 계단':(-200,5),
    '2학년 교무실':(-200,-30),
    '2-4':(-200,-50),
    '2-3':(-200,-70),
    '2-2':(-200,-90),
    '2-1':(-200,-140),
    '본관 4층 좌측 계단':(-200,-160),
    '본관 4층 좌측 화장실':(-200,-180),

    
    #후관 2층
    '후관 입구':(-300,30),
    '후관 2층 계단':(-300,30),
    '미술실':(-300,50),

    #후관 3층
    '후관 3층 좌측 계단':(-350,30),
    '방통고협의실':(-350,50),
    '방송통신고 교무실':(-350,70),
    '영어교실':(-350,100),
    '국어교실':(-350,120),
    '후관 3층 화장실':(-350,160),
    '후관 3층 우측계단':(-350,145),

    '후관 4층 좌측 계단':(-390,30),
    '사회교실1':(-390,50),
    '수학교실1':(-390,100),
    '수학교실2':(-390,120),
    '후관 4층 화장실':(-390,160),
    '후관 4층 우측 계단':(-390,145),

    '세종관 입구':(-25,220),
    '세종관 1층 중앙':(-25,240),
    '진로진학상담부':(-80,250),
    '세종관 1층 화장실':(-50,250),
    '인문사회부':(0,245),
    '도서관':(0,255),
    '세종관 1층 계단':(-25,250),
    '세종관 2층 계단':(-25,270),
    '2학년 야자실':(-25,270),
    '세종관 3층 계단':(-25,300),
    '1학년 야자실':(-25,300),
    '매점':(100,250),
    '경비실':(10,-300),
    '창학관 - 세종관 이음길':(300,170)
}
num=list(graph.keys())
def 목적지(start,end):
    q=[]
    visited=defaultdict(lambda:sys.maxsize)
    cur=0
    t=[]
    heappush(q,(0,start))
    visited[start]=0
    while q:
        x,y=heappop(q)
        if visited[y]<x:
            continue
        for i in graph[y]:
            if visited[i]<=graph[y][i]+x:
                continue
            else:
                cost=graph[y][i]+x
                visited[i]=cost
                heappush(q,(cost,i))
    cur=end
    t=[end]
    last=cur
    while cur!=start:
        last=cur[::]
        for i in graph[cur]:
            if visited[cur]-visited[i]==graph[cur][i]:
                t.append(i)
                cur=i
                break

        #디버깅용 코드
        if last==cur:
            #문제가 있으면 출력
            print(start,end,cur)
            exit()
    return t
def 위치설정():
    if lang==0:
        t=0
        maxv=len(graph)//10
        while True:
            if t!=maxv:
                for i in range(10):
                    print(f"[{i+t*10}] - {num[i+t*10]}")
            else:
                for i in range(len(graph)%10):
                    print(f'[{i+t*10}] - {num[i+t*10]}')
            if t!=0:
                print('[300] - 이전 페이지',end=' ')
            if t!=maxv:
                print('[301] - 다음 페이지')
            else:
                print()
            n=intinput(input())
            if n==300 and t!=0:
                t-=1
            elif n==301 and t!=maxv:
                t+=1
            else:
                if 0<=n and n<len(num):
                    print(f"{num[n]} 이(가) 맞으십니까?")
                    print('[0] - 맞다  [1] - 아니다')
                    a=intinput(input())
                    if a==0:
                        return num[n]
                else:
                    print('잘못된 입력입니다.')
    elif lang==1:
        t=0
        maxv=len(graph)//10
        while True:
            if t!=maxv:
                for i in range(10):
                    print(f"[{i+t*10}] - {English_keys[num[i+t*10]]}")
            else:
                for i in range(len(graph)%10):
                    print(f'[{i+t*10}] - {English_keys[num[i+t*10]]}')
            if t!=0:
                print('[300] - Previous',end=' ')
            if t!=maxv:
                print('[301] - Next')
            else:
                print()
            n=intinput(input())
            if n==300 and t!=0:
                t-=1
            elif n==301 and t!=maxv:
                t+=1
            else:
                if 0<=n and n<len(num):
                    print(f"Is {English_keys[num[n]]} correct?")
                    print('[0] - Yes  [1] - No')
                    a=intinput(input())
                    if a==0:
                        return num[n]
                else:
                    print('Invalid input')
    else:
        t=0
        maxv=len(graph)//10
        while True:
            if t!=maxv:
                for i in range(10):
                    print(f"[{i+t*10}] - {Japanese_keys[num[i+t*10]]}")
            else:
                for i in range(len(graph)%10):
                    print(f'[{i+t*10}] - {Japanese_keys[num[i+t*10]]}')
            if t!=0:
                print('[300] - 前',end=' ')
            if t!=maxv:
                print('[301] - 次')
            else:
                print()
            n=intinput(input())
            if n==300 and t!=0:
                t-=1
            elif n==301 and t!=maxv:
                t+=1
            else:
                if 0<=n and n<len(num):
                    print(f"{Japanese_keys[num[n]]} 合っていますか？")
                    print('[0] - はい  [1] - いいえ')
                    a=intinput(input())
                    if a==0:
                        return num[n]
                else:
                    print('入力が間違っています')
        
        
def 화장실(start):
    visited=defaultdict(lambda:sys.maxsize)
    q=[]
    heappush(q,(0,start))
    visited[start]=0
    while q:
        x,y=heappop(q)
        if visited[y]<x:
            continue
        for i in graph[y]:
            if visited[i]<=graph[y][i]+x:
                continue
            else:
                cost=graph[y][i]+x
                visited[i]=cost
                heappush(q,(cost,i))
    cur='진로관 2층 화장실'
    for i in visited:
        if '화장실' in i and visited[i]<visited[cur]:
            cur=i
    t=[cur]
    while cur!=start:
        for i in graph[cur]:
            if visited[cur]-visited[i]==graph[cur][i]:
                t.append(i)
                cur=i
                break
    return t
def 도움말():
    if lang==0:
        print("[1] : 목적지 찾기 - 출발지에서 목적지까지 가는 가장 빠른길을 골라드립니다.")
        print('[2] : 화장실 찾기 - 출발지에서 가장 가까운 화장실을 찾아드립니다.')
def pos(x):
    a=list(graph.keys())
    tt.penup()
    tt.goto(*coor[x[0]])
    tt.pendown()
    for i in range(1,len(x)):
        tt.goto(*coor[x[i]])
        tt.pendown()
        dx=coor[x[i-1]][0]-coor[x[i]][0]
        dy=coor[x[i-1]][1]-coor[x[i]][1]
        if '계단' in x[i] and not (49<=a.index(x[i]) and a.index(x[i])<=130):
            tt.penup()
        if (dx**2+dy**2==0):
            continue
        tt.pendown()
        dx*=50
        dy*=50
        minvx=0
        minvy=0
        midx=(dx+minvx)/2
        midy=(dy+minvy)/2
        while abs(midx**2+midy**2-100)>=0.1:
            if midx**2+midy**2>=100:
                dx=midx
                dy=midy
            else:
                minvx=midx
                minvy=midy
            midx=(dx+minvx)/2
            midy=(dy+minvy)/2
        tx=0.707*midx-0.707*midy
        ty=0.707*midx+0.707*midy
        tt.goto(coor[x[i]][0]+tx,coor[x[i]][1]+ty)
        tt.goto(*coor[x[i]])
        tx=0.707*midx+0.707*midy
        ty=-0.707*midx+0.707*midy
        tt.goto(coor[x[i]][0]+tx,coor[x[i]][1]+ty)
        tt.goto(*coor[x[i]])
        if '계단' in x[i] and not (49<=a.index(x[i]) and a.index(x[i])<=130):
            tt.penup()
def 목적지찾기():
    if lang==0:
        print("출발지를 입력해주세요")
    elif lang==1:
        print("Please enter your departure point")
    else:
        print('出発地の入力をお願いします')
    n=위치설정()
    if lang==0:
        print('도착지를 입력해주세요')
    elif lang==1:
        print('Please enter your destination')
    else:
        print('到着地を入力してください')
    m=위치설정()
    print()
    x=목적지(n,m)[::-1]
    pos(x)
    if lang==0:
        print(*목적지(n,m)[::-1],sep='\n')
    elif lang==1:
        for i in 목적지(n,m)[::-1]:
            print(English_keys[i])
    else:
        for i in 화장실(n)[::-1]:
            print(Japanese_keys[i])
    return

def 화장실찾기():
    if lang==0:
        print("이 기능은 화장지를 제공해주지 않습니다.")
        print("출발지를 입력해주세요")
    elif lang==1:
        print('This function does not provide toilet paper')
        print('Please enter your departure point')
    else:
        print('この機能はトイレットペーパーを提供しません')
        print('到着地を入力してください')
    n=위치설정()
    x=화장실(n)[::-1]
    pos(x)
    if lang==0:
        print(*화장실(n)[::-1],sep='\n')
    elif lang==1:
        for i in 화장실(n)[::-1]:
            print(English_keys[i])
    else:
        for i in 화장실(n)[::-1]:
            print(Japanese_keys[i])
    return
def debugging():
    for i in graph:
        for j in graph:
            (목적지(i,j))
def 언어선택():
    global lang
    if lang==0:
        print('언어를 선택해주세요')
        print('[0] - 한국어 \t [1] - English \t [2] - 日本語')
        n=intinput(input())
        if 0<=n and n<=2:
            lang=n
            return
        else:
            print('잘못된 입력입니다.')
            return 언어선택()
    elif lang==1:
        print('Select Language')
        print('[0] - 한국어 \t [1] - English \t [2] - 日本語')
        n=intinput(input())
        if 0<=n and n<=2:
            lang=n
            return
        else:
            print('Invalid input')
            return 언어선택()
    else:
        print('言語を選ぶ')
        print('[0] - 한국어 \t [1] - English \t [2] - 日本語')
        n=intinput(input())
        if 0<=n and n<=2:
            lang=n
            return
        else:
            print('入力が間違っています')
            return 언어선택()
print("오타, 오역/의역이 있을수 있습니다.")
언어선택()
if lang==0:
    print('로딩중',end='')
    for i in range(3):
        time.sleep(0.3)
        print('.',end='')
elif lang==1:
    print('loading',end='')
    for i in range(3):
        time.sleep(0.3)
        print('.',end='')
else:
    print('ローディング中',end='')
    for i in range(3):
        time.sleep(0.3)
        print('.',end='')
print()

while True:
    if lang==0:
        print("원하시는 기능을 선택하여 주십시오")
        print('[1] : 목적지 찾기 \t [2] : 화장실 찾기')
        print('[100] : 언어 재설정')
        n=intinput(input())
        if n==1:
            tt.clear()
            목적지찾기()
        if n==2:
            tt.clear()
            화장실찾기()
        if n==3:
            print("주의 : 이기능은 디버깅으로, 문제가 생긴것 같을때 돌려보는 기능입니다. 진행하시겠습니까?")
            t=input('Y/N')
            if 'y' in t.lower():
                debugging()
                print('문제가 발견되지 않았습니다.')
        if n==100:
            언어선택()
    elif lang==1:
        print("Please select the function you want")
        print('[1] : Find Destination \t [2] : Finding Restroom')
        print('[100] : Change Language')
        n=intinput(input())
        if n==1:
            tt.clear()
            목적지찾기()
        if n==2:
            tt.clear()
            화장실찾기()
        if n==100:
            언어선택()
    else:
        print("ご希望の機能をお選びください")
        print('[1] : 目的地探し \t [2] : トイレ探し')
        print('[100] : 言語変更')
        n=intinput(input())
        if n==1:
            tt.clear()
            목적지찾기()
        if n==2:
            tt.clear()
            화장실찾기()
        if n==100:
            언어선택()
