import pandas as pd
import datetime
import smtplib

GMAIL_ID = "ramtekeabhishek63@gmail.com"
GMAIL_PASSWORD = "ultjlnktzsjnpeeu"

def sendEmail(to,sub,msg) :
    print(f"Email to {to} sent with subject {sub} and msg {msg}")
    s = smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PASSWORD)
    s.sendmail(GMAIL_ID, to, f"subject : {sub} \n \n {msg}")

if __name__ == "__main__" :
    #sendEmail(GMAIL_ID, " subject", "text message")
    #exit()
    df = pd.read_excel("data.xlsx")
    #print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    #print(type(today))

    writeInd = []
    for index,item in df.iterrows() :
        #print(index,item["Birthday"])
        bday = item["Birthday"]
        Bday = bday[0:5]

        if today == Bday and yearNow not in str(item["Year"]) :
            sendEmail(item["Email"],item["Name"],item["Dialogue"])
            writeInd.append(index)
    #print(writeInd) 
    for i in writeInd :
        yr = df.loc[i,"Year"] 
        df.loc[i,"Year"] = str(yr) + "," + str(yearNow)
    df.to_excel("data.xlsx",index = False)   
