# page request: https://jonathansoma.com/lede/foundations-2018/classes/apis/multiple-pages-of-data-from-apis/

# api pagination canvas https://canvas.instructure.com/doc/api/file.pagination.html

# Notes:
#   Courses link:
#       "https://canvas.instructure.com/api/v1/courses?access_token="
#   Assignments link for college success strategies:
#       "https://canvas.instructure.com/api/v1/courses/56470000000015120/assignments?access_token="


# MODULE IMPORTS
import requests
import time
import configparser
import datetime
from datetime import date
from requests.auth import HTTPBasicAuth
import json #might be unnecessary
import pprint




courseId = str(56470000000015120) #I believe this is the course ID for College Success strats

# Access token
access_token = "5647~6sxmke1PdjSLbsrwcgMIVk8XeBnKXdOtlvrgpix1SyDYqO0BxosvaMzV8iuCOuWN"
# Class link
url = "https://canvas.instructure.com/api/v1/courses?per_page=1000;access_token="
# Class request
classRequest = requests.get(url + access_token)

def assignmentsRequestFunc(courseId): # Not sure if this is still necessary
  url2 = "https://canvas.instructure.com/api/v1/courses/"+ courseId + "/assignments?per_page=1000;access_token="
  # assignments request
  assignmentsRequest = requests.get(url2 + access_token)
  return assignmentsRequest

# course request
coursesRequest = requests.get(url + access_token)

# FUNCTION: Seperator
def seperator():
  print("#######################")

def 

# Might not be neccessary
class courses:
  def __init__(self, name, id, start_at, end_at, current_status):
    self.name = str(name)
    self.id = int(id)
    self.start_at = str(start_at)
    self.end_at = str(end_at)
    self.current_status = current_status
    start_at_list = [start_at[0:4],start_at[5:7],start_at[8:10]]
  
  def currentCourse(end_at):
    today = str(date.today()) #gets todays date
    today_list = [today[0:4], today[5:7], today[5:7], today[8:10]] #makes today into a list of year?, month?, day? 
    if end_at != None: #if the end at value is none then...
      end_at_list =[end_at[0:4],end_at[5:7],end_at[8:10]] #turn the end at list into the same comparable list as the day
      if today_list[0] < end_at_list[0]:
        if today_list[1] < end_at_list[1]:
          if today_list[2] < end_at_list[2]:
            current_status = "True"
            return current_status # return current status as true if method is called to say that this is good to go to pull the assignments from, if not then it returns false, just like with the line 4 lines up and the proceeding. 
          else:
            current_status = "False"
            return current_status
        else:
          current_status = "False"
          return current_status
      else:
        current_status = "False"
        return current_status
    else:
      current_status = "False"
      return current_status # 
      
def coursePopulator():
  for x in classRequest.json():
    r = courses.currentCourse(x["end_at"])
    test = courses(x["name"], x["id"], x["start_at"], x["end_at"], r)
    print(test.name)
    print(test.current_status)
coursePopulator()



def get_new_assignments():
  courses = requests.get(url + access_token) # courses
  abridged_courses = courses.text[1:-1]
  # json_text_file = open("jsontext.json", "w")
  # json_text_file.write(courses.text)
  # json_text_file.close()
  # abridged_courses = "{" + abridged_courses + "}"
  print(type(courses.text))
  data = json.loads(courses.text)
  print(type(data))
  print(courses.text[0])
  print("!!!!!!!!!!!!!!!!!!!!!!!!!")
  print("")
  print("!!!!!!!!!!!!!!!!!!!!!!!!!")
  pprint.pprint(data) #pprint prints it in an easier to read format

# get_new_assignments()


    

    # TODO: For loop throught the courses
        # Get the id of the course
        # Make a request to get assiments for that particular course
        # Figure out the newest data

#dead honest, I stole this little bit of code. it was helpful though
def run_schedule():
  while True:
    now = datetime.datetime.now()
    target = datetime.datetime.combine(datetime.date.today(), datetime.time(hour=2,minute=0))
    
    if target < now:
      target += datetime.timedelta(days=1)
    time.sleep((target-now).total_seconds())
    # do something
    print("test")

def main():
  run_schedule()

if __name__ == '__main__':
  main()
