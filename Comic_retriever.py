#########################
#Russell Arlt           #
#CIT 112 David Hosler   #
#Comic Retriever        #
#########################

import webbrowser
import bs4
import requests
import re
import logging # all the imported modules that I like to have seperated cause I'm crazy

#logging.disable()
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')# RA This allows us to set the level of debugging we want to see,with the level of error, and the message generated.
logging.debug('Program start') # start that program!
makelist = [] # a list for when we pop parts of the name of the link out.
list2 = [] # a list for the webpages.
input("Press enter to open a comic webpage:")
webbrowser.open('https://www.giantitp.com/comics/oots.html') # opens the web page to find the comics.
Target_web_page = requests.get('https://www.giantitp.com/comics/oots.html') # getting the web page to create the beautiful soup with.
logging.debug(f"we are going to {Target_web_page}.") # well this gives us a Response 200 which means we are going to the webpage lol.
Russ_soup = bs4.BeautifulSoup(Target_web_page.text, 'html.parser') # creating the variable for the beautiful soup and making it a text, that can be parsed with the html parser.
elements = Russ_soup.select('p.ComicList') # creating an element that selects the p.ComicList tags.
for link in Russ_soup.find_all('a'): # for each link in the soup, we want to find all of them that have the a tag.
    makelist.append(link.get('href')) # now we append that makelist with the link tag.
num1=0 # creating a number variable that is set to 0
num2=0 # creating a second number variable set to 0
input("Press enter to see and download 10 comics!: ") # This tells the user whats happening.
while True: # loop time!
    for i in makelist: # for a variable in our list
        if num1 < 18: # if the number created above is less than 18
            x = makelist.pop(0) # this will pop out or delete in this case, the variable that is at 0
            num1 += 1 # start our incrementing.
        elif num1 > 18: # once it hits 18 it will be at the web page that we want to get to.
            break # break from the for loop as we don't want to pop out any more
    for i in makelist: # for loop for the list again
        if num2 < 10: # we use the number created about and while it is less than 10
            list2.append('https://www.giantitp.com' + i) #we append a new list, with the web link that all the comics are a part of, and add the link to it.
            num2 += 1 # increment
        elif num2 >= 10: # once we hit 10
            break # break this loop
    for i in list2: # start a new for loop
        webbrowser.open(i) # we open the links one at a time with webbrowser
        var = i # we take i and set it to a variable to be able to get it from a request.
        regex_num = re.compile(r'\d{4}') # creating a regex statement to get the comic number
        findnum = re.findall(regex_num, i) # looking at the variable var and the regex statement
        New_Target = requests.get(var) # we get the webpage so we can make a beautiful soup from it
        new_soup = bs4.BeautifulSoup(New_Target.text, 'html.parser') # create a new variable to hold the parsed text of the soup object
        var1 = 'oots' + findnum[0] # here we create a variable adding oots, and the number of the comic!
        #print(var1) # here we print it for some reason.
        imagelist = new_soup.find_all('img') # we create a list in this line to find all of the images on the webpage
        image = imagelist[17] # we create a variable that holds the 17th variable in the image list, which is the comic we need.
        image_string = str(image) # we make the image a string, as it isnt at the moment.
        newstring = image_string.replace('<img src="', "") # create a string that is the name of the image, replacing the first part of the image name with nothing.
        finalstring = newstring.replace('"/>', '') # creating a string that is the name of the new image, replacing the last part of the image with nothing.
        print(finalstring) # Printing the literal string of the image name.
        the_image = requests.get(finalstring).content # variable that is getting the content of the link.
        image_file = open(f'{findnum[0]}.png', 'wb') # opening a file that is named the number of the comic, as a png, written with binary.
        image_file.write(the_image) # here we write the image, or I guess in this case save it.
        image_file.close() # now we close it. Like always.
        input(f"Folder updated with comic #{findnum[0]}, press enter to continue: ") # Here we let the user know we updated the comic. They should press enter to continue.
        print() # a nice line break here
    break # break out of the loop when its done
print() # another nice line break
print("All comics recorded.") # Let them know that all comics are recorded.

#buncha stuff I tried before I got it all.

#keep_looking = re.findall(regex_num, new_soup)
#print(keep_looking)
#input()
#body_tag = new_soup.body
#for child in body_tag.descendants:
#print(child)
#input()
#for image in new_soup.find_all('img'):
#print(image)
#target_picture = requests.get()
#what1 = type(Russ_soup)
#print(what1)
#what2 = type(elements)
#print(what2)
#what3 = type(makelist)
#print(what3)