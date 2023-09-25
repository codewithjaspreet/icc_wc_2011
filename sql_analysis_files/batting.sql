create database worldcup;

-- Initialising table 1 - Batsman_Data


create table batting (

	player_name varchar(50),
    runs int ,
    balls int ,
    minutes_played int ,
    fours int ,
    sixes int ,
    strike_rate float 
    

);

-- Initialising Bowling Table

CREATE TABLE bowling (
    Player_Name VARCHAR(255),
    Overs FLOAT,
    Maidens INT,
    RunsGiven INT,
    WicketsTaken INT,
    EconomyRate FLOAT,
    DotBalls INT,
    FoursHitten INT,
    SixesHitten INT,
    WideDeliveries INT,
    NoBalls INT
);

select * from batting;


-- Question 1. Top 5 Run Scorer in World Cup 2011

select bt.player_name, sum(bt.runs) as total_runs from batting bt
group by bt.player_name order by total_runs desc limit 5;


-- Question 2. Player who played most number of balls 


select bt.player_name ,sum(bt.balls) total_balls_played from batting bt
group by bt.player_name order by total_balls_played desc limit 1;



-- Question 3. Player who spent most time on pitch in hours in the whole series 


select bt.player_name ,
Round(sum(bt.minutes_played) / 60,2)  as total_time_spent 

from batting bt
group by bt.player_name order by total_time_spent desc limit 1;


-- Question 4 . Player who spent most time on pitch in minutes in a single match

select bt.player_name  ,  max(bt.minutes_played) as max_time 
from batting bt group by  bt.player_name  order by max_time desc limit 1;


-- Top 3 Most aggressive batsman who have played atleast 100 balls 


select bt.player_name  ,  max(bt.strike_rate) as striker , sum(bt.balls)  as total_balls_played
from batting bt
group by  bt.player_name 
having total_balls_played >= 100
order by striker desc limit 3;


-- The Player with most no. of ducks

select bt.player_name , count(*) as total_ducks 
from batting bt 
where bt.runs = 0 
group by bt.player_name
order by total_ducks desc limit 1;


-- Top 5 players with most no.of sixes in the tounament

select bt.player_name  , sum(sixes) as total_six

from batting bt 

group by bt.player_name

order by total_six desc limit 5;



-- Top 5 Players with most no. of fours in the tounament

select bt.player_name  , sum(fours) as total_fours

from batting bt 

group by bt.player_name

order by total_fours desc limit 5;


-- Player Most no.of half centuries 


select bt.player_name  , count(*) as total_50

from batting bt 

where runs >= 50 

group by bt.player_name

order by total_50 desc limit 1;


-- Player Most no.of centuries 



select bt.player_name  , count(*) as total_100

from batting bt 

where runs >= 100 

group by bt.player_name

order by total_100 desc limit 1;






--  Top 3 Highest batting scores 

select bt.player_name  ,max(runs) as max_run

from batting bt 
group by  bt.player_name

order by max_run desc limit 3;

