from bs4 import *
import pandas as pd
import requests
from tkinter import *
from tkinter import filedialog

def convert_to_excel():
    # Ask user to select the .txt file
    txt_path=filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    
    # Read the contents of the .txt file
    with open(txt_path, 'r') as file:
        lines=file.readlines()
    
    # Process the data and create a DataFrame
    data=[]
    for i in range(0, len(lines), 3):
        description=lines[i].split(": ")[1].strip()
        link=lines[i+1].split(": ")[1].strip()
        data.append([description, link])
    
    df=pd.DataFrame(data, columns=["Description", "Link"])
    
    # Ask user to save the Excel file
    excel_file_path=filedialog.asksaveasfilename(defaultextension=".xlsx")
    
    # Save the DataFrame as an Excel sheet
    df.to_excel(excel_file_path, index=False)

def scrape_webpage(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text, 'html.parser')
    
    image_descriptions=[]
    image_links=[]
    
    # Find all image tags on the webpage
    images=soup.find_all('img')
    
    for img in images:
        # Extract the description (alt attribute) and link (src attribute) of each image
        description=img.get('alt', '')
        link=img.get('src', '')
        
        # Append the description and link to their respective lists
        image_descriptions.append(description)
        image_links.append(link)
    
    return image_descriptions, image_links

def get_images():
    url=entry.get()
    
    # Scrape the webpage for image descriptions and links
    descriptions, links=scrape_webpage(url)
    
    # Save the descriptions and links in a .txt file
    with open('image_data.txt', 'w') as file:
        for i in range(len(descriptions)):
            file.write(f"Description: {descriptions[i]}\n")
            file.write(f"Link: {url}{links[i]}\n\n")
                     

def on_entry_click(event):
    if entry.get() == 'Please enter your url here . . .':
       entry.delete(0, "end")
       entry.insert(0, '')
       entry.config(fg = 'black')
       
def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'Please enter your url here . . .')
        entry.config(fg = 'grey')
        
window=Tk()
window.title("Web Scraper")
height=250
width=500
x=(window.winfo_screenwidth()//2)-(width//2)
y=(window.winfo_screenheight()//2)-(height//2)
window.geometry('{}x{}+{}+{}'.format(width,
                                     height,
                                     x,
                                     y))

icon=PhotoImage(file='Icon.png')
window.iconphoto(True,
               icon)
label=Label(window,
            text="Web Scraping Solutions",
            font=('Helvetica',
                  15,
                  'bold'))
label.place(x=140,
            y=10)

entry=Entry(window,
            width=30)
entry.insert(0, 'Please enter your url here . . .')
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.config(font='Helvetica',
             fg = 'grey')
entry.place(x=80,
            y=50)

fetch=Button(window,
             text="Fetch",
             fg='#0A64DC',
             activeforeground='#0A64BC',
             height=1,
             width=7,
             command=get_images)
fetch.place(x=275,
             y=90)

export=Button(window,
              text="Save As",
              fg='#CF202A',
              height=1,
              width=7,
              activeforeground='#CF202A',
              command=convert_to_excel)

export.place(x=180,
             y=90)

label_description=Label(window)
label_description.place(x=25,
                        y=190)
label_link=Label(window)
label_link.place(x=65,
                 y=200)

window.mainloop()


# NOTE :-
# I have used this as an example url you can use any of your choice
# https://books.toscrape.com/