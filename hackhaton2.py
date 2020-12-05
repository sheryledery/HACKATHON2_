from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import os
from PIL import Image, ImageTk
import sqlite3
Profile = {1:""}

# def win1():
#window
main = Tk()
main.title("Address Book")
main.geometry("550x480")
main.resizable(width=True, height=True)


def add_person():
    name= entryName.get()
    phone = entryPhone.get()
    more = entryInfo.get()
    #create connection
    conn = sqlite3.connect('persons.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO persons ('Name', 'Phone', 'More_Infos') values (?, ?, ?)", (name, phone, more))
    conn.commit()
    conn.close()
    conn = sqlite3.connect('persons.db')
    cur = conn.cursor()
    select = cur.execute("SELECT * FROM persons order by id desc")
    select = list(select)
    tree.insert('', END , values = select[0])
    conn.close()
    conn = sqlite3.connect("persons.db")
    cur = conn.cursor()
    select = cur.execute("SELECT * FROM persons order by id desc")
    select = list(select)
    id = select[0][0]
    filename = entryPhoto.get()
    im = Image.open(filename)
    rgb_im = im.convert('RGB')
    rgb_im.save(("/Users/macbookpro/Desktop/HACKHATON2/profilephoto/profile_" + str(id) + "." + "jpg"))
    conn.close()



def delete_person():
    idSelect = tree.item(tree.selection())['values'][0]
    conn = sqlite3.connect('persons.db')
    cur = conn.cursor()
    delete = cur.execute("delete from persons where id = {}".format(idSelect))
    conn.commit()
    tree.delete(tree.selection())



def sortByName():
    #clear the treeview
    for x in tree.get_children():
        tree.delete(x)
    #create connection
    conn = sqlite3.connect("persons.db")
    cur = conn.cursor()
    select = cur.execute("select*from persons order by name asc ")
    conn.commit()
    for row in select:
        tree.insert('', END , values = row)
    conn.close()



def SearchByName(event):
    for x in tree.get_children():
        tree.delete(x)
    name = entrySearchByName.get()
    conn = sqlite3.connect("persons.db")
    cur = conn.cursor()
    select = cur.execute("SELECT * FROM persons where Name = (?)", (name,))
    conn.commit()
    for row in select:
        tree.insert('', END , values = row)
    conn.close()


def SearchByPhone(event):
    for x in tree.get_children():
        tree.delete(x)
    phone = entrySearchByPhone.get()
    conn = sqlite3.connect("persons.db")
    cur = conn.cursor()
    select = cur.execute("SELECT * FROM persons where Phone = (?)", (phone,))
    conn.commit()
    for row in select:
        tree.insert('', END , values = row)
    conn.close()


def BrowsePhoto():
    entryPhoto.delete(0, END)
    filename = filedialog.askopenfilename(title = "Select File")
    entryPhoto.insert(END, filename)


def TreeActionSelect(event):
    label_image.destroy()
    idSelect = tree.item(tree.selection())['values'][0]
    nameSelect = tree.item(tree.selection())['values'][1]
    phoneSelect = tree.item(tree.selection())['values'][2]
    moreinfoSelect = tree.item(tree.selection())['values'][3]
    imgProfile = "/Users/macbookpro/Desktop/HACKHATON2/profilephoto/profile_" + str(idSelect) + "." + "jpg"
    load = Image.open(imgProfile)
    load.thumbnail((100, 100))
    photo = ImageTk.PhotoImage(load)
    Profile[1] = photo
    lblImage = Label(main, image = photo)
    lblImage.place (x = 10, y = 350)
    lid = Label(main, text = "ID : " + str(idSelect))
    lid.place(x = 110, y= 350)
    lname = Label(main, text = "Name : " + nameSelect)
    lname.place(x=110, y=380)
    lphone = Label(main, text = "Phone : " + str(phoneSelect))
    lphone.place(x = 110, y = 410)
    Tmore = Text(main)
    Tmore.place(x= 260, y= 360, width = 280, height = 100)
    Tmore.insert(END, "More Infos : " + moreinfoSelect)

    


#title
lblTitle = Label(main, text= "Address Book", font=('Arial', 21), bg = "lightblue", fg = "white" )
lblTitle.place(x=0, y=0, width= 250, height=42)

#search area (search by name)
lbSearchByName = Label(main, text = "Search by name: ", bg="lightblue", fg="white")
lbSearchByName.place(x=250, y=0, width=120)
entrySearchByName = Entry(main)
entrySearchByName.bind("<Return>", SearchByName)
entrySearchByName.place(x= 380, y=0, width= 160)

#search area (search by phone)
lbSearchByPhone = Label(main, text = "Search by phone: ", bg="lightblue", fg="white")
lbSearchByPhone.place(x=250, y=20, width=120)
entrySearchByPhone = Entry(main)
entrySearchByPhone.place(x= 380, y=20, width= 160)

#label & First Name & Last Name
lblName = Label(main, text="First & Last name: ", bg="black", fg= "white")
lblName.place(x=5, y=50, width= 125)
entryName = Entry(main)
entryName.place(x=140, y=50, width= 400)
 
#label & Entry Phone
lblPhone = Label(main, text="Phone Number: ", bg="black", fg= "white")
lblPhone.place(x=5, y=80, width= 125)
entryPhone = Entry(main)
entrySearchByPhone.bind("<Return>", SearchByPhone)
entryPhone.place(x=140, y=80, width= 400)

#label & Entry Photo
lblPhoto = Label(main, text="Profile Photo: ", bg="black", fg= "white")
lblPhoto.place(x=5, y=110, width= 125)
buttonPhoto = Button(main, text= "Browse", bg= "lightblue", fg = "white", width= 10, command = BrowsePhoto)
buttonPhoto.place(x=480, y=110, height=25)
entryPhoto = Entry(main)
entryPhoto.place(x=140, y=110, width= 400)

#picture object
load = Image.open("/Users/macbookpro/Desktop/HACKHATON2/profilephoto/bydefault.png")
load.thumbnail((130,130))
photo = ImageTk.PhotoImage(load)
label_image = Label(main, image = photo)
label_image.place(x=10, y=350)

#label & add Infos
lblInfo = Label(main, text="More Info: ", bg="black", fg= "white")
lblInfo.place(x=5, y=140, width= 125)
entryInfo = Entry(main)
entryInfo.place(x=140, y=140, width= 400)

#Command button (add someone)
buttonAdd = Button(main, text="Add Customer ", bg= "black", fg= "black", command = add_person)
buttonAdd.place(x=5, y=170, width= 255)

#delete button
buttonDelete = Button(main, text="Delete Selection ", bg= "black", fg= "black", command = delete_person)
buttonDelete.place(x=5, y=205, width= 255)

#edit button
buttonEdit = Button(main, text="Edit Selection ", bg= "black", fg= "black")
buttonEdit.place(x=5, y=240, width= 255)

#sort by name button
buttonSort = Button(main, text="Sort by Name ", bg= "black", fg= "black", command = sortByName)
buttonSort.place(x=5, y=275, width= 255)

#exit button
buttonExit = Button(main, text="Exit App ", bg= "black", fg= "black", command= quit)
buttonExit.place(x=5, y=310, width= 255)

#add TreeView
tree = ttk.Treeview(main, columns = (1, 2, 3), height= 3, show="headings")
tree.place(x=265, y=170, width=290, height=175)
tree.bind("<<TreeviewSelect>>", TreeActionSelect)

# Add headings
tree.heading(1, text= "ID")
tree.heading(2, text= "Name")
tree.heading(3, text= "Phone")
tree.column(1, width=50)
tree.column(2, width=105)
tree.column(3, width=100)

#display data in treeview obect
conn = sqlite3.connect('persons.db')
cur = conn.cursor()
select = cur.execute("select * from persons")
for row in select:
    tree.insert('', END , value = row)
conn.close()


 

main.mainloop()