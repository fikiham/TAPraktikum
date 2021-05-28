import time
from settings import *
from tkinter import *

root = Tk()
root.title("Tokopedia Price Tracker")
mainLabel = Label(root, text="INPUT YOUR LINK", width=50, anchor=N)
bruhLabel = Label(root, text="The URL is not a Tokopedia link")
linkEntry = Entry(root, width=25, borderwidth=5)
wannaLoop = IntVar()
firstFrame = LabelFrame(root)


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
                mainLabel = Label(root, text=second, width=50, anchor=N)
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


submitButton = Button(root, text="SUBMIT", command=myClick, width=20, borderwidth=4)
clearButton = Button(root, text="CLEAR", command=myClear, width=20, borderwidth=4)
loopAfterCB = Checkbutton(root, text="Check price every 24hr and send email?",
                          borderwidth=2, anchor=W, variable=wannaLoop, onvalue=1,
                          offvalue=0, command=loop_after)


def startProg():
    global mainLabel, second
    root.geometry("500x300")
    for URL in stringLink:
        if URL.find(authentication) >= 0:
            first = second
            second = first + "\n" + check_price(URL)[0] \
                     + f" (Rp {check_price(URL)[1]})"
            mainLabel = Label(root, text=second, width=50, anchor=N)
    firstFrame.grid_forget()
    linkEntry.grid(row=0, column=0)
    submitButton.grid(row=1, column=0)
    clearButton.grid(row=2, column=0)
    mainLabel.grid(row=0, column=1, rowspan=4)
    startButton.destroy()
    loopAfterCB.grid(row=4, column=1, columnspan=2, sticky=W)


def stopProg():
    root.quit()


startButton = Button(firstFrame, text="START THE PROGRAM", command=startProg,
                     width=20, borderwidth=5)
stopButton = Button(firstFrame, text="No", command=stopProg,
                    width=20, borderwidth=5)
firstFrame.grid(row=0, column=0, padx=50, pady=50)
startButton.grid(row=1, column=1)
stopButton.grid(row=2, column=1)

root.mainloop()

openSourceText.close()
if loopAfter:
    while True:
        body = ""
        for URL in stringLink:
            if URL.find(authentication) >= 0:
                link, title, price = check_then_mail(URL)
                body += f"URL: {link}\nTitle: {title}\nPrice: {price}\n\n"
            else:
                print(URL, "NO")
        send_mail(body)
        time.sleep(60 * 60 * 24)
else:
    pass
