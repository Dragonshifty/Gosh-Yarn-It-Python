import tkinter as tk
from tkinter import *
from buttons_and_labels import MyButton, MyLabel, MyEntry, MyEntryRight
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import json
from functools import partial
from PIL import ImageTk, Image


# Variables
TITLE = "Gosh Yarn It"
yarn_dict = {}
yarn_list = ["1"]


# Main Window Setup
root = Tk()
root.title(TITLE)
root.geometry("579x600")
root.resizable(0, 0)
root.config(bg="#7d4f50")
# img = PhotoImage(file="lbg2.png")
# background_label = Label(root, image=img)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)


# Field Variable StringVar declarations
name_var = StringVar()
col_var = StringVar()
brand_var = StringVar()
loc_var = StringVar()
mat_var = StringVar()
balls_var = StringVar()
as_var = StringVar()
weight_var = StringVar()
dye_var = StringVar()
yards_var = StringVar()
purchased_var = StringVar()
yarn_index = StringVar()


# Open json master file or create if file not found
try:
    with open("yarn_data.json", "r") as f:
        data = json.load(f)
    # Convert to master dictionary
    yarn_dict = json.loads(data)
except FileNotFoundError:
    create_new = mb.askokcancel(title="Create new Stash", message="Master Stash file not found. Create a new file?")
    if create_new:
        yarn_dict = {
            1: {
                "Name": "",
                "Brand": "",
                "Colour": "",
                "Location": "",
                "Material": "",
                "Balls in Stash": "",
                "As of Date": "",
                "Weight": "",
                "Dye Lot": "",
                "Yards per Ball": "",
                "Purchased From": ""
                 }
            },
        with open("yarn_data.json", "w") as f:
            pass
    else:
        exit()



# Functions

def save_to_json():
    '''Open and write to json file'''
    json_data = json.dumps(yarn_dict)

    try:
        # Save to json file
        with open("yarn_data.json", "w") as f:
            json.dump(json_data, f)
    except:
        mb.showerror(title="Error", message="Something went wrong.")

def set_fields():
    """Setting label and input boxes"""
    name_var.set(yarn_dict[yarn_list[0]]["Name"])
    col_var.set(yarn_dict[yarn_list[0]]["Colour"])
    brand_var.set(yarn_dict[yarn_list[0]]["Brand"])
    loc_var.set(yarn_dict[yarn_list[0]]["Location"])
    mat_var.set(yarn_dict[yarn_list[0]]["Material"])
    balls_var.set(yarn_dict[yarn_list[0]]["Balls in Stash"])
    as_var.set(yarn_dict[yarn_list[0]]["As of Date"])
    weight_var.set(yarn_dict[yarn_list[0]]["Weight"])
    dye_var.set(yarn_dict[yarn_list[0]]["Dye Lot"])
    yards_var.set(yarn_dict[yarn_list[0]]["Yards per Ball"])
    purchased_var.set(yarn_dict[yarn_list[0]]["Purchased From"])
    yarn_index.set(yarn_list[0])

def default():
    """Set or restore to starting fields"""
    yarn_list[0] = "1"
    set_fields()

def previous():
    """Cycle back to previous yarn index - return to beginning on error"""
    try:
        global yarn_list
        holding = yarn_list[0]
        holding = int(holding)
        holding -= 1
        holding = str(holding)
        yarn_list[0] = holding

        set_fields()
    except KeyError:
        yarn_list[0] = "1"
        default()

def next():
    """Cycle forwards to next yarn index - return to beginning on error"""
    try:
        global yarn_list
        holding = yarn_list[0]
        holding = int(holding)
        holding += 1
        holding = str(holding)
        yarn_list[0] = holding

        set_fields()
        change_image()

    except KeyError:
        yarn_list[0] = "1"
        default()

def update_field(field, field_entry):
    '''Saves individual field to json file'''
    # Ask for confirmation
    check = mb.askokcancel(title="Save and overwrite?", message="Do you wish to save?")
    if check:

        # Update yarn dictionary
        index = yarn_index.get()
        new_entry = field_entry.get()
        yarn_dict[index][field] = new_entry

        save_to_json()


