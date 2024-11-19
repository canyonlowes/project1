import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry('300x300')
green = "POKER HOME SCREEN_1.jpg"
gold = "gold1.jpg" #this is the default home screen. Only replaced by certain themes like cats
cat_home = "cat1.jpg"
cat_game_background = "cat2.jpg"
christmas_home = "christmasbg4.jpg"
christmas_game_background = "christmasbg1.jpg"
purple = "purple.jpg"
black = "black1.jpg"
old_fashioned_game = "guns1.jpg"
old_fashioned_home = "brown1.jpg"
red = "red1.jpg"
pink = "pink2.jpg"

selected_theme = gold 
home_background = gold

def clear_page(): 
    for widget in window.winfo_children():
        widget.pack_forget()

def testpage():
    image = Image.open(home_background)
    resized_image = image.resize((1920, 1080), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)
    window.bg_image = bg_image
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    setting_button = tk.Button(window, text='Settings', font=('Georgia', 20), command=settings)
    setting_button.pack(pady=10)
    go = tk.Button(window, text = 'go', font = ('georgia', 20),command=lambda:testpage2())
    go.pack(pady=20)
    
def testpage2():
    image = Image.open(selected_theme)
    resized_image = image.resize((1920, 1080), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)
    window.bg_image = bg_image
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    hi = tk.Label(window, text = 'HI!')
    hi.pack(pady = 8)
    back = tk.Button(window, text = 'Back',font = ('georgia', 20),command=lambda:testpage())
    back.pack(pady=10)


def settings():
    image = Image.open(selected_theme)
    resized_image = image.resize((1920, 1080), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)
    window.bg_image = bg_image
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    settings_label = tk.Label(window, text='Settings', font=('Georgia', 20))
    settings_label.pack(pady=20)
    
    background_button = tk.Button(window, text='Change Background', font=('Georgia', 20), command=background_menu)
    background_button.pack(pady=20)

def background_menu():
    clear_page()
    new_background_label = tk.Label(window, text='Choose Background', font=('Georgia', 20))
    new_background_label.pack(pady=20)
    color_button = tk.Button(window, text = 'Colors', font = ('georgia', 20),command=lambda:colors())
    color_button.pack(pady = 20)
    other_button = tk.Button(window, text = 'Other', font = ('georgia', 20),command=lambda:other_bg())
    other_button.pack(pady = 20)
    
    def colors():
        clear_page()  

        green_button = tk.Button(window, text='Green', font=('Georgia', 20), command=lambda: commit_theme(green))
        green_button.pack(pady=0)
    
        gold_button = tk.Button(window, text=' Gold ', font=('Georgia', 20), command=lambda: commit_theme(gold))
        gold_button.pack(pady=0)

        purple_button = tk.Button(window, text='Purple', font=('Georgia', 20), command=lambda: commit_theme(purple))
        purple_button.pack(pady=0)

        black_button = tk.Button(window, text = 'Black', font = ('georgia', 20), command=lambda:commit_theme(black))
        black_button.pack(pady=0)

        red_button = tk.Button(window, text = 'Red', font = ('georgia', 20), command=lambda:commit_theme(red))
        red_button.pack(pady=0)

        pink_button = tk.Button(window, text = 'Pink', font = ('georgia', 20), command=lambda:commit_theme(pink))
        pink_button.pack(pady=0)

        back_button = tk.Button(window, text = 'Back',font = ('georgia', 10),command=lambda:background_menu())
        back_button.pack(pady = 50)
    
    def other_bg ():
        clear_page()

        cat_button = tk.Button(window, text = ' Cats  ', font = ('georgia', 20),command=lambda:commit_theme(cat_game_background))
        cat_button.pack(pady = 0)

        christmas_button = tk.Button(window, text = 'Christmas', font = ('georgia', 20),command=lambda:commit_theme(christmas_game_background))
        christmas_button.pack(pady = 0)

        old_fashioned_button = tk.Button(window, text = 'Old Fashioned', font = ('georgia', 20),command=lambda:commit_theme(old_fashioned_game))
        old_fashioned_button.pack(pady = 0)


        back_button = tk.Button(window, text = 'Back',font = ('georgia', 10),command=lambda:background_menu())
        back_button.pack(pady = 50)

def commit_theme(theme):
    global selected_theme
    global home_background
    selected_theme = theme 
    if selected_theme == cat_game_background:
        home_background = cat_home
        testpage()
    elif selected_theme == christmas_game_background:
        testpage(christmas_home)
    elif selected_theme == old_fashioned_game:
        testpage(old_fashioned_home)
    else:
        testpage(gold)

testpage()

window.mainloop()

#note for next time: remove paremter on welcome, add global home_background to commit_theme. just look at what i if you pick cat as your theme :)