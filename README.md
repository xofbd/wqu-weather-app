# Weather Greeting Application
This project demonstrates how to use Python to create web application. It is a primarily meant for educational purposes, specifically created for the WorldQuant University Introduction to Data Science Module.

The skills and tools used are:
* Python's `requests` package.
* Python's `flask` web framework.
* working with JSONs.
* modular programming

When a client visits the application, it
1. gets the client's IP address.
1. uses the IP address to look up their location.
1. uses their location data to greet them with temperature of the city they are located in.

## Prerequisites
All required Python packages can be found in the `requirements.txt` file. Additionally, the provided `Makefile` can be used to created a virtual environment by running `make venv`. You will also need a Heroku account and have installed the Heroku CLI. For more information on the Heroku CLI, go to https://devcenter.heroku.com/articles/heroku-cli#download-and-install.

## Running the app locally using Flask
You may want to run the app using Flask locally before deploying it to Heroku, especially if you have made any changes to the code. To run locally:

1. clone the repository.
1. in the repository, run `make deploy`.
1. open the link provided in the command line.

If you are using Windows, you can:
1. create and activate the virtual environment.
1. `set FLASK_APP=weather_app/app.py` in the command line.
1. run `python -m flask run`.
1. open the link in the command line.

Alternatively, you can deploy using [Docker](https://www.docker.com/).
1. `docker build -t weather_app .`
1. `docker run -d -p 5000:5000 weather_app`

## Deploying to Heroku
Make sure your app is ready to be deployed to Heroku by running Flask locally. To deploy to Heroku:

1. clone the repository (if you haven't yet).
1. `heroku login` and enter your credentials.
1. `heroku create` or `heroku create app-name` where app-name is a custom app name.
1. `git push heroku master`.
1. `heroku open` or open the app online through your Heroku profile.

## Future work
Since this is a short demonstration of what you can do using Python for creating web application, consider extensions to the project. Some ideas include:
1. showing a plot of the forecast.
1. using their location to display other location specific data.

## License
This project is distributed under the GNU General Purpose License. Please see `LICENSE` for more information.
