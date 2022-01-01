from flask import Flask
import  datetime
import json
app = Flask(__name__)

@app.route("/")
def main():
    html = '''
<html>
<head>
    <style>
        #centered{
            background-color: rgba(124, 124, 124, 1);
            padding: 30px;
            border-radius: 20px;
            text-align: center;
        }
        h2{
            font-size: 50px;
        }
        body{
            background-image: url("./static/background.jpg");
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-size: 100% 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0px;
        }
        #demo{
            color: white;
            font-weight: bold;
            font-size: 50px;
        }
        #rings{
            width: 80px;
        }
    </style>
</head>

<html>
    <body>
        <div id="centered">
            <h2>Do ślubu pozostało</h2>
            <img id="rings" src="./static/rings.png" >
            <div id="demo"></div>
        </div>
        <script>
            // Set the date we're counting down to
            var countDownDate = new Date("Jan 3, 2022 13:00:00").getTime();
            
            // Update the count down every 1 second
            var x = setInterval(function() {
            
              // Get today's date and time
              var now = new Date().getTime();
            
              // Find the distance between now and the count down date
              var distance = countDownDate - now;
            
              // Time calculations for days, hours, minutes and seconds
              var days = Math.floor(distance / (1000 * 60 * 60 * 24));
              var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
              var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
              var seconds = Math.floor((distance % (1000 * 60)) / 1000);
            
              // Display the result in the element with id="demo"
              document.getElementById("demo").innerHTML = days + "d " + hours + "h "
              + minutes + "m " + seconds + "s ";
            
              // If the count down is finished, write some text
              if (distance < 0) {
                clearInterval(x);
                document.getElementById("demo").innerHTML = "To już <3";
              }
            }, 1000);
            </script>
    </body>
</html>
    '''
    return html
@app.route("/ile")
def ile():
    # datetime(year, month, day, hour, minute, second)
    a = datetime.datetime.now()
    b = datetime.datetime(2022, 1, 3, 13, 00, 00)
    # returns a timedelta object
    c = a - b
    seconds = (b - a).total_seconds()
    seconds_in_day = 60 * 60 * 24
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60

    days = seconds // seconds_in_day
    hours = (seconds - (days * seconds_in_day)) // seconds_in_hour
    minutes = (seconds - (days * seconds_in_day) - (hours * seconds_in_hour)) // seconds_in_minute
    seconds = (seconds - (days * seconds_in_day) - (hours * seconds_in_hour) - (minutes * seconds_in_minute))
    thisdict = {
        "days": str(days),
        "hours": str(hours),
        "minutes": str(minutes),
        "seconds": str(seconds)
    }
    return json.dumps(thisdict)
app.run()