from typing import Text
from bs4 import BeautifulSoup
import os


import functions
import requests
from flask import Flask, render_template,request, url_for

app=Flask(__name__)
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/search",methods=["POST"])
def search():
    url=request.form["url"]
    result=main_scraper(url,"Test") #this result should be an Array
    return render_template("index.html",result=result)


def main_scraper(url,directory):
    
    array=[]
    functions.create_directory(directory)
    source_code=requests.get(url)
    source_text=source_code.text
    soup=BeautifulSoup(source_text,"html.parser")
    #...........................................
    divs=soup.find_all("div")#array
    a_tags=soup.find_all("a")#array
    img_tags=soup.find_all("img")#array

    for img_tag in img_tags:
        img_src=img_tag.get("src")
        obj={'img_src':img_src}
        array.append(obj)
        

    for div in divs:
        div_text=div.text
        obj={'div_text':div_text}
        array.append(obj)
    
    for a_tag in a_tags:
        a_href=a_tag.get("href")
        obj={'a_href':a_href}
        array.append(obj)
    
    return array

    #print("image:"+img_source)     print("..........................Product..................................")
       # img_source=product.find('a').get('href')
       # href=product.find('a').find('img').get('src')
       # title=product.find('p').text
       # price=product.find('p',{'class':'price'}).text

        #array.append({'img_source':img_source,'href':href,'title':title,'price':price})
    #print("title:"+title)
    #print("href:"+href)
    #print("price: "+str(price))
    #print("................................End................................")
    #print("")
    #print("")

    #functions.write_to_file(directory+"/products.txt","................................Product................................................")
    #functions.write_to_file(directory+"/products.txt","image:"+img_source)
    #functions.write_to_file(directory+"/products.txt","title: "+title)
    #functions.write_to_file(directory+"products.txt","href: "+href)
    #functions.write_to_file(directory+"/products.txt","price: "+ str(price))
    #functions.write_to_file(directory+"/products.txt","................................End................................................")








if __name__=="__main__": 
    app.run(debug=True)