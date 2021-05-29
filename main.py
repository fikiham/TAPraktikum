import time
from settings import *
from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Tokopedia Price Tracker")
root.config(background="#B7E4C7")
mainLabel = Label(root, text="INPUT YOUR LINK", width=50, anchor=N, bg="#B7E4C7")
bruhLabel = Label(root, text="The URL is not a Tokopedia link")
linkEntry = Entry(root, width=25, borderwidth=5)
background = ImageTk.PhotoImage(Image.open("source/TA_Background3.png"))
credit = ImageTk.PhotoImage(Image.open("source/credit.png"))
canvas = Label(root, image=background, bg='black')
canvas2 = Label(root, image=credit, bg="#B7E4C7")
wannaLoop = IntVar()
firstFrame = LabelFrame(root, bg="#B7E4C7")


def myClear():
    openSourceText = open('source/source.txt', 'w')
    linkEntry.delete(0, END)
    mainLabel.grid_forget()
    bruhLabel.grid_forget()


def myClick():
    global mainLabel, second
    try:
        check_price(linkEntry.get())
        mainLabel.grid_forget()
        openSourceText = open('source/source.txt', 'a+')
        openSourceText.write(f";\n{linkEntry.get()}")
        openSourceText = open('source/source.txt', 'r')
        stringLink = openSourceText.read().split(";")
        for URL in stringLink:
            if URL.find(authentication) >= 0:
                first = second
                second = first + "\n" + check_price(URL)[0] \
                         + f" (Rp {check_price(URL)[1]})"
                mainLabel = Label(root, text=second, width=50, anchor=N, bg="#B7E4C7")
        mainLabel.grid(row=0, column=1, rowspan=4)
        bruhLabel.grid_forget()
        linkEntry.delete(0, "end")
        second = "Title (Price)"
    except:
        bruhLabel.grid(row=3, column=0)


def loop_after():
    global loopAfter
    if wannaLoop.get() == 1:
        loopAfter = True
    elif wannaLoop.get() == 0:
        loopAfter = False


submitButton = Button(root, text="SUBMIT", command=myClick, width=20, borderwidth=4, bg="#40916C")
clearButton = Button(root, text="CLEAR ALL", command=myClear, width=20, borderwidth=4, bg="#40916C")
loopAfterCB = Checkbutton(root, text="Check price every 24hr and send email after program ends?",
                          borderwidth=2, anchor=S + W, variable=wannaLoop, onvalue=1,
                          offvalue=0, command=loop_after, bg="#B7E4C7")


def startProg():
    global mainLabel, second
    root.geometry("500x200")

    for URL in stringLink:
        if URL.find(authentication) >= 0:
            first = second
            second = first + "\n" + check_price(URL)[0] \
                     + f" (Rp {check_price(URL)[1]})"
            mainLabel = Label(root, text=second, width=50, anchor=N, bg="#B7E4C7")
    firstFrame.grid_forget()
    canvas.grid_forget()
    linkEntry.grid(row=0, column=0)
    submitButton.grid(row=1, column=0)
    clearButton.grid(row=2, column=0)
    mainLabel.grid(row=0, column=1, rowspan=4)
    loopAfterCB.grid(row=4, column=1, columnspan=2, sticky=W)
    canvas2.grid(row=4, column=0)


def stopProg():
    root.quit()


startButton = Button(firstFrame, text="START THE PROGRAM", command=startProg,
                     width=20, borderwidth=5)
stopButton = Button(firstFrame, text="No", command=stopProg,
                    width=20, borderwidth=5)
firstFrame.grid(row=0, column=0, padx=100, pady=105)
startButton.grid(row=0, column=0)
stopButton.grid(row=0, column=1)
canvas.grid(row=0, column=0, rowspan=4, columnspan=2)

root.resizable(False, False)
root.mainloop()

openSourceText.close()
if loopAfter:
    while True:
        body = ""
        for URL in stringLink:
            if URL.find(authentication) >= 0:
                link, title, price = check_then_mail(URL)
                body += f"URL: {link}\nTitle: {title}\nPrice: Rp{price}\n\n"
            else:
                print(URL, "NO")
        send_mail(body)
        time.sleep(60 * 60 * 24)
else:
    pass
