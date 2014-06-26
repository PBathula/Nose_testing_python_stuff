for datafile in *.txt
do
    bash goostats $datafile |:head -1
done
