from flask import Flask, render_template, jsonify, request
import requests
import numpy as np
import pandas as pd
import os
import sys
sys.dont_write_bytecode = True
# set the project root directory as the static folder, you can set others.
app = Flask(__name__)
#Dont cache anything
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

BlankGif = "R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==" #Load Blank Gif in -1 Spot

DataReading = "data.csv"
DataTraining = "training_data.csv"

def LoadAPI(currUser = None, botMark = None):
    global DataReading, DataTraining, BlankGif, FetchIcon

    #Read the current path
    if os.path.exists(os.path.join(os.getcwd(), DataReading)) == True:
        df1 = pd.read_csv(os.path.join(os.getcwd(),DataReading),encoding = "ISO-8859-1", engine="python", dtype=str, error_bad_lines=False)
    else:
        print("Specified Data Path Does Not Exist!")
        os._exit()

    df2 = pd.read_csv(os.path.join(os.getcwd(),DataTraining), encoding = "ISO-8859-1", engine="python", error_bad_lines=False)


    if not currUser:
        #No variable has been passed, first session
        for i in range(df1.shape[0]):
            #Check to see if this user has been compared before, if its not, get their values
            if df1.loc[i]['Name'] not in df2['Name']:
                return ReturnToUser(df1.iloc[i,0:])
    else:
        #Write the status
        writeData = open(os.path.join(os.getcwd(), DataTraining), "a+")
        print("Reading Location {} in df1".format(currUser))
        getLoc = df1.loc[df1['Name']==currUser].index[0]
        print("Location of {} in df1 found at {}".format(currUser, getLoc))
        print("Write to file")
        writeData.write("\n")
        writeData.write("{},{},{}".format(currUser, df1.iloc[getLoc, 1:].tolist(), botMark))
        #Reread the training data for the new info
        df2 = pd.read_csv(os.path.join(os.getcwd(),DataTraining), encoding = "ISO-8859-1", engine="python", error_bad_lines=False)
        for i in range(df1.shape[0]):
            #Check to see if this user has been compared before, if its not, get their values
            if df1.loc[i]['Name'] not in df2['Name']:
                return ReturnToUser(df1.iloc[i,0:])

def ReturnToUser(info):
    valueFormat = info
    return {
    "status": 1,
    "name": valueFormat["Name"],
    "equipment":
    {
        "helmet": FetchIcon(valueFormat["helmet"]),
        "amulet" : FetchIcon(valueFormat["amulet"]),
        "weapon": FetchIcon(valueFormat["weapon"]),
        "body": FetchIcon(valueFormat["body"]),
        "shield": FetchIcon(valueFormat["sheild"]),
        "legs": FetchIcon(valueFormat["legs"]),
        "gloves": FetchIcon(valueFormat["gloves"]),
        "boots": FetchIcon(valueFormat["boots"])
    },
    "skills":
    {
        "attack": int(valueFormat["Attack"]),
        "defence": int(valueFormat["Defence"]),
        "strength": int(valueFormat["Strength"]),
        "hitpoints": int(valueFormat["Hitpoints"]),
        "ranged": int(valueFormat["Ranged"]),
        "prayer": int(valueFormat["Prayer"]),
        "magic": int(valueFormat["Magic"]),
        "cooking": int(valueFormat["Cooking"]),
        "woodcutting": int(valueFormat["Woodcutting"]),
        "fletching": int(valueFormat["Fletching"]),
        "fishing": int(valueFormat["Fishing"]),
        "firemaking": int(valueFormat["Firemaking"]),
        "crafting": int(valueFormat["Crafting"]),
        "smithing": int(valueFormat["Smithing"]),
        "mining": int(valueFormat["Mining"]),
        "herblore": int(valueFormat["Herblore"]),
        "agility": int(valueFormat["Agility"]),
        "thieving": int(valueFormat["Thieving"]),
        "slayer": int(valueFormat["Slayer"]),
        "farming": int(valueFormat["Farming"]),
        "runecrafting": int(valueFormat["Runecrafting"]),
        "hunter": int(valueFormat["Hunter"]),
        "construction": int(valueFormat["Construction"])
    },
    "location": valueFormat["Location"]
    }



def FetchIcon(id):
    idCopy = int(id)
    if idCopy == -1:
        return 'data:image/png;base64,' + BlankGif
    else:
        return 'data:image/png;base64,' + requests.get("https://www.osrsbox.com/osrsbox-db/items-json/{}.json".format(idCopy)).json()['icon']

def FetchLocationPic(loc):
    #Optional but since we have location, maybe later we can send a picture of location
    return 0

@app.route('/getNextUser', methods=['GET'])
def api():
    if(request.args.get('currUser')):
        currUser = request.args.get('currUser') #Send the InfoBack Of User
        botMark = request.args.get('botMark') #Send the InfoBack Of User
        return jsonify(LoadAPI(currUser, botMark))
    else:
        return jsonify(LoadAPI(None, None))

@app.route('/')
def root():
    return app.send_static_file("index.html")

@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    if os.path.exists(os.path.join(os.getcwd(), DataTraining)) == False:
        print("Training data {} does not exist, creating".format(DataTraining))
        f = open(os.path.join(os.getcwd(), DataTraining), "w")
        f.write("Name,data,is_bot")
        f.close()
    else:
        print("Training data {} detected".format(DataTraining))
    app.run(port=5003, debug=True)
