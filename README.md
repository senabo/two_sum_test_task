## Test task for Harmonic Advance

----------------------------------

It's an app that allows you to find indices of the two numbers such that they add up to the target. 
You should send an array of integers with unique elements and target number to the `two-sum` endpoint.


#### To run the project locally: 
create .env file in root project dir (from env.sample):

    cp .env.sample .env

build and run the project: 

    docker-compose up --build

run tests: 

    docker-compose exec backend python manage.py test