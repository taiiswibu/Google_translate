from tkinter import*
from PIL import Image, ImageTk
import googletrans
from googletrans import Translator
#print(googletrans.LANGCODES)
#tạo TK Windơw
root =Tk()
root.title('Google Galaxy')
root.geometry("560x630")
root.iconbitmap(r"C:\codebaitappython\Google_dich\tutorial\logo.ico")
#tạo cái background

load = Image.open(r"C:\codebaitappython\Google_dich\tutorial\background.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image = render)
img.place(x=0,y=0)

# Tạo Label Translator
name = Label(root,text= "Translator",fg="#800000",bd=0,bg="#03152D")
name.config(font=("Transformers Movie",30))
name.pack(pady =10)

# Tạo Textbox đầu vào
box = Text(root,width=28,height=8,font=("ROBOTO",16))
box.pack(pady=20)
#tạo một đối tượng fame gán vao biến
button_frame=Frame(root).pack(side=BOTTOM)

# Hàm xóa text trên cả 2 textbox
def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)

# Hàm dịch văn bản
def translate():
    # Lấy text từ Textbox đầu vào
    xuat = box.get(1.0,END)
    print(xuat)
    # Tạo object Translator và thực hiện dịch văn bản
    t = Translator()
    a =t.translate(xuat,src="vi",dest = "en")
    b = a.text
     # Hiển thị kết quả dịch lên Textbox đầu ra
    box1.insert(END,b)

# Tạo nút Clear text
clear_button = Button(button_frame,text="Clear text",font=(("Arial"),10,'bold'),bg='#303030',fg="#FFFFFF",command=clear)
clear_button.place(x=150,y=310)
# Tạo nút Translate
trans_button = Button(button_frame,text="Translste",font=(("Arial"),10,'bold'),bg='#303030',fg="#FFFFFF",command=translate)
trans_button.place(x=290,y=310)

# Tạo Textbox đầu ra
box1 = Text(root,width=28,height=8,font=("ROBOTO",16))
box1.pack(pady=50)


# giữ cho chương trình chyaj và ko đóng lại
root.mainloop()


#t = Translator()
#a =t.translate("em la tuyet voi nhat",src="vi",dest = "en")
#print(a.text)