def save_yarn():
    '''Save all fields to json'''
    # Ask for confirmation
    check = mb.askokcancel(title="Save yarn to stash?", message="Do you wish to save to stash?")
    if check:
        # Get field contents
        name_field = name_var.get()
        col_field = col_var.get()
        brand_field = brand_var.get()
        loc_field = loc_var.get()
        mat_field = mat_var.get()
        balls_field = balls_var.get()
        as_field = as_var.get()
        weight_field = weight_var.get()
        dye_field = dye_var.get()
        yards_field = yards_var.get()
        purchased_field = purchased_var.get()
        index = yarn_index.get()

        # Save to yarn dictionary
        yarn_dict[index]["Name"] = name_field
        yarn_dict[index]["Colour"] = col_field
        yarn_dict[index]["Brand"] = brand_field
        yarn_dict[index]["Location"] = loc_field
        yarn_dict[index]["Material"] = mat_field
        yarn_dict[index]["Balls in Stash"] = balls_field
        yarn_dict[index]["As of Date"] = as_field
        yarn_dict[index]["Weight"] = weight_field
        yarn_dict[index]["Dye Lot"] = dye_field
        yarn_dict[index]["Yards per Ball"] = yards_field
        yarn_dict[index]["Purchased From"] = purchased_field

        save_to_json()


def new_yarn():
    '''Get new index key for new yarn entry. Create new yarn entry.'''

    # Get index keys
    index_list = []
    for key in yarn_dict.keys():
        index_list.append(key)

    # Get current highest index list and increment by 1
    new_key_temp = int(max(index_list)) + 1
    new_key = str(new_key_temp)

    yarn_dict[new_key] = {
        "Name": "",
        "Brand": "",
        "Colour": "",
        "Location": "",
        "Material": "",
        "Balls in Stash": "",
        "As of Date": "",
        "Weight": "",
        "Dye Lot": "",
        "Yards per Ball": "",
        "Purchased From": ""
    }
    yarn_list[0] = new_key

    set_fields()

def change_image():
    # try:
    p_index = yarn_index.get()
    img = Image.open(f"{p_index}.jpg")
    resized_image = img.resize((300, 205))
    new_image = ImageTk.PhotoImage(resized_image)
    l = Label(image=new_image).grid(column=1, row=9, columnspan=4, pady=10)
    # except:
    #     l = Label(image=new_image).grid(column=1, row=9, columnspan=4, pady=10)


# Set fields
default()
change_image()


# Title
title_cavas = tk.Canvas(width=400, height=50, bg="black").grid(column=1, row=1, columnspan=4, pady=10)



# Initialise button/label/entry items

name_button = MyButton(root, "Name", partial(update_field, "Name", name_var), border=0).grid(column=1, row=2, padx=4, pady=2)
name_entry = Entry(root, textvariable=name_var, width=41, font=("Hellvetica", 11),
                highlightthickness=2,  borderwidth=2, relief="groove")\
                .grid(column=2, row=2, padx=2, columnspan=2)

index_label = MyLabel(root, yarn_index).grid(column=4, row=2)

colour_button = MyButton(root, "Colour", partial(update_field, "Colour", col_var)).grid(column=1, row=3, padx=4, pady=2)
colour_entry = MyEntry(root, col_var).grid(column=2, row=3, pady=5)

weight_entry = MyEntryRight(root, weight_var).grid(column=3, row=3, pady=5)
weight_button = MyButton(root, "Weight", partial(update_field, "Weight", weight_var), border=0).grid(column=4, row=3, padx=4, pady=2)

brand_button = MyButton(root, "Brand", partial(update_field, "Brand", brand_var)).grid(column=1, row=4, padx=4, pady=2)
brand_entry = MyEntry(root, brand_var).grid(column=2, row=4, pady=5)

location_entry = MyEntryRight(root, loc_var).grid(column=3, row=4, pady=5)
location_button = MyButton(root, "Location", partial(update_field, "Location", loc_var), border=0).grid(column=4, row=4, padx=4, pady=2)

material_button = MyButton(root, "Material", partial(update_field, "Material", mat_var)).grid(column=1, row=5, padx=4, pady=2)
material_entry = MyEntry(root, mat_var).grid(column=2, row=5, pady=5)

balls_in_stash_entry = MyEntryRight(root, balls_var).grid(column=3, row=5, pady=5)
balls_in_stash_button = MyButton(root, "Balls in Stash", partial(update_field, "Balls in Stash", balls_var), border=0).grid(column=4, row=5, padx=4, pady=2)

yards_per_ball_button = MyButton(root, "Yards per Ball", partial(update_field, "Yards per Ball", yards_var)).grid(column=1, row=6, padx=4, pady=2)
yards_per_ball_entry = MyEntry(root, yards_var).grid(column=2, row=6, pady=5)

