```sql

select  * from bowling;

```


## Top 5 Bowler with the most wicket in the tounament 

```sql

    select bw.player_name ,  sum(bw.wicketstaken) as total_wickets from  bowling bw

    group by  bw.player_name

    order by  total_wickets desc  limit 5;
    
```


## Player who gave most extras runs in the tounament (Extras =  total Wide runs( 1 each) + total no.of no ball( 1 run each ignoring  the free hit runs)

```sql

select bw.player_name ,  sum(bw.WideDeliveries) + sum(bw.NoBalls) as total_extra from  bowling bw

group by  bw.player_name

order by  total_extra desc  limit 1;

```


## Top 3 Most expensive bowlers

```sql

select bw.player_name ,  sum(runsgiven) as total_runs from  bowling bw

group by  bw.player_name

order by  total_runs desc  limit 3;

```

## Bowler who with most no.of overs bowled

```sql

select bw.player_name ,  Round(sum(overs) , 2) as total_overs from  bowling bw

group by  bw.player_name

order by  total_overs desc  limit 1;

```


## Top 3 Bowlers who bowled complete spell of 10 overs in a match for how many times



```sql

select bw.player_name  , count(*) as total_times from  bowling bw

where overs = 10

group by  bw.player_name

order by  total_times desc   limit 3;

```





