/*this file doesnt load anything, it just contains the query's ran to make joined tables for analysis*/
create table regioned_breweries select name,city,brewery.state,rating,brewery_id,region from breweries inner join regions on breweries.state=regions.state_code;

create table regioned_beers select b.*,r.region,r.rating from beers as b inner join regioned_breweries as r on b.brewery_id=r.brewery_id;