##  Initialising table 1 - Batsman_Data
##  Initialising table 2 - Bowlers_Data


```sql



create database worldcup;



create table batting (

	player_name varchar(50),
    runs int ,
    balls int ,
    minutes_played int ,
    fours int ,
    sixes int ,
    strike_rate float 
    

);


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

```


select * from batting;


##  Top 5 Run Scorer in World Cup 2011

```sql
    select bt.player_name, sum(bt.runs) as total_runs from batting bt
    group by bt.player_name order by total_runs desc limit 5;

```

## Player who played most number of balls 


```sql


select bt.player_name ,sum(bt.balls) total_balls_played from batting bt
group by bt.player_name order by total_balls_played desc limit 1;

```



##  Player who spent most time on pitch in hours in the whole series 

```sql
select bt.player_name ,
Round(sum(bt.minutes_played) / 60,2)  as total_time_spent 

from batting bt
group by bt.player_name order by total_time_spent desc limit 1;
```

##  Player who spent most time on pitch in minutes in a single match
```sql
select bt.player_name  ,  max(bt.minutes_played) as max_time 
from batting bt group by  bt.player_name  order by max_time desc limit 1;

```
## Top 3 Most aggressive batsman who have played atleast 100 balls 

```sql
select bt.player_name  ,  max(bt.strike_rate) as striker , sum(bt.balls)  as total_balls_played
from batting bt
group by  bt.player_name 
having total_balls_played >= 100
order by striker desc limit 3;
```

## The Player with most no. of ducks


```sql

select bt.player_name , count(*) as total_ducks 
from batting bt 
where bt.runs = 0 
group by bt.player_name
order by total_ducks desc limit 1;



```
