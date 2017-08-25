#row 1 of my dataset df1 looks like:

"""	Resolution Letter		 Action						Type							Description

1		B					ESTABLISH		BUS ZONE AND SIDEWALK WIDENING			16th Street, north side, from Church Street to 78 feet easterly (6-foot wide bus bulb replaces bus zone); 16th Street, north side, from Dolores Street to 71 feet westerly (6-foot wide bus bulb– bus stop relocated to far side); 16th Street, south side, from Dolores Street to 83 feet easterly (6-foot wide bus bulb– bus stop relocated to far side); 16th Street, north side, from Valencia Street to 118 feet westerly (6-foot wide bus bulb– bus stop relocated to far side, relocates a blue zone, removes four metered parking spaces and one yellow parking zone); 16th Street, south side, from Valencia Street to 118 feet easterly (6-foot wide bus bulb– bus stop relocated to far side, removes 3 metered parking spaces and one yellow parking zone); 16th Street, north side, from Mission Street to 126 feet easterly (6-foot wide bus bulb replaces bus zone); 16th Street, south side, from Mission Street to 116 feet westerly (6-foot wide bus bulb replaces bus zone); 16th Street, south side, from Shotwell Street to 146 feet easterly (6-foot wide bus bulb replaces bus zone); 16th Street, north side, from Folsom Street to 118 feet westerly (6-foot wide bus bulb replaces bus zone); 16th Street, north side, from Potrero Avenue to 115 feet westerly (6-foot wide bus bulb replaces bus zone); 16th Street, north side, from RhodeIsland Street to 95 feet westerly (6-foot wide bus bulb replaces bus zone); 16th Street, north side, from Wisconsin Street to 118 feet westerly (6-foot wide bus bulb replaces bus zone); 16th Street, north side, from Missouri Street to 118 feet westerly (6-foot wide bus bulb replaces bus zone).

The values in 'Description' represent the changes in public transport infrastructure. Many rows, like row 1, of df1 have a lot of values, of mixed data type, packed under the column 'Description'. It's easy to notice the delimiter ';' separating each value.
I am interested in splitting, say, each of 10 values in row 2 under the column 'Description' into a separate row. When I get 10 rows, I want the other corresponding values of row 2 to repeat to complete the change. Meaning: The 10 values of 'Description' in row 2 are split at ';' and accompanied by 10 corresponding values of 'Resolution Letter', 'Action', and 'Type' to fit the new change.

"""



df1=(df1.set_index(df1.columns.drop('Description',1).tolist()).Description.str.split(';', expand=True).stack().reset_index().rename(columns={0:'Description'}).loc[:, df1.columns])
#Breaking the above code down in parts:
#df.columns.drop('Description',1).tolist(): It removes 'Description' in axis=1 and returns the labels['Resolution Letter', 'Action', 'Type'] in list type.
#Description.str.split(';', expand=True).stack():It splits the values in Description at ';' and palces each value in a column. Here 'expand=True' extends the number of columns based on the maximum number of values, say, after splitting if there are 10 values in one row and 20 values in another. It extends the number of columns to 20. The rows that do not have that many values will have 'none'. The 'stack()' option puts these values in rows. Why 'stack()'? because I want each value in a separate row.
#reset_index(): This option will reset the index from 0. Prior to this step the dataset retains the two types of indices: one from before splitting the 'Description' column and one from after splitting.
#rename(columns={0:'Description'}).loc[:, df1.columns]: sets the space for other columns based on the number of row values of Description.
#Chaining the above methods and setting index according to the new change by using set_index.

"""As expected the output looks like (after the change):

		Resolution Letter	Action					Type								Description
	
3			B				ESTABLISH	BUS ZONE AND SIDEWALK WIDENING	16th Street, north side, from Church Street t...
4			B				ESTABLISH	BUS ZONE AND SIDEWALK WIDENING	16th Street, north side, from Dolores Street ...
5			B				ESTABLISH	BUS ZONE AND SIDEWALK WIDENING	16th Street, south side, from Dolores Street ...
6			B				ESTABLISH	BUS ZONE AND SIDEWALK WIDENING	16th Street, north side, from Valencia Street...
7			B				ESTABLISH	BUS ZONE AND SIDEWALK WIDENING	16th Street, south side, from Valencia Street...
8			B				ESTABLISH	BUS ZONE AND SIDEWALK WIDENING	16th Street, north side, from Mission Street ...
9			B				ESTABLISH	BUS ZONE AND SIDEWALK WIDENING	16th Street, south side, from Mission Street ...
10			B				ESTABLISH	BUS ZONE AND SIDEWALK WIDENING	16th Street, south side, from Shotwell Street...
11			B				ESTABLISH	BUS ZONE AND SIDEWALK WIDENING	16th Street, north side, from Folsom Street t...
12			B				ESTABLISH	BUS ZONE AND SIDEWALK WIDENING	16th Street, north side, from Potrero Avenue ...
13			B				ESTABLISH	BUS ZONE AND SIDEWALK WIDENING	16th Street, north side, from RhodeIsland Str...
14			B				ESTABLISH	BUS ZONE AND SIDEWALK WIDENING	16th Street, north side, from Wisconsin Stree...
15			B				ESTABLISH	BUS ZONE AND SIDEWALK WIDENING	16th Street, north side, from Missouri Street..."""