as_of_date_entry = MyEntryRight(root, as_var).grid(column=3, row=6, pady=5)
as_of_date_button = MyButton(root, "As of Date", partial(update_field, "As of Date", as_var), border=0).grid(column=4, row=6, padx=4, pady=2)

dye_lot_button = MyButton(root, "Dye Lot", partial(update_field, "Dye Lot", dye_var)).grid(column=1, row=7, padx=4, pady=2)
dye_lot_entry = MyEntry(root, dye_var).grid(column=2, row=7, pady=5)

purchased_entry = MyEntryRight(root, purchased_var).grid(column=3, row=7, pady=5)
purchased_button = MyButton(root, "Purchased", partial(update_field, "Purchased From", purchased_var)).grid(column=4, row=7, padx=4, pady=2)

previous_button = MyButton(root, "Previous", previous).grid(column=1, row=8)

save_yarn_button = MyButton(root, "Save to Stash", save_yarn).grid(column=2, row=8)

new_yarn_button = MyButton(root, "New Yarn", new_yarn).grid(column=3, row=8)

next_button = MyButton(root, "Next", next).grid(column=4, row=8)

p_index = yarn_index.get()
img = Image.open(f"{p_index}.jpg")
resized_image = img.resize((300, 205))
new_image = ImageTk.PhotoImage(resized_image)
l = Label(image=new_image).grid(column=1, row=9, columnspan=4, pady=10)


# yarn_canvas.create_image(0,0, anchor=NW, image=img)

# with open("yarn_data.json", "r") as f:
#     data = json.load(f)
#     yarn_data = json.loads(data)
#
# yarn_data["1"]["Purchased From"] = "Hobii"
# yarn_data["2"]["Purchased From"] = "Hobii"
# yarn_data["3"]["Purchased From"] = "Hobii"
#
# json_data = json.dumps(yarn_data)
#
# with open("yarn_data.json", "w") as f:
#     json.dump(json_data, f)

#####################

# yarn = {
#     1: {
#         "Name": "Art of Knitting",
#         "Brand": "Acrylic",
#         "Colour": "Green",
#         "Location": "Sofa",
#         "Material": "Yarn, innit",
#         "Balls in Stash": "66g",
#         "As of Date": 1417,
#         "Weight": "Ribbon",
#         "Dye Lot": 7001,
#         "Yards per Ball": "125m"
#     },
#     2: {
#         "Name": "Yarn Two",
#         "Brand": "Ribbon",
#         "Colour": "Pink",
#         "Location": "Hiding",
#         "Material": "Super",
#         "Balls in Stash": "55g",
#         "As of Date": "5/10",
#         "Weight": "Ribbon",
#         "Dye Lot": "Blue",
#         "Yards per Ball": "75/82m"
#     },
#     3: {
#         "Name": "Yarn Three",
#         "Brand": "Hobbi",
#         "Colour": "Bright Blue",
#         "Location": "Upstairs",
#         "Material": "Super",
#         "Balls in Stash": 6,
#         "As of Date": "5/18",
#         "Weight": "Seven",
#         "Dye Lot": "Pruple",
#         "Yards per Ball": "80g"
#     }
# }

# json_data = json.dumps(yarn)
# with open("yarn_data.json", "r") as f:
#     data = json.load(f)
#
# yarn_dict = json.loads(data)
#
# name_label.config(text=yarn_dict["1"]["Name"])











# btn3 = My_Button(root, "Rename a file", rename_file)
# btn3.grid(column=3, row=2, padx=4, pady=2)
# btn4 = My_Button(root, "Delete a file", delete_file)
# btn4.grid(column=1, row=3, padx=4, pady=2)
# btn5 = My_Button(root, "Open a folder", open_folder)
# btn5.grid(column=2, row=3, padx=4, pady=2)
# btn6 = My_Button(root, "Delete a folder", delete_folder)
# btn6.grid(column=3, row=3, padx=4, pady=2)
# btn7 = My_Button(root, "Move a folder", move_folder)
# btn7.grid(column=1, row=4, padx=4, pady=2)
# btn8 = My_Button(root, "EXIT", root.destroy)
# btn8.grid(column=2, row=4, padx=4, pady=2)
# btn8.config(fg="white")
# btn9 = My_Button(root, "List files in folder", list_files_in_folder)
# btn9.grid(column=3, row=4, padx=4, pady=2)



# Finalizing the window
root.update()
root.mainloop()
