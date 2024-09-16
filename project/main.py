from bs4 import BeautifulSoup

with open('E:\WEBSCRAPING\project\home.html', 'r') as html_file:
  content = html_file.read()
 
  soup = BeautifulSoup(content, 'lxml') #soup is an instance of beautufilsoup 
'''# print(soup.prettify())   #to prettify the content
 
  courses_html_tags = soup.find_all('h5')       #"finds" method get all similar specific element but "find" only get first elmnt
  print(courses_html_tags)  #printing tags in html tags form
  for course in courses_html_tags: #used iteration of courses tags list to print their innet text only
      print(course.text)'''
      
course_cards = soup.find_all('div', class_='card')
for course in course_cards:
  course_name = course.h5.text
  course_price = course.a.text
  
  print(course_name)
  print(course_price)
      

  
  
  
  
  