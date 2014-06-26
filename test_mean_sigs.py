from mean_sightings import get_sightings
filename = 'sightings_tab_sm.csv'
def test_water_is_correct():
	watrec,watmean = get_sightings(filename,'water')
	assert watrec==2, 'Number of records for water is wrong'
	assert watmean==17, 'mean for water is wrong'
def test_clay_is_correct():
	clayrec,claymean = get_sightings(filename,'clay')
	assert clayrec==2, 'Number of records for clay is wrong'
	assert claymean==25, 'Mean for clay is wrong'
def test_not_present():
	norec,nomean = get_sightings(filename,'Not Present')
	assert norec==0,'Biosignature not present has zero recs'
	assert nomean==0,'mean is not present for missing biosig'
