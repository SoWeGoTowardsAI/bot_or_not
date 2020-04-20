from flask import Flask, render_template, jsonify, request
import requests
import numpy as np
import pandas as pd
import os
# set the project root directory as the static folder, you can set others.
app = Flask(__name__)

BlankGif = "R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==" #Load Blank Gif in -1 Spot

DataReading = "data.csv"
DataTraining = "training_data.csv"

def LoadAPI(currUser = None, botMark = None):
    global DataReading, DataTraining, BlankGif, FetchIcon

    #Read the current path
    if os.path.exists(os.path.join(os.getcwd(), DataReading)) == True:
        df1 = pd.read_csv(os.path.join(os.getcwd(),DataReading),encoding = "ISO-8859-1", engine="python")
    else:
        print("Specified Data Path Does Not Exist!")
        os._exit()

    #Ready to write results to 
    if os.path.exists(os.path.join(os.getcwd(), DataTraining)) == False:
        print("Training data path does not exist, creating")
        f = open(os.path.join(os.getcwd(), DataTraining), "w")
        f.write("Name,data,is_bot")
        f.close()
    df2 = pd.read_csv(os.path.join(os.getcwd(),DataReading),encoding = "ISO-8859-1", engine="python")


    if not currUser:
        #No variable has been passed, first session
        for i in range(df1.shape[0]):
            #Check to see if this user has been compared before, if its not, get their values
            if df1.loc[i]['Name'] not in df2['Name']:
                valueFormat = df1.iloc[i,0:]
                return {
                "status": 1,
                "name": valueFormat["Name"],
                "helmet": FetchIcon(valueFormat["helmet"]),
                "amulet" : FetchIcon(valueFormat["amulet"]),
                "weapon": FetchIcon(valueFormat["weapon"]),
                "body": FetchIcon(valueFormat["body"]),
                "shield": FetchIcon(valueFormat["sheild"]),
                "legs": FetchIcon(valueFormat["legs"]),
                "gloves": FetchIcon(valueFormat["gloves"]),
                "boots": FetchIcon(valueFormat["boots"]),
                "attack": valueFormat["Attack"],
                "defence": valueFormat["Defence"],
                "strength": valueFormat["Strength"],
                "hitpoints": valueFormat["Hitpoints"],
                "ranged": valueFormat["Ranged"],
                "prayer": valueFormat["Prayer"],
                "magic": valueFormat["Magic"],
                "cooking": valueFormat["Cooking"],
                "woodcutting": valueFormat["Woodcutting"],
                "fletching": valueFormat["Fletching"],
                "fishing": valueFormat["Fishing"],
                "firemaking": valueFormat["Firemaking"],
                "crafting": valueFormat["Crafting"],
                "smithing": valueFormat["Smithing"],
                "mining": valueFormat["Mining"],
                "herblore": valueFormat["Herblore"],
                "agility": valueFormat["Agility"],
                "thieving": valueFormat["Thieving"],
                "slayer": valueFormat["Slayer"],
                "farming": valueFormat["Farming"],
                "runecrafting": valueFormat["Runecrafting"],
                "hunter": valueFormat["Hunter"],
                "construction": valueFormat["Construction"],
                "location": valueFormat["Location"]
                }
    else:
        #Write the status
        writeData = open(os.path.join(os.getcwd(), DataReading), "a")
        getLoc = df1.loc[df1['Name']==currUser].index[0]
        writeData.write("{},{},{}".format(currUser, df1.iloc[getLoc, 1:13].tolist(), botMark))
        for i in range(df1.shape[0]):
            #Check to see if this user has been compared before, if its not, get their values
            if df1.loc[i]['Name'] not in df2.values():
                valueFormat = df1.iloc[i,0:13]
                return {
                "status": 1,
                "name": valueFormat["Name"],
                "helmet": FetchIcon(valueFormat["helmet"]),
                "amulet" : FetchIcon(valueFormat["amulet"]),
                "weapon": FetchIcon(valueFormat["weapon"]),
                "body": FetchIcon(valueFormat["body"]),
                "shield": FetchIcon(valueFormat["sheild"]),
                "legs": FetchIcon(valueFormat["legs"]),
                "gloves": FetchIcon(valueFormat["gloves"]),
                "boots": FetchIcon(valueFormat["boots"]),
                "attack": valueFormat["Attack"],
                "defence": valueFormat["Defence"],
                "strength": valueFormat["Strength"],
                "hitpoints": valueFormat["Hitpoints"],
                "ranged": valueFormat["Ranged"],
                "prayer": valueFormat["Prayer"],
                "magic": valueFormat["Magic"],
                "cooking": valueFormat["Cooking"],
                "woodcutting": valueFormat["Woodcutting"],
                "fletching": valueFormat["Fletching"],
                "fishing": valueFormat["Fishing"],
                "firemaking": valueFormat["Firemaking"],
                "crafting": valueFormat["Crafting"],
                "smithing": valueFormat["Smithing"],
                "mining": valueFormat["Mining"],
                "herblore": valueFormat["Herblore"],
                "agility": valueFormat["Agility"],
                "thieving": valueFormat["Thieving"],
                "slayer": valueFormat["Slayer"],
                "farming": valueFormat["Farming"],
                "runecrafting": valueFormat["Runecrafting"],
                "hunter": valueFormat["Hunter"],
                "construction": valueFormat["Construction"],
                "location": valueFormat["Location"]
                }


def FetchIcon(id):
    if id == -1:
        return 'data:image/png;base64,' + BlankGif
    else:
        return 'data:image/png;base64,' + requests.get("https://www.osrsbox.com/osrsbox-db/items-json/{}.json".format(id)).json()['icon']

def FetchLocationPic(loc):
    #add JSON to location
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

if __name__ == '__main__':
    app.run(port=5003, debug=True)
