import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox


class Cipher:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('CIPHER SYSTEM')
        self.window.geometry('400x300')
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack()
        self.tab1 = Frame(self.notebook)
        self.tab2 = Frame(self.notebook)
        self.tab1.pack(fill="both", expand=1)
        self.tab2.pack(fill="both", expand=1)
        self.notebook.add(self.tab1, text="Encryption")
        self.notebook.add(self.tab2, text="Decryption")
        self.tit1= tk.Label(self.tab1, text= "Keyword Columnar Cipher",font=20, bg="#404258")

        #tab1 encryption
        self.tit1 = tk.Label(self.tab1, text="Keyword Columnar Cipher", font=('Times bold', 29), bg="#BAD1C2",fg="#404258").pack()
        self.label1 = tk.Label(self.tab1, text="Enter the plain text you want to Encrypt:").pack()
        self.plaintxt = tk.Entry(self.tab1, width=90)
        self.klabel1 = tk.Label(self.tab1, text="Enter key:")
        self.Enkey = tk.Entry(self.tab1, width=90)
        self.cvalue = tk.StringVar()
        self.En_button = ttk.Button(self.tab1, text='Encryption', command=self.Encrypt)
        self.ctxt = tk.Label(self.tab1, text='encrypted text:')
        self.c_label = tk.Label(self.tab1, textvariable=self.cvalue)
        self.exit_button1 = tk.Button(self.tab1, text="Exit", command=self.window.destroy)
        self.plaintxt.pack()
        self.klabel1.pack()
        self.Enkey.pack()
        self.En_button.pack()
        self.ctxt.pack()
        self.c_label.pack()
        self.exit_button1.pack()

        #tab2 Decryption
        self.tit2 = tk.Label(self.tab2, text="Keyword Columnar Cipher", font=('Times bold', 29), bg="#BAD1C2", fg="#404258").pack()
        self.label2 = tk.Label(self.tab2, text="Enter the plain text you want to Decrypt:").pack()
        self.ciphertxt = tk.Entry(self.tab2, width=90)
        self.klabel2 = tk.Label(self.tab2, text="Enter key:")
        self.Dekey = tk.Entry(self.tab2, width=90)
        self.pvalue = tk.StringVar()
        self.De_button = ttk.Button(self.tab2, text='Decryption', command=self.Decrypt)
        self.ptxt = tk.Label(self.tab2, text='decrypted text:')
        self.p_label = tk.Label(self.tab2, textvariable=self.pvalue)
        self.exit_button2 = tk.Button(self.tab2, text="Exit", command=self.window.destroy)
        self.ciphertxt.pack()
        self.klabel2.pack()
        self.Dekey.pack()
        self.De_button.pack()
        self.ptxt.pack()
        self.p_label.pack()
        self.exit_button2.pack()
        tk.mainloop()

    def Encrypt(self):

        Ptext=self.plaintxt.get()
        key= self.Enkey.get()

        if(Ptext==""):
            tk.messagebox.showinfo("ERRORٍٍِ", "NO TEXT WAS ENTERED!!")

        if(key==""):
            tk.messagebox.showinfo("ERRORٍٍِ", "NO KEY WAS ENTERED!!")

        else:
            key = key.lower()
            Ekey = [' '] * (len(key))
            i = 0
            while (i < len(Ekey)):#fill the array with key char
                Ekey[i] = key[i]
                i += 1
            Ekey.sort()# in order to arrange the chars of key in order
            Ek = [0] * (len(Ekey))# for the order at which we will read the columns according to the key
            i = 0
            while (i < len(Ekey)):
                j = 0
                while (j < len(key)):# sort the key in order to specify what colmun would be read first
                    if (Ekey[i] == key[j]):
                        Ek[i] = j
                        break
                    j += 1
                i += 1
            numColumns = len(key)
            Plaintext = Cipher.RemoveSpace(self,Ptext)
            numRows=0
            if (len(key)!=0):
                numRows = int(len(Plaintext) / len(key))
                lastRow = len(Plaintext) % len(key)
                if (lastRow != 0):
                    numRows += 1
            chars = [[' '] * (numColumns) for x in range(numRows)]
            count = 0
            i = 0
            while (i < numRows):# filling the rows with the text characters
                j = 0
                while (j < numColumns):
                    if (count < len(Plaintext)):
                        chars[i][j] = Plaintext[count]
                    count += 1
                    j += 1
                i += 1
            enc = ""
            column = 0
            k = 0
            while (k < numColumns):# reading the text column by column
                row = 0
                while (row < numRows):
                    column = Ek[k]
                    enc+=chars[row][column]
                    row += 1
                k += 1
                enc+=" "
            self.cvalue.set(enc)

    def Decrypt(self):
        Ctext = self.ciphertxt.get()
        key = self.Dekey.get()

        if (Ctext == ""):
            tk.messagebox.showinfo("ERRORٍٍِ", "NO TEXT WAS ENTERED!!")

        if (key == ""):
            tk.messagebox.showinfo("ERRORٍٍِ", "NO KEY WAS ENTERED!!")

        else:
            key= key.lower()
            Ciphertext = Cipher.RemoveSpace(self,Ctext)
            numColumns = len(key)
            lastRow = 1
            numRows = int(len(Ciphertext) / len(key))
            lastRow = len(Ciphertext) % len(key)
            if (lastRow != 0):
                numRows += 1
            chars = [[""] * (numColumns) for x in range(numRows)]
            if (lastRow != 0):
                i = lastRow
                while (i < numColumns):
                    chars[numRows - 1][i] = ' '
                    i += 1
            Dkey = [' '] * (len(key))
            i = 0
            while (i < len(Dkey)):
                Dkey[i] = key[i]
                i += 1
            Dkey.sort()
            Dk = [0] * (len(Dkey))
            i = 0
            while (i < len(Dkey)):
                j = 0
                while (j < len(key)):
                    if (Dkey[i] == key[j]):
                        Dk[i] = j
                        break
                    j += 1
                i += 1
            count = 0
            i = 0
            while (i < numColumns):
                j = 0
                while (j < numRows):
                    if (chars[j][Dk[i]] != ' '):
                        if (count < len(Ciphertext)):
                            chars[j][Dk[i]] = Ciphertext[count]
                        count += 1
                    j += 1
                i += 1
            p = ""
            row = 0
            while (row < numRows):
                column = 0
                while (column < numColumns):
                    p +=str(chars[row][column])
                    column += 1
                row += 1
            self.pvalue.set(p)

    def RemoveSpace(self,s):
        str = ""
        i = 0
        while (i < len(s)):
            if (ord(s[i]) != 32):
                str += s[i]
            i += 1
        return str.lower()

cipher= Cipher()






