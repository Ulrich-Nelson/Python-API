
from model_rpg import Personnage, Item
from tkinter import * # pip3 install tkinter && pip3 install validate_email

class Windows():

    def __init__(self):
        self.form_data = {
            'sexe': 0,
            'input_name': {},
            'type_ethnie': '',
            'type_personnage': '',
        }
        self.listOption = ['Guerrier', 'Voleur', 'Mage']

    def register_personnage(self):
        root = Tk()
        root.config(bg = "#87CEEB")
        root.title('Register RPG')

        screen_x = int(root.winfo_screenwidth())
        screen_y = int(root.winfo_screenwidth())
        window_x = 800
        window_y = 600
        position_x = (screen_x // 2) - (window_x // 2)  
        position_y = (screen_y // 2) - (window_y // 2)  

        geo = '{}x{}+{}+{}'.format(window_x, window_y, position_x, position_y)
        root.geometry(geo)

        label_name = Label(root, text="Entrez votre nom:",bg = "green", fg = "white", font=('bold'))
        label_name.place(x=200, y=70)

        self.form_data['input_name'] = Entry(root,width=40)
        self.form_data['input_name'].place(x=390, y=70)

        label_name = Label(root, text="Entrez votre sexe:", bg = "green", fg = "white",font=('bold'))
        label_name.place(x=200, y=150)

        self.form_data['sexe'] = IntVar()
        Radiobutton(root, text='Homme', value=1, variable=self.form_data['sexe']).place(x=380, y=150)
        Radiobutton(root, text='Femme', value=2, variable=self.form_data['sexe']).place(x=450, y=150)
        Radiobutton(root, text='Tran', value=3, variable=self.form_data['sexe']).place(x=520, y=150)

        label_name = Label(root, text="Entrez votre type:", bg = "green", fg = "white", font=('bold'))
        label_name.place(x=200, y=230)

        self.form_data['type_personnage'] = StringVar()
        self.form_data['type_personnage'].set(self.listOption[1])
        OptionMenu(root, self.form_data['type_personnage'],*self.listOption).place(x=380, y=230)

        label_name = Label(root, text="Entrez votre ethnie:",bg = "green", fg = "white", font=('bold'))
        label_name.place(x=200, y=300)

        self.form_data['type_ethnie'] = StringVar()
        listOption = ["Congo", "Mongolie", "France", "USA", "Japon", "Cote_Ivoire", "Argentine", "Haiti", "Angleterre"]
        self.form_data['type_ethnie'].set(listOption[0])
        OptionMenu(root, self.form_data['type_ethnie'],*listOption).place(x=380, y=300)

        Button(root, command=self.click_button, text='Envoyez', bg = "green", fg = "white", width=30).place(x=300, y=450)

        root.mainloop()

     
    def click_button(self):
        test = Personnage(self.form_data['input_name'].get(), int(self.listOption.index(self.form_data['type_personnage'].get())), self.form_data['type_ethnie'].get(), self.form_data['sexe'].get()) # new Personnage
        test.add_item_to_stock(Item(1, self.form_data['type_personnage'].get())) # Add un item
        print(test)

# if __name__ == '__main__':