from flask import Flask, render_template
import random
app = Flask(__name__)
# list of cat images
images = [
"https://media4.giphy.com/media/AwF74xIsyoiKQ/giphy.gif?cid=ecf05e47kb243v3oda8bciepcvtm69w3amxc7jvpe5nch3mp&rid=giphy.gif",
"https://media1.giphy.com/media/gvlzz2kUlk05q/giphy.gif?cid=ecf05e47kb243v3oda8bciepcvtm69w3amxc7jvpe5nch3mp&rid=giphy.gif",
"https://media2.giphy.com/media/BzyTuYCmvSORqs1ABM/giphy.gif?cid=ecf05e4704i1kebnyymf2w37ef1cis7f9svbct43jpk01vfm&rid=giphy.gif",
"https://media0.giphy.com/media/l4KibK3JwaVo0CjDO/giphy.gif?cid=ecf05e4704i1kebnyymf2w37ef1cis7f9svbct43jpk01vfm&rid=giphy.gif",
"https://media1.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif?cid=ecf05e4704i1kebnyymf2w37ef1cis7f9svbct43jpk01vfm&rid=giphy.gif"
]
@app.route('/')
def index():
    url= random.choice(images)
    return render_template('index.html', url=url)
if __name__ == "__main__":
    app.run(host="0.0.0.0")
